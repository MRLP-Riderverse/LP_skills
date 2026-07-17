# Tail vs Read Scaling Notes

This note-capture workflow has two different read shapes:

## Use tail-style reads for
- verifying the newest QuickThoughts entry
- checking formatting/separators after capture
- showing the recent-note preview in the UI
- quick glance/lookback workflows where only the last few entries matter

## Use full reads for
- recap generation
- monthly archive jobs
- focused search across the whole inbox when the query spans history
- audits that need the complete file content

## Why this matters
QuickThoughts is append-only and grows over time. Most human-visible checks only need the newest note, so full-file scans become avoidable overhead. A bounded tail window is usually enough for:
- recent preview
- capture verification
- last-entry formatting checks

## Recommended implementation pattern
1. Keep `note` capture append-only.
2. Add a tail-based helper for recent entries (bounded byte window + backward scan for timestamp lines).
3. Optionally cache recent preview data by file mtime.
4. Leave recap/archive/search paths as full scans until they show measurable pain.
5. If the inbox grows a lot, add a tiny index instead of widening the default read.

## Practical rule
If the question is "did the last capture look right?", read the tail.
If the question is "what does the whole inbox say?", read the file.
