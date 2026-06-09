# NCR Okara SEO Audit — Agent Instructions

**Site:** https://www.nocoderequired.net/  
**Repo:** this folder (`no-code-required`)  
**Full playbook:** `../prophet404_memory_backup/memory/MEMORY_OKARA_SEO_AUDIT.md`  
**Copy-paste prompts:** `../OKARA_SEO_AUDIT_PROMPT.md`

---

## Your job

Run an Okara-style SEO audit (what Okara charges ~$100/page for). **Find mistakes, fix them in code, build, and push.** Do not stop at a list of issues.

---

## Step 1 — Live site sanity check

- Open https://www.nocoderequired.net/ — confirm CSS loads (not raw bullet-list HTML).
- `hugo.toml` → `baseURL` must match live www domain.
- View-source homepage: confirm stylesheet returns 200 (not 307 redirect loop).

---

## Step 2 — Audit 8 hub pages

| Page | Path | Schema |
|------|------|--------|
| Homepage | `/` | Organization + WebSite |
| Blog index | `/posts/` | CollectionPage |
| Start Here | `/start-here/` | WebPage + HowTo |
| FAQ | `/faq/` | WebPage + FAQPage (8+ Q&As) |
| About | `/about/` | AboutPage + Person |
| Privacy | `/privacy/` | WebPage |
| Categories | `/categories/` | CollectionPage |
| Tags | `/tags/` | CollectionPage |
| Tools (NCR only) | `/tools/` | ItemList + WebPage |

Each hub needs: frontmatter `description` (155 chars), 100+ word body intro, internal links.

---

## Step 3 — Schema & posts

- All posts: `"@type": ["BlogPosting", "Article"]` in `layouts/partials/templates/schema_json.html`
- **Do NOT add FAQ/HowTo/Review to every post** — only when content type matches (see below)
- FAQ partial: `layouts/partials/schema_faq.html` — posts with `faqs:` frontmatter (3–5 Q&As)
- HowTo partial: `layouts/partials/schema_howto.html` — posts with `howto:` + numbered steps
- Review partial: `layouts/partials/schema_review.html` — posts with `reviews:` (tool comparisons)
- Check posts missing: `description`, `keywords`, `cover.image`, duplicate H1 in body
- Okara citation gaps (Zapier cited instead of NCR) → ensure `/faq/` Q&As target those queries

### When to add schema (per post, at publish time)

| Post type | Add | Skip |
|-----------|-----|------|
| Tool comparison / "best X tested" | `reviews:` + `faqs:` | — |
| Step-by-step tutorial | `howto:` | FAQ unless there's a Q&A section |
| Opinion / news / personal story | nothing extra | all three |
| Mixed tutorial + FAQ section | `howto:` + `faqs:` | reviews |

After publish: run [Google Rich Results Test](https://search.google.com/test/rich-results) on high-traffic posts only — not required for every post.

Example frontmatter:
```yaml
faqs:
  - q: "Question people search for?"
    a: "Direct answer in 1–3 sentences."
howto:
  totalTime: "PT15M"
  steps:
    - name: "Step title"
      text: "What to do."
reviews:
  - item: "Tool Name"
    url: "https://tool.com"
    rating: 4.5
    summary: "One-sentence honest verdict."
```

---

## Step 4 — Technical SEO

- `params.homeTitle` in hugo.toml
- hreflang `en` + `x-default` in head
- og:image 1200×630
- Meta descriptions via `seo_description.html` (155 char cap)

---

## Step 5 — Build, check, push

```bash
hugo --minify
ncrcheck <slug>   # for any changed posts
ncrpush
```

Confirm in view-source after deploy: FAQPage on `/faq/`, Article on posts.

---

## Report template

```
NCR OKARA AUDIT — [date]

LIVE CHECK: CSS ok / baseURL ok
HUB PAGES: [fixed | ok | missing]
SCHEMA: FAQPage / Article / HowTo / CollectionPage — [status]
POSTS: [count missing cover/keywords/description]
FIXED: [list commits/changes]
ALREADY OK: [list]
NEEDS CONTENT (not code): [covers, new FAQ Q&As, etc.]
PUSHED: yes/no — commit hash
```

---

## Do NOT

- Break NCR design or Zoe brand styling
- Copy QI theme files into NCR
- Publish future-dated posts
- Skip hugo build before push
