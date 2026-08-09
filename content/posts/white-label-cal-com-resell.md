---
title: "White-label this open-source tool and sell it for $200/month"
date: 2026-05-22
draft: false
description: "Cal.com is an open-source scheduling tool that does everything Calendly does — for free. But here's the real play: white-label it and sell it to professionals who don't know it exists. Dentists, lawyers, therapists. $200/month each. Here's how."
tags: ["AI tools", "no-code", "automation", "business", "open source", "monetization"]
categories: ["tools"]
slug: "white-label-cal-com-resell"
cover:
  image: "/images/white-label-cal-com-resell.jpg"
faqs:
  - q: "How do I white-label Cal.com and sell it as my own service?"
    a: "You can rebrand Cal.com with your own logo, colors, and domain by self-hosting it and modifying the configuration files. Then package it as a premium scheduling solution for niche professionals who won't know it's open-source underneath."
  - q: "Is it legal to resell an open-source tool like Cal.com?"
    a: "Yes, Cal.com uses the AGPLv3 license which allows commercial use and modification as long as you comply with the license terms. You're selling your hosting, support, and customization — not the software itself."
  - q: "Which industries are best for selling white-label scheduling software?"
    a: "Service-based professionals like dentists, lawyers, therapists, and consultants are ideal because they need appointment booking but lack technical skills. They'll happily pay $200/month for a branded solution that 'just works.'"
  - q: "How much can I realistically charge for a white-label Cal.com setup?"
    a: "Most resellers charge between $100-$300/month per client depending on the niche and support level included. At $200/month, you only need 10 clients to generate $2,000 in recurring monthly revenue."

---

{{< audio src="/audio/white-label-cal-com-resell.mp3" >}}

## White-label this open-source tool and sell it for $200/month

Last week I was paying $12/month for Calendly. Then I found Cal.com — an open-source alternative that does everything Calendly does, plus more, for free.

But that's not the interesting part.

The interesting part is the business model hiding inside this repo. White-label it. Sell it to professionals who'll never find it themselves. $200/month per client. No coding required.

I spent a weekend figuring out how this works. Here's what I found.

---

## What is Cal.com?

Cal.com is an open-source scheduling tool. Think Calendly, but you own it. You can:

- Self-host it (run it on your own server)
- Customize every pixel (your branding, your colors, your domain)
- Connect it to Stripe for paid bookings
- Integrate it with Google Calendar, Outlook, Zoom, Teams
- Use their API to build scheduling into your own product

The founders hit $5 million in annual revenue in 3 years. Not by selling the tool itself — by selling the white-label version to businesses who needed branded scheduling.

That's the model. And you can copy it this weekend.

---

## The white-label play

Here's how it works:

1. **You install Cal.com on your server** (or use their hosted version with white-label enabled)
2. **You customize it** — put your client's logo, colors, and domain on it
3. **You sell it to professionals** — dentists, lawyers, therapists, coaches, personal trainers
4. **You charge $200/month** — for a tool that costs you $0 to run

Why would dentists pay $200/month for something they could get free? Because they don't know it exists. They don't know how to install it. They don't want to learn. They want it to work. They'll pay for that.

---

## The math

- 10 clients × $200/month = $2,000/month
- 25 clients × $200/month = $5,000/month
- 50 clients × $200/month = $10,000/month

Your costs? A $5/month VPS and about 2 hours of setup per client. After that, it runs itself.

---

## Who to sell to

These industries will pay for branded scheduling:

- **Dentists** — they need appointment booking, but they're not tech people
- **Lawyers** — consultation scheduling, paid discovery calls
- **Therapists** — HIPAA-compliant session booking
- **Personal trainers** — session scheduling with payment
- **Real estate agents** — property viewing scheduling
- **Accountants** — tax season appointment booking
- **Salons and spas** — online booking with deposits

Every single one of these businesses is paying someone else for scheduling right now. Usually Calendly Pro ($12/month) or Acuity ($16/month). You're offering them a branded version for their business — same tool, better branding, and they never have to think about it.

---

## How to set it up

### Step 1: Install Cal.com

The easiest way is with Docker:

```bash
git clone https://github.com/calcom/cal.com.git
cd cal.com
cp .env.example .env
docker compose up -d
```

That's it. You have a running scheduling platform.

### Step 2: Customize for your client

- Upload their logo
- Set their brand colors
- Connect their domain (e.g., book.drdavis.com)
- Link their Google Calendar
- Connect Stripe if they want paid bookings

### Step 3: Sell it

Reach out to local professionals. Show them their branded booking page. Ask: "Would you pay $200/month for this?"

Most will say yes. Because right now they're either paying for Calendly, or they're scheduling by hand via phone calls.

---

## Why this works

The founder of Cal.com proved the model. They raised $32 million because the white-label scheduling market is real. Businesses need branded booking tools. They don't want to build them. They don't want to maintain them. They want to pay someone to handle it.

That someone could be you.

You don't need to code. You need to install Docker, customize a few settings, and talk to 10 local businesses. That's the entire business.

---

## The bottom line

Cal.com is free, open-source, and battle-tested. The founders built a $5M/year business from it. You can build a smaller version of the same business — white-label it, sell it to local professionals, collect $200/month from each one.

This is the kind of thing I talk about on [@manalbuilds](https://instagram.com/manalbuilds) — real tools, real income, no courses needed.

---

*Coming soon: How Coolify replaces Vercel, Railway, and $200/month in hosting fees*

---

> FTC Disclosure: This post is not sponsored. I'm not affiliated with Cal.com. I just think their model is worth copying.

## References

1. Cal.com GitHub — https://github.com/calcom/cal.com
2. Cal.com Official Website — https://cal.com
3. Cal.com White Label Documentation — https://cal.com/docs/white-label
4. Cal.com Review 2026 — https://efficient.app/apps/cal
