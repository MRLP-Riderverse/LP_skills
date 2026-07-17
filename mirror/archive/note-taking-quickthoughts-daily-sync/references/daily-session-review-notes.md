# Daily Session Review Notes Workflow

Session-derived learning from building the local-first Hermes/OpenCode review cron.

## Purpose

Create durable QuickThoughts topic blocks from the previous day’s agent sessions without sending raw private logs to cloud APIs.

## Current implementation

- Script: `~/.hermes/scripts/daily_session_review_notes.py`
- Cron job: `daily-session-review-notes`
- Job ID: `a39e977fa5b0`
- Schedule: `20 2 * * *` (2:20 AM Atlantic), intentionally after the 2:00 AM QuickThoughts sync to avoid collision.
- Delivery: Telegram status report.
- Model: local Ollama `qwen3:8b`
- Sources, processed serially:
  1. Hermes session JSON files in `~/.hermes/sessions/session_YYYYMMDD_*.json`
  2. OpenCode sqlite DB at `~/.local/share/opencode/opencode.db`
- Appending: use the canonical `note` command, not direct writes to `QuickThoughts.txt`.

## Key Ollama/Qwen3 pitfall

Qwen3 models in Ollama may return content in a separate `thinking` field and an empty `response` if thinking mode is enabled. This can waste the whole output budget and look like a timeout/blank response.

Use the Ollama server endpoint directly and include top-level `"think": false`:

```json
{
  "model": "qwen3:8b",
  "prompt": "...",
  "stream": false,
  "think": false,
  "options": {
    "temperature": 0.2,
    "num_predict": 1200,
    "num_ctx": 4096
  }
}
```

This turned a blank 60s+ response into a normal response in ~2s on a tiny test, and made the full dry-run viable.

## Dry-run validation pattern

Before enabling writes, run:

```bash
~/.hermes/scripts/daily_session_review_notes.py --date $(date -d yesterday +%F) --dry-run
```

A successful dry-run should report:

- date reviewed
- chars collected per source
- note block count per source
- rendered `Notes, by Hermes : [...]` blocks

## OpenCode DB notes

OpenCode sessions are in sqlite:

```bash
sqlite3 ~/.local/share/opencode/opencode.db '.tables'
```

Important tables:

- `session`: id, title, directory, time_created, time_updated
- `part`: session_id, data, time_created
- `message`: session_id, data, time_created

Times are stored as epoch milliseconds. Query by previous local day using ms boundaries.

## Design choices

- Run sources in series, not parallel, because the local machine may not handle multiple large local model calls well.
- Treat multi-minute Qwen3 runs as normal for an overnight privacy-first job.
- Use cloud API only as an explicit fallback, not the default.
- Output topic blocks, not one monolithic summary.
- Keep each block under about 1000–1200 chars to match the user's QuickThoughts chunking preference.
- Avoid raw debugging noise; capture durable ideas, reminders, workflow updates, references, and project context.
