---
name: cron-delta-briefing
description: Run recurring cron-delivered briefings in delta-only mode with dedup against prior outputs, strict output hygiene, and [SILENT] fallback.
category: devops
---

# Cron Delta Briefing Workflow

Use this skill for recurring scheduled briefings where the final deliverable should contain only genuinely new information since the last run.

## Trigger
- Scheduled daily/weekly briefing jobs
- Any cron-delivered report where repeated items must be suppressed
- Any workflow where the delivered artifact must be concise, deduplicated, and final-response safe

## Core rules
- Always establish the previous delivered brief before drafting the new one.
- Compare against the last 3 briefings; items already reported there are stale unless the topic has a real new development.
- Prefer primary sources and dated items.
- If no meaningful change exists, return exactly `[SILENT]`.
- The briefing itself must be the final assistant response; never append a delivery note or summary.
- Use bullets, not tables, and write in English only for delivery channels that strip formatting.

## Workflow
1. **Find the baseline**
   - Use session search to locate the most recent briefing session.
   - If a delivered cron output artifact exists, read that too and use it as the baseline artifact.
   - For multi-run cycles, compare against the last 3 briefings before deciding whether a topic is stale.

2. **Deduplicate aggressively**
   - Treat items from the last 3 briefings as stale.
   - Re-include a topic only if there is a concrete new release, post, commit, or status change.
   - Quiet/dormant sources stay silent until they change.
   - If a source has already been confirmed dormant and nothing changed, do not re-confirm it.

3. **Collect only deltas**
   - Pull dated, primary-source items.
   - Keep one line of relevance per item.
   - Avoid raw research logs and unverified speculation.
   - Check the current source map reference for the freshest canonical URLs and source-specific probe notes.

4. **Synthesize the cycle**
   - Summarize the new pattern emerging from this run only.
   - Keep actionable items directly tied to the new data.

5. **Finish cleanly**
   - Final response is the briefing or `[SILENT]`.
   - No closing sentence, no recap, no "delivered" message.

## Pitfalls
- Re-reporting known quiet sources.
- Letting the output drift into a full sweep instead of a delta.
- Adding a postscript after the briefing.
- Using tables in Telegram-bound output.

## References
- See `references/delta-briefing-checklist.md` for the concise baseline + output-hygiene checklist.
- See `references/current-source-map.md` for current source map details.
- See `references/2026-07-10-frontier-stack-session-notes.md` for a current example of delta-only source handling, release-body/commit-body fallbacks, and quiet-source suppression in a frontier-stack briefing.
