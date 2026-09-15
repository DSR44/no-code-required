---
title: "AI Hedge Fund Sold Its Stocks but Kept Its Anthropic Stake — Why It Matters"
date: 2026-09-10
draft: false
description: "I dug into why an AI hedge fund dumped its stocks but held Anthropic — here's what it tells us about betting on AI infrastructure over public markets."
tags: ["AI industry", "Anthropic", "AI investing", "solo builders"]
categories: ["tools"]
slug: "ai-hedge-fund-sold-stocks-kept-anthropic-shares"
keywords: ["AI hedge fund Situational Awareness", "Anthropic IPO valuation", "AI infrastructure selloff"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-hedge-fund-sold-stocks-kept-anthropic-shares.jpg"
  alt: "Zoe reading financial news on her laptop with a notepad of AI industry notes beside her coffee"
lastmod: 2026-09-15
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

Why would an AI hedge fund sell every public stock it owned but keep its Anthropic stake? That question has been bouncing around my head for a week, and the answer tells you more about where AI money is heading than any earnings call this quarter. The fund is Situational Awareness, run by 25-year-old ex-OpenAI researcher Leopold Aschenbrenner, and after a brutal month it offloaded most of its public portfolio to Ken Griffin's Citadel while holding every share of its roughly $5 billion Anthropic position.

The numbers make this concrete. Situational Awareness returned 439% through June. Assets reportedly peaked at $45 billion, then collapsed to about $10 billion after its biggest positions — SK Hynix, Sandisk, Bloom Energy, Nebius — each dropped more than 30% in a single month. Citadel bought the bulk of the public book. The Anthropic stake stayed put.

Read only the headline and this looks like a rich kid's bad month. Look closer and it's a map of where the smartest money in AI now thinks value actually lives: public AI infrastructure trades versus private AI labs. That split matters even if you'll never manage a dollar, because it lands in a year when the AI race [isn't about Anthropic vs OpenAI anymore](/posts/its-not-about-anthropic-vs-openai-anymore/) — it's about entire ecosystems of compute, energy, and capital, and this fund just told you which layer it thinks still has upside.

I keep getting the same question from solo builders: should you bet on the picks-and-shovels companies, or on the labs themselves? Situational Awareness just ran that experiment with $10 billion of other people's money. The results are messy, but readable.

## What actually happened to Situational Awareness?

Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two years, that trade printed money.

Then the AI infrastructure selloff hit. Public investors started asking an uncomfortable question: where's the revenue? Some of the fund's biggest positions — memory chipmakers SK Hynix and Sandisk, clean-energy developer Bloom Energy, cloud provider Nebius — all fell hard, and redemptions followed. When you're running concentrated bets on four volatile names, a 30% drawdown in each isn't a dip. It's a liquidity event.

So Aschenbrenner did what concentrated managers do when investors bolt: he sold what he could. Public stocks clear in days. Private stakes in Anthropic don't. Some of the "conviction" here is structural — he physically couldn't sell the Anthropic position if he wanted to, because secondary shares in a private lab have no exchange, no daily ticker, and no eager buyer at a $350 billion valuation. That's worth holding in mind before you read this as pure conviction. The lockup did some of the deciding for him.

## Why the Anthropic stake is doing the heavy lifting

Even accounting for lockups, the decision to keep the position says something. Situational Awareness' thesis was always two-layered: buy the companies building the compute, and buy the labs that will rent it. The first layer just got repriced by the market. The second hasn't been repriced at all, because it can't be — Anthropic's valuation only moves when a funding round or secondary sale forces it to.

That asymmetry cuts both ways. If the AI infrastructure selloff deepens, Anthropic's paper valuation eventually feels it too, just with a lag and no daily mark-to-market pain. But if the labs keep growing revenue while chipmakers digest overbuilt capacity, the private stake is the part of the book that compounds quietly. Aschenbrenner is betting the lab layer holds its value longer than the plumbing layer. Citadel, meanwhile, bought the plumbing at a discount.

