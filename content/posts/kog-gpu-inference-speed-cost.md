---
title: "How I Measured AI Wait Time Costs — and When Fast Mode Is Worth It"
date: 2026-10-27
draft: false
description: "A French startup claims 30x faster AI inference on GPUs you already own. I timed my own AI workflows to see what waiting really costs — here's the test."
tags: ["AI inference", "GPU", "AI tools", "productivity", "startups"]
categories: ["tools"]
slug: "kog-gpu-inference-speed-cost"
keywords: ["AI inference speed", "GPU inference optimization", "AI wait time cost"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/kog-gpu-inference-speed-cost.jpg"
  alt: "Zoe at a cafe table timing tasks with her phone beside a laptop running an AI workflow"
faqs:
  - q: "What is Kog claiming?"
    a: "The French startup Kog says software optimization can get dramatically faster AI inference out of the standard datacenter GPUs enterprises already own — its demo hit 3,000 tokens per second per request, with a 30x speedup as the stated goal."
  - q: "Did the demo work on a laptop GPU?"
    a: "No. The demo ran on datacenter-class hardware (AMD MI300X and Nvidia H200). Consumer laptop GPUs were not part of it, which disappointed some of the Hacker News crowd."
  - q: "Why does inference speed matter for non-coders?"
    a: "Because you pay for waiting twice: once in money (premium speed tiers like Claude's Fast Mode) and once in interrupted focus. If a 10-minute task takes an hour of waiting, that hour is your real cost."
  - q: "When is paying for faster AI worth it?"
    a: "When the wait interrupts work you'd otherwise be actively doing — not when the task runs in the background while you do something else. Fast tiers pay off on interactive workflows, not batch jobs."
---

{{< audio src="/audio/kog-gpu-inference-speed-cost.mp3" >}}

A French startup says it can squeeze 30 times more speed out of the GPUs you already pay for — and while the chip companies race to build new silicon, Kog's bet is that software alone can unlock what's sitting idle in the hardware. That story got me thinking about something less glamorous and more immediate: how much time I personally lose waiting for AI to finish thinking. I timed my own workflows for a week. The number was embarrassing, and the fix cost nothing.

The news first, because it sets the stakes. Kog hit the front page of Hacker News in May with a demo showing real-time LLM inference at 3,000 tokens per second per request on standard datacenter GPUs — the AMD MI300X and Nvidia H200 that enterprises already own. The caveat matters: that demo used a small, purpose-built 2-billion-parameter model (now open-sourced as Laneformer 2B), not the giant models most of us use. But CEO Gaël Delalleau — a solid-state physicist turned white-hat hacker who reverse-engineers GPUs down to the assembly level — is confident the same approach scales. And the market agrees there's demand: inference speed has become a bottleneck worth paying for, with Anthropic charging a price multiple for Claude's Fast Mode. This hardware-and-software race has real consequences for what you'll pay — it's the same dynamic behind [Anthropic building its own chips](/posts/anthropic-in-house-silicon-team/) and [ZML making inference hardware-agnostic](/posts/zml-free-inference-tool-ai-chips/).

## What I actually did

Kog's first target market is telling: software engineering, where users of coding agents wait hours for results. But you don't need to be a developer to have the same problem — you just haven't measured it.

So I measured. For one work week, every time I used an AI tool — drafting, image generation, long document analysis, agent runs — I started a timer and noted whether I was actively waiting (staring at a spinner) or passively waiting (task runs while I do something else). I also noted which tool and which tier.

The results: about 3 hours and 40 minutes of active waiting across the week. The worst offender was long document analysis — 20-plus minutes of staring at a progress bar while my focus evaporated. Image generation was fast but frequent. And roughly 90 minutes of that waiting happened inside tasks I'd have paid a premium to shorten.

## Do this yourself

Twenty minutes to set up, a week to collect:

1. **Pick your top five AI tasks.** The ones you do most often: drafts, edits, images, research summaries, agent runs.
2. **Time them for a week.** Phone timer, two columns: active wait (you're blocked) and passive wait (you're free). Don't estimate — measure. Everyone overestimates the big tasks and forgets the frequent small ones.
3. **Convert active wait to money.** Your hourly rate times your weekly active-wait hours. If it's over $50 a week, you have a real decision to make.
4. **Check the fast tier math.** For your worst interactive task, compare the fast-mode price against the minutes it saves. If a fast tier costs a few dollars extra and saves 30 minutes of blocked time, it's cheap. If it saves nothing because the task runs in the background, skip it. The same math applies to which subscriptions deserve your money — see [what to actually pay for in the AI subscription wars](/posts/ai-subscription-price-war-what-to-pay-for/).
5. **Restructure one workflow.** Take your biggest active-wait task and make it passive: split the document, run it while you do something else, or batch it to the end of the day. This costs nothing and often beats paying for speed.

If your wait problems are really agent problems — multiple steps, retries, machine-driven installs — that's a different fix, covered in [how coding agents taught robots to install GPUs](/posts/ai-coding-agents-taught-robots-install-gpus/).

## What failed

Two honest misses.

**Fast Mode wasn't worth it for me.** I tested the premium speed tier on my two worst tasks. On the document-analysis task it saved real minutes — worth it. On image generation it saved seconds I didn't feel, because generation is inherently a background task for me. Speed pricing only pays where waiting blocks you.

**Batching backfired once.** Moving a daily drafting task to "end of day" meant I did it when my energy was gone, and the quality dropped enough that I redid it — losing more time than the wait ever cost. Some waits are cheaper than bad timing.

## Who should skip this

If your AI use is occasional and conversational — quick questions, short answers — your wait time is rounding-error small. Skip the measurement.

Skip it too if you already batch everything asynchronously; you've solved this problem structurally. But if any part of your day involves watching an AI tool think — long reports, big edits, agent chains — the Kog story is your preview of coming price tags. The startups racing to fix inference speed are pricing your impatience, and knowing your own number is how you stay on the right side of it. It's worth asking, too, whether the tools you wait for are actually the right ones — [what AI productivity tools actually deliver](/posts/ai-productivity-tools-what-actually-works-2026/) is a companion question.

## The takeaway

The inference speed race will play out over years — Kog still has to prove its approach works on large models, and its Series A depends on it. But you don't have to wait for the industry to fix your waiting. One week of honest timing tells you what those spinners cost, and most of the fix is free: restructure the task before you pay for the speed.
