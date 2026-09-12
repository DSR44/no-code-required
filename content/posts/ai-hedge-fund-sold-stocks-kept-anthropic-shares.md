---
title: "AI Hedge Fund Sold Its Stocks but Kept Its Anthropic Stake — Why It Matters"
date: 2026-09-10
draft: false
description: "I dug into why an AI hedge fund dumped its stocks but held Anthropic — here's what it tells us about AI hype, private markets, and where smart money is heading."
tags: ["AI industry", "Anthropic", "AI investing", "solo builders"]
categories: ["tools"]
slug: "ai-hedge-fund-sold-stocks-kept-anthropic-shares"
keywords: ["AI hedge fund Situational Awareness", "Anthropic IPO valuation", "AI infrastructure selloff"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-hedge-fund-sold-stocks-kept-anthropic-shares.jpg"
  alt: "Zoe reading financial news on her laptop with a notepad of AI industry notes beside her coffee"
lastmod: 2026-09-12
    a: "You're not managing a $10 billion book, so what do you take from this? Three things I'd actually act on."
faqs:
  - q: "What actually happened to Situational Awareness?"
    a: "Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner, Columbia valedictorian at 19 and briefly on OpenAI's superalignment team before being dismissed, built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two yea"
  - q: "Why keep Anthropic specifically?"
    a: "Anthropic isn't public, which means the fund couldn't sell it even if it wanted to; there's no liquid market for a stake in a private AI lab. But that constraint cuts both ways. Private positions don't get marked to market in a panic, don't get margin-called, and don't force a fund to sell its best idea to cover its worst month. When Citadel bought the public book, the Anthropic stake stayed untou"
  - q: "What's the agent reliability problem nobody's pricing in?"
    a: "While the fund was unwinding, four major AI models suffered overlapping downtime within the same window. That's rare, since these systems normally run on separate infrastructure with independent failure modes. When the models that power business automation all blink at once, every company building on them feels it, and every lab's enterprise contracts get stress-tested."
  - q: "What does this mean if you're not running a $10 billion fund?"
    a: "You can't buy Anthropic shares, and you probably can't replicate a leveraged macro bet on memory chips either. Good. The useful takeaway is the sorting logic, not the trades."
---
{{< audio src="/audio/ai-hedge-fund-sold-stocks-kept-anthropic-shares.mp3" >}}

Why would an AI hedge fund sell every stock it owns but keep its Anthropic stake? That question is why I can't stop thinking about Situational Awareness, the AI hedge fund run by 25-year-old ex-OpenAI researcher Leopold Aschenbrenner. After a brutal month, the fund sold most of its public stock portfolio to Ken Griffin's Citadel. It kept every share of its roughly $5 billion position in Anthropic.

The numbers that frame this: Situational Awareness returned 439% through June, assets reportedly peaked at $45 billion, then fell to about $10 billion after its biggest positions (SK Hynix, Sandisk, Bloom Energy, Nebius) each dropped more than 30% in a month. Citadel bought the bulk of the public book. The Anthropic stake stayed put.

If you only read the headline, that looks like a rich kid's bad month. Look closer and it's a map of where the smartest money in AI now thinks value actually lives: public AI infrastructure trades versus private AI labs. The logic behind that split is worth understanding even if you'll never manage a dollar. It lands in a year when the AI race [isn't about Anthropic vs OpenAI anymore](/posts/its-not-about-anthropic-vs-openai-anymore/) but about entire ecosystems — compute, energy, capital — and this fund just told you which layer it thinks still has upside.

I've been chewing on this for a week because it answers a question I keep getting from solo builders: should I bet on the picks-and-shovels companies, or on the labs themselves? Situational Awareness just ran that experiment with $10 billion of other people's money. The results are messy, but readable.

## What actually happened to Situational Awareness?

Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner, Columbia valedictorian at 19 and briefly on OpenAI's superalignment team before being dismissed, built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two years, that trade printed money.

Then the AI infrastructure selloff hit. Public investors started asking an uncomfortable question: where's the revenue? Some of the fund's biggest positions — memory chipmakers SK Hynix and Sandisk, clean-energy developer Bloom Energy, cloud provider Nebius — all fell more than 30% in a month. Borrowed money amplified the losses, magnifying both the earlier wins and the drawdown. Assets fell from roughly $20 billion to about $10 billion, and Citadel stepped in to buy the bulk of the public portfolio, a classic Griffin move of picking through leveraged unwinds.

The part worth pausing on: in a July 24 letter to investors, Aschenbrenner called the selloff one of the best buying opportunities in the space, then proceeded to sell anyway. You can read that as capitulation. I read it as a reclassification. He no longer believes the commodity layer (chips, memory, power) is where the durable margin sits; the labs that own the models do.

## Why keep Anthropic specifically?

