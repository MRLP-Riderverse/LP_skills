---
name: hermes-persona-layering
description: Review and optimize Hermes persona context across SOUL.md, USER.md, MEMORY.md, and configured personality layers without conflating identity, user profile, hot memory, or warm storage.
version: 1.0.0
author: MidnightRider.sol + Hermes
license: MIT
metadata:
  hermes:
    tags: [hermes, persona, soul, memory, user-profile, prompt-optimization]
    related_skills: [hermes-agent, note-capture-workflow, quickthoughts-daily-sync]
---

# Hermes Persona Layering

Use this skill when reviewing, designing, or optimizing Hermes identity and context files: `~/.hermes/SOUL.md`, `~/.hermes/memories/USER.md`, `~/.hermes/memories/MEMORY.md`, and configured `display.personality` / `agent.system_prompt` layers.

## Core model

Treat persona context as distinct layers:

- SOUL.md: stable agent identity, voice, behavioral boundaries, and operating principles. Keep it compact and behaviorally actionable.
- USER.md: durable facts about the user, preferences, recurring conventions, and stable working context.
- MEMORY.md: hot operational cache. Keep only facts that materially improve nearly every session: active configuration, tool quirks, critical paths, high-stakes preferences, and current system conventions.
- QuickThoughts: warm storage for durable ideas, philosophy, research, session outcomes, and long-term context that does not need injection into every prompt.
- GBrain: searchable indexed storage populated by the QuickThoughts sync pipeline.
- Configured personality: an additional style/system-prompt layer. Audit it for conflict with SOUL.md before changing either file.

## Review procedure

1. Read the live `~/.hermes/SOUL.md` and measure its size. Do not assume the bundled Docker/template SOUL is active.
2. Inspect `config.yaml` for `display.personality` and `agent.system_prompt`; these can add a second persona layer.
3. Inspect `USER.md` and `MEMORY.md` separately. Do not merge their responsibilities.
4. Classify each line as identity, user preference, hot operational fact, warm long-term knowledge, or stale status/task history.
5. Remove completed-work/status notes from hot memory instead of archiving them as permanent facts.
6. Before removing a durable concept from hot memory, capture a concise version through the canonical QuickThoughts `note` CLI, then verify the persisted entry.
7. Only then remove or compress the hot-memory entry with the memory tool.
8. Re-read the resulting file and report measured size/usage. Never claim an optimization without verifying the write.

## Token discipline

Optimize semantics before shaving characters. A 1 KB SOUL is usually acceptable if every line changes behavior. The highest-value reductions usually come from:

- deleting completed-work notes;
- moving non-every-session philosophy and research to QuickThoughts;
- removing redundant implementation detail;
- eliminating conflicting duplicate personality prompts;
- retaining canonical paths, active preferences, and safety-critical tool quirks.

Do not move core behavioral identity out of SOUL merely to reduce byte count. Do move philosophical or historical context out of MEMORY when it is not needed on every turn.

## Personality conflict check

If SOUL.md establishes a deliberate identity but `display.personality` selects a stock persona (for example, playful, catgirl, pirate, or hype), flag the collision. Prefer one coherent persona source. Do not silently overwrite the user's intended style; present the conflict and proposed resolution before changing configuration unless the user explicitly authorizes the change.

## Safety and verification

- Never directly rewrite QuickThoughts.txt; use the append-only `note` workflow.
- Do not edit USER.md while reviewing MEMORY.md unless the user explicitly expands scope.
- Keep SOUL, USER, and MEMORY changes separate and auditable.
- Use the runtime file under `~/.hermes/` as the source of truth; bundled files under the Hermes repository may be templates or fallback content.
- After edits, verify file contents, byte/line counts, memory usage, and any relevant config values.

## Supporting detail

See `references/persona-layering-review-july-2026.md` for the first session-tested review pattern and observed layering conflict.
