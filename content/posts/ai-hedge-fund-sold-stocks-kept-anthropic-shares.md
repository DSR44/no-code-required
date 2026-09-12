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
faqs:
  - q: "What actually happened"
    a: "Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two year"
  - q: "What Citadel's purchase tells you"
    a: "Citadel doesn't catch falling knives out of charity. Griffin's team bought the public portfolio at distressed prices, which means a firm famous for risk discipline looked at those same SK Hynix, Bloom, and Nebius positions and saw recoverable value — just not at 5x leverage, and not as a single concentrated bet on one macro thesis."
  - q: "What this means if you're building solo"
    a: "You're not managing a $10 billion book, so what do you take from this? Three things I'd actually act on."
---
{{< audio src="/audio/ai-hedge-fund-sold-stocks-kept-anthropic-shares.mp3" >}}

Why would an AI hedge fund sell every stock it owns but keep its Anthropic stake? That question is why I can't stop thinking about Situational Awareness, the AI hedge fund run by 25-year-old ex-OpenAI researcher Leopold Aschenbrenner. After a brutal month, the fund sold most of its public stock portfolio to Ken Griffin's Citadel. It kept every share of its roughly $5 billion position in Anthropic.

If you only read the headline, that looks like a rich kid's bad month. Look closer and it's a map of where the smartest money in AI now thinks value actually lives — public AI infrastructure trades versus private AI labs — and the logic behind that split is worth understanding even if you'll never manage a dollar. It lands in a year when the AI race [isn't about Anthropic vs OpenAI anymore](/posts/its-not-about-anthropic-vs-openai-anymore/) but about entire ecosystems — compute, energy, capital — and this fund just told you which layer it thinks still has upside.

I've been chewing on this for a week because it answers a question I keep getting from solo builders: should I bet on the picks-and-shovels companies, or on the labs themselves? Situational Awareness just ran that experiment with $10 billion of other people's money. The results are messy, but readable.

## What actually happened

Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two years, that trade printed money.

Then the AI infrastructure selloff hit. Public investors started asking an uncomfortable question: where's the revenue? Some of the fund's biggest positions — memory chipmakers SK Hynix and Sandisk, clean-energy developer Bloom Energy, cloud provider Nebius — all fell more than 30% in a month. The losses were amplified by leverage, the borrowed-money strategy that magnifies both wins and drawdowns. Assets fell from roughly $20 billion to about $10 billion, and Citadel stepped in to buy the bulk of the public portfolio — a classic Griffin move of picking through leveraged unwinds.

Here's the part worth pausing on. In a July 24 letter to investors, Aschenbrenner called the selloff one of the best buying opportunities in the space, then proceeded to sell anyway. You can read that as capitulation. I read it as a reclassification: he no longer believes the commodity layer — chips, memory, power — is where the durable margin sits. The labs that own the models do.

## Why keep Anthropic specifically?

Anthropic isn't public, which means the fund couldn't sell it even if it wanted to — there's no liquid market for a stake in a private AI lab. But that constraint cuts both ways. Private positions don't get marked to market in a panic, don't get margin-called, and don't force a fund to sell its best idea to cover its worst month. When Citadel bought the public book, the Anthropic stake stayed untouched because it was the one asset nobody could force out the door.

There's also a fundamental case. Anthropic's Claude models have become the default choice for AI coding agents and enterprise automation, which is where actual revenue is showing up right now. And the company keeps shipping research that shapes how the whole industry thinks about agent safety — including a recent report on how autonomous AI agents behave when they hit obstacles like CAPTCHAs and access restrictions online. That kind of work matters commercially, not just ethically: enterprises won't deploy agents at scale until someone solves the trust problem, and Anthropic is positioning itself as the lab that solves it.

## The agent reliability problem nobody's pricing in

While the fund was unwinding, something odd happened in the AI world that most market commentary missed: four major AI models suffered overlapping downtime within the same window — a rare event, since these systems normally run on separate infrastructure with independent failure modes. When the models that power business automation all blink at once, every company building on them feels it, and every lab's enterprise contracts get stress-tested.

That's the bet hiding inside the Anthropic stake. The next phase of AI revenue isn't chips or power — it's agents that work reliably enough for a Fortune 500 CIO to sign off on. Anthropic's own research into agent behavior, including why autonomous agents get stuck on things as mundane as CAPTCHA walls, is exactly the unglamorous work that determines which lab enterprises trust with production workloads. Reliability is the product. The fund seems to understand that.

## What this means if you're not running a $10 billion fund

You can't buy Anthropic shares, and you probably can't replicate a leveraged macro bet on memory chips either. Good. The useful takeaway is the sorting logic, not the trades.

When a fund this concentrated in AI infrastructure decides the infrastructure trade is crowded, that's information about the cycle stage. Public picks-and-shovels names — the SK Hynixes and Nebiuses of the world — are priced on next quarter's orders. Private labs are priced on the assumption that model capability keeps compounding and someone eventually wins a durable, high-margin franchise. Aschenbrenner just told you which assumption he'd rather own after watching both get tested.

If you're a solo builder or angel-stage investor, the practical version looks like this. First, treat public AI infrastructure stocks as cyclical trades, not permanent holdings — size them like you'd size a commodity position, because that's how the big money now treats them. Second, if you want exposure to the labs, look at secondary-market platforms or public companies with meaningful private AI stakes, and accept the illiquidity as the price of admission. Third, watch enterprise adoption signals — agent reliability incidents, downtime windows, procurement wins — more closely than chip order data. The revenue question that tanked the infrastructure trade gets answered at the application layer first.

One honest caveat: this is one fund, run by one young manager, after one terrible month. Survivorship bias runs rampant in AI commentary, and a $5 billion paper stake in a private company is easy to "keep" when there's no bid to sell into. Don't build a thesis on a single data point. Build it on the pattern — and the pattern across AI investing this year is that capital is rotating from the stuff AI runs on to the models themselves.

The uncomfortable summary: the loudest AI bull of the cycle looked at the public market's version of the AI trade and chose the private one. That's not a guarantee of anything. It is, however, the clearest signal I've seen this year about where the next phase of AI value is expected to show up — and it's not in a memory chip factory.