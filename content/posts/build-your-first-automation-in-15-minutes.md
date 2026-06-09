---
title: "Build your first automation in 15 minutes"
date: 2026-05-13
draft: false
description: "You've heard about automation but never built one. Here's your first — takes 15 minutes, costs nothing, and saves you 30 minutes every day."
tags: ["AI tools", "automation", "no-code", "Zapier", "n8n", "tutorial", "beginner", "productivity"]
categories: ["tools"]
slug: "build-your-first-automation-in-15-minutes"
cover:
  image: "/images/posts/build-your-first-automation-in-15-minutes.jpg"
howto:
  totalTime: "PT15M"
  estimatedCost:
    currency: "USD"
    value: "0"
  steps:
    - name: "Create a Zapier account"
      text: "Go to zapier.com, sign up for free, and click Create Zap."
    - name: "Set the trigger"
      text: "Search for Gmail (or your email provider), select New Email as the trigger, connect your account, and filter to a specific sender so only important emails run the automation."
    - name: "Set the action"
      text: "Search for Google Sheets, select Create Spreadsheet Row, connect Google, pick your sheet, and map email subject, sender, date, and body to columns."
    - name: "Test the Zap"
      text: "Click Test in Zapier, confirm a matching email appears as a new row in your Google Sheet, then fix field mapping if anything is wrong."
    - name: "Publish and turn it on"
      text: "Click Publish, name your Zap, and turn it on so every matching email logs automatically."
---

# Build your first automation in 15 minutes

I built my first automation to solve a problem I had every single morning: I'd check 5 websites for updates, then copy-paste the interesting ones into a note. It took 20 minutes. Every day.

So I built an automation that does it for me. It runs at 8am. It checks all 5 sites. It sends me a summary. I haven't done it manually since.

Here's how to build your first one — even if you've never touched an automation tool before.

## Pick your tool

Three options, pick based on your comfort level:

**Zapier** — easiest. Drag and drop. Most integrations. Free tier: 100 tasks/month.
→ [zapier.com](https://zapier.com)

**Make** — more visual, more control. Free tier: 1,000 operations/month.
→ [make.com](https://make.com)

**n8n** — most powerful, open source. Free if you self-host.
→ [n8n.io](https://n8n.io)

For your first automation, use **Zapier**. It's the fastest path from zero to working.

## The automation: Email → Spreadsheet

This is the simplest useful automation. Every time you get an email from a specific sender (a client, a newsletter, a service), it automatically logs it to a Google Sheet.

Why this matters: it creates a searchable record of important emails without you doing anything.

### Step 1: Create a Zapier account (2 minutes)

1. Go to [zapier.com](https://zapier.com)
2. Sign up (free)
3. Click "Create Zap"

### Step 2: Set the trigger (3 minutes)

1. Search for "Gmail" (or your email provider)
2. Select "New Email" as the trigger
3. Connect your email account (Zapier walks you through this)
4. Set a filter: only trigger on emails from a specific sender (e.g., your boss, a client, a service)

**Why filter:** without it, every email triggers the automation. You only want the important ones.

### Step 3: Set the action (3 minutes)

1. Search for "Google Sheets"
2. Select "Create Spreadsheet Row" as the action
3. Connect your Google account
4. Select the spreadsheet and worksheet
5. Map the fields: email subject → Column A, sender → Column B, date → Column C, body → Column D

### Step 4: Test it (2 minutes)

1. Click "Test" in Zapier
2. It'll pull a recent email that matches your filter
3. Check your Google Sheet — did it appear?
4. If yes, you're done

### Step 5: Turn it on (1 minute)

1. Click "Publish"
2. Name your Zap (e.g., "Client emails to Sheet")
3. Turn it on

That's it. Every matching email now gets logged automatically. You just saved 5 minutes per day — 30 hours per year.

## Three more automations to build next

### Automation 2: Social media backup (10 minutes)

**Trigger:** New post on your Instagram/Twitter
**Action:** Save the caption + link to a Google Sheet

Why: if your account gets suspended, you have a backup of all your content.

### Automation 3: New subscriber notification (5 minutes)

**Trigger:** New subscriber on your email list (Mailchimp, ConvertKit, etc.)
**Action:** Send yourself a Slack/Discord/Telegram message

Why: you know instantly when someone joins. Makes the growth feel real.

### Automation 4: File organizer (10 minutes)

**Trigger:** New file in a specific Google Drive/Dropbox folder
**Action:** Move it to a subfolder based on file type (PDFs → /PDFs, images → /Images)

Why: your downloads folder is chaos. This fixes it.

## What automation actually is

Automation isn't "AI doing your job." It's a rule that runs without you.

"If X happens → do Y."

That's it. Every automation is just this pattern:
- **Trigger** — the "if" (new email, new form submission, scheduled time)
- **Action** — the "then" (send email, create row, post message)

Once you understand that pattern, you can automate anything.

## The comparison

| Tool | Best for | Free tier | Learning curve |
|------|---------|-----------|----------------|
| [Zapier](https://zapier.com) | Beginners, quick wins | 100 tasks/mo | Easy |
| [Make](https://make.com) | Visual thinkers | 1,000 ops/mo | Easy-Medium |
| [n8n](https://n8n.io) | Developers, full control | Self-hosted free | Medium |
| [IFTTT](https://ifttt.com) | Smart home, simple triggers | Free | Easy |
| [Pipedream](https://pipedream.com) | API-heavy workflows | Free | Medium-Hard |

## Start with 15 minutes

Don't try to automate your whole business. Build one automation. Use it for a week. See if it actually saves time.

If it does, build the next one. If it doesn't, delete it and try a different one.

The best automations are the ones you forget exist — because they just work.

---

**Coming soon:**
- *Voice AI: what GPT-5 can actually do now* (coming June 14) — voice agents explained
- *The ChatGPT education study that got retracted* (coming June 15) — what went wrong
- *AI orchestrators: one model controlling all the others* (coming June 16) — the next layer

---

*Some links in this post may be affiliate links. If you sign up through them, I may earn a small commission at no extra cost to you. I only recommend tools I've actually tested.*
