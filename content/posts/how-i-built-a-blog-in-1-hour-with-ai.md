---
title: "How I built a blog in 1 hour with AI"
date: 2026-05-02
draft: false
tags: [ai tools, no code, blogging, hugo, vercel, beginner]
categories: [AI Tools]
description: "I'd never built a website before. Used AI to set up a blog, deploy it, and publish my first post — all in under an hour. Here's exactly how."
ShowToc: true
cover:
    image: "/images/posts/how-i-built-a-blog-in-1-hour.jpg"
    alt: "Building a blog with AI tools"
    caption: ""
howto:
  totalTime: "PT60M"
  estimatedCost:
    currency: "USD"
    value: "10"
  steps:
    - name: "Set up Hugo with AI guidance"
      text: "Ask ChatGPT or Claude to walk you through installing Hugo, creating the blog structure, and writing your first post as a text file."
    - name: "Install a theme"
      text: "Pick a Hugo theme like PaperMod and install it with one git submodule command."
    - name: "Write your first post"
      text: "Create a markdown file with frontmatter title and date, then write your content in plain text."
    - name: "Deploy to Vercel via GitHub"
      text: "Push files to GitHub, connect the repo to Vercel, and click Deploy — every future push auto-updates the site."
    - name: "Add a custom domain"
      text: "Buy a domain and add DNS records pointing to Vercel — takes about 5 minutes with AI walking you through it."
---

# How I built a blog in 1 hour with AI

I'd never built a website before. Never touched a terminal. Never used GitHub. Didn't know what "deploy" meant.

Last month, I built this blog. Published my first post. Got it live on the internet.

The whole thing took about an hour.

Here's exactly how — no jargon, no assumptions, just the steps.

## What you need (almost nothing)

Before I started, I thought I'd need:
- A computer science degree ❌
- Coding skills ❌
- A developer ❌
- Thousands of dollars ❌

