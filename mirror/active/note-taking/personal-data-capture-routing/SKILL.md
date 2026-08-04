---
name: personal-data-capture-routing
description: "Use for informal personal-data capture and routing."
category: note-taking
aliases: [personal-data, lived-data, quickthoughts-routing, informal-observation-capture]
---

# Personal Data Capture and Routing

Use this skill when the user wants to preserve informal observations, bodily or environmental context, small transitions, energy states, errands, or future personal-data infrastructure ideas. The goal is to gather richer reality before imposing a rigid journal schema.

## Core Principle

Treat QuickThoughts as the append-only raw intake stream and preserve details that ordinary productivity systems discard: sensory experience, movement, hydration, appetite, environmental conditions, media context, physical-space transitions, distraction, forgotten intentions, and subjective energy. Do not decide in advance that a detail is irrelevant.

The near-term pipeline is:

```text
raw QuickThoughts capture
→ minimal semantic tags
→ deterministic local parsing/routing
→ derived folders/files
→ GBrain contextual index
→ longitudinal metrics and pattern hypotheses
→ purpose-built mobile UX
```

QuickThoughts is the source of truth. GBrain is a derived contextual index, not proof that a note was captured or a quantitative metric was counted.

## Low-Friction Capture

When the user explicitly asks to note, save, remember, log, or capture something, use the canonical note-capture workflow and do not rewrite old raw entries. Preserve the user's voice, lightly normalize only obvious readability issues, and do not convert a small life-log observation into an essay.

For a concept or future system idea, capture one compact durable proposition that preserves the discovered structure. For a rich state observation, retain the concrete sensory and situational details because they may later explain transitions or energy patterns.

Do not force every observation through a questionnaire. Occasional informal entries are valid data; consistency should grow from low friction rather than from an elaborate form.

## Temporary Tag Convention

Use literal breadcrumbs in the note text until a parser exists:

- `[HUMAN]` — personal observation or authored reality
- `[PULSE]` — immediate state, energy, attention, or mood signal
- `[ACTIVITY]` — what the person was doing or physically experiencing
- `[FRICTION]` — blockage, transition loss, avoidance, or context-switch cost
- `[ENDDAY]` — end-of-day reflection
- `[TASK]` — actionable item
- `[SOMEDAY]` — non-urgent actionable item
- `[FUTURE]` — later concept, infrastructure, or system direction

Use the smallest confident set. Tags are indexing breadcrumbs, not a diagnosis or a complete ontology. Do not invent details merely to justify a tag.

## Delegated Tagging

A delegated offshoot may classify a raw observation and return one proposed tagged note, but it must not write to QuickThoughts. Give it the available tag set and explicitly require it to:

1. Preserve the user's concrete meaning and informal voice.
2. Avoid inventing time, location, quantity, causality, or health claims.
3. Avoid over-tagging; use only categories clearly supported by the text.
4. Explain each selected tag briefly.

The parent agent reviews the proposal and remains responsible for the actual append through the canonical note CLI. If the proposal is clean, human approval can be lightweight, but the parent should still verify the persisted result. A successful pattern is:

```text
raw observation
→ delegated minimal tag proposal
→ parent/human review
→ tagged append through note CLI
→ persisted-entry verification when useful
```

## Memory Offload and Refactoring

Persistent memory is a hot cache, not an archive. When it approaches capacity:

1. Capture a complete backup-style memory dump into QuickThoughts before destructive cleanup.
2. Move session-specific project state, historical decisions, model-routing references, and long explanations into the note archive.
3. Keep only compact stable preferences, active configuration, critical URLs, and high-value recurring workflow facts in memory.
4. Refactor duplicate or verbose entries rather than accumulating parallel versions.
5. Verify both the backup note and the resulting memory allowance.

Never treat raw QuickThoughts cleanup as part of ordinary memory offload. Capture is append-only; routing and consolidation belong in future derived files.

## GBrain and Metrics

Use deterministic local scans for exact counts, dates, episode numbers, tags, and deduplication. Use GBrain to retrieve surrounding context and related passages. A semantic search result is not a count and may include weakly related pages; do not report quantitative findings from search hits alone.

Before claiming that a note is in GBrain, distinguish:

- present in the local QuickThoughts inbox
- present in a synced daily source page
- retrievable through GBrain search

When a metric matters, report the source scope, deduplication rule, and whether automated/system entries were excluded. Start with descriptive pattern maps and hypotheses; do not imply diagnosis or deterministic prediction from sparse, mixed-source data.

## Structured Environmental Telemetry

Recurring measurements such as weather are useful longitudinal context. Keep raw measurements in a local append-only structured archive first, with minimal metadata such as local observation time, location/context, primary measurement, conditions/state, units, and provenance. For the user's low-frequency weather schedule, a deterministic wrapper may also append a compact human-readable note through the canonical `note` CLI using a dedicated `Weather` source label; this requires no LLM and preserves the existing QuickThoughts → GBrain sync path.

Use this boundary:

```text
weather cron → local structured archive + compact QuickThoughts note → existing GBrain sync → historical recall
```

For prior-weather questions, search the local archive and GBrain/QuickThoughts-derived pages before using web search. Use deterministic local scans for exact dates and measurements; use GBrain for contextual retrieval, and use the web only for gaps.

Treat explicit current-weather one-shots as valid curiosity telemetry too, regardless of location. Route them through the same deterministic weather wrapper so each request becomes a compact `Notes, by Weather` observation without invoking an LLM or GBrain per report. This preserves the user's questions as a searchable trail rather than logging only scheduled home-weather checks.

Keep presentation layers separate: Telegram may use extra blank lines for human visual scanning, while multiline QuickThoughts entries should use single newlines between structured rows when blank-line padding adds no meaning. Preserve both from the same raw report without mutating older entries.

## Privacy and UX Direction

Prefer local-first storage and an accessible CLI foundation. Discord or another cloud platform may be a useful prompt gateway, but it is not a fundamental fix for capture friction and should not replace the local source of truth. A future mobile app should be designed around proven capture patterns from the CLI/raw stream rather than invented before real use reveals them.

## Support Files

- `references/tagging-and-delegation.md` — compact reference for the temporary tag grammar and delegated-classifier contract.

## Verification Checklist

Before finishing a capture/routing task:

- Was the raw note preserved through the canonical append-only path?
- Were tags minimal and supported by the text?
- Did any delegated worker avoid direct file writes?
- If memory was refactored, was a full backup captured first?
- Are exact metrics based on deterministic source scans rather than semantic search counts?
- Is any future parser described as derived routing rather than raw-data mutation?
