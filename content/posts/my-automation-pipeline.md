---
title: "My automation pipeline"
date: 2026-05-20
draft: false
tags: ["AI tools", "automation", "no-code", "n8n", "productivity", "build in public"]
categories: ["tools"]
description: "I built an automated content pipeline that runs itself. Blog posts get written, published, distributed, and announced — all without me touching anything. Here's how it works and how you can build one too."
ShowToc: true
cover:
  image: "/images/posts/my-automation-pipeline.jpg"
faqs:
  - q: "How can I automate my blog publishing and distribution?"
    a: "You can build an automation pipeline using no-code tools like Zapier or Make to connect your writing, publishing, and social media platforms. The system triggers each step automatically, so a new post gets published and shared without manual intervention."
  - q: "Which tools are needed for a hands-off content pipeline?"
    a: "A typical stack includes a content management system like WordPress, an automation platform like Zapier, and social media schedulers like Buffer. These tools connect via APIs to pass your content through each stage seamlessly."
  - q: "Can I set up automated announcements for new blog posts?"
    a: "Yes, you can configure your automation to send notifications to email lists, Slack channels, or Discord servers whenever a post goes live. This ensures your audience is alerted immediately without you having to send a single message."
  - q: "How do I ensure my automated pipeline runs reliably?"
    a: "Start by testing each connection in your workflow individually before linking them together. Use built-in logging and error notifications in your automation platform to monitor runs and quickly fix any failures."

---

I used to publish content like this: write the post, log into WordPress, paste it in, format it, add images, publish, then manually share it on five different platforms. Each post took 30 minutes just to distribute.

Now my pipeline does all of that. I write. Everything else happens automatically.

Here's the exact system — no fluff, no "you should try automation." Just the pipeline.

---

## What the pipeline does

**The flow:**
1. I write a blog post (Markdown file)
2. I push it to GitHub
3. GitHub builds the site automatically
4. An RSS monitor detects the new post
5. A notification bot announces it on Telegram
6. Social media posts get scheduled automatically
7. A Notion database tracks what's published and what's not

**The entire distribution chain — from "I'm done writing" to "the world can see it" — takes about 3 minutes. Most of that is the git push.**

---

## The tools in my pipeline

### GitHub + Hugo — the content layer

I write in Markdown. Plain text. No WordPress, no WYSIWYG editor, no drag-and-drop. Just me and a text file.

When I push to GitHub, Hugo (a static site generator) builds the entire website in about 2 seconds. No database. No server-side rendering. Just static HTML that loads instantly.

**Why this matters:** My blog loads in under 1 second. No plugins to update. No security vulnerabilities. No hosting bills beyond the free tier.

### RSS Monitor — the trigger

I have a script that checks my blog's RSS feed every 30 minutes. When it detects a new post, it triggers the rest of the pipeline.

This is the "listener" — it watches for changes and kicks off everything downstream.

### Telegram Bot — the notification layer

When a new post is detected, my Telegram bot sends me a message with the title, URL, and a summary. It also sends the post to a notification channel.

**Why Telegram:** It's free. It's instant. It has a bot API that's easy to work with. Discord works too, but Telegram is simpler for personal notifications.

### Notion — the tracking layer

Every post gets logged in a Notion database with:
- Title
- Publish date
- Status (Draft / Published)
- Topic
- Blog (which site it's for)
- URL (when published)

The Notion database is my single source of truth. I can see everything that's scheduled, everything that's published, and everything that's still in draft.

### n8n — the glue

n8n connects everything. It watches the RSS feed, calls the Telegram bot, updates the Notion database, and can trigger social media posts.

**Why n8n:** It's free. Self-hosted. Visual workflow builder. I can see exactly what's happening at each step. When something breaks, I can trace the issue in 30 seconds.

---

## The setup (how to build your own)

**Step 1: Content layer**
- Pick a static site generator (Hugo, Astro, Next.js)
- Host on GitHub Pages, Vercel, or Netlify (all free)
- Write in Markdown

**Step 2: RSS feed**
- Most static site generators produce an RSS feed automatically
- Hugo: `/index.xml`
- Astro: `/rss.xml`
- Verify your feed URL exists

**Step 3: Monitor + trigger**
- Use n8n, Make, or a simple cron job
- Check the RSS feed every 30 minutes
- Compare with the last known post
- If new → trigger notification

**Step 4: Notification**
- Create a Telegram bot (BotFather, 5 minutes)
- Get your chat ID
- Send a message when new content is detected

**Step 5: Tracking**
- Create a Notion database
- Add columns: Title, Date, Status, Topic, URL
- Use Notion's API to auto-update when posts are published

**Step 6: Social media**
- Use n8n to schedule posts across platforms
- Or use a tool like Postiz, AiToEarn, or Buffer
- Auto-post when RSS detects new content

---

## What this cost me

| Component | Cost |
|-----------|------|
| GitHub Pages | Free |
| Hugo | Free |
| n8n (self-hosted) | Free |
| Telegram Bot | Free |
| Notion | Free |
| VPS for n8n | $5/month |

**Total: $5/month.** That's it. No monthly SaaS subscriptions. No per-task pricing. No hidden fees.

Compare that to:
- WordPress hosting: $10-30/month
- Zapier: $20-50/month (per task pricing kills you)
- Social media scheduler: $15-30/month
- Newsletter tool: $10-50/month

**I'm saving $50-100/month by building my own pipeline.** And it works better because I control every piece.

---

## What I'd do differently

If I started over:

1. **Start with n8n from day one.** I wasted months on custom scripts before switching to a visual workflow tool.

2. **Use a hosted Hugo service** (like Cloudflare Pages) instead of self-hosting. Free, faster, zero maintenance.

3. **Add social media automation earlier.** I was manually posting to Instagram and Twitter for months before automating it.

4. **Track metrics from the start.** I should have been logging views, clicks, and engagement from day one. I started tracking too late.

---

## The real value

The pipeline saves me about 2 hours per week on distribution. That's 100 hours per year. But the real value isn't time — it's consistency.

When distribution is automatic, I never forget to share a post. I never skip the notification. I never "do it later" and then forget. The pipeline doesn't have bad days. It doesn't get lazy. It just works.

**That consistency is what builds an audience.** Not one viral post. Not a clever hack. Showing up every day, reliably, with the pipeline handling the boring stuff while I focus on writing.

---

*Want me to share the exact n8n workflow? Drop a comment and I'll post the JSON.*

---

*This post mentions tools I use daily. No affiliate links — I just like them.*
