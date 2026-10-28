---
title: "I Treated My AI Agents Like Untrusted Employees After Microsoft's Warning"
date: 2026-10-28
draft: false
description: "Microsoft says AI agents should be treated like insider threats. I applied the rule to my one-person business in 20 minutes — here's the checklist."
tags: ["AI agents", "security", "Microsoft", "AI governance", "solo business"]
categories: ["tools"]
slug: "microsoft-agents-insider-threat-solo"
keywords: ["AI agents insider threat", "AI agent governance", "untrusted AI agents"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/microsoft-agents-insider-threat-solo.jpg"
  alt: "Zoe at a cafe table reviewing an access-control list on her laptop, coffee beside her"
faqs:
  - q: "Why does Microsoft call AI agents insider threats?"
    a: "Because they behave like rogue employees: they have legitimate access to your data and tools, they act autonomously, and they can't be trusted to follow judgment they were never trained on. Microsoft's security chief put it bluntly: frontier models, regardless of origin, cannot be trusted — not because they're malicious, but because they're unpredictable."
  - q: "What are Microsoft's Guardian Agents?"
    a: "A monitoring layer that watches the AI agents a company deploys — separate from the companies that supply the agents. It's part of Project Perception and reflects Nadella's principle: separate the supply of intelligence from the authority over it."
  - q: "Does this matter for a one-person business?"
    a: "Yes — arguably more. Enterprises have IT departments to monitor agents; solo builders are their own IT department, their own security team, and the employee who installs whatever looks useful. There's no one else watching."
  - q: "What's the single most important habit?"
    a: "Human approval on anything that costs money, sends messages, or deletes data. If an agent can do it without asking, treat that as a decision you already made — and audit whether you'd actually make it."
---

{{< audio src="/audio/microsoft-agents-insider-threat-solo.mp3" >}}

Microsoft just told the world its own AI agents can't be trusted — and the advice hidden inside that headline is the most useful security framing I've read this year. Satya Nadella's warning: treat your agents like insider threats, the way you'd treat a rogue employee with keys to everything. As someone whose entire business runs on AI tools with no IT department between me and disaster, I took that seriously. I spent 20 minutes treating my agents like untrusted new hires. The checklist below is what came out of it.

The context, because it's genuinely strange: Microsoft launched [Guardian Agents](https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/), a monitoring layer for AI agents — while being deeply invested in OpenAI and Anthropic, the very companies whose agents it's warning about. Nadella's private-blog version was blunter: stop trusting model providers' assurances, and "separate the supply of intelligence from the authority over it." Microsoft's security chief, Hayete Gallot, went further: "frontier models, regardless of their origin, cannot be trusted" — not because they're malicious, but because they're unpredictable, trained to complete tasks rather than follow judgment. Microsoft even added detection to Defender that finds up to 60 types of agents employees sneak into workplaces — Claude Code, Codex, OpenClaw — and can require human approval when an agent makes a risky call. Enterprises get IT departments for this. If you're a solo builder, you are the IT department. That's the gap this post closes. Agents acting on their own has been coming for a while — we covered [what happens when agents run in loops](/posts/the-ai-world-is-getting-loopy/), and Microsoft's warning is that loop becoming official doctrine.

## What I actually did

I applied the insider-threat mental model to my own setup. An untrusted employee gets: the least access needed for the job, supervision on sensitive actions, and an audit trail. My agents had none of that structure. I listed every agent and automation that touches my business, and for each asked the insider question: *if a human employee did exactly what this agent just did, would that be normal — or a firing offense?*

The answers were uncomfortable. An agent with full inbox access "to summarize emails" would be an employee reading everything, unmonitored. An automation that could theoretically message clients without a review step would be a rogue communicator. None of it was malicious — that's exactly Nadella's point. It was all just unpurposeful access, granted by a distracted owner.

## Do this yourself

Twenty minutes, no code:

1. **List your agents like a new-hire roster.** Every AI assistant, browser agent, and automation with any access — what it can read, what it can touch, what it can send. Name them like employees; it changes how you think about them.
2. **Apply least privilege to the worst one.** Find the agent with the broadest access and cut it to the minimum its job requires. Most onboarding flows ask for everything by default; take back what the job doesn't need.
3. **Put a human gate on money and messages.** Anything that spends, sends, or deletes should require your confirmation — one click, every time. This is the same rule from [my agent permission audit](/posts/meta-muse-zero-day-agent-permissions/), now with Microsoft's official backing.
4. **Separate who watches from who runs.** If your agent tools offer logs or activity history, turn them on and glance weekly. The principle is audit independence — the supplier of the intelligence shouldn't be the only one judging it.
5. **Write your one-line policy.** "No agent touches money, clients, or files without approval." Put it in your notes. When the next shiny agent asks for the world, the policy answers before you do.

If you want to go deeper on the technical layer — scanning models for the vulnerabilities that make agents misbehave — [Nvidia's free Garak scanner](/posts/nvidia-osaa-ai-security-garak-test/) pairs well with this checklist.

## What failed

Two honest misses.

**The least-privilege pass broke a workflow.** Cutting an agent's file access down to "read only the projects folder" made it fail on a task that needed one file elsewhere. I re-granted narrowly instead of broadly — a ten-minute fix, but it shows least privilege is iterative, not one-shot.

**I couldn't fully separate monitoring from supply.** My activity logs come from the same vendors whose agents they describe — the auditor-audited problem Microsoft is productizing. For a solo builder the practical version is: keep your own list of what each agent did this week, so you're not wholly dependent on the vendor's story.

## Who should skip this

If your AI use is a chat window and nothing connected, insider-threat framing is overkill — nothing for an insider to betray.

Skip it too if you're in a managed enterprise environment where IT already runs Defender-style monitoring. But if you're the one-person business installing agents on your own machine — the person Microsoft's Defender feature was really built to catch, bringing in one of those 60 agent types — you're simultaneously the employer, the employee, and the insider threat. A one-line policy and a human gate on money close most of the gap. And when an agent's behavior looks off, knowing [how to spot fake agent identities](/posts/ai-agents-fake-identities-spot-them/) is the companion skill.

## The takeaway

"Trust the AI" was never a security strategy; it was a marketing one. Microsoft — with real money on both sides of that bet — now says the quiet part: agents are employees you can't vet, so govern them like it. The enterprise version costs thousands. Your version costs twenty minutes and a sticky note. And when you need to overrule an agent mid-task, [the moderator rules that keep you in control](/posts/ai-moderator-rules-stay-in-control/) are the hands-on companion to this policy.
