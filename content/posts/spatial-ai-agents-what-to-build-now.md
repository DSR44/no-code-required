---
title: "What Solo Builders Should Build With Spatial AI Now"
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
lastmod: 2026-08-25
faqs:
  - q: "What does spatial AI mean for solo builders?"
    a: "Today's AI agents — the ones powering automated workflows and tool-calling systems — work in text space. They read data, process instructions, output API calls. Powerful but blind. They can't see a screen or understand physical context."
  - q: "What should I build with spatial AI right now?"
    a: "Three categories have clear near-term potential, and the component pieces already exist."
  - q: "Can I actually build this today?"
    a: "Partially. General Intuition's world models aren't publicly available yet. But the component pieces are:"
  - q: "Where should a solo builder start?"
    a: "Pick one niche. Not a general-purpose tool — a visual browser agent for a specific industry (e-commerce, real estate, healthcare admin) that can navigate their specific interfaces."
---

{{< audio src="/audio/spatial-ai-agents-what-to-build-now.mp3" >}}

A startup just raised $2.3 billion to train AI agents on Fortnite gameplay footage. General Intuition is building world models from 2 billion video game clips per year — teaching AI to understand space, time, and movement by watching how humans navigate dynamic environments. For solo builders, this shifts AI agents from text processors into visual operators that can see screens, navigate interfaces, and make spatial decisions.

I covered [what General Intuition does and why video game data is different](/posts/general-intuition-ai-agents-video-game-data/) in my last post. This one is about what to actually build with this technology.

## What does spatial AI mean for solo builders?

Today's AI agents — the ones powering [automated workflows](/posts/build-your-first-automation-in-15-minutes/) and [tool-calling systems](/posts/ai-agents-explained-what-tool-calling-actually-means/) — work in text space. They read data, process instructions, output API calls. Powerful but blind. They can't see a screen or understand physical context.

Spatial AI changes that. General Intuition's models learn spatial reasoning, cause and effect, and anticipatory decision-making by watching first-person footage of players making decisions in real time. For builders, the next generation of AI agents won't just automate text tasks. They'll automate visual ones — navigating apps, interpreting dashboards, moving through interfaces, making decisions based on what they see.

## What should I build with spatial AI right now?

Three categories have clear near-term potential, and the component pieces already exist.

**Visual workflow agents.** Current automation tools like [Zapier](/posts/zapier-pricing-2026-what-you-pay/) and [Make](/posts/make-vs-zapier-which-one-is-actually-easier/) work through APIs — structured connections between apps. But most business processes still involve clicking through interfaces, reading dashboards, and making visual judgments. A visual workflow agent could log into your Shopify dashboard, identify products with declining sales, check competitor pricing on Amazon, and draft a pricing adjustment recommendation — by actually looking at the screen, not calling an API.

**AI-powered QA.** Every software product needs testing. Right now it's either manual (humans clicking through interfaces) or scripted (automated test suites that break every time the UI changes). An agent that understands screen layout and interaction patterns could test your app the way a human would — clicking buttons, filling forms, navigating flows — but with automation's consistency. Unlike scripted tests, it wouldn't break when you move a button three pixels to the left.

**Context-aware customer support.** Current [AI customer support](/posts/ai-handle-customer-messages-solopreneur/) works through text — reading tickets, matching patterns, generating responses. Spatial AI could watch a customer's screen (with permission), understand what they're trying to do, and guide them visually. Think of it as a screen-sharing assistant that sees what you see and points at the right button. For SaaS products with complex interfaces, this would cut support tickets significantly.

## Can I actually build this today?

Partially. General Intuition's world models aren't publicly available yet. But the component pieces are:

**Computer vision** is mature. GPT-4V, Gemini, and Claude can all interpret screenshots and identify UI elements.

**Browser automation** is mature. Playwright, Puppeteer, and Selenium can control any web interface.

**LLM reasoning** is mature. Current models can plan multi-step actions based on visual input.

What's missing is unified spatial reasoning — the ability to understand that "this button is in the top-right corner of a modal that appeared after I clicked the settings gear." That's what world models will add. You can build 80% of the solution today with existing tools, then upgrade the reasoning layer when spatial models ship.

## Where should a solo builder start?

Pick one niche. Not a general-purpose tool — a visual browser agent for a specific industry (e-commerce, real estate, healthcare admin) that can navigate their specific interfaces.

The reason: spatial AI is only useful when it understands context. A general-purpose visual agent needs to understand every interface. A niche agent needs to understand one type deeply. That's achievable now.

Start with browser automation + computer vision + an LLM for decision-making. Wrap it in a simple UI. Charge per task or per month. When spatial reasoning models become available, swap in the better model and your product improves overnight.

I covered [how AI agents are becoming employees](/posts/ai-agents-are-becoming-employees/) — spatial AI is what makes them competent employees instead of fast text processors.

General Intuition's $2.3B raise signals that AI agents are moving from text to space, from APIs to interfaces, from reading to seeing. You don't need to train world models on 2 billion video clips. Combine existing vision, automation, and reasoning tools into products that solve real problems for specific users. The spatial layer will come. Build the product now.

More on AI tools and building strategies at [/start-here/](/start-here/).

---

**FAQ**

**What is spatial AI and why does it matter for solo builders?**
Spatial AI refers to AI systems that understand space, time, and movement — not just text. Companies like General Intuition train these models on video game footage to teach AI how to navigate physical and digital environments. For solo builders, this means AI agents that can see screens, click buttons, and make visual decisions.

**Can I build spatial AI tools without training my own models?**
Yes. Computer vision (GPT-4V, Gemini, Claude), browser automation (Playwright, Puppeteer), and LLM reasoning are all mature and available now. You can combine these to build visual workflow agents today, then upgrade to spatial reasoning models when they become publicly available.

**What's the best niche for a spatial AI agent?**
Pick one industry with repetitive visual workflows — e-commerce, real estate, or healthcare admin work well. A niche agent only needs to understand one type of interface deeply, which is achievable with current technology. General-purpose visual agents require far more spatial context.

**How is spatial AI different from current AI automation?**
Current AI automation works through APIs — structured data connections between apps. Spatial AI works through vision — it looks at screens, interprets layouts, and navigates interfaces the way a human does. This lets it handle tasks that don't have API access or require visual judgment.
