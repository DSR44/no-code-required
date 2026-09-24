---
title: "Ordering DoorDash From the Command Line: The 2-Month Reality Check"
date: 2026-09-24
draft: false
description: "DoorDash's dd-cli is two months old now. What's actually in the tool, who can use it, and whether you should let an AI agent spend your money."
tags: ["AI tools", "ai-agents", "DoorDash", "command line", "agentic commerce"]
categories: ["tools"]
slug: "doordash-command-line-reality-check"
keywords: ["order DoorDash command line", "dd-cli DoorDash terminal", "DoorDash CLI update", "AI agent food ordering", "agentic commerce DoorDash"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/doordash-command-line-reality-check.jpg"
  alt: "Zoe in a cozy home office at a laptop with a terminal window open, coffee mug nearby"
---
{{< audio src="/audio/doordash-command-line-reality-check.mp3" >}}

Two months ago I wrote about DoorDash launching a command-line ordering tool and called it the most important signal solo builders had gotten in months. Back then it was a waitlist beta with a demo video. This week I went back through the actual repository, the release notes, and a growing pile of issue-tracker friction reports — because the gap between "demo" and "daily tool" is where most of these things quietly die. This one is doing better than I expected, with caveats that matter if you're tempted to hand it your credit card.

If you're new here: `dd-cli` is DoorDash's official terminal tool. Search restaurants, browse menus, build a cart, apply a promo, set a tip, submit the order — all without opening the app. It's built to be driven by a human, or called by AI agents with shell access like Claude Code or Codex. My first post covered [why agentic commerce matters for solo builders](/posts/doordash-cli-agentic-commerce-solo-builders/) — this one covers what the tool actually looks like now that real people are using it.

## What's actually in the tool now

The feature list is wider than the launch coverage suggested. Beyond the basics, current builds support saved addresses and default selection, card payment methods, store and menu search, individual and group carts, building a cart from a shopping list, listing and applying eligible promos, applying company or employee payment budgets, order preview with full pricing, pickup or delivery, ASAP or scheduled, priority versus standard speed, and order history with receipts.

That last category is the sleeper feature. Reordering a past order with one command is the workflow most people will actually use daily, and it's exactly the kind of repetitive task agents handle well. DoorDash also ships a browser checkout URL as a fallback whenever a step can't complete in the terminal — which sounds like a cop-out until you realize it's the safety valve for the edge cases agents fumble.

Support is macOS on Apple Silicon and Linux on x86_64; Windows users are still out in the cold. It also exposes its service to AI chatbots like ChatGPT and Claude, and the same agent-hits-browser pattern shows up everywhere — it's the same failure mode I described in [why AI browser agents keep getting stuck](/posts/why-ai-browser-agents-keep-getting-stuck-and-what-solo-builders-can-use-instead/).

## The friction report: what using it really costs

Now the part the launch coverage skipped. The issue tracker reads like a field guide to early-tool pain:

On Linux, even printing the help text for service commands fails unless you've exported an access token manually, because the tool insists on a keychain that desktop Linux doesn't have in the form it expects. Promos are half-in: you can list and apply codes from the terminal, but some eligible promos can only actually be redeemed by falling back to the browser checkout URL — the tool itself tells you this in a help message. And a user filed a feature request this week asking DoorDash to put expiry dates on promotions, because right now the CLI will happily show you a promo that may or may not still be alive.

None of these are dealbreakers. All of them are the texture of a v0.2 tool. If you're the person who installs things on day one for fun, you'll enjoy the archaeology. If you want software that never surprises you, wait a quarter.

## The security question you should actually think about

Here's the part I'd underline for the "let my agent handle dinner" crowd. The tool is distributed as a bare binary with a checksum to verify and a security notice that boils down to: you're running third-party internet software, verify it or don't complain. Fine. The more interesting decision isn't the download — it's what happens after `dd-cli login`.

Once authenticated, the CLI holds a token that can spend money on your saved payment methods. If you let an AI agent drive your shell, you've given that agent a food budget with no separate confirmation step. There's no per-order approval flow, no spend cap you can set in the terminal, nothing that makes an agent pause before submitting. DoorDash's own docs suggest the browser-checkout fallback as the safety hatch for ambiguous cases, which implies the design intent: agents should stop short of the final submit and let a human click. My take: keep it that way for now. Let agents search, build carts, and preview totals — press the button yourself. This matches the rule I keep repeating in these posts: [an AI agent with tool access is only as trustworthy as the blast radius you gave it](/posts/ai-agents-explained-what-tool-calling-actually-means/).

The same logic runs underneath [the web MCP standard](/posts/webmcp-web-standard-ai-agents-browser/) — when your wallet token sits in a shell or browser an agent controls, the confirmation step is the whole ballgame.

Also do the boring thing the README begs you to do: verify the SHA256 checksum before running the binary. It takes thirty seconds and it's the difference between a food order and a mystery process on your machine.

## The waitlist is the real gate

One thing that hasn't changed: this is still waitlist-only. You can download the binary today, but full functionality requires an approved account, and login is gated behind DoorDash's approval queue. The sign-up form asks what you'd build with it, which has been true since launch — DoorDash is curating its early ecosystem, not just scaling a waitlist. If you applied in July and heard nothing, that's the norm, not a bug. The realistic timeline for "order dinner from my terminal" as an ordinary-person experience is months, not weeks.

## What this says about where commerce is going

The reason I keep covering this unglamorous tool: it's the cleanest live example of companies rebuilding their products for agents instead of screens. DoorDash now has ordering surfaces in iMessage, a chatbot, ChatGPT, Claude connectors, and the terminal. Each one is a bet that the next order won't start in their app. The same pattern showed up in [Salesforce making its own interface optional](/posts/salesforce-aiforce-headless-slackbot/) this week — when two companies this size both stop defending their UI, the shift isn't a trend anymore, it's the default.

For a solo builder, the practical playbook hasn't changed since my first post: watch which companies expose clean programmatic interfaces, because those are the rails your future workflows run on. DoorDash just moved from "announced" to "installable with friction" — which is exactly the stage where you should kick the tires on a throwaway account, not your main card.

The bottom line: `dd-cli` is real, limited, slightly rough, and quietly the most honest preview of agentic commerce you can touch today. If you're brand new to this whole space, the [start-here guide](/start-here/) is the better first stop — then come back and read the GitHub issues before you grant anything shell access to your wallet.
