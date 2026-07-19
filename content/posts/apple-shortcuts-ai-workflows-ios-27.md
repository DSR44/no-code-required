---
title: "Apple Shortcuts App Now Uses AI to Build Workflows — Here Is How"
date: 2026-06-28
draft: false
description: "iOS 27 lets you describe automations in plain language and Apple Intelligence builds them for you. Here's how to use Apple Shortcuts with AI."
tags: ["AI tools", "Apple", "automation", "iOS", "shortcuts", "no-code"]
categories: ["tools"]
slug: "apple-shortcuts-ai-workflows-ios-27"
keywords: ["Apple Shortcuts AI", "iOS 27 shortcuts automation", "Apple Intelligence shortcuts", "iPhone automation no code", "shortcuts natural language"]
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/apple-shortcuts-ai-workflows-ios-27.jpg"
  alt: "Zoe excited about building automations on her iPhone"
faqs:
  - q: "How do I use Apple Intelligence to create a shortcut?"
    a: "Open the Shortcuts app on your iPhone running iOS 27, tap the 'Create' button, and describe the automation you want in plain language, like 'Text my ETA when I leave work.' Apple Intelligence will generate the workflow for you."
  - q: "Can I build automations without knowing any code?"
    a: "Yes, the new AI feature in Apple Shortcuts lets you describe your desired automation in plain English, and the system builds the entire workflow automatically, requiring no coding knowledge."
  - q: "Which iPhone models support the AI-powered Shortcuts feature?"
    a: "The AI-powered Shortcuts feature requires iOS 27 and is available on iPhone models that support Apple Intelligence, which includes the iPhone 15 Pro and later."
  - q: "Are there examples of automations I can create with the new AI?"
    a: "You can create automations like 'Send a daily weather report to my family group,' 'Turn on my smart lights when I arrive home,' or 'Log my water intake in the Health app after I say I drank water.'"

---
{{< audio src="/audio/apple-shortcuts-ai-workflows-ios-27.mp3" >}}

I've been ignoring Apple Shortcuts for years. Every time someone told me "you should automate that," I'd open the app, stare at the blank canvas of triggers and actions, and close it again. It looked like a developer tool pretending to be consumer software. Then iOS 27 happened, and now I describe what I want in plain English — and the app builds it for me. If you've been sleeping on Shortcuts like I was, this is the update that changes everything.

## What changed in iOS 27

The Shortcuts app has existed since 2018, but it always had a learning problem. You needed to understand triggers, actions, variables, and how apps expose their functions to the system. It was powerful for people who understood automation logic — and completely opaque for everyone else.

