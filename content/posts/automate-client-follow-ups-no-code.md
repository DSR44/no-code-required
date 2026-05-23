---
title: "How I Automated My Client Follow-Ups in an Afternoon (No Code, No Developer)"
date: 2026-05-23
draft: false
description: "Learn how to automate client follow-ups without any code. A practical guide for solo business owners using Make.com — built and tested in an afternoon."
tags: ["AI tools", "automation", "no-code", "Make.com", "Zapier", "email marketing", "small business", "productivity", "client management"]
categories: ["tools"]
slug: "automate-client-follow-ups-no-code"
cover:
  image: "/images/posts/20260523_125724_Zoe_young_woman_dark_brown_shoulder-len.jpg"
---
{{< audio src="/audio/automate-client-follow-ups-no-code.mp3" >}}


# How I Automated My Client Follow-Ups in an Afternoon (No Code, No Developer)

Every three days, I'd open my inbox and copy-paste "just checking in!" to a client who hadn't replied. Every three days. Like clockwork. Except it wasn't clockwork — it was dread dressed up as discipline.

I did this for two months. Twelve follow-up emails. Every single one manually written, manually tracked, manually sent. And I know I'm not the only one, because the number one complaint I hear from solo business owners isn't "I don't have enough clients." It's "I keep losing the ones I almost had."

