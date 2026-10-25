---
title: "How I Audited My Mac's AI Agent Permissions After Meta's Muse 0-Day"
date: 2026-10-25
draft: false
description: "Meta's Muse needed a hotfix for a 0-day that handed over account tokens. I audited every AI agent permission I've granted — here's the 20-minute version."
tags: ["AI agents", "security", "Meta", "Muse", "macOS"]
categories: ["tools"]
slug: "meta-muse-zero-day-agent-permissions"
keywords: ["Meta Muse zero day", "AI agent permissions", "AI assistant security"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/meta-muse-zero-day-agent-permissions.jpg"
  alt: "Zoe at a cafe table reviewing a permissions checklist on her laptop, coffee beside her"
faqs:
  - q: "What was the Meta Muse zero-day?"
    a: "A flaw that let any local app or terminal command change Muse's transcription endpoint. Attackers pointed it at their own server, captured the account token, and gained full control of the Muse account. Meta shipped a hotfix about 12 hours after disclosure."
  - q: "Did attackers need physical access to the Mac?"
    a: "No — that's Meta's framing, and it's misleading. A ClickFix social-engineering trick was enough to run the required command, which makes the exploit effectively remote."
  - q: "Why was Muse vulnerable when macOS has protections?"
    a: "Muse requires extraordinarily broad permissions — mic, camera, files, location, calendars, and connected accounts — which undoes macOS's default defenses. It also used cloud transcription instead of the on-device option macOS already provides."
  - q: "What should I do with AI agents I already use?"
    a: "Audit what each one can access, revoke what it doesn't need, turn off purchasing where possible, and treat agent tokens like passwords — anything that can read them can be you."
---

{{< audio src="/audio/meta-muse-zero-day-agent-permissions.mp3" >}}

Meta's newest AI assistant got hacked with a single terminal command, and the scariest part isn't the bug — it's how normal the setup was. Muse, the assistant Meta introduced to book appointments, fill out forms, handle customer service, and even make purchases, needed a hotfix last week for a zero-day that handed attackers the token to your entire account. When I read the details, I didn't write a post about Meta. I opened my own Mac and audited every AI agent permission I've granted. What I found took 20 minutes and changed how I configure every agent from here on.

The context first. We covered [what Muse and Spark actually are when they work](/posts/meta-muse-spark-1-1-what-solo-builders-need-to-know/) — Meta's push to make agents do real work for regular people. Muse is that push at full speed: it connects to your WhatsApp, email, calendar, and social accounts, writes files, uses your mic and camera, and creates new tools on the fly when a task needs one. That last part is the pitch and the problem. To do all this, Muse asks for extraordinarily broad permissions — permissions that quietly dismantle the macOS defenses Apple spent years building.

## What I actually did

The zero-day, found by macOS security researcher Patrick Wardle, worked like this: any locally installed app or terminal command — regardless of its permissions — could change a list of undocumented Muse settings. One of those settings controlled where voice transcription happened. Point it at an attacker's server instead of Meta's, and the next voice prompt carried the account token straight to the attacker. Full account control: WhatsApp history, email, calendar, purchases. Wardle demonstrated attacks that wrote files to disk and took photos with no visible sign anything happened. A ClickFix social-engineering trick — the same scam that's infecting Macs and PCs at scale — was enough to trigger it, which is why Meta's "not a remote exploit" defense missed the point.

Meta shipped a hotfix about 12 hours after disclosure. But the design choices that made it possible — cloud transcription when macOS offers on-device, agent tokens any local process could touch — are choices every AI agent currently makes to some degree.

So I made a list. Every AI assistant, agent, and automation I'd granted access to something: my calendar, my email, my files, my browser. Then I went through it permission by permission.

## Do this yourself

Twenty minutes, no code:

1. **List every agent with account access.** Chat assistants that read your calendar, meeting notetakers on your calls, browser agents, shopping agents, and anything connected to your email. Write down what each one can touch.
2. **Check for on-device alternatives.** Muse's transcription flaw existed because dictation ran in the cloud. Wherever an agent offers an on-device or local processing option — transcription, file analysis — switch it on. Local means the data never leaves your machine for an attacker to intercept.
3. **Revoke purchasing power.** Amazon already blocked Muse from shopping on its site, calling it an "unauthorized AI agent." Follow the platform's lead: don't let agents spend money without a confirmation step you control. This is the same tension [agentic commerce is hitting everywhere](/posts/doordash-cli-agentic-commerce-solo-builders/).
4. **Treat agent tokens like passwords.** Anything that can read an agent's authentication token can be you — send email, read messages, spend money. Store tokens in your password manager or the system keychain, never in plaintext files or clipboard history.
5. **Re-grant on a schedule.** For each agent, set a mental (or calendar) rule: access expires unless you re-confirm it quarterly. Agents change, updates ship, permissions creep back.

If you want the deeper picture of agent-on-agent risk after this audit, [the agent-vs-agent defense stack](/posts/agent-attacks-agent-aisi-defense-stack/) covers what happens when agents fight each other — and it's no longer hypothetical.

## What failed

Two honest misses.

**I found permissions I'd granted years ago and forgot.** A meeting notetaker still had calendar access from a project that ended in 2024. A browser extension agent had file access "for downloads" I'd never used. The audit found four stale permissions — none catastrophic, all unnecessary.

**Revoking broke one automation mid-flight.** I removed email access from an agent that turned out to send my weekly client summaries. The fix took ten minutes, but the lesson stands: re-grant deliberately, with the least access that makes the workflow work — not the access the onboarding screen asks for by default.

## Who should skip this

If you use AI strictly in a browser, chat-only, with no account connections, you're mostly fine — there's little for an attacker to hijack. Come back when you connect your first calendar.

Skip this too if you're fully managed by an IT department that handles this for you. But if you run your own one-person business on a Mac with agents touching email, files, or money, you're the exact profile this attack was built for. Pair the audit with [Nvidia's free AI vulnerability scanner](/posts/nvidia-osaa-ai-security-garak-test/) if you run your own model endpoints, and learn to [spot fake AI agent identities](/posts/ai-agents-fake-identities-spot-them/) — the impersonation side of the same problem.

## The takeaway

The Muse zero-day will be patched, forgotten, and cited in security talks for years. The durable lesson is simpler: every AI agent you grant broad permissions is a standing invitation, and the industry's answer — "we tested it hard" — doesn't survive contact with a determined researcher. Twenty minutes of permission auditing is the cheapest security you'll ever buy. Do it before the next agent asks for your calendar.