iOS 27 adds [Apple Intelligence](https://www.apple.com/os/ios/) directly into the Shortcuts creation flow. Instead of dragging blocks and connecting actions manually, you describe what you want in natural language. "When I get home, turn on my lights and start my evening playlist." "Every morning at 7am, summarize my calendar and send it to my partner." "When I take a screenshot, save it to my Notes folder and tag it."

The AI interprets your intent, identifies which apps and actions are needed, and builds the shortcut for you. You can review it, tweak it, or just run it. It's the difference between learning a programming language and telling someone what you want — except that someone is your phone.

## How to actually use it

Here's the step-by-step for creating your first AI-powered shortcut.

**Open Shortcuts and tap the new "Describe" button.** It's at the top of the creation screen — a text field with a sparkle icon. This is where Apple Intelligence lives.

**Type or speak what you want.** Be specific but don't worry about technical terms. Instead of "create automation with location trigger," say "when I arrive at the gym, start my workout playlist and open my timer app." The AI handles the translation.

**Review the generated shortcut.** iOS 27 shows you each step it created, color-coded by app. You'll see something like: Trigger (Location: Gym) → Action (Play Playlist: Workout) → Action (Open App: Timer). If something looks wrong, tap any step to edit it.

**Run it once manually first.** Before setting it to auto-trigger, run the shortcut from the app to make sure everything works the way you expect. This is especially important if it involves sending messages or modifying settings.

**Set your trigger.** Once it works, choose how it activates: automatically (on a trigger like time, location, or event) or manually (tap to run). The new triggers in iOS 27 include message sending, photo capture, and arriving at specific locations — far more options than previous versions.

This workflow is similar to what [I do with other AI automation tools](/posts/build-your-first-automation-in-15-minutes/), but the advantage here is that it's already on your phone. No third-party app, no subscription, no account to create.

## The real use cases that save time

After two weeks of testing, here are the shortcuts that actually changed my daily routine.

**Morning briefing.** "At 7am on weekdays, show me today's calendar events, the weather, and my top 3 reminders." This replaced three separate app checks every morning. The AI built a shortcut that pulls from Calendar, Weather, and Reminders in one view.

**Screenshot filing.** "When I take a screenshot, move it to my Screenshots album and delete it from Recents." I take dozens of screenshots for work — this keeps my photo library clean automatically.

**Evening wind-down.** "At 10pm, enable Do Not Disturb, set brightness to 30%, and play my Sleep playlist." Simple, but I never remembered to do all three manually. Now it just happens.

**Meeting prep.** "5 minutes before any calendar event with 3+ people, open the event notes and set a 25-minute timer." This one was more complex — the AI needed to understand calendar filtering — but it got it right on the second try.

The pattern I've noticed: the best shortcuts aren't the flashy ones. They're the small, repetitive things you do 10 times a day without thinking. That's where [automation actually saves time](/posts/stop-doing-things-manually-5-ai-workflows/) — not in the grand gestures, but in the friction you didn't know was there.

## What it can't do (yet)

The natural language interface is impressive, but it has limits. Complex conditional logic — "if this AND that, but NOT this other thing" — still requires manual editing. The AI handles simple if/then well, but multi-step branching gets confused.

Cross-app data passing is also hit or miss. "Take the address from this message and open it in Maps" works. "Take the address from this message, find the nearest coffee shop, and add both to my calendar" sometimes fails because the AI can't chain the data correctly between three apps.

And Siri integration is still... Siri. You can trigger shortcuts by voice, but the voice recognition for complex shortcut names is unreliable. I've taken to naming my shortcuts with simple, distinct words — "Morning" instead of "Weekday Morning Briefing With Weather."

If you've used tools like [Make or Zapier](/posts/make-vs-zapier-which-one-is-actually-easier/), you'll notice Shortcuts is still more limited in terms of third-party integrations. But for Apple-native automation — things involving your calendar, messages, photos, HomeKit, and system settings — it's now genuinely competitive.

## How this compares to other tools

If you're already using [Zapier](/posts/zapier-vs-make-vs-n8n-which-automation-tool/) or Make for web-based automation, Shortcuts isn't a replacement — it's a complement. Shortcuts excels at device-level automation: things that happen on your phone, with your phone's data. Zapier excels at connecting web services.

The real power move is using both. I have a Shortcut that captures my gym check-in time, then a Zapier workflow that logs it to a Google Sheet. Neither tool alone could do both — the phone-level trigger and the cloud-level data storage require different systems.

For beginners who haven't automated anything yet, start with Shortcuts. It's free, it's already on your phone, and with iOS 27's natural language interface, there's zero learning curve. Once you've outgrown what it can do, that's when you explore third-party tools. Check out [the AI tools I'd learn first](/posts/the-7-ai-tools-id-learn-first-if-i-started-over-in-2026/) for where to go next.

## The bottom line

Apple Shortcuts in iOS 27 is what happens when AI makes a power tool accessible to everyone. You don't need to understand automation logic, triggers, or variables — you just describe what you want and the app figures it out. If you have an iPhone, this is the lowest-effort automation you can start with today. For more ways to put AI to work in your daily routine, head to [/start-here/](/start-here/).
