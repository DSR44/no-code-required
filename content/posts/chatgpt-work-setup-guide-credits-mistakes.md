---
title: "ChatGPT Work: 3 Costly Mistakes Before Your First Workflow"
date: 2026-07-23
draft: false
description: "ChatGPT Work launched July 9. Before you burn credits on your first workflow, here's what it actually costs and 3 setup mistakes to avoid."
tags: ["AI tools", "automation", "OpenAI", "ChatGPT"]
categories: ["tools"]
slug: "chatgpt-work-setup-guide-credits-mistakes"
keywords: ["ChatGPT Work", "ChatGPT Work credits cost", "ChatGPT Work setup guide"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/chatgpt-work-setup-guide-credits-mistakes.jpg"
  alt: "Zoe at laptop reviewing AI workflow dashboard with cost breakdown on screen"
---
{{< audio src="/audio/chatgpt-work-setup-guide-credits-mistakes.mp3" >}}

If you've been following the [ChatGPT Work launch](/posts/openai-chatgpt-work-autonomous-agent/) from two weeks ago, you already know the pitch: give it a goal, walk away, come back to finished work. What nobody's talking about is what happens between "walk away" and "finished work" — specifically, how much of your plan's credits disappear in the process. I've been stress-testing ChatGPT Work since launch day, and there are three things I wish someone had told me before I handed it my first real task.

## The Codex merger nobody explained clearly

If you used [OpenAI's Codex](/posts/openai-codex-hardware-what-it-means/) before July, you probably have questions. Did Codex get replaced? Is it a separate product now? Why does the desktop app have three different "views"?

Here's what actually happened. Codex didn't die — it got absorbed. The coding-focused agent technology now powers ChatGPT Work under the hood. On the desktop app, you'll see three views: **Chat** (normal conversational ChatGPT), **Work** (the agentic workflow engine), and **Codex** (still exists as a separate view for code-focused tasks). Mobile only shows Chat and Work — Codex isn't available there yet.

The confusing part: "ChatGPT Classic" is what they're calling the old conversational-only experience. It's now hidden behind a "quick chat" button on desktop and a dropdown on mobile. OpenAI is clearly pushing everyone toward the Work view, but if you just need quick answers, the classic mode uses fewer credits and responds faster.

The takeaway: if you were a Codex user, your workflows still work — they just live inside ChatGPT Work now. If you're brand new, skip the Codex view entirely and go straight to Work. That's where the real automation lives.

## What ChatGPT Work actually costs (real numbers)

OpenAI's pricing page says plans go "up to $100 a month" with "built-in usage limits" through a credit system. Here's what that means in practice.

ChatGPT Work uses [GPT-5.6](https://openai.com/index/gpt-5-6/), which runs in three performance tiers. The highest tier — the one you'll want for complex workflows — costs **$5 per million input tokens** and **$30 per million output tokens**. For context, a single research task that reads a 50-page document, analyzes it, and produces a summary can easily consume 100K+ tokens.

I tested three real-world workflows to see what they actually burned:

**Workflow 1: Competitor analysis.** "Find five competitors to [specific SaaS product], compare their pricing pages, and summarize in a table." This touched 12 web pages and produced a 2-page report. **Cost: roughly 8% of a Plus plan's monthly credits.**

**Workflow 2: Meeting prep.** "Read these 3 documents in my Google Drive, pull out key metrics, and draft talking points for my Tuesday sales call." Three files totaling about 20 pages. **Cost: roughly 5% of monthly credits.**

**Workflow 3: Content calendar.** "Research trending topics in [niche], draft 4 blog post outlines with SEO keywords, and save them to my Drive." This one ran for about 40 minutes and used the built-in browser extensively. **Cost: roughly 15% of monthly credits.**

That's three tasks and you've already used about 28% of your monthly allotment on a Plus plan. [The sticker shock is real](https://arstechnica.com/ai/2026/06/ai-costs-how-much-github-copilot-users-react-to-new-usage-based-pricing-system/) — and it's the same reaction [Anthropic users had](https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/) when Claude's agent SDK started billing by token. If you're weighing [ChatGPT alternatives](/posts/chatgpt-alternatives-2026-actually-worth-switching/), the credit math matters more than feature lists.

The fix: start every workflow in **Chat mode** first. Draft your prompt, refine it, make sure it's specific enough. Then paste the final version into Work. A vague prompt in Work mode means the agent iterates, retries, and burns credits figuring out what you actually wanted. A clear prompt on the first try saves you 30-50% of the cost.

## Three setup steps before your first workflow

Most people open ChatGPT Work and immediately throw a big task at it. That's the expensive way to learn. Here's what to do first.

### 1. Connect only the tools you'd actually trust a junior employee with

ChatGPT Work plugs into [Slack, Teams, Google Drive, and SharePoint](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) through plugins you authorize once. On desktop, it can also read and modify local files and use a built-in browser. That's a lot of access.

The [Compliance API](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers) lets enterprise admins limit what the agent can touch. But if you're on a Plus or Pro plan, you're the admin — and the default is wide open.

Connect Google Drive? Sure, if you're okay with the agent reading any file it thinks is relevant to your task. Connect Slack? Only if you want it potentially pulling message history for context. My recommendation: start with Drive only, in a specific folder you create for agent tasks. Add Slack and Teams later, once you've seen how the agent handles simpler workflows.

### 2. Set up your first Scheduled Task (it's the best feature nobody uses)

[Scheduled Tasks](/posts/apple-shortcuts-ai-workflows-ios-27/) are ChatGPT Work's version of [automations you'd build in Make or Zapier](/posts/build-your-first-automation-in-15-minutes/) — except you describe them in plain English. "Every morning at 8am, check my Downloads folder for new PDFs, summarize any that are longer than 5 pages, and send me the summaries in a Slack DM."

The reason to set this up first: Scheduled Tasks run on a predictable credit budget. You know exactly how much they cost per day because they're doing the same thing every time. It's the safest way to learn your actual credit consumption before you start handing off complex, variable-length workflows.

### 3. Learn the "@" trick

In ChatGPT Work, you can type **@** followed by a tool name to force the agent to use that specific integration. Without it, the agent decides which tools to use based on your prompt — and sometimes it guesses wrong. If you want it to pull from Google Drive specifically, say `@Google Drive` in your prompt. It saves the agent a discovery step, which saves you tokens.

This is also how you handle edge cases. If the agent's default choice of tool isn't giving you what you want, the @ mention overrides it. Think of it like [AI tool calling](/posts/ai-agents-explained-what-tool-calling-actually-means/) — but you're the one making the call.

## Who should (and shouldn't) use this yet

ChatGPT Work is [genuinely useful for solopreneurs](/posts/ai-agents-becoming-employees-solo-business/) who do repetitive knowledge work — research, document analysis, competitive intel, content planning. If you spend more than 3 hours a week on tasks that follow the same general pattern each time, this tool can probably cut that in half.

But it's not ready for everyone. If you're on a free plan, you'll burn through your credits in a day. If you're not comfortable writing specific, detailed prompts, you'll waste money on agent retries. And if you need the agent to handle sensitive data — financial records, client PII, medical information — the [enterprise controls](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers) exist but require setup most small teams won't do.

The sweet spot right now: Plus or Pro plan, non-sensitive workflows, specific prompts, and the patience to watch your credit dashboard for the first week. That's how you build the intuition for what this tool can actually do — without the surprise bill at the end of the month.

If you're exploring more ways to [automate your business without code](https://www.nocoderequired.net/ai-tool-advisor.html), ChatGPT Work is one piece of the puzzle. The skill isn't coding — it's being specific about what you want. And that's a skill [anyone can build](/start-here/).