---
name: quickthoughts-daily-sync
description: Deterministic daily sync of QuickThoughts to GBrain with Telegram reports
version: 1.0.0
author: MidnightRider.sol
license: MIT
schedule: "0 2 * * *"  # Daily at 2:00 AM Atlantic Time
metadata:
  hermes:
    tags: [quickthoughts, gbrain, automation, sync, telegram, daily]
    related_skills: [note-capture, gbrain-raw-import, note-routing-policy]
    cron_job_name: daily-quickthoughts-sync
---

# QuickThoughts Daily Sync

Automatically review the previous completed day’s QuickThoughts entries, build per-day markdown blocks for GBrain, and send a Telegram status report.

## Features

- **Previous-Day Review**: Processes the last completed local day, not the live partial day
- **Missed Days Handling**: Automatically syncs any unsynced completed days
- **Daily Grouping**: Creates one `quickthoughts-YYYY-MM-DD.md` file per day
- **Deterministic Index Blocks**: Produces local markdown blocks without depending on cloud models
- **Telegram Status**: Sends concise Telegram summaries
- **Stateful**: Tracks last reviewed day to avoid duplicates

## Architecture

```
QuickThoughts.txt (source of truth)
    ↓
[sync.py script]
    - Reviews the previous completed day
    - Creates dated .md files in ~/brain/sources/
    - Runs gbrain import --no-embed
    - Sends Telegram report
    - Updates state file
    ↓
GBrain (indexed & searchable)
Telegram (status summary)
State file (prevents duplicates)
```

## Usage

### Manual Sync

```bash
# Normal sync (checks if already synced today)
hermes skill run quickthoughts-daily-sync

# Force sync (even if already synced today)
hermes skill run quickthoughts-daily-sync --force

# Dry run (show what would be synced)
hermes skill run quickthoughts-daily-sync --dry-run

# Check status
hermes skill run quickthoughts-daily-sync --status

# Reset state (clear last sync date)
hermes skill run quickthoughts-daily-sync --reset
```

### Cron Job (Automatic)

The skill runs automatically via cron at **2:00 AM Atlantic Time** daily.

```bash
# View cron job
hermes cron list

# Job name: daily-quickthoughts-sync
# Schedule: 0 2 * * * (daily at 2 AM AST)
# Delivery: Telegram (to your home channel)
```

## Configuration

### State File

Location: `~/.hermes/state/quickthoughts-sync-state.json`

```json
{
  "last_sync_date": "2026-04-20",
  "last_sync_timestamp": "2026-04-20T02:00:01-03:00",
  "total_entries_synced": 47,
  "last_report_sent": "2026-04-20T02:00:15-03:00"
}
```

### Local Model

The default workflow does not require any model configuration.
If a future variant uses a local model, keep it optional and offline-only.

### Telegram Delivery

Uses `telegram-notify` command.

## Report Format

### Success Report
```
🧠 QuickThoughts Sync - 2026-04-20

✅ 4 entries imported to GBrain

Themes:
• OpenCode exploration
• UI/interface tools (Thunderbolt, OpenWebUI)
• Workflow memory (LangGraph, LangChain)

Action:
• Review browser harness
• Test OpenWebUI

Mentioned:
• Jasper
• DRiP
• ExoAgent

Sync: 02:00 AST ✅
```

### No New Entries
```
🧠 QuickThoughts Sync

ℹ️ No new entries since last sync (2026-04-20)

Next sync: Tomorrow, 2:00 AM AST
```

### Failure Report
```
🧠 QuickThoughts Sync - FAILED ❌

Error: GBrain import failed: database locked

Last successful sync: 2026-04-19

Run manually: hermes skill run quickthoughts-daily-sync --force
```

## Failure Handling

If the sync hits an error:
- log the failure in the cron output
- keep the state file unchanged
- rerun after fixing the underlying local issue
- avoid adding extra external dependencies

## File Structure

```
~/.hermes/skills/note-taking/quickthoughts-daily-sync/
├── SKILL.md                 # This file
├── scripts/
│   └── sync.py             # Main sync script
├── templates/
│   └── telegram_report.md  # Report template (optional)
├── tests/
│   └── test_sync.py        # Unit tests
└── references/
    ├── USAGE.md            # Detailed usage guide
    ├── cron-scan-pitfalls.md
    └── robustness-notes.md  # Session-tested reliability lessons
```

## Troubleshooting

### Cron prompt-scan pitfall

If this skill is loaded into a cron job and the job is blocked *before execution*, check the generated cron output first. A common cause is the prompt scanner rejecting literal secret-file inspection examples in the skill text.

- Keep cron-loaded prompt text free of sensitive-file examples unless absolutely required.
- Prefer narrow, non-sensitive inspection examples or generic wording.
- See `references/cron-scan-pitfalls.md` for the exact blocker and safe rewrite pattern.
- See `references/robustness-notes.md` for the hardened workflow choices that came out of the 2026-05 reliability pass.

### Issue: "Already synced today" but entries missing

**Cause**: State file says today was synced, but GBrain doesn't have the file

