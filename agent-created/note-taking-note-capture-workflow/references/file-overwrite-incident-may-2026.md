# File Overwrite Incident — Late May 2026

## What happened

The QuickThoughts.txt file was overwritten twice in late May 2026, destroying months of accumulated notes. By May 31, the file contained only that day's entries — everything from prior weeks and months was gone.

## Timeline

1. **April 19** — First crash. The notecore UI was patched, QuickThoughts corrupted. A reconstructed backup was saved at `.auto_backups/QuickThoughts_backup_20260419_183939.txt` (46KB, 626 lines). The auto-backup script was set up but only ran once.

2. **May 5** — Manual backup made: `QuickThoughts.txt.backup2` (24KB, 332 lines). This captures the state after the April reconstruction but before the second hit.

3. **May 25, ~19:33** — The QuickThoughts.txt file was deleted and recreated from scratch (new inode 9047258). The old 690+ line file was replaced. The trigger was likely a Hermes session using `write_file` instead of `note` CLI. Evidence: file birth timestamp is May 25 19:33, while the recap file was also created at 19:26-19:27 that day — same session window.

4. **May 25-30** — The `note` CLI correctly appended new entries to the freshly created empty file, rebuilding content day by day.

5. **May 30-31** — During a GPT transfer report skill testing session (memory offload + label testing), something overwrote the file AGAIN. The May 25-30 entries were wiped. Only entries captured on May 31 survived because they were appended after the last overwrite.

6. **May 31** — User discovered the file had only ~13 lines / 3KB, all from today. Expected ~1000 lines / ~100K+ characters.

## Root cause

**Hermes used `write_file` (full file replacement) instead of `note` CLI (append-only) to write captured notes.** This is the same class of bug as the earlier "patch on open file" incident, but more destructive because:

- `write_file` replaces the ENTIRE file with no append mode, no backup, no undo
- The auto-backup script had only run once (April 19) — no backups existed for May
- The file had no git history (not under version control)
- The inode recreation (new file vs modified file) means even filesystem-level recovery tools cannot find the old content

## Why it happened

- The agent was in a long session with compaction, losing the "always use note CLI" constraint from earlier in the same session
- Memory offload + GPT transfer report were new workflows being tested simultaneously
- The `gpt-transfer-report` skill correctly specifies `note` CLI usage, but the agent used `write_file` during the memory offload step instead
- The `write_file` tool has no guardrail preventing it from targeting QuickThoughts.txt

## Recovery sources

| Source | Coverage | Format |
|--------|----------|--------|
| GBrain daily pages (May 2-30) | Complete — 20 daily pages | Markdown with raw ⁜ entries |
| Auto-backup (April 19) | Pre-crash data (626 lines) | Raw file copy |
| backup2 (May 5) | Post-reconstruction partial | Raw file copy |
| Pipeline windows (March-April) | Earlier data | Date-windowed extracts |

**GBrain was the only recovery source for May 5-30 data.** The 2AM daily sync cron had been running and created one page per day. Without GBrain, the May data would have been permanently lost.

## What the user said

"its like my routing policy doesnt work anymore as intended.. wtf... something must have happened during yesterday's chat when we made a new tweak for our gpt transfer report"

"im now talking about the data from after our corrupted repairs and just before today.. like you and i were pounding away at notes for the last few weeks... what happened?"

The user specifically noted the irony: the routing policy (the `note-capture-workflow` skill itself) was designed to prevent exactly this, but something bypassed it during the same session where they were testing the new GPT transfer workflow.

## Corrective actions

1. Added `write_file` as the #1 most dangerous tool in the `note-capture-workflow` Core Rule
2. Added dedicated "CRITICAL PITFALL: write_file on QuickThoughts.txt" section with explicit STOP instruction
3. Added full recovery procedure (9 steps) to the skill
4. Added this reference file for future sessions
5. Updated the existing "File already open shortcut bias" pitfall to include `write_file` variant
6. Patched `gpt-transfer-report` skill with explicit `write_file` prohibition

## Lesson

The `write_file` tool on an append-only file is a category error — like using `rm` when you mean `touch`. The `note` CLI exists specifically because QuickThoughts must never be fully replaced. Any future session that touches QuickThoughts MUST load `note-capture-workflow` first, and any tool call targeting QuickThoughts.txt with `write_file` should be treated as a hard stop.
