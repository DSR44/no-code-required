---
title: "Spatial AI Agents Are Coming: What Solo Builders Should Build Right Now"
date: 2026-07-07
draft: false
description: "General Intuition raised $2.3B to train AI agents on video game data. What spatial AI means for solo builders and the tools you should start building today."
tags: ["AI tools", "AI agents", "spatial AI", "solo builders", "automation"]
categories: ["tools"]
slug: "spatial-ai-agents-what-to-build-now"
keywords: ["spatial AI agents solo builders", "General Intuition AI video games", "build AI agents spatial intelligence"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/spatial-ai-agents-what-to-build-now.jpg"
  alt: "Zoe at laptop with spatial AI visualization and agent workflow on screen"
faqs:
  - q: "What \"spatial AI\" actually means for builders"
    a: "Today's AI agents — the ones powering automated workflows and tool-calling systems — operate in text space. They read data, process instructions, and output text or API calls. They're powerful but blind. They can't see a screen, navigate an interface, or understand physical context."
  - q: "What I'd build first"
    a: "If I were starting today, I'd build a visual browser agent for a specific niche — not a general-purpose tool. Pick one industry (e-commerce, real estate, healthcare admin) and build an agent that can navigate their specific interfaces."
---
{{< audio src="/audio/spatial-ai-agents-what-to-build-now.mp3" >}}

A startup just raised $2.3 billion to teach AI agents how to navigate the real world by watching teenagers play Fortnite. That sentence sounds absurd until you understand what General Intuition is actually building: AI that understands space, time, and movement — not just text. If you're a solo builder, the question isn't whether this technology will matter. It's what you should be building right now to ride the wave.

I covered [what General Intuition does and why video game data is different](/posts/general-intuition-ai-agents-video-game-data/) in my last post. This one is about the practical implications — what spatial AI agents change for the tools you build and the businesses you run.

## What "spatial AI" actually means for builders

Today's AI agents — the ones powering [automated workflows](/posts/build-your-first-automation-in-15-minutes/) and [tool-calling systems](/posts/ai-agents-explained-what-tool-calling-actually-means/) — operate in text space. They read data, process instructions, and output text or API calls. They're powerful but blind. They can't see a screen, navigate an interface, or understand physical context.

Spatial AI changes that. General Intuition's world models are trained on 2 billion video game clips per year — first-person footage of players making decisions, navigating environments, and responding to real-time events. The AI learns spatial reasoning, cause and effect, and anticipatory decision-making by watching how humans interact with dynamic environments.

For solo builders, this means the next generation of AI agents won't just automate text tasks. They'll automate visual tasks — navigating apps, interpreting dashboards, moving through interfaces, and making decisions based on what they see on screen.

## Three things to build right now

### 1. Visual workflow agents

Current automation tools like [Zapier](/posts/zapier-pricing-2026-what-you-pay/) and [Make](/posts/make-vs-zapier-which-one-is-actually-easier/) work through APIs — structured connections between apps. But most business processes still involve clicking through interfaces, reading dashboards, and making visual judgments.

A visual workflow agent could: log into your Shopify dashboard, identify products with declining sales, check competitor pricing on Amazon, and draft a pricing adjustment recommendation. Not through APIs — by actually looking at the screen and understanding what it sees.

The building blocks are already here. Browser automation tools like Playwright and Puppeteer can control browsers. Computer vision models can interpret screenshots. What's missing is the spatial reasoning layer — the ability to understand layout, navigation, and visual context. General Intuition's approach is closing that gap.

If you're building automation tools today, start thinking about visual-first workflows, not just API-first ones.

### 2. AI-powered quality assurance

Every software product needs testing. Right now, QA is either manual (humans clicking through interfaces) or scripted (automated test suites that break every time the UI changes).

Spatial AI agents could revolutionize this. An agent that understands screen layout and interaction patterns could test your app the way a human would — clicking buttons, filling forms, navigating flows — but with the consistency and speed of automation. And unlike scripted tests, it wouldn't break when you move a button three pixels to the left.

For solo builders who ship fast and don't have QA teams, this is a massive opportunity. Build a testing tool that uses spatial AI to validate user flows without maintaining brittle test scripts.

### 3. Context-aware customer support

Current [AI customer support](/posts/ai-handle-customer-messages-solopreneur/) works through text — reading tickets, matching patterns, generating responses. Spatial AI could watch a customer's screen (with permission), understand what they're trying to do, and guide them through the process visually.

Think of it as a screen-sharing AI assistant that doesn't just answer questions but sees what you see and points at the right button. For SaaS products with complex interfaces, this would reduce support tickets dramatically.

## The timing question

You might be thinking: this sounds futuristic. Is it actually buildable now?

The answer is partially. The world models General Intuition is building aren't publicly available yet. But the component pieces are:

**Computer vision** is mature. GPT-4V, Gemini, and Claude can all interpret screenshots and identify UI elements.

**Browser automation** is mature. Playwright, Puppeteer, and Selenium can control any web interface.

**LLM reasoning** is mature. Current models can plan multi-step actions based on visual input.

What's missing is the unified spatial reasoning — the ability to understand that "this button is in the top-right corner of a modal that appeared after I clicked the settings gear." That's what world models will add. But you can build 80% of the solution today with existing tools, and upgrade the reasoning layer when spatial models become available.

## What I'd build first

If I were starting today, I'd build a visual browser agent for a specific niche — not a general-purpose tool. Pick one industry (e-commerce, real estate, healthcare admin) and build an agent that can navigate their specific interfaces.

The reason for niche focus: spatial AI is only useful when it understands the context. A general-purpose visual agent needs to understand every interface. A niche agent needs to understand one type of interface deeply. That's achievable with current technology.

Start with browser automation + computer vision + an LLM for decision-making. Wrap it in a simple UI. Charge per task or per month. When spatial reasoning models become available, swap in the better model and your product instantly improves.

I covered [how AI agents are becoming employees](/posts/ai-agents-are-becoming-employees/) — spatial AI is what makes them actually competent employees instead of just fast text processors.

## The bottom line

General Intuition's $2.3B raise isn't just a funding story. It's a signal that the AI agent space is moving from text to space, from APIs to interfaces, from reading to seeing. The solo builders who start building visual-first tools now will have a head start when spatial reasoning models go mainstream.

You don't need to train world models on 2 billion video clips. You need to combine existing vision, automation, and reasoning tools into products that solve real problems for specific users. The spatial layer will come. Build the product now.

More on AI tools and building strategies at [/start-here/](/start-here/).
