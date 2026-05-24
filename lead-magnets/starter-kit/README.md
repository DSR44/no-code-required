# The $0 AI Starter Kit — PDF source

Same pipeline as Sparklebox (`build_pdf.py` + Playwright).

## Rebuild after editing `source.html`

```bash
cd lead-magnets/starter-kit
npm install          # first time only
npx playwright install chromium   # first time only
python3 build_pdf.py
```

Output: `api/assets/the-0-dollar-ai-starter-kit.pdf` (email attachment only — not a public URL)

Landing page: `/starter-kit/`
