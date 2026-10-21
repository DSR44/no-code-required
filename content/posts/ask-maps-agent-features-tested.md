---
title: "Finally: Google Maps Does Things for You (I Tested Its New Agent Features)"
date: 2026-10-21
slug: ask-maps-agent-features-tested
draft: false
description: "Ask Maps is Google's new agent inside Google Maps: it orders food, books hotels, and reads your inbox. I tested every feature — here's what works."
tags: ["Google", "AI agents", "Google Maps", "automation", "AI tools"]
categories: ["tools"]
keywords:
  - Ask Maps
  - Google Maps AI agent
  - Google Maps food ordering
  - Personal Intelligence Google
  - agentic AI travel
ShowToc: true
TocOpen: false
cover:
  image: "/images/posts/ask-maps-agent-features-tested.jpg"
  alt: "Zoe at a cafe table ordering lunch through Google Maps on her phone, laptop open beside her showing a travel itinerary"
faqs:
  - q: "What is Ask Maps in Google Maps?"
    a: "Ask Maps is Google's conversational layer inside Google Maps. The newest version is agentic, meaning it can place food orders, build hotel shortlists with click-through booking, and pull answers from your Gmail and Calendar if you opt in to Personal Intelligence."
  - q: "Can Google Maps order food and book hotels for me?"
    a: "Food ordering works end to end when a restaurant uses Square, Toast, or Uber Eats — Ask Maps builds the cart and you approve payment. Hotels work differently: it searches and filters, but booking always finishes on the partner's site."
  - q: "What is Google's Personal Intelligence and is it safe?"
    a: "Personal Intelligence lets Ask Maps read your Gmail and Calendar to give personalized answers like flight times or reservation details. It is off by default, and you should treat it as a genuine privacy trade — Google stores conversation memory to make follow-ups work."
  - q: "Is Ask Maps available outside the United States?"
    a: "The agentic features, including food ordering and Personal Intelligence, rolled out in the US first. Availability elsewhere has not been announced, so most international users still get the standard experience."
---
{{< audio src="/audio/ask-maps-agent-features-tested.mp3" >}}

Yesterday I typed "order me lunch from somewhere nearby that isn't a chain" into Google Maps, and a map made me a sandwich. Not a link to DoorDash. Not a list of ten restaurants. An actual order, sitting in a cart, waiting for my card.

Google calls this Ask Maps, and the newest version crossed a line maps have never crossed: it does things instead of showing things. It places food orders inside Maps, searches hotels the way you'd describe them to a friend ("somewhere quiet, under $200, walkable to the convention center"), and, if you opt in, reads your Gmail and Calendar to answer questions like "what time does my flight land tomorrow?"

Two disclosures before you hand it your inbox. The deepest version of this sits near Google's AI Ultra tier, the plan I took apart in [Google AI Ultra: What $100 a Month Actually Gets You](/posts/google-ai-ultra-plan-100-dollars/). And because an AI is now making transactional moves on your behalf, the disclosure and trust questions are the same ones I mapped in [The EU AI Act's New Labeling Rules: What Builders Actually Need to Do](/posts/eu-ai-act-transparency-solo-builders/) — regulators already expect you to say when an agent acts for a customer.

I spent a full day testing every feature. Here's what works, what silently fails, and the one setting I'd still keep off.

## What Ask Maps can actually do now

The August rollout added four capabilities that turn Maps from a directory into something closer to an assistant:

- **Agentic food ordering.** Maps now connects directly to ordering systems like Square, Toast, and Uber Eats. You describe what you want; the agent builds a cart, including dietary filters you set in plain language.
- **Conversational hotel search with booking handoff.** You can stack constraints ("pet-friendly, under $180, free cancellation, near the airport") and tap straight through to the partner site to pay. Booking doesn't finish in-app, which I'll get to.
- **Event tickets in Maps.** Ask Maps surfaces ticketed events and routes you to checkout without leaving the map view.
- **Personal Intelligence.** This is the big one and the controversial one. With it on, Ask Maps reads your Gmail and Calendar, remembers what you asked it last time, and answers questions no map could before: "When does my flight land?" or "How far is that hotel from my Tuesday meeting?"

Google also added a live transit widget that surfaces real-time departures and delays the moment you open the app. Small feature, but it's the one I use most now.

## What I actually did

Three tests, each with a different expectation.

