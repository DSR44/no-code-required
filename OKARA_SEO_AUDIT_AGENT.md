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
- FAQ partial: `layouts/partials/schema_faq.html` on `/faq/` and posts with `faqs:` frontmatter
- Check posts missing: `description`, `keywords`, `cover.image`, duplicate H1 in body
- Okara citation gaps (Zapier cited instead of NCR) → ensure `/faq/` Q&As target those queries

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