Anthropic isn't public, which means the fund couldn't sell it even if it wanted to; there's no liquid market for a stake in a private AI lab. But that constraint cuts both ways. Private positions don't get marked to market in a panic, don't get margin-called, and don't force a fund to sell its best idea to cover its worst month. When Citadel bought the public book, the Anthropic stake stayed untouched because it was the one asset nobody could force out the door.

There's also a fundamental case. Anthropic's Claude models have become the default choice for AI coding agents and enterprise automation, which is where actual revenue is showing up right now. The company keeps shipping research that shapes how the industry thinks about agent safety, including a recent report on how autonomous AI agents behave when they hit obstacles like CAPTCHAs and access restrictions online. That work matters commercially as well as ethically: enterprises won't deploy agents at scale until someone solves the trust problem, and Anthropic is positioning itself as the lab that solves it.

## What's the agent reliability problem nobody's pricing in?

While the fund was unwinding, four major AI models suffered overlapping downtime within the same window. That's rare, since these systems normally run on separate infrastructure with independent failure modes. When the models that power business automation all blink at once, every company building on them feels it, and every lab's enterprise contracts get stress-tested.

That's the bet hiding inside the Anthropic stake. The next phase of AI revenue isn't chips or power; it's agents that work reliably enough for a Fortune 500 CIO to sign off on. Anthropic's own research into agent behavior, including why autonomous agents get stuck on things as mundane as CAPTCHA walls, is exactly the unglamorous work that determines which lab enterprises trust with production workloads. Reliability is the product. The fund seems to understand that.

## What does this mean if you're not running a $10 billion fund?

You can't buy Anthropic shares, and you probably can't replicate a leveraged macro bet on memory chips either. Good. The useful takeaway is the sorting logic, not the trades.

When a fund this concentrated in AI infrastructure decides the infrastructure trade is crowded, that's information about the cycle stage. Public picks-and-shovels names (the SK Hynixes and Nebiuses of the world) are priced on next quarter's orders. Private labs are priced on the assumption that model capability keeps compounding and someone eventually wins a durable, high-margin franchise. Aschenbrenner just told you which assumption he'd rather own after watching both get tested.

If you're a solo builder or angel-stage investor, the practical version looks like this. Treat public AI infrastructure stocks as cyclical trades rather than permanent holdings; size them like you'd size a commodity position, because that's how the big money now treats them. If you want exposure to the labs, look at secondary-market platforms or public companies with meaningful private AI stakes, and accept the illiquidity as the price of admission. Watch enterprise adoption signals (agent reliability incidents, downtime windows, procurement wins) more closely than chip order data. The revenue question that tanked the infrastructure trade gets answered at the application layer first.

One honest caveat: this is one fund, run by one young manager, after one terrible month. Survivorship bias runs rampant in AI commentary, and a $5 billion paper stake in a private company is easy to "keep" when there's no bid to sell into. Don't build a thesis on a single data point. Build it on the pattern, and the pattern across AI investing this year is that capital is rotating from the stuff AI runs on to the models themselves.

The uncomfortable summary: the loudest AI bull of the cycle looked at the public market's version of the AI trade and chose the private one. That's no guarantee of anything. It is, though, the clearest signal I've seen this year about where the next phase of AI value is expected to show up, and it's nowhere near a memory chip factory.

## FAQ

**Why did Situational Awareness sell its stocks but keep Anthropic?**
The fund's public positions (SK Hynix, Sandisk, Bloom Energy, Nebius) fell more than 30% in a month during the AI infrastructure selloff, so Citadel bought the public portfolio during the unwind. The roughly $5 billion Anthropic stake couldn't be sold because private AI lab shares have no liquid market, and private positions also can't be margin-called or force a fund to dump its best asset in a panic.

**Who is Leopold Aschenbrenner?**
He's the 25-year-old founder of Situational Awareness, a Columbia valedictorian at 19 who was briefly on OpenAI's superalignment team before being dismissed. His fund bet that scaling AI would require a massive buildout of semiconductors, compute, memory, and energy, a thesis that returned 439% through June before the selloff cut assets from roughly $20 billion to about $10 billion.

**Can regular investors buy Anthropic stock?**
No. Anthropic is private, so there's no public market for its shares. The practical routes are secondary-market platforms that trade private company stakes, or public companies holding meaningful private AI positions, with the tradeoff that these are illiquid and hard to price.

**What is the agent reliability problem in AI?**
Four major AI models suffered overlapping downtime within the same window, which is rare because they normally run on separate infrastructure. When models powering business automation fail simultaneously, every company building on them feels it. The next phase of AI revenue depends on agents being reliable enough for enterprise CIOs to approve, which is why Anthropic's research into agent behavior (like getting stuck on CAPTCHAs) matters commercially.
