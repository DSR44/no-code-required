---
title: "I made a TikTok dance video for $0.39 with AI — here's the exact prompt"
date: 2026-05-22
draft: false
description: "No dancer. No camera. No studio. I used GPT Image 2.0 to generate a 9-panel storyboard, then fed it into PixVerse to create a 10-second dance video. Total cost: $0.39. Here's the exact prompt and JSON I used — copy it, change the style, make it yours."
tags: ["AI tools", "no-code", "automation", "video generation", "TikTok", "GPT Image", "PixVerse"]
categories: ["tools"]
slug: "tiktok-dance-video-ai-for-39-cents"
---

{{< audio src="/audio/tiktok-dance-video-ai-for-39-cents.mp3" >}}

# I made a TikTok dance video for $0.39 with AI — here's the exact prompt

Last night I spent $0.39 and made a TikTok dance video. No dancer. No camera. No studio. Two AI tools. One prompt. Ten seconds of content.

Here's exactly how I did it — and the full prompt you can steal.

---

## The pipeline

Two tools. Two API calls. That's it.

1. **GPT Image 2.0** ($0.09) — generates the 9-panel storyboard
2. **PixVerse v6** ($0.295) — turns the storyboard into video

Total: **$0.39** for a 10-second dance video that looks like it cost $500 to produce.

---

## Step 1: Generate the storyboard

I used GPT Image 2.0 with a 9:16 aspect ratio and a detailed prompt that specified every panel in a 3x3 grid. Each panel is a different shot type — wide, medium, close-up — showing a different dance move.

Here's the exact prompt I used:

```
Generate a clean TikTok dance storyboard in a 9:16 portrait layout 
with 9 panels arranged in a 3x3 grid. A fit confident woman with 
minimal stylish outfit. Soft natural lighting, plain dance studio 
background, neutral tones. Each panel shows a different dance moment:

top-left: wide neutral pose
top-center: arm wave
top-right: close-up expression
mid-left: hip sway
mid-center: step and turn
mid-right: hair flip
bottom-left: full dance combo
bottom-center: signature pose
bottom-right: direct eye contact smile

Clean minimal smartphone-style TikTok aesthetic.
```

The output is a single image with all 9 panels. That image becomes your input for the video model.

---

## Step 2: Animate with PixVerse v6

Take the storyboard image URL and feed it into PixVerse v6 image-to-video. The prompt I used:

```
A fit woman performing a TikTok dance sequence, smooth flowing 
dance movements, energetic hip hop style dance, dynamic camera, 
warm studio lighting, smartphone vertical video feel
```

Set aspect ratio to 9:16 and duration to 10 seconds. That's it.

---

## The reusable JSON (steal this)

I saved the full storyboard as a JSON template. You can modify the panels, change the style, and regenerate different versions:

```json
{
  "name": "TikTok Dance Storyboard v1",
  "image_model": "gpt-image-2-text-to-image",
  "video_model": "pixverse-v6-i2v",
  "cost": {"image": 0.09, "video": 0.295, "total": 0.385},
  "aspect_ratio": "9:16",
  "duration": 10,
  "panels": [
    {"pos": "top-left", "shot": "Wide", "action": "Neutral pose"},
    {"pos": "top-center", "shot": "Medium", "action": "Arm wave"},
    {"pos": "top-right", "shot": "Close-up", "action": "Expression"},
    {"pos": "mid-left", "shot": "Medium-wide", "action": "Hip sway"},
    {"pos": "mid-center", "shot": "Tracking", "action": "Step and turn"},
    {"pos": "mid-right", "shot": "Close-up", "action": "Hair flip"},
    {"pos": "bottom-left", "shot": "Wide", "action": "Full combo"},
    {"pos": "bottom-center", "shot": "Medium", "action": "Signature pose"},
    {"pos": "bottom-right", "shot": "Close-up", "action": "Eye contact"}
  ],
  "style_variants": ["minimal", "street", "fitness", "elegant", "retro"]
}
```

### Style variants you can try

Change the prompt text to match these themes:

| Style | Background | Outfit | Vibe |
|-------|-----------|--------|------|
| **Minimal** (default) | Dance studio, neutral | Simple top + shorts | Clean, TikTok native |
| **Street** | Urban backdrop, neon | Streetwear, hoodie | Edgy, urban |
| **Fitness** | Gym, equipment visible | Athletic wear | Energetic, strong |
| **Elegant** | Ballroom, curtains | Flowing dress | Cinematic, premium |
| **Retro** | 70s disco, colorful | Vintage outfit | Fun, nostalgic |

Just swap the prompt text and regenerate. Same grid, different look.

---

## The math

If you post one dance video a day:

- **Daily cost:** $0.39
- **Monthly cost:** $11.70
- **Videos per month:** 30

Compare that to:
- Hiring a dancer: $200-500 per video
- Filming yourself: Hours of setup, lighting, editing
- Stock footage: Generic, not yours

$0.39 per video vs $200+. That's a 500x cost reduction.

---

## What you need

An API key from muapi.ai — that gives you access to GPT Image 2.0, PixVerse v6, and 100+ other models through one endpoint. No subscriptions, pay per generation.

This is the kind of thing I build and share on [@manalbuilds](https://instagram.com/manalbuilds). Real tools. Real output. No courses.

---

*More storyboard templates coming soon. Subscribe to the newsletter to get them first.*

---

> FTC Disclosure: This post is not sponsored. I'm not affiliated with muapi.ai. I just use their API.

## References

1. muapi.ai API Documentation — https://muapi.ai
2. GPT Image 2.0 — OpenAI's latest image generation model
3. PixVerse v6 — Video generation from images
