---
title: "How I Automated My Client Follow-Ups in an Afternoon (No Code, No Developer)"
date: 2026-05-23
draft: false
description: "Learn how to automate client follow-ups without any code. A practical guide for solo business owners using Make.com — built and tested in an afternoon."
tags: ["AI tools", "automation", "no-code", "Make.com", "Zapier", "email marketing", "small business", "productivity", "client management"]
categories: ["tools"]
slug: "automate-client-follow-ups-no-code"
keywords: ["how to automate client follow-ups without coding", "no-code client follow-up automation", "Make.com follow-up sequence"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/my-automation-pipeline.jpg"
  alt: "Automation workflow on a laptop screen in a cozy workspace"
---
{{< audio src="/audio/automate-client-follow-ups-no-code.mp3" >}}

I was copy-pasting the same "just checking in" email every three days — until I built a follow-up sequence in an afternoon that runs itself.

Every three days, I'd open my inbox and paste the same message to a client who hadn't replied. Twelve follow-up emails over two months. Every one manually written, manually tracked, manually sent. And I know I'm not the only one — the number one complaint I hear from solo business owners isn't "I don't have enough clients." It's "I keep losing the ones I almost had."

So I stopped doing it manually. In one afternoon, I built a follow-up sequence using [Make.com](https://make.com) that now handles every single lead automatically. Here's how — and why you should do the same.

## The problem with doing follow-ups manually

Here's a number that should scare you: [research shows 80% of sales need at least 5 follow-ups](https://www.brevetgroup.com/25-sales-follow-up-statistics), but 44% of salespeople give up after one.

One.

If you're a solo business owner wearing every hat — sales, delivery, admin, marketing — you're probably in that 44%. Not because you don't care, but because follow-up is the kind of task that feels important but never urgent. It sits at the bottom of your to-do list while client work and invoicing eat your day.

The cost isn't abstract. If you land one extra client per month from better follow-up, that could be $500, $2,000, or $10,000+ depending on what you sell. Over a year, that's real money walking out the door because you forgot to send an email.

I covered this same problem from a different angle in [How AI calls other tools (and why you should care)](/posts/how-ai-calls-other-tools/) — the short version is that your tools can now talk to each other without you being the middleman.

## What automating follow-ups actually means for a solo business owner

"Automating follow-ups" sounds complicated. It isn't.

It's just a rule: **if X happens, do Y.**

- **Trigger:** Someone fills out your contact form (or books a call, or downloads your lead magnet)
- **Action:** Wait 24 hours → send a follow-up email → wait 3 days → send another → wait 4 days → send a final one

That's the same [trigger + action](/posts/webhooks-how-tools-talk-to-each-other/) pattern every no-code automation uses — just applied to your inbox instead of a developer tutorial.

You write the emails once. The system sends them forever. You never touch it again unless you want to change the wording.

That's it. No developer. No code. No $500/month software.

## The 3 tools that can do this (and which one to start with)

### 1. Make.com — start here

This is what I used. Make is a visual automation builder — you drag boxes around and connect them with lines. No code. Free tier gives you 1,000 operations per month, which is more than enough for a solo business.

→ [make.com](https://make.com)

Why I picked Make over Zapier: more control, better free tier, and I can build multi-step sequences without hitting limits. If you've never built an automation, start with [Build your first automation in 15 minutes](/posts/build-your-first-automation-in-15-minutes/) — same mindset, smaller scope.

### 2. Zapier — easier, less flexible

If you've never touched an automation tool before, Zapier is the gentlest start. More templates, more integrations, but the free tier caps at 100 tasks/month in 2026.

→ [zapier.com](https://zapier.com)

Good for: "I just want something working in 10 minutes."

### 3. MailerLite or ConvertKit — for email sequences

These are email marketing tools, not automation platforms. But they have built-in sequence features — you write 3–5 emails, set the delays, and they send automatically when someone subscribes.

→ [mailerlite.com](https://mailerlite.com) | [convertkit.com](https://convertkit.com)

Good for: if the follow-up is a nurture sequence vs a one-off trigger from a form.

Not sure which fits your workflow? Use the [AI Tool Advisor](/ai-tool-advisor.html) to [find the right tool for your workflow](/start-here/) — answer a few questions and get a specific recommendation.

## Step-by-step: how to build your first follow-up sequence

Here's exactly what I built in Make.com. Takes about 90 minutes from zero.

### Step 1: Create a Make account (2 minutes)

Go to [make.com](https://make.com), sign up (free), and click "Create a new scenario."

### Step 2: Connect your intake form — set the trigger (10 minutes)

1. Add a **Webhooks** module → select "Custom webhook"
2. Make gives you a unique URL — paste this into your contact form's webhook settings (works with [Typeform](https://typeform.com), [Tally](https://tally.so), [Google Forms](https://forms.google.com), or custom forms)
3. Submit a test entry so Make can detect the data fields

### Step 3: Add a delay — wait 24 hours (5 minutes)

1. Add a **Flow Control** module → select "Sleep"
2. Set delay: 24 hours
3. Why 24 hours? Give them time to reply naturally before the automation kicks in

### Step 4: Write and send the first follow-up (15 minutes)

1. Add an **Email** module (Gmail, Outlook, or SMTP)
2. Set the recipient to the email from the form submission
3. Write your follow-up message **before** you wire it up. Keep it short:

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

### Step 7: Test it on yourself (15 minutes)

1. Turn the scenario ON
2. Submit your own email through the form
3. Wait for each email to arrive (or set sleep timers to 1 minute for testing)
4. Check: did all 3 emails arrive? Were the names correct? Did the links work?

### Step 8: Turn it on for real (2 minutes)

1. Reset sleep timers to real delays (24 hours, 3 days, 4 days)
2. Turn the scenario ON
3. Done. Every new lead gets follow-ups. Forever.

## Mistakes that break automations (and how to avoid them)

**Don't automate before you've written the message.**
Most people set up the tool first and write a lazy placeholder that never gets fixed. Write the email in a Google Doc first. Read it out loud. If it sounds like a robot wrote it, rewrite it.

**Don't use your main email address as the sender.**
Set up a separate address (like hello@yourbusiness.com). If something misfires and sends 40 follow-ups to one client, you want it to be from a sub-address you can explain.

**Don't skip the test run.**
I turned on my sequence and immediately got a follow-up email from myself. Embarrassing. Run the full flow on your own email before it touches a real client.

**Don't build a 7-step sequence on day one.**
Start with one follow-up at day 3. Complexity kills completion. Ship the simple version first — you can always add steps later.

**Don't assume the automation is running.**
Check it weekly for the first month. Free-tier tools can pause automations if you hit a limit. I learned this the hard way when [building my first automation](/posts/build-your-first-automation-in-15-minutes/) — the "test on yourself" lesson cost me an awkward afternoon.

## What to do once it's working

Once your 3-email sequence is running, you have two options:

**Option A: Add a second follow-up at day 7.**
Maybe a case study, a testimonial, or a link to a relevant blog post. Something that adds value without asking for anything.

**Option B: Log unresponsive leads to a tracker.**
Add a final step in Make: if no reply after 7 days, create a Notion card with the lead's name, email, and what they asked about. Once a week, review the board and decide: personal phone call, or let it go. This is the same idea behind [my automation pipeline](/posts/my-automation-pipeline/) — small automated steps that remove manual tracking.

This is where it connects to [the tools I'm watching in 2026](/posts/whats-next-tools-2026/) — AI-powered follow-up that adjusts the message based on how the lead interacts is already here. But start with the simple version first.

## The bottom line

Automating follow-ups isn't about replacing yourself. It's about making sure the stuff that matters actually gets done — even when you're busy, tired, or elbow-deep in client work.

I built mine in an afternoon. It's landed me 3 clients in the first month that I would have otherwise lost. The entire system costs me $0 on Make's free tier.

You don't need to be technical. You don't need a developer. You need 90 minutes, Make.com, and the willingness to write 3 short emails.

Not sure which automation tool fits your business? [Answer 3 questions and get a specific recommendation → Start Here](/start-here/)
