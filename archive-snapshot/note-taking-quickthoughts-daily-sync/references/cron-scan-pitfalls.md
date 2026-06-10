# Cron Scan Pitfalls for QuickThoughts Sync

## What happened
The `daily-quickthoughts-sync` cron job was blocked before the agent ran because the loaded skill text contained a literal secret-file inspection example.

Observed blocker:
- `Blocked: prompt matches threat pattern 'read_secrets'`
- The scanner was triggered by an example using a secrets path in a shell snippet.

## Practical rule
When a skill is loaded into a cron job prompt, avoid literal examples that reference secrets files or other sensitive paths if they are not essential to the task.

Prefer:
- generic wording about checking env settings
- narrow, non-exfiltrating examples
- references that do not mention secret file names unless absolutely required

## Safer rewrite pattern
Prefer:
- `grep -n TELEGRAM ~/.hermes/.env`
- or just say "inspect the Telegram env settings"

## Verification clue
If a cron run is blocked before the agent executes, inspect the generated cron output file under:
- `~/.hermes/cron/output/<job_id>/...`

The failure will usually show the scanner label rather than a script/runtime error.
