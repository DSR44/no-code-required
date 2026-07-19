---
title: "How I Use AI to Run Two Blogs Without Hiring Anyone | NCR"
date: 2026-06-03
draft: false
description: "Discover the exact AI automation workflow that lets one person publish on two blogs solo — no team, no VA, no code required. Save 15+ hours weekly."
tags: ["AI tools", "automation", "blogging", "solopreneur"]
categories: ["tools"]
slug: "how-i-use-ai-to-run-two-blogs-without-hiring-anyone"
keywords: ["how to run a blog with ai automation", "ai blog workflow solo creator", "automate blog publishing ai"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/how-i-use-ai-to-run-two-blogs-without-hiring-anyone.jpg"
  alt: "Zoe at a laptop with automation workflow diagrams on screen"
---
{{< audio src="/audio/how-i-use-ai-to-run-two-blogs-without-hiring-anyone.mp3" >}}

I run two blogs. Not one — two. And I do it alone, without a content team, a virtual assistant, or a single line of code. The secret isn't working harder. It's building a system that does the boring parts for you.

Most "AI blogging" advice stops at "use ChatGPT to write your posts." That's like saying the secret to a restaurant is buying ingredients. The actual work is in the kitchen — the prep, the timing, the workflow that turns raw materials into something worth serving. I spent months building that kitchen, and I'm going to show you exactly how it works.

## The two blogs (and why automation matters)

I run [Quiet Inflammation](https://quietinflammation.com) — a health and wellness blog — and [No Code Required](https://nocoderequired.net) — this blog, where I teach non-technical people how to use AI tools. Both publish regularly. Both need research, writing, images, audio narration, and SEO optimization.

If I did all of that manually for both blogs, I'd need 30+ hours a week just on content. That's a full-time job on top of whatever else I'm building. So I automated the parts that don't need my voice, and kept the parts that do.

The result? I publish multiple posts per week across both sites, and the actual hands-on time per post is roughly 45 minutes. Here's how.

## Step 1: Research — let the tools find what matters

Every post starts with research, but I'm not Googling for an hour. I have two systems running in the background.

**Blogwatcher** monitors RSS feeds and scrapes new articles from sources I've curated — Reddit threads, wellness blogs, no-code communities, even bioRxiv for health science. Every day it pulls in new content and flags what's trending. I scan the output in 5 minutes and spot what's worth writing about.

**Web search** fills the gaps. When I pick a topic, I search for the top 3 competitor articles and read them. Not to copy — to find what they missed. Most competitor content is either too shallow ("10 Best AI Tools!") or too technical. I write for the person in between — the one who wants to actually do something, not just read about it.

If you want to set up your own monitoring, I wrote about [building your first automation in 15 minutes](/posts/build-your-first-automation-in-15-minutes/) — it covers the basics of RSS triggers and simple workflows.

## Step 2: Writing — AI as co-writer, not ghostwriter

Here's where most people get it wrong. They ask ChatGPT to "write a blog post about X" and publish whatever comes out. That's not automation — that's delegation to a machine that doesn't know your voice.

I use AI differently. I give it my research, my angle, my outline, and ask it to help me flesh out sections. The structure and voice are mine. The AI handles the heavy lifting of turning bullet points into flowing paragraphs. Think of it like having a writing partner who's really fast at first drafts but needs your editorial eye.

My writing stack is simple:
- **Research notes** from blogwatcher and web search
- **Outline** that I create based on what competitors missed
- **AI assistance** to expand sections, suggest transitions, and check readability
- **My edit pass** — this is where the voice happens, and it's non-negotiable

The edit pass is the part you can't automate. It's what makes the post yours. I wrote more about this in [the tools I actually use every day](/posts/the-tools-i-actually-use-every-day/) if you want the full breakdown.

## Step 3: Images — consistent brand without a designer

Every post needs a cover image. Every image needs to match the blog's brand. Without automation, that's 20-30 minutes of fiddling with Canva or Midjourney per post.

I built a script that generates cover images automatically. For No Code Required, the images use Zoe — our editorial avatar — in warm coffee-shop settings. For Quiet Inflammation, it's Naia in lo-fi anime style. The script enforces 16:9 landscape format, applies the right style for each blog, and saves the image to the correct folder.

One command. Thirty seconds. Done.

If you're curious about the AI image tools landscape, I tested a bunch of them in [AI images — which tool actually works](/posts/ai-images-which-tool-actually-works/).

## Step 4: Audio narration — every post gets a voice

Every single post on both blogs gets an audio version. Not because I love extra steps — because a significant chunk of my readers prefer listening. Commuting, cooking, walking the dog — they consume content differently.

ElevenLabs handles this. I extract the clean body text (no frontmatter, no markdown), send it to their API with Rachel's voice, and save the MP3 to the static folder. The blog's audio player picks it up automatically.

The whole process takes about 2 minutes per post, including the time it takes the API to generate the audio. Compare that to recording yourself for every post — that's easily 15-20 minutes saved per article.

## Step 5: SEO and links — the part people skip

This is where most solo bloggers drop the ball. They write a great post, publish it, and move on. No internal links. No meta description. No keyword targeting. Then they wonder why Google doesn't send traffic.

I have a checklist that runs automatically:
- **Internal cross-links** — every post links to 5-10 related posts on the site. I have a database of all published posts, and the system suggests relevant links based on tags and categories.
- **External tool links** — every tool I mention gets a direct link. No "just Google it" laziness.
- **Meta description** — auto-generated from the first paragraph, trimmed to 155 characters.
- **Keywords** — pulled from my keyword research and included in the frontmatter.

The internal linking alone has been huge for SEO. Google sees that my posts connect to each other like a web, not isolated pages. That signals authority. I broke down the whole data-exchange layer in [APIs explained like you're 5](/posts/apis-explained-like-youre-5/) if you want to understand how tools talk to each other under the hood. And if you're wondering whether any of this actually translates to income, I covered that honestly in [how to actually make money with AI tools](/posts/how-to-actually-make-money-with-ai-tools/).

## Step 6: Publish and verify — the final gate

After all the pieces are in place, publishing is one command. But I don't just push and pray. The system runs a validation pass first — checks that the image exists, the audio file is there, the frontmatter is complete, and the links aren't broken.

Only after everything passes does the post go live. And then I verify the deployment actually succeeded — because a git push isn't a published post. The site has to build and deploy correctly.

This catches problems before readers do. Broken images, missing audio, formatting issues — all fixed before they become your problem.

## The full pipeline at a glance

Here's what the workflow looks like end to end:

1. **Blogwatcher scan** → spot trending topics (5 min)
2. **Web search** → read top 3 competitors (10 min)
3. **Write with AI assist** → outline + expand + edit (30 min)
4. **Cover image** → one command, brand-consistent (30 sec)
5. **Audio narration** → ElevenLabs API call (2 min)
6. **SEO pass** → links, meta, keywords (5 min)
7. **Validate + publish** → one command (1 min)

Total: roughly 50 minutes per post. For two blogs. With consistent branding, audio, and SEO on every single article.

## What you can't automate

I want to be honest about this. The system handles the mechanics — the repetitive, time-consuming parts that burn you out. But the things that make a blog worth reading? Those are still human.

**Your perspective** — AI can write paragraphs, but it can't decide what matters. The angle you choose, the gaps you spot in competitor content, the things you decide to say that nobody else is saying — that's you.

**Your voice** — Even with AI assistance, every post goes through my edit pass. I rewrite sentences that sound generic. I add the analogies that make things click. I cut the filler. The final product sounds like me, not like a template.

**Your judgment** — What to publish, when to publish, what to skip, what to double down on. No automation can make those calls. They require taste, and taste is built by doing the work.

## The bottom line

Running two blogs solo isn't about being superhuman. It's about building a system that handles the 80% of work that's repetitive, so you can pour your energy into the 20% that actually matters. AI is the engine. You're still the driver.

If you want to start building your own automation pipeline, [start here](/start-here/) — I put together a guide for exactly this kind of setup. No code required. Obviously.
