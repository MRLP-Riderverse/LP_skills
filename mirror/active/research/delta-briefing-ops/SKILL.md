---
name: delta-briefing-ops
description: "Operate delta-only cron-delivered technology briefings: dedup against prior runs, probe primary sources, and deliver concise English-only bullet briefs with strict no-rehash rules."
---

# Delta Briefing Operations

Use this skill for scheduled or recurring technology briefs that must be **delta-only**: only report genuinely new items since the last delivery, with strict deduplication and a compact final format.

## Trigger
- User asks for a daily/weekly tech briefing
- Cron job must emit only new items since the last brief
- Briefing must be delivery-safe for Telegram / chat systems
- Need to compare current source activity against recent prior sessions

## Core rules
- Read the **last delivered brief** before drafting.
- Treat anything reported in the last **3 briefings** as stale unless there is a concrete new development.
- Prefer **primary sources**: feeds, release notes, GitHub releases/commits, official blogs.
- If nothing meaningful is new, output exactly **[SILENT]**.
- The briefing itself must be the **final output**; never append a summary or delivery note.
- Write in **English only** and use **bullet lists**, not tables.
- For crypto/week-in-review work, bias toward protocol/operator sources before media: Ethereum Foundation, EthResearch, Vitalik, Bitcoin Optech / Bitcoin Core, GitHub releases, DeFiLlama, and L2Beat.

## Workflow
1. **Find the previous brief**
   - Use session search for the briefing topic.
   - Open the most recent relevant session and read around the anchored brief message.
   - Do not trust the session title alone; the actual delivered brief can be embedded in a later maintenance/debug session.
   - Treat the delivered brief as the source of truth for dedup, not the existence of a generated-but-not-delivered draft.

2. **Establish the delta window**
   - Default to 7 days for fast-moving infra.
   - Extend to 14 days for slower essays/blogs.
   - Narrow the window if repeated items are likely to recur.
   - When a cron job renders a brief, treat the latest cron output artifact as the canonical delivered version for dedup/verification if it exists.

3. **Probe sources in priority order**
   - Feeds / RSS / Atom
   - GitHub releases
   - GitHub commits when releases lag
   - Article pages for context after the dated item is confirmed
   - Homepage scan only as a fallback
   - For sources with sparse output, prefer a real silence over widening the window invisibly.

4. **Filter hard**
   - Discard items already covered in the last 3 briefs.
   - Keep follow-ups only if they materially change the assessment.
   - Do not re-confirm known dormancies.
   - If a topic has no verified delta in the current window, leave it out rather than paraphrasing old news.

5. **Synthesize for action**
   - Reduce the result to a few bullets.
   - Prefer implication over description.
   - Include dates and URLs for every item.
   - Group by theme when multiple new items point at the same operational lesson.

6. **Delivery discipline**
   - The briefing itself must be the final assistant message.
   - Never append a closing sentence, recap, or delivery note after the brief.
   - Use bullet lists, not tables.
   - Write the entire brief in English only.

See `references/2026-07-06-session-notes.md` for the latest retrieval/dedup quirks and source-specific notes from a real delta run.
- See `references/2026-07-11-frontier-stack-probe-notes.md` for fresh source-specific notes: Solana RSS, Agave prerelease labeling, Ollama RCs, LangGraph CLI vs core, x402 PR-body-first verification, and Simon cloud/local boundary signals.

## Output shape
Default brief:
- **What’s new:** genuinely new items only
- **What changed:** updates to previously reported items
- **Cross-stack signal:** one pattern from the cycle’s new data
- **Actionable:** 1–3 concrete moves based only on new information

If there is no meaningful delta across all sources:
- return exactly **[SILENT]**

## Pitfalls
- Do not add a closing line after the briefing; delivery systems often capture only the last assistant message.
- Do not use markdown tables for chat-bound delivery.
- Do not duplicate sections in multiple languages.
- Do not rely on alias resolution for tools/skills; use the canonical skill name when a tool requires one.
- Treat provider throttles during synthesis as a runtime issue, not a source failure: retry once, then simplify or split collection vs synthesis.
- If the previous brief is embedded in a later debug session, use the message window around the anchor to recover it.

## Support files
- `references/2026-07-06-session-notes.md` — latest probe notes, dedup retrieval quirks, and source deltas.
- `references/2026-07-11-frontier-stack-probe-notes.md` — fresh source-specific notes: Solana RSS, Agave prerelease labeling, Ollama RCs, LangGraph CLI vs core, x402 PR-body-first verification, and Simon cloud/local boundary signals.
- `references/2026-07-15-frontier-stack-dedup-notes.md` — current verified source map, dated feed endpoints, and dedup lessons from the July 15 delta run.
- `references/crypto-weekly-briefing-2026-07-13.md` — source map and endpoint notes for Ethereum / Bitcoin / L2 weekly briefings (feeds, release notes, TVL APIs, and repo scans).

## Relationship to other skills

