---
name: creative-diagramming
description: "Create architecture diagrams, flow diagrams, and hand-drawn diagram artifacts."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [diagramming, architecture, flow, excalidraw, svg, visualization]
    category: creative
    related_skills: []
---

# Creative Diagramming

Use this skill when the user needs a diagram rather than prose: architecture maps, flow diagrams, sequence diagrams, infrastructure layouts, and sketch-style visual explanations.

## When to use
- User asks for architecture, cloud, or infra diagrams
- User wants a hand-drawn / whiteboard style diagram artifact
- User wants a flowchart, sequence diagram, or concept map
- User wants a diagram that is meant to be shared or edited later

## Choose the output format
### HTML/SVG architecture diagram
Best when the subject is technical infrastructure and the goal is a polished, dark, presentation-ready diagram.

### Excalidraw JSON
Best when the user wants a sketchy, editable, collaborative diagram that can be opened in Excalidraw.

## Core workflow
1. Identify the system or relationship to be shown.
2. Pick the right diagram language for the audience.
3. Keep the number of nodes and arrows low enough to read quickly.
4. Label the critical paths and boundaries first.
5. Verify spacing, arrow direction, and legibility before delivery.

## Principles
- One diagram, one message
- Prefer clear grouping over decorative complexity
- Use consistent semantics for color, boundaries, and arrow styles
- Put the main story in the center; keep supporting details secondary

## Format-specific notes
### HTML/SVG diagrams
- Best for dark technical layouts and polished deliverables
- Use precise geometry, readable labels, and restrained color coding
- Optimize for browser viewing and static sharing

### Excalidraw diagrams
- Best for rough, editable, hand-drawn style communication
- Keep shapes simple and text legible
- Favor editability over perfect alignment

## Related sibling content
This umbrella absorbs the former narrow skills `architecture-diagram` and `excalidraw`.