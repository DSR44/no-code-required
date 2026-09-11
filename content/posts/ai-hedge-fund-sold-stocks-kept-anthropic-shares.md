---
title: "AI Hedge Fund Sold Its Stocks but Kept Its Anthropic Stake — Why It Matters"
date: 2026-09-10
draft: false
description: "I dug into why an AI hedge fund dumped its stocks but held Anthropic — here's what it signals about AI bets and what it means for your portfolio."
tags: ["AI industry", "Anthropic", "AI investing", "solo builders"]
categories: ["tools"]
slug: "ai-hedge-fund-sold-stocks-kept-anthropic-shares"
keywords: ["AI hedge fund Situational Awareness", "Anthropic IPO valuation", "AI infrastructure selloff"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-hedge-fund-sold-stocks-kept-anthropic-shares.jpg"
  alt: "Zoe reading financial news on her laptop with a notepad of AI industry notes beside her coffee"
lastmod: 2026-09-11
faqs:
  - q: "What actually happened"
    a: "Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two year"
  - q: "What Citadel's purchase tells you"
    a: "Citadel doesn't catch falling knives out of charity. Griffin's team bought the public portfolio at distressed prices, which means a firm famous for risk discipline looked at those same SK Hynix, Bloom, and Nebius positions and saw recoverable value — just not at 5x leverage, and not as a single concentrated bet on one macro thesis."
  - q: "What this means if you're building solo"
    a: "You're not managing a $10 billion book, so what do you take from this? Three things I'd actually act on."
---
{{< audio src="/audio/ai-hedge-fund-sold-stocks-kept-anthropic-shares.mp3" >}}

Why would an AI hedge fund sell everything except its Anthropic stake? That question is why I can't stop thinking about Situational Awareness, the fund run by 25-year-old ex-OpenAI researcher Leopold Aschenbrenner. After a brutal month, the fund sold most of its public stock portfolio to Ken Griffin's Citadel. It kept every share of its roughly $5 billion position in Anthropic.

If you only read the headline, that looks like a rich kid's bad month. Look closer and it's a map of where the smartest money in AI now thinks value actually lives — public AI infrastructure trades versus private AI labs — and the logic behind that split is worth understanding even if you'll never manage a dollar. It lands in a year when the AI race [isn't about Anthropic vs OpenAI anymore](/posts/its-not-about-anthropic-vs-openai-anymore/) but about entire ecosystems — compute, energy, capital — and this fund just told you which layer it thinks still has upside.

I've been chewing on this for a week because it answers a question I keep getting from solo builders: should I bet on the picks-and-shovels companies, or on the labs themselves? Situational Awareness just ran that experiment with $10 billion of other people's money. The results are messy, but readable.

## What actually happened

Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two years, that trade printed money.

Then the AI infrastructure selloff hit. Public investors started asking an uncomfortable question: where's the revenue? Some of the fund's biggest positions — memory chipmakers SK Hynix and Sandisk, clean-energy developer Bloom Energy, cloud provider Nebius — all fell more than 30% in a month. The losses were amplified by leverage, the borrowed-money strategy that magnifies both wins and drawdowns. Assets fell from roughly $20 billion to about $10 billion, and Citadel stepped in to buy the bulk of the public portfolio — a classic Griffin move of picking through leveraged unwinds.

Here's the part worth pausing on. In a July 24 letter to investors, Aschenbrenner called the selloff one of the best buying opportunities since early last year. Then he sold the public book anyway.

## Why keep Anthropic and dump the rest

The answer, as far as anyone can tell from the letter and reporting around it, is control. Public chip and energy stocks trade on quarterly earnings, sentiment, and leverage unwinds — none of which Aschenbrenner can influence. A private lab stake is different. Anthropic raises on its own schedule, values on multi-year model roadmaps, and doesn't get marked to market every time a memory-chip order disappoints. When you believe the endgame is a handful of frontier labs capturing most of the value, illiquidity isn't a bug; it's insulation from everyone else's panic.

There's also a simpler read: he thinks the labs win and the infrastructure layer gets competed away. Memory prices spike, energy developers overbuild, cloud providers margin-squeeze each other. The lab sitting on top collects the economics. Whether that holds is the actual bet.

## The case against the labs is getting louder

Before you copy the trade, hear the other side, because it showed up in the news this month. Ars Technica reported that four major AI models suffered rare overlapping downtime on the same day — Anthropic, OpenAI, Google, and others all had outages within the same window. If the frontier labs' products can't stay up individually, the "labs capture everything" thesis takes a hit, because enterprises building on a single lab inherit that single point of failure.

Anthropic's own research cuts the other way, oddly. A September TechCrunch report on Anthropic's agentic safety work found that rogue AI agents hate CAPTCHAs — the models repeatedly failed basic human-verification gates when trying to act autonomously. That's good news for safety, but it's also a reminder that agent-driven revenue, the thing that's supposed to justify lab valuations, remains further off than the bull case assumes.

Put those together and you get the bear case for keeping the Anthropic stake: the labs are operationally fragile and their monetization story is still speculative. Aschenbrenner is betting the fragility is temporary and the monetization is not. Reasonable people disagree, which is exactly why the split is interesting.

## What this means if you're a solo builder

You're not going to buy Anthropic pre-IPO. So what do you take from a fund's portfolio decision?

Two things. First, the public "AI infrastructure" trade is now a momentum trade, not a thesis trade. If leveraged funds like Situational Awareness are the marginal buyer of SK Hynix and Nebius, those stocks fall hard when leverage unwinds — and they did, 30% in a month. If you own them, size positions like they're momentum stocks, because that's how they're trading.

Second, watch what the funds keep, not what they sell. Forced sales tell you about leverage; voluntary retention tells you about conviction. Aschenbrenner kept Anthropic. Other smart money has kept private AI positions while trimming public ones. The signal isn't "buy AI labs" — it's that the people closest to the technology believe value concentrates at the model layer, and they're willing to eat illiquidity to stay there.

For your own work, that translates into something practical: if you're building on top of a frontier lab's API, your moat isn't the model — everyone has the model. It's the workflow, the data, the distribution you wrap around it. The hedge fund logic and the indie builder logic converge on the same conclusion. The scarce asset is the thing you can't buy on the open market.

## The uncomfortable caveat

I'd be irresponsible not to mention the leverage. A 439% run followed by a 30%-in-a-month drawdown isn't skill on the way up and bad luck on the way down; it's the same strategy at different points in the cycle. Aschenbrenner may be right about Anthropic. He was also wrong about timing and sizing, and his investors paid for it with a 55% asset decline.

Take the portfolio signal, skip the leverage lesson. One of those is free.

The trade worth studying isn't the Citadel sale. It's the share count that didn't change.