---
title: "Startup Trains AI Agents on Video Game Data, Raises $300M"
slug: "general-intuition-ai-agents-video-game-data"
date: 2026-07-01
draft: false
description: "General Intuition raised $300M to train AI agents using 2 billion video game clips. Here's why that matters for the future of AI."
tags: ["AI tools", "AI agents", "startups", "gaming", "no-code"]
categories: ["tools"]
slug: "general-intuition-ai-agents-video-game-data"
keywords: ["General Intuition AI", "AI agents video game training", "world models AI", "AI spatial reasoning", "gaming data AI training"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/general-intuition-ai-agents-video-game-data.jpg"
  alt: "Zoe excited about AI training with video game data on her laptop"
lastmod: 2026-09-06
faqs:
  - q: "What does General Intuition actually do?"
    a: "General Intuition trains \"world models,\" AI systems that learn how objects move through space, how actions cause consequences, and how to anticipate what happens next. It spun out of Medal, a clip-sharing platform with 10 million monthly users who upload roughly 2 billion first-person gameplay videos per year — every kill, every movement, every decision captured from the player's perspective. Most"
  - q: "Why is video game data better than real-world video?"
    a: "Gameplay footage is structured by default, and that's the whole argument. Every frame contains spatial information (where objects are, how they're moving, what the player is looking at), and every action has a measurable outcome: did the player survive, score, complete the objective? The feedback loop is built in. An AI watching gameplay learns what happened and what worked."
  - q: "Why should solo builders care?"
    a: "Fair question, and the honest answer is: not immediately. The agents you can deploy today (like Slackbot or the agents I described hiring) are language-based. They process text, make decisions in text, and act through APIs. They can't see, and they can't navigate physical space."
  - q: "Is a $2B valuation justified for a gaming AI startup?"
    a: "The valuation isn't a bet on gaming. It's a bet that the next generation of AI agents needs to understand the physical world, and that video games are the fastest way to teach them. If you run a small business, the immediate takeaway is that the agent economy is expanding beyond text and into space. Start listing tasks that would benefit from an AI that can see and move rather than read and write."
---

{{< audio src="/audio/general-intuition-ai-agents-video-game-data.mp3" >}}

Here's a sentence I didn't expect to write: the next generation of AI agents might learn to navigate the real world by watching teenagers play Fortnite. A startup called General Intuition just raised $300 million, backed by Jeff Bezos and Eric Schmidt, to train AI agents on 2 billion video game clips per year. The valuation sits above $2 billion. But the money is the boring part. The interesting part is the mechanism: instead of building AI that processes text, they're building AI that understands space, time, and movement.

## What does General Intuition actually do?

General Intuition trains "world models," AI systems that learn how objects move through space, how actions cause consequences, and how to anticipate what happens next. It spun out of Medal, a clip-sharing platform with 10 million monthly users who upload roughly 2 billion first-person gameplay videos per year — every kill, every movement, every decision captured from the player's perspective. Most people see a highlight reel. General Intuition sees a training dataset for spatial intelligence.

The models most people know, like the ones behind ChatGPT, learn patterns from text. World models learn by watching a simulated physical world operate. Video games turn out to be an efficient proxy for reality: they contain physics, spatial reasoning, cause and effect, and real-time decision-making, all in a format that's cheaper and safer to collect than real-world footage. CEO Pim de Witte [describes the approach](https://techcrunch.com/2026/06/18/general-intuition-in-talks-to-raise-300m-at-around-2b-valuation/) as building agents that can "perceive, anticipate, and interact in real time." Think of how you learned to drive by watching traffic, not by reading a manual. Same idea. This is the same leap I covered in [AI agents becoming employees](/posts/ai-agents-are-becoming-employees/), applied to the physical world instead of the digital one.

## Why is video game data better than real-world video?

Gameplay footage is structured by default, and that's the whole argument. Every frame contains spatial information (where objects are, how they're moving, what the player is looking at), and every action has a measurable outcome: did the player survive, score, complete the objective? The feedback loop is built in. An AI watching gameplay learns what happened and what worked.

