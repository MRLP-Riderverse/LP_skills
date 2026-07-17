---
name: creative-notation-art
description: "ASCII art, ASCII video, and text-based visual composition for quick, expressive output."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ascii, text-art, animation, visual-composition, creative]
    category: creative
    related_skills: []
---

# Creative Notation Art

Use this skill for text-first visual work: static ASCII art, animated ASCII/video treatments, and any situation where the medium itself is the style.

## When to use
- User wants ASCII art, text art, terminal art, or an emoji-free visual made from characters
- User wants an ASCII animation, ASCII video, or frame-based text motion treatment
- User wants a fast, disposable visual with strong stylistic constraints and minimal dependencies

## Core workflow
1. Decide the output form: static composition, frame sequence, or animated render.
2. Choose the character palette and contrast strategy first; style comes from density and spacing.
3. Build a readable silhouette before adding details.
4. Verify the artifact at the actual target width so the composition survives rendering.
5. Iterate on spacing before adding more content.

## Static ASCII
- Favor strong shapes and a small character palette
- Use whitespace intentionally; empty space is part of the image
- Keep titles and borders simple unless the user asks for ornament
- Match the output width to the user's display or delivery channel

## Animated ASCII / video
- Treat motion as a sequence of stable keyframes, not random frame churn
- Keep the background and major anchors consistent across frames
- Reduce fine detail when motion increases; flicker kills readability
- Prefer a short loop or a clearly bounded sequence unless the user asked for a longer piece

## Quality bar
- The subject should be recognizable at a glance
- The composition should read before the decoration does
- If animation is used, the motion should add meaning rather than noise

## Related sibling content
This umbrella absorbs the former narrow skills `ascii-art` and `ascii-video`.