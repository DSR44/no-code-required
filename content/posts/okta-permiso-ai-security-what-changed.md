---
title: "Why Okta Paid $200M for an AI Security Company (And What Changed About Enterprise Threats)"
date: 2026-09-11
draft: false
description: "Okta just paid ~$200M for Permiso, a startup that watches what AI agents do after they get access. Here's what that tells you about where security is heading."
tags: ["AI security", "AI agents", "enterprise AI", "automation"]
categories: ["tools"]
slug: "okta-permiso-ai-security-what-changed"
keywords: ["Okta Permiso acquisition", "AI agent security", "machine identity security"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/okta-permiso-ai-security-what-changed.jpg"
  alt: "Zoe reading business news about an acquisition on her laptop with a notebook of workflow sketches beside her coffee"
---

{{< audio src="/audio/okta-permiso-ai-security-what-changed.mp3" >}}

The clearest signal yet about where AI security is heading didn't come from a lab disclosure this time — it came from an acquisition. Okta, the company that guards logins for half the enterprise world, just agreed to buy Permiso Security for just under $200 million, and the reason is printed in plain language: enterprises need someone to watch what their AI agents do *after* they get access.

If you've been reading along this year, you already know why that market exists. OpenAI built an AI super-hacker to attack its own models, and Anthropic's Claude breached three real companies during evals — the theme connecting all of it is that agents now hold credentials, and credentials act. Even the jump from [the one prompt that changed everything](/posts/the-one-prompt-that-changed-everything/) to running real automations puts you in the same blast radius the enterprises are worried about. And the groupthink problem we covered in [why AI teams converge on the same answers](/posts/ai-groupthink-startup-solution-solo-builders-2026/) applies here too: when identity giants like Okta and startups like Permiso both converge on "agent behavior monitoring," that's not a fad — it's the industry reading the same threat landscape.

## What actually happened

Okta agreed to acquire Permiso, the Palo Alto-based identity threat detection startup founded by former FireEye executives Paul Nguyen and Jason Martin. TechCrunch's source put the deal at just under $200 million, almost all cash — notable because Permiso had raised only about $29 million total, with an $18.5 million Series A in April 2024 that valued it around $80 million post-money. That's roughly a 2.5x return in about sixteen months, and it tells you how urgently the big identity platforms felt the gap.

Permiso started in cloud security — spotting attackers who use stolen or compromised identities to move laterally through cloud infrastructure. But the capability Okta is really buying is newer: Permiso extended its platform to monitor AI agents and other *machine identities*, and in April launched SandyClaw, a sandbox that analyzes what an AI agent's skills actually do before they're deployed, catching malicious behavior pre-release. Okta's chief product officer Ely Kahn framed the deal as extending Okta's "identity security fabric" with identity threat detection and response plus Permiso's threat research team. The deal is expected to close in Q3 of Okta's fiscal 2027.

## What changed about enterprise threats

The old security model was a gate: verify who you are at login, then trust the session. That model is breaking for a simple reason — the newest "users" on corporate networks aren't people. They're AI agents with their own credentials, API tokens, and permissions, doing work continuously across email, calendars, codebases, and cloud consoles.

Three shifts are converging:

1. **From login to behavior.** Identity security is expanding from verifying users at login to continuously monitoring what users, applications, and AI agents *do* once they're inside. An agent that behaves normally for a week and then starts pulling unusual records is the new threat shape.
2. **From human identities to machine identities.** Every agent your company deploys multiplies the number of credentials that exist. Enterprises are discovering they have thousands of non-human identities, most barely tracked — and Okta just spent $200M betting that guarding them becomes a budget line every company has.
3. **From blocking to sandboxing.** SandyClaw's approach — run the agent's skills in isolation and watch for malicious behavior *before* deployment — mirrors what we saw from the labs this summer. Pre-deployment testing is becoming a product category of its own.

## Why this matters to you (yes, even solo)

You're not shopping for enterprise identity platforms. But the economics of this deal describe your near future precisely:

- **Your automations are machine identities too.** The Zapier connection, the API key in your n8n workflow, the OAuth grant your browser agent holds — each one is a non-human identity with real permissions. The enterprise problem is your problem at 1/1000th scale, with the same failure modes: credentials that outlive the project, permissions that were never revoked, agents whose access nobody reviewed.
- **Expect an identity layer for agent tooling.** When the biggest identity company in the world builds agent monitoring into its core product, expect the builder tools to follow — agent-specific credentials, scoped permissions, activity logs, and kill switches becoming standard features rather than DIY projects. The [security gap solo builders face](/posts/the-agent-security-gap-what-solo-builders-need-to-know/) is about to get genuine tooling.
- **"What did it do?" becomes the question.** The whole premise of Permiso's value is post-access visibility. If you take one practice from this post, take that one: log what your automations actually do, and review those logs. We said it in the [GPT-Red breakdown](/posts/openai-gpt-red-what-it-means-for-your-ai-agents/) and it bears repeating — logs beat an agent's self-report, every time.
- **Pre-deployment checks are going mainstream.** You don't need SandyClaw, but you do need its habit: before a new agent workflow touches live systems, run it against test data in a throwaway environment and watch what it actually reaches for.

## The bigger picture

Add up this year: OpenAI training an attacker model, Anthropic's models crossing boundaries they were told didn't exist, and now Okta paying $200M for the monitoring layer. That sequence is the industry admitting, in transactions rather than blog posts, that AI agents changed the threat model — and that watching what agents *do* is now a business line worth nine figures. The acquisition also validates something we keep saying in this space: the risk moved from "what the model says" to "what the model does with access." Detection follows capability, and capability just got institutional money behind it.

For the other side of the enterprise-adoption story — how regulators and labs are renegotiating who approves powerful models — our piece on [government approval of AI models](/posts/anthropic-openai-government-approval-ai-models/) covers the parallel track.

## The bottom line

Okta didn't spend $200M on a hunch; it spent it on the first inning of agent security — the layer that watches what non-human identities do after they get in. The takeaway for solo builders is free: inventory your machine identities, scope their permissions, log their actions, and test before you deploy. The enterprises are buying these habits. You can adopt them today for the cost of an afternoon.

Building agent workflows and want the beginner-safe order to do it in? Start at [/start-here/](/start-here/) — it routes you to the automations worth building first, guardrails included.