# Cron Delivery Truncation Bug — 10 Jun 2026

## What happened
The frontier-stack-morning-brief cron (`801ddb3a905f`) ran at 05:54 and generated a full ~9KB briefing (message ID 37980 in session `cron_801ddb3a905f_20260610_054520`). The agent then emitted a SECOND assistant message (ID 37982): *"Briefing delivered. All five sources fetched and cross-referenced..."* — a 1-line closing summary.

The delivery system captured the **last** assistant message as the final output. The saved file (`2026-06-10_05-54-40.md`) was only **1,752 bytes** vs. the usual 8,000-10,000+. The full briefing was in the session but never delivered.

## Evidence
- Saved output: `~/.hermes/cron/output/801ddb3a905f/2026-06-10_05-54-40.md` (1,752 bytes)
- Previous day: `2026-06-09_06-06-29.md` (8,893 bytes)
- Session transcript: full briefing at message 37980, closing message at 37982
- User reported: "it said 'read through all 5….' but only sent me a mini paragraph"

## Root cause
The `z-ai/glm-5.1` model on long multi-tool cron runs tends to "wrap up" after producing a large output. This wrap-up message becomes the final assistant response. The Hermes cron delivery system saves/delivers only the **last** assistant message in the session.

## Fix applied
1. Updated cron prompt for `801ddb3a905f` to explicitly state: "Your briefing IS your final response. Do NOT add any follow-up, summary, or 'Briefing delivered' message after the briefing."
2. Added pitfall #16 to `frontier-stack-evaluation` SKILL.md
3. Updated `references/daily-tech-briefing-template.md` with cron delivery rules

## Same-session observation: Music brief language contamination
The music-artist-monitor weekly brief (`678966b39112`, same morning) delivered fully (19,294 bytes) but contained entire duplicated table sections in Dutch ("Web3 Muziek", "Impact op onafhankelijke artiesten"). Source: Dutch ForkLog content bled into context and the model mirrored the table structure in Dutch.

Fix: Added pitfall #17 (language contamination) and #18 (Telegram table stripping) to `frontier-stack-evaluation` SKILL.md. Also updated music brief cron prompt to enforce English-only and bullet lists instead of tables.

## Pattern to watch
This is likely a `z-ai/glm-5.1` model behavior — it tends to produce a "closure" message after large outputs in cron contexts. The fix is prompt-level (explicit instruction), not system-level. If the model changes, re-test whether the closure behavior persists.