**Fix**:
```bash
# Check state
python -m json.tool ~/.hermes/state/quickthoughts-sync-state.json

# Force re-sync
hermes skill run quickthoughts-daily-sync --force

# Or reset state entirely
hermes skill run quickthoughts-daily-sync --reset
```

### Issue: Ollama not responding

**Cause**: This workflow does not require Ollama.

**Fix**:
- Ignore this for the default job
- Only troubleshoot a local model if you explicitly switch to a model-backed variant

### Issue: GBrain import fails

**Common causes**:
- Database locked by another process
- Sources folder missing
- File permissions

**Fix**:
```bash
# Check GBrain status
~/.bun/bin/gbrain stats

# Check sources folder exists
ls ~/brain/sources/

# Kill stale GBrain processes
pkill -f gbrain

# Re-run sync
hermes skill run quickthoughts-daily-sync --force
```

### Issue: Telegram not receiving reports

**Cause**: `telegram-notify` not configured or bot token missing

**Fix**:
```bash
# Test telegram-notify
telegram-notify "test"

# Inspect Telegram env settings
grep -n TELEGRAM ~/.hermes/.env
```

### Issue: Skill missing after curator prune

**Cause**: The curator's LLM review pass can move skills into `~/.hermes/skills/.archive/` without updating cron job references. This has happened repeatedly (June 5 and June 8, 2026). The sync cron may fail silently if its skill path is archived.

**Fix**:
```bash
# Check if skill is in archive
ls ~/.hermes/skills/.archive/note-taking-quickthoughts-daily-sync/ 2>/dev/null

# Restore if found
mv ~/.hermes/skills/.archive/note-taking-quickthoughts-daily-sync ~/.hermes/skills/note-taking/quickthoughts-daily-sync
hermes curator pin quickthoughts-daily-sync
```

**Prevention**: Pin this skill with `hermes curator pin quickthoughts-daily-sync` to prevent future pruning. See `gbrain-operations` skill → `references/curator-prune-safety.md` for full audit and restore procedures.

## Edge Cases

| Scenario | Handling |
|----------|----------|
| No new entries | Skip import, send "no new entries" report |
| GBrain import fails | Log to cron output, keep state unchanged, rerun after fix |
| Local model unavailable | Not applicable in the default workflow |
| Multiple days missed | Sync all missed completed days in one batch |
| QuickThoughts file missing | Send alert, skip sync, log error |
| Cron job fails | Fix the local issue and rerun |

## Testing

### Unit Tests

```bash
cd ~/.hermes/skills/note-taking/quickthoughts-daily-sync
python3 tests/test_sync.py
```

### Manual Test

```bash
# Add test entry to QuickThoughts
note "Test entry for sync validation"

# Run sync
hermes skill run quickthoughts-daily-sync --force

# Verify in GBrain
~/.bun/bin/gbrain search "Test entry for sync validation"

# Check state file
python -m json.tool ~/.hermes/state/quickthoughts-sync-state.json
```

## Related Automations

### Daily session review notes

A related local-first cron workflow reviews yesterday's Hermes and OpenCode sessions, summarizes them with local Ollama `qwen3:8b`, and appends durable topic blocks through the canonical `note` command. See `references/daily-session-review-notes.md` for the current script path, cron job ID, OpenCode DB notes, and the important Qwen3 `think:false` Ollama pitfall.

## Related Skills

- **note-capture**: How notes get into QuickThoughts initially
- **gbrain-raw-import**: Manual import workflow (this skill automates it)
- **note-routing-policy**: Deciding what stays local vs goes to cloud
- **telegram-notifier-tool**: Sending reports to Telegram

## Future Improvements

1. **Smart Batching**: If >100 entries, batch by week instead of day
2. **Trend Analysis**: Weekly/monthly summaries of themes and patterns
3. **Auto-Tagging**: Suggest tags for GBrain pages based on content
4. **Conflict Detection**: Warn if same topic appears frequently without resolution
5. **Export Options**: Generate weekly PDF/Markdown summaries

## Philosophy

**"Set it and forget it"** - The goal is zero-maintenance daily sync. You write notes naturally, the system handles the rest. No manual imports, no forgotten entries, no duplicate work.

**Local-first, privacy-preserving** - The default workflow stays on-device and avoids external model dependencies. Raw notes stay in your local GBrain.

**Fail closed** - When a run fails, keep the state unchanged and retry after the local issue is fixed.

**GBrain is the safety net** - In late May 2026, QuickThoughts.txt was overwritten by a `write_file` call during a Hermes session, destroying ~690 lines / ~46KB of accumulated notes. The auto-backup script had only run once (April 19). The ONLY recovery source for May 5-30 data was the GBrain daily pages created by this sync cron. If the cron had not been running daily at 2AM, the data would have been permanently lost. This is why the daily sync matters — it's not just for searchability, it's the last line of defense against file-level data loss.

---

**Created:** 2026-04-20  
**Last Updated:** 2026-04-20  
**Tested On:** GBrain v0.12.3, Ollama v0.1.x, QuickThoughts (Notecore)
