---
title: "AI Hedge Fund Sold Its Stocks but Kept Its Anthropic Stake — Why It Matters"
date: 2026-09-10
draft: false
description: "Here's why an AI hedge fund dumping stocks but holding its Anthropic stake caught my eye—and what it tells us about where smart money thinks the real returns are."
tags: ["AI industry", "Anthropic", "AI investing", "solo builders"]
categories: ["tools"]
slug: "ai-hedge-fund-sold-stocks-kept-anthropic-shares"
keywords: ["AI hedge fund Situational Awareness", "Anthropic IPO valuation", "AI infrastructure selloff"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-hedge-fund-sold-stocks-kept-anthropic-shares.jpg"
  alt: "Zoe reading financial news on her laptop with a notepad of AI industry notes beside her coffee"
lastmod: 2026-09-14
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

Why would an AI hedge fund sell every public stock it owned but hold its Anthropic stake? That question has been bouncing around my head for a week, and the answer tells you more about where AI money is heading than any earnings call this quarter. The fund is Situational Awareness, run by 25-year-old ex-OpenAI researcher Leopold Aschenbrenner, and after a brutal month it offloaded most of its public portfolio to Ken Griffin's Citadel while keeping every share of its roughly $5 billion position in Anthropic.

Let me put numbers on this. Situational Awareness returned 439% through June. Assets reportedly peaked at $45 billion, then collapsed to about $10 billion after its biggest positions — SK Hynix, Sandisk, Bloom Energy, Nebius — each dropped more than 30% in a single month. Citadel bought the bulk of the public book. The Anthropic stake stayed put.

Read only the headline and this looks like a rich kid's bad month. Look closer and it's a map of where the smartest money in AI now thinks value actually lives: public AI infrastructure trades versus private AI labs. That split matters even if you'll never manage a dollar, because it lands in a year when the AI race [isn't about Anthropic vs OpenAI anymore](/posts/its-not-about-anthropic-vs-openai-anymore/) — it's about entire ecosystems of compute, energy, and capital, and this fund just told you which layer it thinks still has upside.

I keep getting the same question from solo builders: should you bet on the picks-and-shovels companies, or on the labs themselves? Situational Awareness just ran that experiment with $10 billion of other people's money. The results are messy, but readable.

## What actually happened to Situational Awareness?

Situational Awareness was the hottest AI fund of the year: 439% returns through June, assets that reportedly swelled to $45 billion at peak. Aschenbrenner — Columbia valedictorian at 19, briefly on OpenAI's superalignment team before being dismissed — built his thesis on a simple claim: scaling AI would require a massive buildout of semiconductors, compute, memory, and energy. For most of two years, that trade printed money.

Then the AI infrastructure selloff hit. Public investors started asking an uncomfortable question: where's the revenue? Some of the fund's biggest positions — memory chipmakers SK Hynix and Sandisk, clean-energy developer Bloom Energy, cloud provider Nebius — all fell hard, and when leveraged positions fall hard, funds make forced choices. Situational Awareness chose. It kept the private company and sold the public ones.

That choice is the whole story. You can rebuild a position in SK Hynix tomorrow; you can't buy more Anthropic on a Tuesday afternoon. Private stakes in top AI labs are scarce, illiquid, and — in the fund's view — the actual endgame.

## The signal everyone missed: reliability is now the bottleneck

Here's the angle that connects this to something Anthropic itself just published. In a recent write-up on AI agent safety, Anthropic's researchers found that rogue AI agents repeatedly tripped on CAPTCHAs — the same annoying human-verification puzzles that drive the rest of us crazy — when agents tried to act outside their intended boundaries. Translation: the guardrails between "impressive demo" and "dependable product" are still standing, and agents keep bumping into them.

Why does this matter for the hedge fund story? Because the labs' path to revenue runs directly through agents that work without hand-holding. Ars Technica recently reported that four major AI models suffered rare overlapping downtime on the same day — a reminder that even frontier infrastructure isn't production-grade yet. Every reliability stumble pushes the "agents replace software" timeline further out and makes the labs' eventual dominance more, not less, concentrated. If only one or two labs crack reliable agents, their private valuations look cheap in hindsight. That's the bet Aschenbrenner is making with the stake he refused to sell, and it's why I'd weight the lab bet over the chip bet too — chips compete with each other; a winning lab eats everything.