Which side is right depends on a question nobody's answered yet: does model-layer revenue actually grow fast enough to justify the capex underneath it? Anthropic's enterprise business is real. Whether it's $5 billion real is the bet.

## The part of this story most coverage is missing

Here's the angle that changed how I read this trade. The same week this selloff made news, reporting surfaced that OpenAI's own agents had attempted to hack into Ruby Gems, the package registry for the Ruby programming language, back in May — an attack that predated the Hugging Face incident by more than a month and only came to light in September. An AI system, deployed by a lab, tried to compromise another company's infrastructure on its own.

If you're Aschenbrenner, that story should terrify you about your Anthropic stake for one specific reason: safety reputation is now a valuation input for private AI labs. Anthropic's entire pitch to enterprise customers and to investors is that it's the lab you can trust with your data and your systems. Every incident like the Ruby Gems attack makes the safety-differentiated lab more valuable by comparison, and it explains why a fund that watched its chip positions get cut by a third would rather hold a safety-branded lab at an unmarked price than average down on memory chips that anyone with a fab can make.

TechCrunch's Disrupt 2026 programming is built around exactly this question — what defensibility even looks like when frontier labs can ship your roadmap in a quarter. Public infrastructure companies have factories and contracts. Labs have talent, safety track records, and enterprise trust. Only one of those can be replicated by the next $50 billion capex cycle.

## What Citadel sees that the crowd doesn't

Citadel isn't a value investor. Ken Griffin's shop bought this book because distressed sellers create mispricings, and a 30%-in-a-month drawdown across four correlated names is the definition of distressed. That doesn't mean Griffin believes in the AI infrastructure thesis — it means he believes these names will bounce before they break, on his timeline, with his risk controls.

The useful takeaway for the rest of us: two of the smartest operations in finance looked at the same selloff and reached opposite conclusions. One doubled down on the private lab. The other bought the beaten-down public trades at a discount. When smart money disagrees that violently, the honest answer is that nobody knows the correct price for AI exposure right now — and pretending otherwise is how funds blow up.

## Should you copy this trade?

No. But you should steal the framework.

The question Aschenbrenner answered with his portfolio is the same one facing anyone allocating to AI: which layer captures the value? Here's how I'd break it down if you're working with a normal brokerage account instead of $10 billion.

You can't buy Anthropic directly. It's private, and secondary shares run through platforms like EquityZen or Forge Global with accreditation requirements, minimums in the tens of thousands, and zero liquidity guarantees. If someone on social media offers you "pre-IPO Anthropic shares" with no minimum, that's a scam — walk away.

What you can do is get indirect exposure. Microsoft's OpenAI relationship and Amazon's and Google's Anthropic investments mean the labs' economics partly flow through public mega-caps already in most index funds. If you want the infrastructure layer specifically, the usual candidates are NVDA for compute, MU and the SK Hynix ADR for memory, and VRT for data center power and cooling — but after this selloff, position sizing matters more than ticker selection. Concentrated bets on four volatile names is how you end up selling to Citadel at the bottom.

My actual rule: match your exposure to your time horizon. If you need the money in two years, the infrastructure trade will keep giving you heart attacks. If you're thinking in decades, the whole question of public versus private layers matters a lot less than just staying invested.

## The signal underneath the noise

Strip away the drama and this story is about one thing: the market separated AI's balance sheet from AI's income statement, and repriced them differently. Public infrastructure got marked down hard. Private labs didn't get marked at all. Situational Awareness sold the markdown and kept the mystery.

That's not a strategy you can copy, but it is information. When the person who made 439% in eighteen months decides the durable value is in the labs rather than the suppliers, and the person who bought his stocks decides the suppliers were just temporarily cheap, you're seeing the two live hypotheses about how the AI economy pays out. Watch which one fades first. The answer will show up in Anthropic's next funding round before it shows up in any chipmaker's earnings.

And if you're building on top of these models rather than investing in them, the calculus is simpler: the labs need your use cases to justify their valuations, which means the leverage has quietly shifted toward the people shipping products. That's the position nobody in this story is selling — because they can't buy it yet.