**Test one: the lunch order.** I asked for a non-chain lunch spot with a vegetarian option. Ask Maps returned two candidates, showed me their menus inline, and asked which one to order from. I picked the taqueria, it added an avocado torta to a cart, and I checked out on the restaurant's Square page. Total elapsed time: about ninety seconds, versus five minutes of app-switching the old way. The cart handoff was the clunky part. Ask Maps assembles the order, but you review and pay on the partner's page, which adds a step Google's demo videos gloss over.

**Test two: the hotel search.** I ran a fictional conference trip: quiet room, under $200, walkable to a venue. The agent returned a tight shortlist with prices and walking times, then handed me to each hotel's booking page. Useful, but calling this "booking" oversells it. Compare it with what Google's browser agents can already do, which I covered in [Google's AI Agents Can Now Browse the Web for You](/posts/google-ai-agents-browse-web-for-you/) — those actually complete multi-step checkouts. Ask Maps stops at the door.

**Test three: Personal Intelligence.** I turned it on, which grants Gmail and Calendar access, then asked what time my next flight lands. It pulled the confirmation from my inbox and answered correctly in one try. It also started remembering preferences across sessions: when I asked a follow-up about "that Seattle place," it knew which restaurant I meant without me repeating it. That memory is genuinely useful and genuinely the part that should make you pause.

## Do this yourself (it takes about ten minutes)

If you're in the US and want to try the agentic features, here's the shortest path:

1. **Open Google Maps and tap the Ask Maps bar** at the top. If you don't see it, update the app; the feature is still rolling out.
2. **Try a food order first.** Search something like "order falafel near me that's open now." Pick a restaurant whose menu loads inline — that means its ordering system is connected. Review the cart, then complete payment on the partner page.
3. **Test hotel search with stacked constraints.** Give it three or four requirements at once. The more specific, the better the shortlist.
4. **Only then decide about Personal Intelligence.** Open the Ask Maps settings and toggle it on if you want Gmail-and-Calendar answers. My rule: turn it on for a week, ask what you actually need, then decide whether the convenience justifies an AI reading your mail.
5. **Ask a follow-up from memory.** Once a session exists, reference something from earlier ("the one we looked at yesterday"). This is where the agent feel shows up.

If none of that clicks for you, remember the slower path still exists: my [15-minute starter guide to your first automation](/posts/build-your-first-automation-in-15-minutes/) covers the same idea with tools you fully control.

## What failed (and what I'd still keep off)

- **No true end-to-end booking.** Hotels and food both require a handoff to a partner site for payment. The agent prepares; you execute. If you expected the DoorDash-style automation I wrote about in [DoorDash's New CLI Is a Preview of How Agentic Commerce Actually Works](/posts/doordash-cli-agentic-commerce-solo-builders/), this is a half-step toward that.
- **Generic answers without Personal Intelligence.** With it off, suggestions felt like any other search result. The personalization is the product here; without it, you're using a prettier search box.
- **Memory is permanent until you clear it.** Ask Maps stores your conversation history to power follow-ups. You can delete it in settings, but you have to know to look.

## Who should skip this

Skip it entirely if you're outside the US, where the rollout hasn't reached yet. Skip it if the idea of Google reading your inbox makes your jaw tighten; that instinct is correct, and [the privacy trade almost nobody talks about](/posts/the-privacy-problem-nobody-talks-about/) applies fully here. And skip it if you want real booking automation — the handoff friction will annoy you more than the convenience helps.

There's also a subtler risk worth naming. When one app quietly starts doing errands for you, it becomes harder to notice which decisions you've delegated. I made that exact argument in [The AI Groupthink Problem Nobody Wants to Admit](/posts/ai-groupthink-problem-solo-builders/): the more an agent anticipates you, the less you notice what it chose to anticipate. That's not a reason to avoid the feature. It's a reason to keep ordering your own lunch once in a while.

## The bottom line

Ask Maps is the first mass-market agent that does something concrete instead of promising to. The food ordering works today. Hotel search is useful but incomplete. Personal Intelligence is powerful and the most invasive thing Google has shipped into a default app in years.

My advice: use it for food, keep Personal Intelligence off until a specific question forces you to turn it on, and treat the hotel feature as a research tool rather than a booking tool. And if you want to understand what the assistant era looks like beyond maps, start with [The AI Tools I Actually Use Every Day](/posts/the-tools-i-actually-use-every-day/) — or the full [start-here guide](/start-here/) that ties all of it together.