Real-world video doesn't offer that. Companies like [Runway](https://runwayml.com/) and World Labs are training on real-world footage, but that data is expensive to collect, hard to annotate, and tangled up in privacy issues. Game data skips all three problems. This is also a fundamentally different training approach from [how language models work](/posts/what-is-an-llm-no-code-explanation/) — and the difference matters because the agents that will be useful in physical settings (robots, autonomous systems, [AI employees](/posts/ai-agents-are-becoming-employees/)) need to understand space and time, not only language.

OpenAI apparently agrees. They reportedly tried to acquire Medal for its dataset, and when that fell through, other major AI labs came knocking too.

## Why should solo builders care?

Fair question, and the honest answer is: not immediately. The agents you can deploy today (like [Slackbot](/posts/salesforce-slackbot-vs-microsoft-google-ai-agents/) or the [agents I described hiring](/posts/ai-agents-are-becoming-employees/)) are language-based. They process text, make decisions in text, and act through APIs. They can't see, and they can't navigate physical space.

That changes when General Intuition ships its product, expected late summer or early fall 2026. The first applications will probably land in gaming and robotics simulation. After that, the picture widens: agents with spatial reasoning could monitor physical spaces, navigate warehouses, inspect infrastructure, or guide autonomous systems. My practical advice for now is modest. The tools you're using today are the text layer; the spatial layer is coming. You don't need to build world models. You need to know they're arriving and leave room in your workflows to plug them in.

## Who else is building world models?

General Intuition has company, and the field moves fast:

- **Runway** started with AI video generation for filmmakers and is pivoting toward world models for real-world simulation
- **Decart** released a world model that can simulate hours of photorealistic driving
- **World Labs** (Fei-Fei Li's company) launched Marble, its first commercial world model product
- **Google's Genie 3** began integrating Google Maps data to simulate real streets

What separates General Intuition is the data. Competitors scrape the internet or generate synthetic datasets; General Intuition gets 2 billion new first-person gameplay videos every month from Medal's existing user base. Replicating that would take years. The company plans to spend the new funding on compute and ship a product by late summer, and if it delivers, it'll be the first world model trained on interactive, first-person data at scale.

## Is a $2B valuation justified for a gaming AI startup?

The valuation isn't a bet on gaming. It's a bet that the next generation of AI agents needs to understand the physical world, and that video games are the fastest way to teach them. If you run a small business, the immediate takeaway is that the agent economy is expanding beyond text and into space. Start listing tasks that would benefit from an AI that can see and move rather than read and write. For more on where agents are heading, start at [/start-here/](/start-here/).

## FAQs

**What is a world model in AI?**
A world model is an AI system trained to understand how physical environments work: how objects move, how actions produce consequences, and how to predict what happens next. Unlike language models trained on text, world models learn from video or simulation, which makes them better suited for robotics, autonomous systems, and any agent that has to operate in physical space.

**How much did General Intuition raise?**
General Intuition raised $300 million at a valuation above $2 billion, with backing from Jeff Bezos and Eric Schmidt. The company trains its AI on roughly 2 billion first-person video game clips per year sourced from Medal, its clip-sharing parent platform with 10 million monthly users.

**Why train AI on video game clips instead of real-world video?**
Gameplay footage is structured, cheap to collect, and free of privacy complications, while real-world video is expensive, hard to annotate, and legally messy. Games also include built-in feedback: every action has a measurable outcome, so the AI learns which decisions worked rather than only what happened.

**When will General Intuition's product launch?**
The company expects to release its first product in late summer or early fall 2026, with initial applications in gaming and robotics simulation. It plans to use the new funding to scale compute ahead of that launch.

**Who are General Intuition's competitors?**
Runway (pivoting from video generation to world models), Decart (photorealistic driving simulation), World Labs (Marble, its first commercial product), and Google's Genie 3 (which integrates Google Maps data). General Intuition's edge is its proprietary stream of 2 billion gameplay videos monthly from Medal's users.
