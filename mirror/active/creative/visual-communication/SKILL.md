---
name: visual-communication
description: "Design tokens, design references, and infographic generation for visual identity work."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [design, tokens, references, infographic, visual-communication, ui]
    category: creative
    related_skills: []
---

# Visual Communication

Use this skill when the goal is to translate ideas into a coherent visual language: formal design specs, design references, or high-density information graphics.

## When to use
- User wants a DESIGN.md or token-based visual spec
- User wants a library of real-world design references or design-system inspiration
- User wants an infographic, visual summary, or information graphic
- User wants to move from brand direction to a concrete visual system

## Core workflow
1. Decide whether the deliverable is a spec, a reference, or a finished graphic.
2. Extract the visual identity: color, typography, density, motion, spacing, and tone.
3. Convert that identity into reusable tokens, patterns, or composition rules.
4. Keep the output internally consistent; visual communication fails when components disagree.
5. Verify that the artifact communicates the intended hierarchy without explanation.

## Community/mobile public-site UX passes
Use this pattern for small public community sites, static mirrors, directories, and event calendars where the backend/source-of-truth is intentionally structured but the public surface must feel warm and local.

- Start from the **first mobile screen before any taps**. If the user supplies phone screenshots, treat them as primary evidence for first impression; do not overfit to desktop layout.
- Separate public identity from internal machinery. Hide or rewrite admin/export/source terms such as `published`, `active`, `placeholder`, `static event layer`, `generated from`, `source repo`, `drafts`, and implementation status unless the public user benefits from seeing them.
- Collapse overlapping navigation intents. If “discover”, “search”, and “explore” point into the same underlying directory, make them one clear experience: a search/browse path with optional lenses, not three conceptual tabs.
- For local/cultural belonging, lead with place, warmth, and purpose before controls: identity headline, human lede, one primary CTA, one secondary CTA, and a small preview of live content.
- Make related/contextual data visually subordinate. Related places, venue context, or source metadata should either live inside the main card as clearly-labeled sub-info or below a strong divider with different styling; do not render it in the same card style as primary content.
- Prefer public labels like “Find local places”, “What’s happening”, “Related events”, “Linked places”, “Coming up”, and “Local places” over database labels like “Directory browse”, “Event feed”, “Official entries”, or “Filter options”.

## Subsections
### Formal design specs
Use token-based specs when the user needs a machine-readable design system with exact values.

### Design reference libraries
Use reference catalogs when the user wants to imitate or borrow an established visual language.

### Infographic generation
Use infographic workflows when the source content is dense and the goal is structured visual explanation.

## Quality bar
- The result should be easy for another agent or designer to reuse
- Tokens, references, and layout choices should reinforce one another
- The output should make the hierarchy obvious at a glance

## References
- `references/community-mobile-ux-pass.md` — first-impression mobile UX cleanup pattern for public community directory/event sites.

## Related sibling content
This umbrella absorbs the former narrow skills `design-md`, `popular-web-designs`, and `baoyu-infographic`.