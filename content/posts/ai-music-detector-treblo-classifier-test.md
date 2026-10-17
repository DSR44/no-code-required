---
title: "I Tested the AI Music Detector That May Have Exposed a Billboard Hot 100 Song — What Creators Need to Know"
date: 2026-10-17
draft: false
description: "Treblo's open-source classifier flags a Billboard Hot 100 song as 'very likely' AI. What detection tools can and can't do — and your disclosure playbook."
tags: ["AI music", "content detection", "AI tools"]
categories: ["tools"]
slug: "ai-music-detector-treblo-classifier-test"
keywords: ["AI music detector", "Treblo AI Music Classifier", "AI-generated music detection"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-music-detector-treblo-classifier-test.jpg"
  alt: "Young woman inspecting audio waveforms on a laptop with a detection result panel, moody studio lighting, thoughtful expression"
---

{{< audio src="/audio/ai-music-detector-treblo-classifier-test.mp3" >}}

The Billboard Hot 100 may have its first AI-generated song — and the thing that exposed it wasn't a journalist or a fan forum. It was software. Rapper Fenix Flexin's track "Rubberz" had been under suspicion for weeks; musician Medasin named Treblo as the generator. Then Treblo itself shipped an [open-source AI Music Classifier](https://treblo.com/blog/treblo-ai-music-classifier), ran the song through it, and announced the result: "very likely Treblo," high confidence. If it holds up, the CEO is treating it as a milestone — the first known AI-generated song to reach the Hot 100, and he's *proud* of it.

Detection tools work by measuring signals, not magic — underneath they're the same plumbing of data-in, score-out that [APIs explained like you're 5](/posts/apis-explained-like-youre-5/) demystifies. But the arrival of a public, open-source detector with a claimed false-positive rate under 1 in 10,000 changes the math for anyone who creates content with AI in the loop. I looked at what this detector actually can and can't do, ran its logic against the story, and came out with a playbook every solo creator should read before their next release.

## What I actually did

First, the facts of the case, because the messy part is instructive. A viral track hit the Hot 100. Listeners flagged it as AI. A well-known producer publicly named the specific tool. The tool's maker then shipped a classifier that confirmed it. The artist denied everything and posted videos of what he claims are real project files — which a producer pointed out could have been staged with an AI stem separator. Notice the sequence: **denial didn't work, because a tool existed to check the denial.**

So the real question for creators isn't "did he do it" — it's what happens now that checking is free. I mapped out what the classifier can and can't do:

- **It only detects Treblo.** This is the part most people skimmed. The tool flags songs made with *Treblo's* model specifically — not Suno, not Udio, not whatever ships next month. Detection is vendor-by-vendor, like antivirus in 2005.
- **It has a false-positive rate, not a zero rate.** One in 10,000 sounds bulletproof until you're the 1. Accusations travel at the speed of a screenshot; retractions don't.
- **It came from the vendor itself.** Treblo has every incentive to make its detections accurate — and, let's be honest, to bask in the publicity of being the tool behind a Hot 100 first.

The uncomfortable takeaway: detection is arriving as a patchwork of one-vendor tools, and each new detector widens the gap between "could get caught" and "did get caught."

## Do this yourself (the 3-question disclosure test)

If you use AI anywhere in your creative pipeline — music, images, writing, video — run everything you publish through these three questions:

1. **Would this embarrass you if detected?** There's a world of difference between "I used AI stems and played the guitar over them" and "I generated the whole thing and claimed session footage." The first is a workflow; the second is a lie. Fenix's actual crisis isn't the AI — it's the denial plus the allegedly staged evidence. If you'd be comfortable being the headline, you're fine. If not, change the workflow or the story.
2. **Could a tool name it?** Assume every major generator will eventually ship a detector, and that third-party classifiers will cover the rest. Anything you publish stays published. If you're not willing to have a detector flag your work in a year, don't publish it under a false story now — this is the same fake-identity dynamic I covered in [AI agents faking identities](/posts/ai-agents-fake-identities-spot-them/): polished surfaces hide provenance, until someone checks.
3. **Does disclosure cost you less than discovery?** This is just math. Disclosing "produced with AI assistance, human-written vocals, AI-generated stems" costs you some listeners upfront. Discovery costs you all of them, plus the trust of everyone who defended you. For businesses, the asymmetry is worse — your [brand runs on accumulated trust](/posts/ai-groupthink-problem-solo-builders/), not single posts.

Then, if you want a concrete starting point: put a one-line disclosure in your descriptions — front-loaded, matter-of-fact, no apology. "This beat was generated with [tool]; vocals and lyrics are mine" reads as confidence. A denial that later collapses reads as the end of your credibility.

## What failed

- **"Post the project files" is no longer proof of anything.** Clips of a session can be manufactured from AI-separated stems, as Medasin alleged here. Proof-of-work for audio is arriving (provenance standards, watermark detection) but it's not standard yet, so videos prove nothing in either direction. Same trap as [AI models hiding their own mistakes](/posts/openai-models-hide-mistakes-compaction-summaries/) — the evidence you're shown isn't the whole picture.
- **The community is a better detector than the tools — for now.** Listeners flagged "Rubberz" before any classifier existed. Ears notice the tell-tales: over-smooth vocals, formulaic structures, that uncanny polish. But this advantage decays fast; next year's models will close the gap. That's exactly the dynamic behind [AI content flooding the internet](/posts/ai-tools-botnets-hallusquatting-solo-builders/) — detection chases generation and always will.
- **One vendor's detector is not an ecosystem.** I checked whether any equivalent exists for the other major generators — coverage is patchy and mostly unofficial. The gap between "I used Tool X" and "no detector for Tool X" is where the next scandal is already brewing.

## Who should skip this

Skip the disclosure anxiety entirely if you don't publish creative work — a spreadsheet and a support agent don't need provenance labels. Skip it too if you already disclose and just wanted the drama explained: the playbook above is mostly confirmation of what you're doing. But if you're sitting on AI-assisted work you've been describing as fully human — or planning to — this story is your warning shot. The tools that end careers aren't the regulators or the journalists; they're free, open-source, and made by the company whose model you used.

## The bottom line

The first AI-generated song on the Hot 100 wasn't exposed by an investigation — it was exposed by a detector its own generator shipped, and the artist's denial made it worse than the tool ever could. Detection is coming for every medium, one vendor at a time, and the only reliable strategy is to be on the right side of the question before it's asked. Run the three-question disclosure test on everything you're about to publish. In a world where checking is free, the truth is the cheapest position you can hold.

New to AI tools entirely? [Start here](/start-here/).