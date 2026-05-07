---
title: "The one prompt that changed everything"
date: 2026-05-07
draft: false
description: "Meta-prompting: the technique where you ask AI to improve your prompts before it answers. I tested it for 3 months. Here's what actually happened."
tags: ["AI tools", "prompting", "ChatGPT", "meta-prompting", "productivity", "no-code"]
categories: ["tools"]
slug: "the-one-prompt-that-changed-everything"
cover:
  image: "/images/posts/the-one-prompt-that-changed-everything.jpg"
---

# The one prompt that changed everything

I spent months typing into ChatGPT like I was texting a friend. Short. Vague. Hoping for the best.

And I'd get short, vague, garbage back.

Then I tried something called meta-prompting. It's not my invention — it was popularized by Dharmesh Shah, the founder of HubSpot. The idea is dead simple: instead of trying to write the perfect prompt yourself, you ask the AI to ask you questions first.

The results went from "meh" to "how did it know that?"

## What is meta-prompting?

Meta-prompting is the technique of using AI to improve your prompts before it answers them. Instead of throwing a vague question at ChatGPT and hoping for the best, you give the AI permission to ask clarifying questions first.

The process:

1. You write your prompt — even if it's rough
2. The AI asks you questions to fill in the gaps
3. You answer, and the AI generates a better response because it now has context

Dharmesh Shah built a free tool called [Metaprompt.com](https://metaprompt.com/) that automates this. You paste your rough prompt, it asks optimization questions (What's the goal? Who's the audience? What tone?), and then generates a refined version.

There's also a Chrome extension called [MetaPrompt](https://chromewebstore.google.com/detail/metaprompt-ai-prompt-engi/glkfhecdpcmaclfkhkibmoijipnnjkbf) that enhances your prompts in ChatGPT and Claude with one click.

But I don't use either. I use one sentence.

## The sentence

Here it is. Copy it. Use it on any AI — ChatGPT, Claude, Gemini, whatever:

> **"Before you answer, ask me 3 questions that would help you give a better response."**

That's it. That's the whole thing.

## Why this works

AI models are trained to answer whatever you throw at them. Even if your question is vague, incomplete, or missing critical context — they'll still try. And the answer will be generic because they're guessing what you mean.

When you tell the AI to ask you questions first, three things happen:

1. **It identifies the gaps.** The AI figures out what it doesn't know about your situation. Instead of guessing, it asks.

2. **It forces specificity.** You can't be vague when answering "Who is this for?" or "What's your budget?" You're forced to be concrete.

3. **It builds context.** Each answer you give adds a layer of context. By the time the AI actually answers your original question, it has a complete picture.

This is the difference between:
- ❌ "Write me a blog post about fitness" → generic Wikipedia summary
- ✅ AI asks "Who's the audience? What's the tone? What should the reader do after reading?" → specific, useful, actually publishable

## Real examples where this changed my output

### Writing blog posts

**Before:** "Write a blog post about AI tools" → a summary nobody would read.

**After the questions prompt:** The AI asked me who the audience was, what tools I'd personally tested, and what I wanted readers to do. The post it wrote was specific, personal, and actually sounded like me.

### Building automations

**Before:** "Help me automate my email" → generic Zapier tutorial I could've Googled.

**After:** The AI asked what email provider I use, how many emails per day, and what I wanted to automate. It built me a workflow that actually works with my specific setup.

### Making decisions

**Before:** "Should I use Notion or Obsidian?" → a comparison table.

**After:** The AI asked how many notes I have, whether I collaborate with others, and what I'd tried before. It recommended Obsidian with a specific plugin setup for my exact use case.

## How it compares to the "real" meta-prompting tools

Dharmesh's [Metaprompt.com](https://metaprompt.com/) is more structured — it presents optimization questions as a checklist and generates a refined prompt you can reuse. If you're building prompts you'll use over and over (for agents, workflows, automation), use that.

The [MetaPrompt Chrome extension](https://chromewebstore.google.com/detail/metaprompt-ai-prompt-engi/glkfhecdpcmaclfkhkibmoijipnnjkbf) is more seamless — it automatically enhances your prompts in ChatGPT and Claude. One click, better prompts. Good if you don't want to think about it.

My one-sentence version is the bare minimum. It won't generate a reusable prompt template. But it works instantly, requires zero setup, and you can use it in any AI tool right now.

| Approach | Best for | Setup time |
|----------|----------|-----------|
| "Ask me 3 questions" | One-off conversations, quick answers | 0 seconds |
| Metaprompt.com | Building reusable prompt templates | 2 minutes |
| MetaPrompt Chrome extension | Seamless daily use in ChatGPT/Claude | 1 minute |

## The upgrade: add this too

Once you've got the questions prompt working, add this to the end:

> **"After I answer, suggest one thing I haven't considered."**

This catches the thing you forgot to ask about. The AI sees your full context after the Q&A — it'll often flag something you missed entirely.

Combine both:

> **"Before you answer, ask me 3 questions that would help you give a better response. After I answer, suggest one thing I haven't considered."**

## When NOT to use this

The questions prompt is overkill for simple stuff:
- "What's the capital of France?" — don't need questions for that
- "Translate this to Spanish" — just translate it
- "Fix this typo" — fix the typo

Use it when the task is complex, subjective, or depends on your specific situation. That's where it shines.

## What else improved after I started doing this

One change cascaded into everything:
- My blog posts got sharper (AI asks about audience and angle)
- My email responses got faster (AI asks about tone and urgency)
- My code debugging got quicker (AI asks about the error and environment)
- My product research got deeper (AI asks about budget and requirements)

The AI didn't get smarter. I just stopped making it guess.

## Try it right now

Open ChatGPT (or Claude, or whatever you use). Type your last prompt again — the one that gave you a mediocre result. But this time, start with:

> **"Before you answer, ask me 3 questions that would help you give a better response."**

See what it asks. Answer honestly. Watch the quality jump.

---

## Tools mentioned

- [ChatGPT](https://chat.openai.com) — the one everyone knows
- [Claude](https://claude.ai) — my daily driver for longer context
- [Metaprompt.com](https://metaprompt.com) — free tool by Dharmesh Shah (HubSpot founder) for structured meta-prompting
- [MetaPrompt Chrome Extension](https://chromewebstore.google.com/detail/metaprompt-ai-prompt-engi/glkfhecdpcmaclfkhkibmoijipnnjkbf) — one-click prompt enhancement in ChatGPT/Claude

---

**Coming soon:**
- *Build your own AI chatbot in 30 minutes* (coming May 9) — no code required, step by step
- *GitHub is not scary — 5-minute intro* (coming May 8) — what it actually is and why you don't need to be a developer

---

*Some links in this post are affiliate links. If you sign up through them, I may earn a small commission at no extra cost to you. I only recommend tools I actually use.*