So I stopped doing it manually. In one afternoon, I built a follow-up sequence using [Make.com](https://make.com) that now handles every single lead automatically. Here's how — and why you should do the same.

## The problem with manual follow-ups

Here's a number that should scare you: [research shows 80% of sales need at least 5 follow-ups](https://www.brevetgroup.com/25-sales-follow-up-statistics), but 44% of salespeople give up after one.

One.

If you're a solo business owner wearing every hat — sales, delivery, admin, marketing — you're probably in that 44%. Not because you don't care, but because follow-up is the kind of task that feels important but never urgent. It sits at the bottom of your to-do list while client work and invoicing eat your day.

The cost isn't abstract. If you land one extra client per month from better follow-up, that could be $500, $2,000, or $10,000+ depending on what you sell. Over a year, that's real money walking out the door because you forgot to send an email.

I covered this same problem from a different angle in [How AI calls other tools (and why you should care)](/posts/how-ai-calls-other-tools/) — the short version is that your tools can now talk to each other without you being the middleman.

## What automating follow-ups actually means

"Automating follow-ups" sounds complicated. It isn't.

It's just a rule: **if X happens, do Y.**

- **Trigger:** Someone fills out your contact form (or books a call, or downloads your lead magnet)
- **Action:** Wait 24 hours → send a follow-up email → wait 3 days → send another → wait 4 days → send a final one

You write the emails once. The system sends them forever. You never touch it again unless you want to change the wording.

That's it. No developer. No code. No $500/month software.

## Three tools that do this (pick one)

### 1. Make.com (start here)

This is what I used. Make is a visual workflow builder — you drag boxes around and connect them with lines. No code. Free tier gives you 1,000 operations per month, which is more than enough for a solo business.

→ [make.com](https://make.com)

Why I picked Make over Zapier: more control, better free tier, and I can build multi-step sequences without hitting limits.

### 2. Zapier (easier, less flexible)

If you've never touched an automation tool before, Zapier is the gentlest start. More templates, more integrations, but the free tier caps at 100 tasks/month.

→ [zapier.com](https://zapier.com)

Good for: "I just want something working in 10 minutes."

### 3. MailerLite or ConvertKit (for email sequences)

These are email marketing tools, not automation platforms. But they have built-in sequence features — you write 3-5 emails, set the delays, and they send automatically when someone subscribes.

→ [mailerlite.com](https://mailerlite.com) | [convertkit.com](https://convertkit.com)

Good for: if your follow-up is purely email-based and you don't need to connect other tools.

Not sure which fits your workflow? Check the [AI Tool Advisor](/ai-tool-advisor.html) — answer a few questions and get a personalized recommendation.

## Step-by-step: Build it in Make.com

Here's exactly what I built. Takes about 90 minutes from zero.

### Step 1: Create a Make account (2 minutes)

Go to [make.com](https://make.com), sign up (free), and click "Create a new scenario."

### Step 2: Set the trigger — "When a form is submitted" (10 minutes)

1. Add a **Webhooks** module → select "Custom webhook"
2. Make gives you a unique URL — paste this into your contact form's webhook settings (works with [Typeform](https://typeform.com), [Tally](https://tally.so), [Google Forms](https://forms.google.com), or custom forms)
3. Submit a test entry so Make can detect the data fields

### Step 3: Add a delay — "Wait 24 hours" (5 minutes)

1. Add a **Flow Control** module → select "Sleep"
2. Set delay: 24 hours
3. Why 24 hours? You want to give them time to reply naturally before the automation kicks in

### Step 4: Send the first follow-up (15 minutes)

1. Add an **Email** module (Gmail, Outlook, or SMTP)
2. Set the recipient to the email from the form submission
3. Write your follow-up message. Keep it short:

> Subject: Following up on your inquiry
>
> Hey [name],
>
> Just wanted to make sure my last message didn't get buried. Happy to answer any questions you have — just hit reply.
>
> [your name]

4. Map the name field from the webhook data

### Step 5: Add another delay + second follow-up (10 minutes)

1. Add another **Sleep** module → 3 days
2. Add another **Email** module with a different message:

> Subject: Quick thought on [their problem]
>
> Hey [name],
>
> I was thinking about [specific thing they mentioned]. Here's a quick tip: [one useful thing].
>
> If you want to chat more, I'm around.
>
> [your name]

### Step 6: Final check-in (10 minutes)

1. **Sleep** → 4 days
2. **Email** — the last one:

> Subject: Last note from me
>
> Hey [name],
>
> I don't want to clog your inbox, so this is my last follow-up. If you'd like to pick things up later, just reply whenever works. No pressure.
>
> [your name]

### Step 7: Test the whole thing (15 minutes)

1. Turn the scenario ON
2. Submit your own email through the form
3. Wait for each email to arrive (or adjust the sleep timers to 1 minute for testing)
4. Check: did all 3 emails arrive? Were the names correct? Did the links work?

### Step 8: Turn it on for real (2 minutes)

1. Reset sleep timers to real delays (24 hours, 3 days, 4 days)
2. Turn the scenario ON
3. Done. Every new lead gets follow-ups. Forever.

## Five mistakes I made (so you don't)

**Mistake 1: Writing the emails inside the automation tool.**
Don't. Write them in a Google Doc first. Read them out loud. If they sound like a robot wrote them, rewrite them. The automation sends the email — you still write it.

**Mistake 2: Using your main email address.**
Set up a separate sending address (like hello@yourbusiness.com). If something goes wrong, your primary inbox isn't compromised.

**Mistake 3: Not testing on yourself first.**
I turned on my sequence and immediately got a follow-up email from myself. It was embarrassing. Test the full flow with your own email before going live.

**Mistake 4: Building a 7-step sequence on day one.**
Start with 3 emails. That's it. If 3 works, add more later. Most solo businesses don't need a 12-email nurture sequence — they need a polite nudge.

**Mistake 5: Setting it and forgetting it forever.**
Check your sequence once a month. Are people replying? Are the emails still accurate? Is the tone still right? Automation runs itself, but the content needs a human eye.

I made similar mistakes when [I built my first automation](/posts/build-your-first-automation-in-15-minutes/) — the "test on yourself" lesson cost me an awkward afternoon.

## What to do next

Once your 3-email sequence is running, you have two options:

**Option A: Add a second follow-up at day 7.**
Maybe a case study, a testimonial, or a link to a relevant blog post. Something that adds value without asking for anything.

**Option B: Log unresponsive leads to Notion.**
Add a final step in Make: if no reply after 7 days, create a Notion card with the lead's name, email, and what they asked about. Once a week, review the board and decide: personal phone call, or let it go.

This is where it connects to [the tools I'm watching in 2026](/posts/whats-next-tools-2026/) — AI-powered follow-up that adjusts the message based on how the lead interacts is already here. But start with the simple version first.

## The bottom line

Automating follow-ups isn't about replacing yourself. It's about making sure the stuff that matters actually gets done — even when you're busy, tired, or elbow-deep in client work.

I built mine in an afternoon. It's landed me 3 clients in the first month that I would have otherwise lost. The entire system costs me $0 on Make's free tier.

You don't need to be technical. You don't need a developer. You need 90 minutes, Make.com, and the willingness to write 3 short emails.

Start here: [answer 3 questions, get a tool recommendation](/start-here/) — I'll tell you exactly which tool fits your setup.

---

**Coming soon:**
- *Voice AI: what GPT-5 can actually do now* (coming June 14) — voice agents explained
- *The ChatGPT education study that got retracted* (coming June 15) — what went wrong
- *AI orchestrators: one model controlling all the others* (coming June 16) — the next layer

---

*Some links in this post may be affiliate links. If you sign up through them, I may earn a small commission at no extra cost to you. I only recommend tools I've actually tested.*
