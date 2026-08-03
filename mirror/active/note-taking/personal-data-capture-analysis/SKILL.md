---
name: personal-data-capture-analysis
description: Use for local-first personal reality capture and analysis.
category: note-taking
aliases: [personal-metrics, reality-log-analysis, local-first-self-observation]
---

# Personal Data Capture and Analysis

This is the class-level workflow for turning informal first-person observations into useful longitudinal evidence without flattening the person into a rigid productivity tracker.

## Core Architecture

Treat the system as a staged pipeline:

```text
low-friction human capture
→ append-only QuickThoughts raw stream
→ deterministic local parsing and routing
→ organized derived files/folders
→ GBrain local index
→ contextual review and pattern hypotheses
→ future prediction map / custom mobile UX
```

QuickThoughts is the raw source of truth. GBrain is a searchable derived index, not the canonical diary. A future mobile app should be treated as a capture/interface layer over the proven local data model, not as a replacement for the CLI foundation.

## Capture Principles

1. Preserve reality before optimizing it. Body signals, pacing, hydration, appetite, weather, media, room changes, social sensing, forgotten intentions, and transitions may become meaningful predictors later.
2. Keep capture low-friction. Informal fragments are valid data; do not require a complete journal entry or a direct agent response every time.
3. Capture explicitly requested material through the canonical QuickThoughts `note` CLI. Never rewrite the append-only inbox directly.
4. Keep direct first-person observations raw/unattributed when that preserves the user's voice. Use an agent source label for Hermes-authored summaries or interpretations.
5. Avoid premature diagnosis. Describe recurring associations as hypotheses, not medical or psychological conclusions.
6. Avoid premature taxonomies. Let useful categories emerge from real use, then formalize only stable vocabulary.

## Temporary Semantic Tags

Literal tags may act as searchable breadcrumbs:

- `[HUMAN]` — personal reality, state, or observation
- `[PULSE]` — quick state check
- `[ACTIVITY]` — physical or behavioral activity
- `[FRICTION]` — blockage, transition problem, or resistance
- `[ENDDAY]` — daily retrospective
- `[TASK]` — actionable item
- `[SOMEDAY]` — non-urgent task or idea
- `[FUTURE]` — later concept or system work

These are provisional text markers, not automatically interpreted GBrain metadata. Preserve raw notes even when routing later derives structured files. Do not invent a new tag for every one-off situation.

## Parsing and Routing

Once enough examples exist, build deterministic filters that separate at least:

- human reality/status observations
- structured pulses and end-of-day checks
- tasks and someday items
- development/system notes
- Hermes-generated summaries
- cron and sync status
- research or GPT-transfer material

Derived routing must be reversible: keep the raw stream untouched, record provenance, and make it possible to regenerate organized files after parser changes.

## GBrain and Metrics

Use GBrain for contextual recall, but do not treat semantic retrieval as an exact counter. For questions such as "how often did I mention X?":

1. Search GBrain to identify likely pages and confirm index coverage.
2. Scan canonical raw/dated Markdown source files deterministically.
3. Deduplicate overlapping daily pages or raw snapshots by stable timestamp plus entry body.
4. Report matched rows, unique entries, unique dates, and extracted entities separately.
5. Distinguish explicit claims from inferred sentiment. "Favorite episode" requires an explicit preference; a positive reaction is evidence of engagement, not proof of favorite status.
6. If search and deterministic counts disagree, report the disagreement and use the source scan for exact counts.

A note in QuickThoughts is not proven to be in GBrain until the relevant daily page/import is verified.

## Analysis Guardrails

- QuickThoughts captures expressed/captured activity, not necessarily all activity.
- Automated sync entries can contaminate time-of-day and activity counts; classify source types before forecasting.
- Burst days can dominate averages; inspect distributions and event clusters, not only weekday means.
- Prefer transition hypotheses such as `recovery → intake → synthesis → execution → decompression → recovery` over deterministic claims about what a weekday means.
- Ask what happens after a burst: execution, more research, decompression, physical activity, social involvement, sparse capture, or maintenance.
- Treat environmental and bodily context as potentially explanatory variables, not noise.

## Memory Boundary

Keep only compact, temporary conventions or durable preferences in hot Hermes memory. Store detailed project architecture, observations, historical examples, and analysis in QuickThoughts/GBrain. When a temporary convention is later codified in this skill or a parser, remove the duplicate memory entry.

## Verification Checklist

Before claiming the workflow worked:

- confirm the note was appended through the canonical CLI
- verify the raw entry and tags are present
- verify the relevant source page exists in GBrain after sync/import
- for counts, run a deterministic source scan and deduplicate
- state what is directly observed versus inferred
- preserve uncertainty where capture is sparse or contaminated by automation

## Related Skills and Reference

- `note-capture-workflow` — canonical append-only QuickThoughts capture
- `gbrain-operations` — GBrain setup, import, and search operations
- `references/exact-counting-and-routing.md` — reusable counting and routing rules from the initial personal-data experiment
