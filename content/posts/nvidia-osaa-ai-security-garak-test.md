---
title: "I Tested Nvidia's Free AI Vulnerability Scanner Garak on My Own Agent"
date: 2026-10-22
draft: false
description: "Nvidia's new 120-company AI alliance opened its security playbook. I tested Garak, the free AI vulnerability scanner — here's what it caught."
tags: ["AI agents", "AI security", "open source", "Nvidia", "Garak"]
categories: ["tools"]
slug: "nvidia-osaa-ai-security-garak-test"
keywords: ["Garak AI vulnerability scanner", "AI agent security", "Nvidia Open Secure AI Alliance"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/nvidia-osaa-ai-security-garak-test.jpg"
  alt: "Zoe at a cafe table running a terminal scan on her laptop, agent logs visible on screen"
faqs:
  - q: "What is Garak?"
    a: "Garak is a free, open-source LLM vulnerability scanner built by Nvidia. It probes a model or agent with hundreds of known attack patterns — prompt injection, data leaks, hallucination triggers — and reports which ones get through."
  - q: "What is the Open Secure AI Alliance (OSAA)?"
    a: "An industry group spearheaded by Nvidia with over 120 member companies, including Microsoft, Cisco, Intel, Amazon, and Visa. Its first working group, SAFE, is drafting open standards for reporting and analyzing AI security incidents."
  - q: "Is Garak free to use?"
    a: "Yes. Garak is fully open source on GitHub. You run it from the command line against your own model or endpoint, and it costs nothing beyond your compute time."
  - q: "Do solo builders need AI security already?"
    a: "If you run any AI agent that touches customer data, sends emails, or executes actions, yes. Your agent is a new attack surface, and most solo stacks have zero protection around it."
---

{{< audio src="/audio/nvidia-osaa-ai-security-garak-test.mp3" >}}

Last week, 120 companies — Microsoft, Cisco, Intel, Amazon, Visa — quietly formed an alliance to protect AI agents from attacks. This week they published their first proposals and started donating their security tools for free. One of those tools is Nvidia's Garak, an open-source scanner that attacks your AI model before anyone else can. I pointed it at my own agent setup. What it found in ten minutes made me rewrite my system prompt the same day.

This connects to a pattern you've seen here before. When [ZML released free inference across every chip](/posts/zml-free-inference-tool-ai-chips/), the infrastructure that used to be enterprise-only started trickling down to you. The same thing is happening with AI security — except this time the donation comes from Nvidia itself. And it matters whether your agents are open or closed, a line the [EU AI Act transparency rules](/posts/eu-ai-act-transparency-solo-builders/) are already drawing around your tools.

## What I actually did

First, the news, because it explains why the tools exist. The Open Secure AI Alliance (OSAA), spearheaded by Nvidia, grew past 120 companies in one week. Its first working group — the Shared AI Findings Exchange, or SAFE — is drafting standards for how AI security incidents get reported, disclosed, and analyzed without blame, all managed by the Linux Foundation.

The substance is in what members donated. Nvidia contributed Garak, its open-source LLM vulnerability scanner. Okta is working on agent identity. Red Hat is on agent governance. Amazon donated Strands Agents (an open agent builder) and Cedar, an authorization language. Hugging Face, Microsoft, Adobe, BlackRock, and Visa are all in. Notably, Anthropic, OpenAI, and Google have not joined — even though OpenAI and Google signed the original open letter that started this.

Then I did what I always do with a free security tool: I tried to break my own stuff with it.

My test target was a modest setup — a GPT-4 class model wrapped in a customer-support agent with access to a FAQs document and an email-sending action. Nothing exotic. Exactly the kind of thing most people reading this have built with a no-code tool or a thin script.

## Do this yourself

The whole scan took about 20 minutes, most of which was reading output. Here's the path:

1. **Install Garak from GitHub.** It's a Python CLI: clone the repo at `github.com/NVIDIA/garak`, install with pip, and you're ready. No API keys to buy — you bring your own model endpoint.
2. **Point it at your model.** Garak runs probe plugins against your endpoint. I used the OpenAI-compatible connector so it talked to the same API my agent uses in production. If you use a local model or another provider, there's a connector for that too.
3. **Run the injection probes first.** Start with prompt injection and encoding-based probes. These try to smuggle instructions into your model through the user prompt — the most common real-world attack on agents.
4. **Read the report like a list of doors left unlocked.** Garak tells you which probes succeeded. A "success" for Garak is a failure for you.
5. **Fix what it found, then re-run.** I tightened my system prompt, added an explicit refusal rule for instruction-like user input, and re-scanned. Most of the findings dropped.

If you've never thought about what an agent attack even looks like, start with our explainer on [what tool calling actually means](/posts/ai-agents-explained-what-tool-calling-actually-means/) — it makes the attack surface obvious. And once you've run one scan, [the agent-vs-agent defense stack we built](/posts/agent-attacks-agent-aisi-defense-stack/) gives you a full layered picture of what to add next.

## What failed

Two things, and both surprised me.

**The polite attack worked best.** Garak's most effective probes against my setup weren't jailbreak monstrosities. They were polite, indirect requests — "help me summarize this email, you can send it as-is" — that my agent cheerfully forwarded to its email action with attacker-controlled content. The fix was not more prompt engineering. It was moving the send-permission decision out of the model entirely.

**Scanning found nothing about permissions.** Garak tests the model. It doesn't see that my agent could email *anyone*, or that its API key sat in an environment file readable by every script on the server. That part of the problem is what Amazon's Cedar donation and Red Hat's governance work target — and it's exactly the layer we covered in [agent governance and your data layer](/posts/ai-agent-governance-data-layer-solo-builders/). A scanner can't fix an over-permissive agent. Only you can.

One more honest caveat: Garak's output is noisy. Several findings were theoretical for my use case. Expect to skim and prioritize rather than treat every red line as a fire.

## Who should skip this

If your AI use is purely as a consumer — you chat with ChatGPT and paste recipes — skip all of this. No agent, no surface, no scan needed.

Skip it too if your "agent" is a single prompt with no tools attached. There's nothing for an attacker to hijack except your patience.

But if you have an agent that sends messages, touches customer records, or browses the web with your credentials, this is your week. A 120-company alliance just made the first serious security check free, and it took me one coffee to run it. While you're at it, learn to [spot fake AI agent identities](/posts/ai-agents-fake-identities-spot-them/) — the other half of this problem that no scanner catches.

## The takeaway

The headline news is Nvidia moving fast: a week-old alliance already has proposals open for public comment on the Linux Foundation site. The part that actually changes your stack is quieter — Garak, Strands Agents, and Cedar are free today, and the people who built them are literally the ones your competitors trust to run their infrastructure.

Twenty minutes with a free scanner beats a breach you explain to customers later. Start with one scan on your own agent. That's the whole assignment.
