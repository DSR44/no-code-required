#!/usr/bin/env python3
"""Validate NCR blog posts — cover, audio, SEO. Used by CI and local pre-push checks."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
POSTS = REPO / "content" / "posts"
STATIC = REPO / "static"

# Narration became a hard publish requirement around mid-May 2026.
# Legacy posts must remain editable (SEO / Read-next links) without audio.
AUDIO_REQUIRED_FROM = "2026-05-20"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        return {}, text
    fm: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm, text[match.end() :].lstrip()


def static_path(web_path: str) -> Path:
    return STATIC / web_path.lstrip("/")


def validate_slug(slug: str) -> list[str]:
    errors: list[str] = []
    post_path = POSTS / f"{slug}.md"
    if not post_path.is_file():
        return [f"Post not found: {post_path}"]

    text = post_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if fm.get("draft", "").lower() == "true":
        return []

    slug_fm = fm.get("slug", slug)
    if slug_fm != slug:
        errors.append(f"Frontmatter slug '{slug_fm}' does not match filename '{slug}'")

    if not fm.get("description"):
        errors.append("Missing description in frontmatter")
    elif len(fm.get("description", "")) > 160:
        errors.append(f"description too long ({len(fm['description'])} chars — max 160)")

    if "keywords:" not in text:
        errors.append("Missing keywords: [...] in frontmatter")

    cover_match = re.search(r"^\s*image:\s*[\"']?([^\"'\n]+)", text, re.M)
    if not cover_match:
        errors.append("Missing cover.image in frontmatter")
    else:
        cover_web = cover_match.group(1).strip().strip('"').strip("'")
        cover_path = static_path(cover_web)
        if not cover_path.is_file():
            errors.append(f"Cover image missing on disk: {cover_web}")
        elif cover_path.stat().st_size < 10_000:
            errors.append(f"Cover image suspiciously small: {cover_web}")

    # Accept the {{< audio >}} shortcode OR a raw <audio> HTML block, then verify the
    # actually-referenced mp3 exists. Older posts predate the slug-named shortcode
    # convention; this checks the real audio file instead of assuming "<slug>.mp3".
    post_date = (fm.get("date") or "")[:10]
    require_audio = (not post_date) or post_date >= AUDIO_REQUIRED_FROM

    audio_ref = re.search(r'{{<\s*audio\s+src=["\']([^"\']+\.mp3)', text)
    if not audio_ref:
        audio_ref = re.search(r'<source[^>]+src=["\']([^"\']+\.mp3)', text)
    if not audio_ref:
        if require_audio:
            errors.append(f'Missing audio: add {{{{< audio src="/audio/{slug}.mp3" >}}}}')
    else:
        audio_path = static_path(audio_ref.group(1))
        if not audio_path.is_file():
            errors.append(f"Missing audio file on disk: {audio_ref.group(1)}")
        elif audio_path.stat().st_size < 200_000:
            errors.append(
                f"Audio too small ({audio_path.stat().st_size} bytes) — regenerate full narration"
            )

    internal_links = len(re.findall(r"\]\(/posts/[^)]+\)", body))
    if internal_links < 5:
        errors.append(f"Only {internal_links} internal /posts/ links — need at least 5")

    word_count = len(re.findall(r"\b\w+\b", body))
    if word_count < 800:
        errors.append(f"Word count too low ({word_count}) — target 800+ words")

    return errors


def changed_slugs() -> list[str]:
    import subprocess

    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "content/posts/"],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    slugs = []
    for line in result.stdout.splitlines():
        name = Path(line).name
        if name.endswith(".md") and not name.startswith("_"):
            slugs.append(name[:-3])
    return slugs


def main() -> int:
    args = sys.argv[1:]
    deploy_gate = "--deploy-gate" in args
    slugs = [a for a in args if not a.startswith("--")]

    if not slugs:
        slugs = changed_slugs()
        if not slugs:
            print("No post slugs to validate (pass slug args or push post changes).")
            return 0

    failed = False
    for slug in slugs:
        errors = validate_slug(slug)
        if errors:
            if deploy_gate:
                # In deploy-gate mode, only HARD failures block the build
                hard_errors = [
                    e
                    for e in errors
                    if any(
                        k in e.lower()
                        for k in ["missing cover", "missing audio", "cover image missing on disk"]
                    )
                ]
                if hard_errors:
                    failed = True
                    print(f"FAIL — {slug} (deploy-gate: HARD failure):")
                    for err in hard_errors:
                        print(f"  ✗ {err}")
                else:
                    print(f"WARN — {slug} (deploy-gate: soft issues, not blocking):")
                    for err in errors:
                        print(f"  ⚠ {err}")
            else:
                failed = True
                print(f"FAIL — {slug}:")
                for err in errors:
                    print(f"  ✗ {err}")
        else:
            print(f"PASS — {slug}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
