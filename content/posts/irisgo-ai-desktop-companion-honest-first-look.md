---
title: "IrisGo: The AI Desktop Companion That Gets It Right"
date: 2026-05-29
draft: false
description: "Andrew Ng-backed IrisGo learns your desktop workflows and runs them for you — here's an honest first look at what it actually does."
tags: ["AI tools", "desktop automation", "AI assistant"]
categories: ["tools"]
slug: "irisgo-ai-desktop-companion-honest-first-look"
keywords: ["IrisGo AI desktop assistant", "Andrew Ng AI tools 2026", "desktop workflow automation"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/irisgo-ai-desktop-companion-honest-first-look.jpg"
  alt: "Person at laptop with AI workflow automation interface, warm editorial setting"
faqs:
  - q: "How does IrisGo learn my desktop workflows?"
    a: "IrisGo observes your repeated actions—like file organization, email sorting, or data entry—and uses AI to identify patterns. It then suggests automating these tasks, which you can approve or customize before it runs them for you."
  - q: "Is IrisGo safe to use with sensitive work files?"
    a: "IrisGo processes data locally on your desktop by default, minimizing cloud exposure. You also review and approve every automated action before it executes, giving you full control over what it accesses."
  - q: "Can IrisGo work with any software on my computer?"
    a: "It integrates with common productivity apps like browsers, office suites, and file managers. However, it may have limited support for highly specialized or legacy software without standard interfaces."
  - q: "How is IrisGo different from other automation tools like AutoHotkey?"
    a: "Unlike rule-based tools, IrisGo uses AI to learn from your behavior without requiring you to write scripts. It adapts to your habits over time, making it more intuitive for non-technical users."
---
{{< audio src="/audio/irisgo-ai-desktop-companion-honest-first-look.mp3" >}}

Every AI assistant I've tried follows the same script: you type a command, it does a thing, you thank it like a polite human, and then you type the same command again tomorrow. It's manual labor wearing a robot costume. So when I heard about IrisGo — an AI desktop companion that learns your workflows by watching you do them once — I had to see if it actually delivers.

Spoiler: it's more interesting than I expected. And more complicated too.

## What Is IrisGo, Exactly?

IrisGo is a desktop application for macOS and Windows that sits on your computer and watches how you work. Not in a creepy surveillance way (supposedly — more on privacy later). The idea is that you show it a task once, and it remembers the process and can repeat it autonomously in the future.

It was co-founded by Jeffrey Lai, a former Apple engineer who helped build the Chinese-language version of Siri. Fun fact: "Iris" is literally "Siri" backward. That's not subtle, and I kind of love it.

The startup closed a $2.8 million seed round led by [Andrew Ng's AI Fund](https://www.founderland.ai/articles/andrew-ng-backs-irisgos-28m-seed-for-ai-pc-workflow-automati-mnlm32yg), with additional backing from Intel, Google for Startups, and NVIDIA. They've also reportedly raised $23M total and struck a deal with Acer to preinstall the app on new laptops. That's not a scrappy side project — that's a real bet on the "proactive AI" category.

If you've been following the AI tool space, this fits neatly into the trend I covered in [AI orchestrators: one model controlling all the others](/posts/ai-orchestrators-one-model-controlling-all-the-others/) — systems that don't wait for instructions but anticipate what needs doing.

## How Does It Actually Work?

The core mechanic is straightforward: you perform a task on your desktop — say, ordering a coffee online — and IrisGo records the steps. Selecting the item, filling in payment info, clicking purchase. Next time, it can repeat the whole flow without you lifting a finger.

But the real value isn't ordering lattes. IrisGo comes with a built-in skills library that includes:

- **Email drafting** — it learns your tone and patterns
- **Invoice processing** — extracts data, fills forms, routes for approval
- **Report building** — pulls from your apps and assembles summaries
- **Document summarization** — condenses long files into action items
- **Coding assistance** — a built-in assistant similar in concept to [OpenAI Codex](https://openai.com/index/introducing-codex/) or Claude Code

The system also watches your ongoing desktop behavior and automatically suggests new tasks it could automate. It's like having an intern who actually pays attention — except this intern doesn't need coffee.

For comparison, this is a very different approach from [Make vs Zapier](/posts/make-vs-zapier-which-one-is-actually-easier/) or even [build your first automation in 15 minutes](/posts/build-your-first-automation-in-15-minutes/). Those tools require you to manually set up triggers and actions. IrisGo tries to skip that entirely by learning from observation.

## The Privacy Question (Yes, There Is One)

Here's where I have to be honest: the concept of an app that "watches your desktop" should make anyone pause.

IrisGo processes most data on-device, which is a meaningful privacy improvement over tools that send everything to the cloud. Their [privacy policy](https://irisgo.ai/privacy) states that cloud processing only happens when explicitly authorized by the user, and it uses end-to-end encryption when it does.

That said — and this is important — it's still a hybrid architecture. Complex tasks get routed to the cloud. If you're handling sensitive client data, financial records, or anything regulated, you'll want to read the fine print carefully before letting it learn your workflows.

I covered the broader privacy implications in [the privacy problem nobody talks about](/posts/the-privacy-problem-nobody-talks-about/), and IrisGo doesn't fully escape those concerns. It's better than most alternatives, but "better than most" and "fully safe" aren't the same thing.

## Who Is This Actually For?

Lai describes the target audience as "knowledge workers — white-collar companies" with repetitive daily tasks. That tracks. If you're someone who:

- Processes the same type of documents regularly
- Follows the same email workflows daily
- Manually pulls data from one app into another
- Builds the same reports on a schedule

...then IrisGo could genuinely save you hours per week.

But if you're a complete beginner who just wants to [use AI writing tools](/posts/i-tested-10-ai-writing-tools/) or [build a blog in one hour with AI](/posts/how-i-built-a-blog-in-1-hour-with-ai/), this probably isn't your entry point. It's more of a power-user tool at this stage.

That said, the Acer preinstall deal is interesting. If IrisGo ships preloaded on new laptops, it lowers the adoption barrier significantly. Nobody has to "decide to try it" — it's just there, learning quietly in the background.

## What Concerns Me

Three things stood out as I dug in:

**1. Demos are controlled environments.** Every IrisGo demo I've seen involves clean, predictable workflows. Real desktops are messy — pop-ups, updates, weird browser states, half-loaded pages. How well does it handle chaos?

**2. The skills library is only as good as its community.** IrisGo's "skills catalog" relies on community-built workflows, similar to how [Zapier](/posts/zapier-vs-make-vs-n8n-which-automation-tool/) has its template library. If the community is small, the catalog is thin, and you're back to building everything yourself.

**3. On-device processing has limits.** The hybrid cloud model means your data does leave your machine sometimes. For a tool that promises privacy-first, that's a caveat that deserves more transparency about exactly what triggers cloud processing.

## What I Like

Despite those concerns, the concept genuinely excites me for a few reasons:

**It's proactive, not reactive.** Most AI tools wait for you to ask. IrisGo tries to figure out what you need before you ask. That's the direction everything is heading — [the AI tools with the highest satisfaction rates](/posts/the-ai-tools-with-the-highest-satisfaction-rates-youve-never-heard-of/) are the ones that reduce friction, not just add features.

**The investor lineup is serious.** Andrew Ng, Intel, Google, NVIDIA — these aren't people who throw money at hype. That backing suggests the underlying tech is solid, even if the product is still early.

**The Acer deal changes the game.** Getting preinstalled on hardware is how every successful platform wins. Chrome did it. Zoom did it. If IrisGo can nail the OEM partnerships, it could become the default desktop AI layer.

## How It Compares to What You're Already Using

If you're already using tools like [ChatGPT](/posts/chatgpt-alternatives-2026-actually-worth-switching/), [Cursor](/posts/cursor-composer-2-5-free-claude-killer/), or [build your own AI chatbot in 30 minutes](/posts/build-your-own-ai-chatbot-in-30-minutes/), IrisGo isn't really competing with those. It's a different layer entirely.

Think of it this way: ChatGPT is a conversation. Zapier is a connection. IrisGo is an observer. It watches, learns, and acts. Whether it can actually do that reliably across millions of different desktop setups is the open question.

You can check it out at [irisgo.ai](https://irisgo.ai) — the beta is available for both macOS and Windows right now.

## The Bottom Line

IrisGo is the most interesting desktop AI concept I've seen this year. It's backed by serious people, built by someone who literally helped create Siri, and targeting a real problem (repetitive knowledge work). Whether it can deliver on the promise outside of polished demos — and whether the privacy model holds up under scrutiny — are questions only time will answer. But for non-coders who want their computer to just *handle things*, this is worth watching closely. If you're just getting started with AI tools, head over to [/start-here/](/start-here/) and we'll get you going with the basics first.
