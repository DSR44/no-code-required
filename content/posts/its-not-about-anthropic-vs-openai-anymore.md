---
title: "Anthropic vs OpenAI: How to Choose the Right AI Model | NCR"
date: 2026-07-09
draft: false
description: "The AI landscape changed. Anthropic and OpenAI aren't the only players that matter anymore — here's how to choose the right model for what you're building."
tags: ["AI tools", "AI models", "no-code", "automation"]
categories: ["tools"]
slug: "its-not-about-anthropic-vs-openai-anymore"
keywords: ["anthropic vs openai 2026", "best AI model for beginners", "which AI tool to use", "AI model comparison 2026", "choosing AI tools"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/its-not-about-anthropic-vs-openai-anymore.jpg"
  alt: "Zoe at laptop comparing AI tools on screen with multiple chat windows open"

lastmod: 2026-09-25
faqs:
  - q: "What's the difference between Anthropic and OpenAI in 2026?"
    a: "A few weeks ago, Decagon CEO Jesse Zhang published something that reframed how I think about this. His argument: frontier models (the expensive, cutting-edge ones like Claude Opus and GPT-5) and open source models (like DeepSeek and Llama) aren't competing with each other. They're two phases of the same lifecycle."
  - q: "Which AI model is actually cheaper?"
    a: "The data backs this up. Looking at Vercel's AI gateway dashboard from this past week, DeepSeek has surged into the lead for raw token volume — processing over a third of all tokens passing through the platform. Z.ai's GLM-5.2 model jumped into fourth place."
  - q: "Which AI should I use for my specific workflow?"
    a: "If you're reading this and thinking \"I just want to know which chatbot to use\" — I get it. Here's the practical version:"
  - q: "What tools let me switch between AI models easily?"
    a: "One of the best developments this year is that choosing a model has become less permanent. Tools like:"
  - q: "What's the real takeaway for choosing an AI model?"
    a: "The Anthropic-vs-OpenAI framing made sense in 2024. It doesn't anymore. The market matured into layers — frontier models for discovery, open source for production, specialized tools for specific tasks — and the winners are the people who understand those layers instead of pledging loyalty to one provider."
---

{{< audio src="/audio/its-not-about-anthropic-vs-openai-anymore.mp3" >}}

Six months ago, picking an AI tool felt like choosing sides in a rap beef. Anthropic or OpenAI? Claude or ChatGPT? Every thread on X was people arguing about which one was "better" like there was a single answer. I spent way too much time reading those threads instead of actually building things.

Here's what I've learned since: that framing is dead. Not because one side won — because the game changed entirely. The AI market in mid-2026 doesn't look like a two-player race anymore. It looks like a layered ecosystem, and understanding those layers is the difference between overpaying for the wrong tool and finding exactly what you need.

The numbers make this concrete: on Vercel's AI gateway this past week, DeepSeek processed over a third of all tokens by volume, yet Anthropic still captured more than half of all AI spending on the platform. Cheap models handle the volume; premium models handle the hard stuff. Both things are true at once.

I've been testing this across [my daily workflows](/posts/the-tools-i-actually-use-every-day/) — from [automating client follow-ups](/posts/automate-client-follow-ups-no-code/) to [building content pipelines](/posts/automate-coaching-business-free-ai-tools/) — and the pattern holds. The question isn't "which AI is best?" It's "which AI is best for this specific thing?"

## What's the difference between Anthropic and OpenAI in 2026?

The short answer: they're not really competing anymore, because frontier models and open source models serve different phases of the same project lifecycle.

A few weeks ago, Decagon CEO Jesse Zhang published something that reframed how I think about this. His argument: frontier models (the expensive, top-tier ones like Claude Opus and GPT-5) and open source models (like DeepSeek and Llama) aren't rivals. They're two phases of one lifecycle.

In practice it works like this. When you're building something new — a workflow you've never tried, a use case you're still figuring out — you start with the frontier model. It handles ambiguity better and gets you to a working prototype faster. Once that use case is proven and routine, you switch to a cheaper open source model that handles the now-predictable task at a fraction of the cost.

Zhang calls it "discovery vs. production." Frontier labs own discovery. Open source increasingly owns production.

This matches what I've seen building [AI-powered automations](/posts/build-your-first-automation-in-15-minutes/). When I'm experimenting — trying to figure out if something is even possible — I want the smartest model available. Once I've locked in the workflow and it runs the same way every day, I don't need Opus-level reasoning. I need something reliable and cheap.

## Which AI model is actually cheaper?

DeepSeek is the cheapest serious option right now, and the usage data shows people taking advantage of it — but spending still concentrates at the premium end for difficult work.

Looking at Vercel's AI gateway dashboard from this past week, DeepSeek has surged into the lead for raw token volume, processing over a third of all tokens passing through the platform. Z.ai's GLM-5.2 model jumped into fourth place.

Scroll down to overall spending, though, and Anthropic still accounts for more than half of all AI spend on the platform. OpenRouter shows the same pattern: DeepSeek V4 Flash handles massive volume at 6 cents per million tokens, while Opus 4.8 runs at $1.37 per million — roughly 23 times more expensive — and still captures the lion's share of spending.

So people use cheaper models for high-volume routine work and pay premium prices for the hard stuff. Both at the same time.

And now Meta just jumped in with its own AI coding models, with their AI chief calling the pricing "very aggressive" compared to Anthropic and OpenAI. The field keeps expanding, not consolidating.

## Which AI should I use for my specific workflow?

Match the model to the task: everyday chat needs nothing special, automations benefit from the two-tier approach, coding still favors Claude, and creative work depends more on the tool than the underlying model.

If you're reading this and thinking "I just want to know which chatbot to use" — I get it. Here's the practical version:

**For everyday tasks** — writing emails, summarizing documents, brainstorming, answering questions — the free or cheap tiers of [ChatGPT](https://chat.openai.com/), [Claude](https://claude.ai/), or [Gemini](https://gemini.google.com/) are all genuinely good enough. The differences between them for routine tasks are marginal. Pick the one you like using.

**For building automations** — if you're using [Make](https://www.make.com/), [Zapier](https://zapier.com/), or [n8n](https://n8n.io/) — the model choice matters more. This is where the two-tier model applies. Start with a powerful model to design your workflow, then switch to a cheaper one once it's proven. Most automation platforms now let you [swap models easily](/posts/ai-subscription-price-war-what-to-pay-for/).

**For coding and technical work** — this is where the market shifted most. Claude's coding capabilities have made it the default for [AI coding agents](/posts/ai-coding-agents-taught-robots-install-gpus/), but DeepSeek and Meta's new models are closing the gap fast. If you're using [AI for development](/posts/anthropic-cowork-claude-agent/), the model you pick today might not be the best choice in three months.

**For content creation** — [image generation](/posts/ai-images-which-tool-actually-works/), [music](/posts/ai-music-i-made-an-album-without-knowing-theory/), video — the model matters less than the tool's interface and features. Midjourney, DALL-E, and Ideogram each have different strengths regardless of which company's language model you prefer.

## How do I stop overthinking and start building?

Ask four questions instead of picking a team: what am I trying to do, am I exploring or executing, how often does the task repeat, and what does my existing stack support?

1. **What am I actually trying to do?** A specific task beats a general preference every time.
2. **Am I exploring or executing?** Exploration wants the smartest model. Execution wants the cheapest one that works.
3. **How often does this task repeat?** One-time tasks justify premium models. Daily workflows justify switching to cheaper alternatives.
4. **What does my existing stack support?** If you're already in [the Make ecosystem](/posts/build-your-first-automation-in-15-minutes/), the models available there matter more than theoretical comparisons.

## What tools let me switch between AI models easily?

OpenRouter, Vercel's AI SDK, and Poe all let you change models without rebuilding your setup, which means choosing wrong is no longer expensive.

- **[OpenRouter](https://openrouter.ai/)** — access hundreds of models through one API; switch between them without changing your code or workflows
- **[Vercel AI SDK](https://sdk.vercel.ai/)** — if you're building anything web-based, it abstracts away the model layer
- **[Poe](https://poe.com/)** — chat with multiple models in one interface, compare outputs side by side

These tools mean you're not locked in. You can [test different models](/posts/ai-tool-overwhelm-how-to-escape/) for different tasks without rebuilding everything from scratch.

## What's the real takeaway for choosing an AI model?

The Anthropic-vs-OpenAI framing made sense in 2024. It doesn't anymore. The market matured into layers — frontier models for discovery, open source for production, specialized tools for specific tasks — and the winners are the people who understand those layers instead of pledging loyalty to one provider.

Stop reading Twitter threads about which AI is "best." Start thinking about which AI is best for the thing you're building right now. Then be ready to switch when the next thing comes along, because it will, and faster than you expect.

If you're just getting started with AI tools and want a clear path through the noise, [/start-here/](/start-here/) has the practical walkthrough. No hype, no provider drama — just what actually works.

## FAQ

**Should I use Anthropic or OpenAI in 2026?**
Neither is the universal answer anymore. Use a frontier model like Claude Opus or GPT-5 while you're designing and proving a workflow, then switch to a cheaper open source model like DeepSeek for the routine execution. On OpenRouter, DeepSeek V4 Flash costs 6 cents per million tokens versus $1.37 for Opus 4.8, so the savings on high-volume work are substantial.

**Why are people paying for expensive models when cheap ones exist?**
Because the two tiers do different jobs. DeepSeek leads Vercel's gateway in token volume (over a third of all tokens), yet Anthropic still captures more than half of total spending. Cheap models handle predictable, high-volume tasks; premium models handle ambiguous, hard problems where a wrong answer costs more than the price difference.

**What's the cheapest good AI model right now?**
DeepSeek V4 Flash runs at 6 cents per million tokens on OpenRouter and has become the volume leader on Vercel's AI gateway. Z.ai's GLM-5.2 also climbed into fourth place on the gateway. For routine, well-defined tasks, these are strong choices; for exploratory or complex work, a frontier model is still worth the premium.

**How do I switch between AI models without rebuilding my workflows?**
Use a model-routing tool. OpenRouter gives you hundreds of models through a single API, Vercel's AI SDK abstracts the model layer for web projects, and Poe lets you compare multiple chat models side by side. Most automation platforms like Make, Zapier, and n8n also let you swap models inside existing workflows.