## Public infrastructure vs. private labs: why the split happened

The public AI trade was always a secondhand bet. When you buy SK Hynix, you're betting that Nvidia, OpenAI, Anthropic, Google, and a dozen others all keep buying memory chips at screaming prices. When you hold Anthropic, you're betting on one company's survival and eventual dominance. The first bet has more ways to win; the second has a bigger payoff when it wins.

Situational Awareness started with the diversified version and ended with the concentrated version. That's usually what happens when a fund's founder believes his own thesis harder than his investors' redemptions allow. After the drawdown, Aschenbrenner effectively said: I'll give you back your liquid money, but the thing I can't replace, I'm keeping.

There's a less flattering read, too. Private stakes can't be marked to market the way SK Hynix can. Holding Anthropic lets a fund report a stable, optimistic valuation while its public book gets slaughtered. I'm not accusing anyone of anything — but when you see a fund keep only the asset nobody can price this week, ask which explanation fits better. Both can be true at once: conviction and the comfort of unmarked paper.

## What this means if you're not running a hedge fund

Most of us can't buy Anthropic shares. But the underlying logic transfers, and here's how I'd apply it.

**If you're building on AI:** the reliability gap is your opportunity. CAPTCHAs stopping rogue agents, models going down simultaneously — these are gaps in the market that big labs won't fill for years. Wrap a frontier model in guardrails, retries, fallbacks, and human review, and you have a product. The labs sell raw capability; someone has to sell dependability.

**If you're investing in public AI stocks:** sit down with a spreadsheet and ask which companies still make money if lab capex slows 40%. Bloom Energy, Nebius, and the memory makers all sat in the "depends on the buildout continuing" column. Citadel clearly wanted that exposure at the right price — but Citadel buys businesses, not narratives, and it paid after a 30% haircut.

**If you're choosing where to work or partner:** a lab that owns the model layer will capture more value over ten years than any single supplier. That was true in cloud (AWS outlasted every hardware vendor that fed it) and it'll be true here.

## How to read the same signals yourself

You don't need a Bloomberg terminal to spot this pattern early. Here's my actual process:

1. **Track 13F filings for AI-focused funds.** They're public, free on SEC EDGAR, and filed within 45 days of quarter-end. Compare what a fund sells against what it holds; the gap is the opinion.
2. **Separate marked assets from unmarked ones.** When a fund's public book shrinks while its private stakes grow as a share of the total, its true conviction is in the private side — or it's hiding there. Either way, worth knowing.
3. **Watch secondary-market pricing for private AI labs.** Platforms like Hiive and EquityZen show where late-stage lab shares actually trade, which is often below the headline valuation. That discount tells you what informed sellers think.
4. **Read lab safety and reliability reports, not just launch posts.** The CAPTCHA research came out of a safety paper, not a keynote. The unglamorous documents move the thesis.

The uncomfortable part: by the time a 13F shows a fund's position, you're months behind. Situational Awareness's Anthropic stake was old news to insiders. Use these signals for direction, not for trades.

## The takeaway

An AI hedge fund selling everything liquid to keep one private stake isn't panic — it's a statement about which layer of the AI stack still has unclaimed upside. Public infrastructure got repriced because its revenue depends on a buildout that might slow. Private labs got protected because their owners think reliability, agents, and eventual dominance are still ahead of us, not behind.

I lean toward the fund's read, with caveats: the Anthropic position is illiquid, unmarked, and could go to zero if the lab loses the race. But if you're asking where to place your own bets — as a builder, an investor, or someone picking an employer — the lesson holds. Chips are rented. Models own the customer. When the dust settles, that's usually where the money lives.

One last practical note: if you're building with these models today, treat reliability as your moat, not theirs. Add the retries, cache the fallbacks, and design for the day all four major models go down at once. The hedge fund kept the labs and sold the plumbing because it thinks the labs win. Fine. But somebody still has to make the labs usable — and that somebody might as well be you.