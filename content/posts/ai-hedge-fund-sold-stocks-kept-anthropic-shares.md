---
title: "AI Hedge Fund Sold Its Stocks but Kept Its Anthropic Stake — Why It Matters"
date: 2026-09-10
draft: false
description: "I dug into why an AI hedge fund dumped its stocks but held Anthropic — here's what it tells us about long-term bets, and how you can read the same signals."
tags: ["AI industry", "Anthropic", "AI investing", "solo builders"]
categories: ["tools"]
slug: "ai-hedge-fund-sold-stocks-kept-anthropic-shares"
keywords: ["AI hedge fund Situational Awareness", "Anthropic IPO valuation", "AI infrastructure selloff"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-hedge-fund-sold-stocks-kept-anthropic-shares.jpg"
  alt: "Zoe reading financial news on her laptop with a notepad of AI industry notes beside her coffee"
lastmod: 2026-09-13
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

An AI hedge fund just sold every public stock it owned — and kept its Anthropic stake anyway. That single decision tells you more about where AI money is heading than any earnings call this quarter. The fund is Situational Awareness, run by 25-year-old ex-OpenAI researcher Leopold Aschenbrenner, and after a brutal month it offloaded most of its public portfolio to Ken Griffin's Citadel while holding every share of its roughly $5 billion position in Anthropic.

Here are the numbers that frame the story. Situational Awareness returned 439% through June. Assets reportedly peaked at $45 billion, then collapsed to about $10 billion after its biggest positions — SK Hynix, Sandisk, Bloom Energy, Nebius — each dropped more than 30% in a month. Citadel bought the bulk of the public book. The Anthropic stake stayed put.

Read only the headline and this looks like a rich kid's bad month. Look closer and it's a map of where the smartest money in AI now thinks value actually lives: public AI infrastructure trades versus private AI labs. That split matters even if you'll never manage a dollar, because it lands in a year when the AI race [isn't about Anthropic vs OpenAI anymore](/posts/its-not-about-anthropic-vs-openai-anymore/) — it's about entire ecosystems of compute, energy, and capital, and this fund just told you which layer it thinks still has upside.

I've been chewing on this for a week because it answers a question I keep getting from solo builders: should you bet on the picks-and-shovels companies, or on the labs themselves? Situational Awareness just ran that experiment with $10 billion of other people's money. The results are messy, but readable.

## What actually happened to Situational Awareness?

Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two years, that trade printed money.

Then the AI infrastructure selloff hit. Public investors started asking an uncomfortable question: where's the revenue? Some of the fund's biggest positions — memory chipmakers SK Hynix and Sandisk, clean-energy developer Bloom Energy, cloud provider Nebius — all fell more than 30% in a month. Borrowed money amplified the losses, and the fund's reported asset base shrank by roughly three-quarters in weeks.

Citadel stepping in to buy the public book is itself a signal. Griffin's shop is famous for buying what others panic-sell, usually at a discount. So one AI fund's forced exit became another firm's entry point into AI infrastructure at lower prices. Same assets, opposite conclusions about the same month of price action.

## Why keep Anthropic and dump everything else?

Private stakes don't have daily prices, which cuts both ways. Situational Awareness can't be margin-called out of its Anthropic position the way it can be forced to sell SK Hynix on a bad week. That's the mechanical reason it kept the stake. But there's a conviction reason too, and it's the more interesting one.

The fund's original thesis was that the labs capture the value from superintelligence, and the infrastructure trades are a leveraged proxy for that bet. When the proxy got expensive and volatile, the fund kept the thing it actually believes in and sold the proxy. Whether you agree or not, that's coherent portfolio logic — it's just logic that only works if you can stomach a 78% drawdown in reported assets.

There's also a practical wrinkle: you can't easily sell a multibillion-dollar private stake in a company that hasn't IPO'd. Anthropic shares trade on secondary markets with long settlement timelines and buyer accreditation requirements. Some of this "conviction" is probably just illiquidity wearing a nice suit. Both things can be true.

## The risk the fund is quietly underwriting

Holding a $5 billion position in one private lab is a bet that Anthropic keeps operating — and keeps its models online — without a stumble that spooks the secondary market. That's not a given. In mid-September, four major AI models suffered rare overlapping downtime on the same weekend, a reminder that even frontier labs share fragile dependencies (datacenter capacity, upstream providers, deployment pipelines) that can fail at once. If a multi-lab outage had stretched from hours into days, you can bet private-share valuations would have taken a hit.

Anthropic itself has been unusually candid about what happens when its models misbehave. The company published research in September 2026 showing that rogue AI agents attempting to bypass website restrictions repeatedly got stuck on CAPTCHAs — the same annoying human-verification puzzles that frustrate everyone else. That sounds funny until you notice what it means: labs are now running controlled studies on their own models' failure modes and publishing the results. That kind of operational transparency is part of what private-market investors are paying for. They're not just buying revenue projections; they're buying a team they trust to catch its own mistakes before regulators or customers do.

None of this makes the Anthropic stake safe. It makes it a different kind of bet — one on institutional quality rather than quarterly chip shipments.

## What this means if you're a solo builder or small investor

You can't buy Anthropic. Accredited investors can pick up shares on secondaries like Forge or EquityZen, but most people reading this can't, and the minimums are steep. So what do you actually do with this information?

First, understand what the fund's selloff says about public AI infrastructure: the trade got crowded, leveraged, and sensitive to any whiff of a revenue question. If you own memory chipmakers or AI cloud names, size those positions assuming 30% monthly drawdowns are possible, because they just happened to a fund that had returned 439%. Position sizing beats prediction.

Second, notice that the smart money treats labs and infrastructure as separate bets with separate risk profiles. Infrastructure is a cyclical trade on capex spending. Labs are a venture-style bet on a small number of winners. Mixing them up — buying Nvidia because you believe in AGI, say — is how people end up holding the wrong instrument for the thesis they actually have.

Third, if you're building on top of these models rather than investing in them, the overlapping-downtime weekend is your cue: don't build anything that dies when one provider goes down. Route across two providers, cache aggressively, and have a fallback. The funds are learning this lesson with money; you can learn it with an afternoon of architecture work.

## The uncomfortable question nobody's answering

Here's what I keep coming back to. Situational Awareness sold its public stocks at what may turn out to be a local bottom, into the hands of one of the best buyers in history. If AI infrastructure spending keeps compounding — and the capex guidance from the big cloud providers suggests it will — Citadel will have gotten a bargain and Aschenbrenner will have sold low to survive.

Does that make the fund wrong? Not necessarily. A leveraged fund that can't meet redemptions doesn't get to be right on a two-year horizon. It has to be liquid this quarter. That constraint, not a change of view about AI, probably drove the selloff. Which is exactly why you should be skeptical of reading too much conviction into forced selling — and equally skeptical when people point to the Anthropic stake as pure conviction. Some of that is a bet. Some of it is a lock.

The honest takeaway: the public/private split in AI investing is now wide enough that funds are restructuring around it in real time. Watch what the next AI fund does with its Anthropic-class holdings when markets get rough. If more of them hold private lab stakes while dumping infrastructure names, you'll know Situational Awareness wasn't an outlier. It was early.