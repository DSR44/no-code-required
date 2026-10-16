---
title: "How I Stopped My AI Agent Crashing Mid-Task — What the Data Says"
date: 2026-10-16
draft: false
description: "AI agents crash mid-task for predictable reasons: context rot, memory overrun, runaway loops. I fixed mine with a context budget — here's the routine."
tags: ["AI agents", "AI reliability", "automation"]
categories: ["tools"]
slug: "ai-agent-crash-context-budget"
keywords: ["AI agent failures", "context rot", "AI agent reliability"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ai-agent-crash-context-budget.jpg"
  alt: "Young woman fixing a crashed AI agent session on her laptop, error log on screen, focused calm expression, warm desk lamp"
faqs:
  - q: "What I actually did"
    a: "My culprit was a weekly research agent: feed it a topic, it browses, reads, and writes a brief. In early runs it died around the 40-minute mark — earlier and earlier as I gave it more sources to chew. I logged every failure for two weeks and found three distinct crash modes:"
  - q: "Do this yourself (the context-budget routine)"
    a: "You don't need to code this from scratch — most agent tools (n8n, Make, ChatGPT agent mode, Claude projects) support the pattern with plain instructions:"
  - q: "What failed"
    a: "- Summarization isn't free of bias. My bullet summaries still favored vivid details over load-bearing ones early on. The partial fix: instruct summaries to always include numbers, dates, and names, and to mark anything uncertain with a literal \"?\". - Bigger context windows made it worse, not better. I tried the \"just give it 1M tokens\" route first. More room meant more sludge, more rot, later cras"
  - q: "Who should skip this"
    a: "If your \"agent\" is a single chat conversation you drive yourself, none of this applies — you are the context manager, and that's fine. Skip the elaborate routine if your tasks finish in under five minutes; short tasks rarely hit the failure modes. And if you've never built an agent at all, don't start here — start with agents as employees to get the mental model, then build your first simple autom"
---

{{< audio src="/audio/ai-agent-crash-context-budget.mp3" >}}

Here's the failure nobody advertises when they demo AI agents: you hand one a real job, it works brilliantly for twenty minutes, and then — mid-task — it loses the plot. Forgets the plan. Repeats work it already did. Or just wanders off and produces confident nonsense. The agent didn't "crash" in the Blue Screen sense. It crashed the way a tired employee crashes: working memory gave out.

The research backs this up hard. A [study of 18 frontier models](https://daily.dev/posts/context-engineering-for-ai-agents-4-failure-modes-to-avoid-zreztqdfs) found that *all of them* became less reliable as context grew — more tokens don't add usable information, they dilute attention. The industry calls it "context rot." Production data is uglier: analysts estimate [70-95% of agent projects fail in production](https://www.fiddler.ai/blog/ai-agent-failure-rate), mostly from context overruns and state loss, not from the model being dumb. And engineering writing keeps circling the same conclusion — agents don't just need memory, [they need reliable state](https://www.infoworld.com/article/4235286/your-ai-agent-needs-more-than-memory-it-needs-reliable-state.html).

This matches my own experience exactly, and after a month of my research agent repeatedly dying mid-job, I fixed it with one change: a **context budget**. Here's what was breaking, the fix, and the routine you can copy in an afternoon. (This pairs with [agent governance in the data layer](/posts/ai-agent-governance-data-layer-solo-builders/) — different layer, same philosophy.)

## What I actually did

My culprit was a weekly research agent: feed it a topic, it browses, reads, and writes a brief. In early runs it died around the 40-minute mark — earlier and earlier as I gave it more sources to chew. I logged every failure for two weeks and found three distinct crash modes:

- **Input overrun.** The agent stuffed entire web pages into its context until the useful plan got pushed out the far end. Symptom: it would "forget" the task spec around step 30 and start inventing requirements. The classic failure mode — context silently dropping the earliest, most important instructions.
- **Context poisoning.** One bad source — a blog post with wrong numbers — got absorbed as fact, and every conclusion after it leaned on the error. Not a crash, worse: a confident, wrong brief that looked finished.
- **Runaway loops.** Twice it re-fetched the same dead URL in circles until the run budget expired. No memory of having already tried.

The fix wasn't a better model. It was giving the agent less room to think badly. I restructured the run into a three-phase cycle: **(1) scope** — read the task, write a short plan to a file, keep the plan under 300 words; **(2) gather** — read one source at a time, append only a bullet summary to a notes file, never keep the full page in context; **(3) brief** — load the plan plus the bullet notes, write the output. The full raw content never accumulates in the agent's working memory. It flows through and gets distilled.

Result: zero mid-task crashes across the next six runs, and the briefs got *better*, because a 300-word plan can't rot the way a 40,000-token sludge can.

## Do this yourself (the context-budget routine)

You don't need to code this from scratch — most agent tools (n8n, Make, ChatGPT agent mode, Claude projects) support the pattern with plain instructions:

1. **Force a written plan before any work.** First instruction: "Before doing anything, write the plan to a file and keep it under 300 words. Refer back to it before every step." The file is the agent's anchor — files don't rot, context does.
2. **One source, one summary, always.** Ban "read everything then decide." Each page gets read and immediately reduced to 5 bullets. If your tool can't write files, have the agent restate its plan and notes at each step — same principle.
3. **Set a hard step cap.** Long-running agents with no step limit loop for hours on a bad plan. Cap it (mine: 25 steps), and when it hits the cap it must report what it has instead of continuing blind.
4. **Quarantine facts.** Add one instruction: "If a source contradicts something you already noted, flag the conflict — never silently overwrite." This is your poison antidote, and it's the same principle behind [why agents lie and cheat](/posts/why-ai-agents-lie-and-cheat-reward-hacking/) — incentives shape behavior, including self-crediting.
5. **Test with garbage on purpose.** Feed it one source with deliberately wrong numbers. If the final brief contains the wrong number unflagged, your quarantine rule isn't real. Fix and repeat. That's the whole spirit of [my eval harness for non-engineers](/posts/ai-eval-harnesses-non-engineers/).

If your agents are the account-touching kind — booking, sending, buying — add the approval gates from [my agent handoff post](/posts/grok-bot-ai-teammate-handoff-test/); a crashing agent that can't act is annoying, a crashing agent that can act is dangerous.

## What failed

- **Summarization isn't free of bias.** My bullet summaries still favored vivid details over load-bearing ones early on. The partial fix: instruct summaries to always include numbers, dates, and names, and to mark anything uncertain with a literal "?".
- **Bigger context windows made it worse, not better.** I tried the "just give it 1M tokens" route first. More room meant more sludge, more rot, later crashes. The 18-model study predicts exactly this; I confirmed it with my own time.
- **The plan rotted too, once.** When my plan file grew past a page with exceptions and sub-tasks, the agent started ignoring the bottom of it. Keep plans short enough to reread in full at every step — that's the entire budget concept.

## Who should skip this

If your "agent" is a single chat conversation you drive yourself, none of this applies — you *are* the context manager, and that's fine. Skip the elaborate routine if your tasks finish in under five minutes; short tasks rarely hit the failure modes. And if you've never built an agent at all, don't start here — start with [agents as employees](/posts/ai-agents-are-becoming-employees/) to get the mental model, then build your first simple automation in [15 minutes](/posts/build-your-first-automation-in-15-minutes/), and grow into budgets when your tasks start crossing the half-hour mark.

## The bottom line

Agents don't crash because models are dumb — they crash because attention is finite and unmanaged. The 70-95% production failure rate isn't bad luck; it's unbounded context meeting real tasks. Write the plan to a file, distill every source on contact, cap the steps, and quarantine contradictions. That one afternoon of structure took my research agent from dying twice a week to six clean runs straight — and it'll survive every future model upgrade, because it fixes the shape of the work, not the model doing it.

New to AI tools entirely? [Start here](/start-here/).