What I actually needed:
- A [GitHub](https://github.com) account (free) ✅
- A [Vercel](https://vercel.com) account (free) ✅
- An AI tool ([ChatGPT](https://chat.openai.com), [Claude](https://claude.ai), whatever you use) ✅
- About 60 minutes ✅

Total cost: $0.

## Step 1: I asked AI to build me a blog

I opened ChatGPT and typed:

> "I want to build a blog. I don't know how to code. Walk me through it step by step."

It suggested Hugo — a tool that generates blogs from simple text files. No database, no WordPress, no monthly fees. Just text files that become a website. ([See Hugo in action](https://gohugo.io))

Then it walked me through:
1. Installing Hugo (3 commands)
2. Creating the blog structure (1 command)
3. Writing my first post (just a text file)
4. Deploying to Vercel (connect GitHub, click deploy)

Every time I got stuck, I asked AI. It explained what went wrong and how to fix it. Like having a developer friend on speed dial.

## Step 2: I chose a theme

Hugo has hundreds of free themes. I picked PaperMod — clean, dark, fast. AI showed me how to install it:

```
git submodule add https://github.com/adityatelange/hugo-PaperMod themes/PaperMod
```

That's it. One command. My blog suddenly looked professional.

## Step 3: I wrote my first post

Hugo posts are just text files with a tiny header:

```markdown
---
title: "My first post"
date: 2026-05-01
draft: false
---

Your content here. Just write normally.
```

No HTML. No formatting codes. Just write.

I wrote about why I was starting the blog. Honest, simple, no fluff. That became my first post.

## Step 4: I deployed it

This is where I thought it would get hard. It didn't.

1. Created a GitHub account (free)
2. Pushed my blog files to GitHub
3. Connected GitHub to Vercel
4. Clicked "Deploy"

Vercel built my blog and gave me a URL. Done.

Every time I push new content to GitHub, Vercel automatically updates the site. No manual uploads, no FTP, no server management.

## Step 5: I added a custom domain

I bought a domain on Namecheap ($10/year). Then I told AI:

> "I bought nocoderequired.net. How do I connect it to Vercel?"

It walked me through adding DNS records. Took 5 minutes. Now my blog lives at nocoderequired.net.

## What surprised me

**It was easier than I expected.** I thought building a website was for developers. Turns out, it's just following steps — and AI can explain every step in plain English.

**The hard part wasn't technical.** The hard part was deciding what to write about. The tech was just a tool.

**Free tools are powerful.** GitHub, Vercel, Hugo — all free. My blog costs $10/year (domain only). Compare that to WordPress hosting at $30/month.

**AI is the real upgrade.** Without AI, I'd have spent weeks learning Hugo, Git, deployment. With AI, I did it in an hour by asking questions.

## What I'd do differently

Looking back, there are a few things I'd change:

1. **Start with the domain first.** I built the whole blog on a Vercel subdomain, then had to reconnect everything when I bought nocoderequired.net. Buy the domain first ($10/year on Namecheap or Cloudflare).

2. **Write 5 posts before publishing.** I published with just one post. The blog looked empty. Write 5 posts first, then go live. Your visitors will stay longer.

3. **Set up analytics from day one.** I waited weeks before adding Vercel Analytics (free). Now I know which posts people read. Add it on day one.

4. **Don't overthink the theme.** I spent 2 hours comparing themes. PaperMod was the right choice from the start. Pick one, move on. You can change it later.

5. **Ask AI to review your posts.** After writing, paste your draft into AI and ask: "What's missing? What would a beginner ask?" It'll find gaps you didn't see.

## Comparison: different ways to build a blog

| Method | Cost | Difficulty | Time | Best for |
|--------|------|------------|------|----------|
| **Hugo + Vercel** (what I used) | $0-10/year | Easy with AI | 1 hour | Fast, free, no maintenance |
| WordPress | $30-100/month | Medium | 2-3 hours | Plugins, SEO tools, flexibility |
| Squarespace | $16-49/month | Easy | 1-2 hours | Beautiful templates, drag-and-drop |
| Ghost | $9-25/month | Easy | 1 hour | Newsletter integration, paid subscriptions |
| Medium | Free | Easiest | 10 minutes | No setup, built-in audience, but no control |

I went with Hugo because:
- **Free forever** (no monthly fees)
- **Fast** (static sites load instantly)
- **No maintenance** (no updates, no security patches)
- **Full control** (you own everything)

The tradeoff: it's slightly more technical than Squarespace. But with AI walking you through it, that tradeoff disappears.

## The tools I used

- **[Hugo](https://gohugo.io)** — static site generator (free)
- **[PaperMod](https://github.com/adityatelange/hugo-PaperMod)** — theme (free)
- **[GitHub](https://github.com)** — code storage (free)
- **[Vercel](https://vercel.com)** — hosting + deployment (free)
- **ChatGPT / Claude** — my guide through the whole process
- **[Namecheap](https://namecheap.com)** — domain ($10/year)

All free except the domain. Total startup cost: $10.

## Can you do this?

Yes. If I can do it with zero coding experience, you can too.

The only skill you need is knowing how to ask questions. And you already know how to do that.

**Start here:**
1. Open your AI tool of choice ([ChatGPT](https://chat.openai.com) or [Claude](https://claude.ai))
2. Type: "I want to build a blog. I don't know how to code. Help me."
3. Follow the steps
4. Ask when you get stuck

That's it. One hour. Your blog is live.

**Want to see what I built?** Check out the [Tools page](/tools/) — all the AI tools I actually use, organized from beginner to power user.

---

**Related reading:**
- [What is AI actually?](/posts/what-is-ai-actually/) — the basics explained without the jargon
- [I didn't plan to learn AI](/posts/i-didnt-plan-to-learn-ai/) — how I got started
- *The tools I actually use every day* (coming May 3) — my real toolkit
- *AI images: which tool actually works?* (coming May 4) — honest comparison

**External resources:**
- [Hugo documentation](https://gohugo.io/documentation/) — official Hugo docs
- [PaperMod theme guide](https://github.com/adityatelange/hugo-PaperMod/wiki) — theme setup
- [Vercel deployment docs](https://vercel.com/docs) — hosting guide
- [GitHub for beginners](https://docs.github.com/en/get-started) — Git basics

---

*Some links in this post may be affiliate links. If you sign up through them, I may earn a small commission at no extra cost to you. I only recommend tools I actually use.*
