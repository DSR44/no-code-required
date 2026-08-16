---
title: "I Built an SEO Brain That Fixes My Blog for Free — Here's the Full Stack"
date: 2026-08-31
draft: false
description: "Stop paying $200/month for SEO tools. Here's the exact Python stack that scans, diagnoses, and auto-fixes every blog post — including AI slop detection."
tags: ["SEO", "automation", "no-code", "AI tools", "blogging"]
categories: ["tools"]
slug: "free-seo-brain-anti-slop-stack"
keywords: ["free SEO tools", "blog automation", "AI content detection", "SEO audit tool", "no-code SEO"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/free-seo-brain-anti-slop-stack.jpg"
  alt: "Terminal screen showing automated SEO scan results with code in the background"
faqs:
  - q: "How can I build a free SEO tool to fix my blog posts?"
    a: "You can build a free SEO tool using a Python stack that scans your blog, diagnoses issues like missing meta tags or poor readability, and auto-fixes them. The blog post details the exact open-source libraries and scripts to set this up without paying for expensive subscriptions."
  - q: "Can Python really replace paid SEO tools like Ahrefs or Semrush?"
    a: "For core tasks like on-page SEO auditing, keyword density checks, and AI content detection, a well-built Python stack can handle most of what paid tools offer. It won't replace advanced backlink analysis, but for blog optimization, it's a powerful free alternative."
  - q: "How do I detect AI-generated slop in my blog content?"
    a: "The Python stack includes an AI slop detection module that analyzes writing patterns, sentence structure, and repetitive phrasing common in low-quality AI content. It flags sections that sound unnatural or generic, helping you edit them for better readability and SEO."
  - q: "What's the full tech stack for an automated SEO blog fixer?"
    a: "The stack uses Python with libraries like BeautifulSoup for scraping, spaCy for NLP analysis, and custom scripts for SEO checks and auto-fixes. It integrates with your blog's CMS or markdown files to scan, diagnose, and update posts in one workflow."

---
{{< audio src="/audio/free-seo-brain-anti-slop-stack.mp3" >}}

I was paying $99 a month for an SEO tool that told me my score was "72 out of 100" and offered zero explanation of what that meant. So I built my own. It cost me nothing, runs on a schedule, and actually fixes the problems it finds.

Most SEO dashboards — they give you a number and leave you to figure out the rest. Mine doesn't give scores. It opens the hood, tells you exactly what's broken in plain language, and generates the fix. Think of it as a mechanic for your blog, not a report card.

I'm going to walk you through the entire stack — every tool, every connection, every automation. No coding experience required to understand it. If you can copy-paste into a terminal, you can run this.

## The Stack — In Order

Each piece handles one job. Here's how data flows through the system:

**Python + cron** — the orchestrator. Python runs the logic, cron fires it on a schedule. Think of cron as the alarm clock and Python as the person who wakes up and does the work. Every morning at specific times, different scripts activate without you touching anything.

**SQLite** — the memory. Every scan result, every issue found, every fix applied gets stored in a local database file. No cloud service, no subscription. It remembers what your blog looked like last week so it can tell you what changed.

**RSS scanners** — the topic scouts. These crawl competitor blogs, industry news sites, and [AI tool directories](/posts/ai-productivity-tools-what-actually-works-2026) every morning. They surface topics your competitors are covering that you haven't touched yet. The scanner digest lands in your calendar automatically.

**OpenRouter** — the writer. When a topic gets picked, OpenRouter connects to AI models to draft the content. But here's the catch — raw AI output is slop. Which brings us to the next piece.

**Anti-AI-Slop Engine** — the quality gate. Before any draft ships, it runs through a checklist of 50+ banned words, 30+ banned phrases, and structural patterns that signal "a robot wrote this." Common AI vocabulary — all flagged. Overused phrases that scream automation — caught and rewritten. If the draft scores too high on slop patterns, it gets rewritten before it ever touches your site. This matters because [Google is actively demoting AI-generated content](/posts/ai-content-flood-what-solo-builders-should-know).

**Notion** — the calendar. Tracks what's scheduled, what's drafted, what's published. The system reads it every 30 minutes to check if anything is due. You get one Telegram message when posts are ready — not a stream of notifications.

**Git + Hugo + Vercel** — the delivery pipeline. Hugo builds your static site from markdown files. Git tracks every change. Vercel hosts it globally with zero config. One push and the post is live. If something breaks, you roll back with one command.

**GSC API** — the feedback loop. Google Search Console tells you which posts are ranking, which are slipping from page 1 to page 2, and which keywords are gaining traction. This data feeds back into the system — posts dropping in rank get flagged for on-page fixes.

**Telegram** — the notification layer. You get alerts when a scan completes, when a post is flagged for slop, when something needs attention. No dashboard to check. The system comes to you.

## The Loop

Here's how it runs every day:

**GSC pulls ranking data** → identifies posts slipping from page 1 to page 2 (the "page-2 rescue" — these posts are close to ranking higher and need targeted fixes).

**On-page fixes get applied** → title tweaks, meta description updates, internal link additions, heading restructures. Small changes that push rankings up.

**RSS scanners find new topics** → competitor coverage, trending discussions, gap analysis against your existing content.

**New drafts get written** → AI generates the first draft from the scanner's topic picks.

**AI slop scan runs** → the draft gets checked against the banned word list, structural patterns, and punctuation tells. Too many hits? It gets rewritten. Clean? It moves forward.

**Ship** → the post goes live through Git push → Hugo build → Vercel deploy.

**Remeasure** → GSC picks up the new post within days. The loop starts again.

## Why This Beats Paid Tools

I've used Ahrefs, SEMrush, and Moz. They're fine if you want dashboards. But they share the same blind spot — they tell you *what* is wrong without telling you *why* it matters or *how* to fix it. You get a score and a generic checklist.

This stack tells you: "Your H1 and title don't match — Google uses both to understand your page topic, and right now they're telling it two different things." That's different from "H1 mismatch detected."

The anti-slop engine alone pays for itself. Google's March 2025 update specifically targeted AI-generated content. Posts that sound like a chatbot wrote them are getting buried. Having a automated gate that catches every lazy AI default before it ships? That's worth more than any SEO score.

## What It Costs

Nothing. Every tool in this stack is open-source or has a free tier:

| Tool | Cost |
|------|------|
| Python | Free |
| SQLite | Free |
| RSS scanners | Free (just HTTP requests) |
| OpenRouter | Pay-per-use (~$0.01 per draft) |
| Notion | Free tier works |
| Git + Hugo | Free |
| Vercel | Free tier (hobby projects) |
| GSC API | Free |
| Telegram Bot API | Free |

Total: roughly $0.01 per blog post in AI model costs. Compare that to $99-299/month for Ahrefs or SEMrush.

## The Bottom Line

You don't need expensive SEO tools to run a blog that ranks. You need a system that scans, fixes, and ships on autopilot — and catches AI slop before Google does. The full stack is sitting in a [GitHub repo](https://github.com/jalaalrd/anti-ai-slop-writing) and a handful of Python scripts. If you can run a terminal command, you can set this up in an afternoon.

Want to see what other automation I use for content? Check out [how I handle AI tool overwhelm](/posts/ai-tool-overwhelm-how-to-escape) — it pairs well with this stack.
