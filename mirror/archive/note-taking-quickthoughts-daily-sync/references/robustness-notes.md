# QuickThoughts Sync Robustness Notes

## Why the workflow was hardened

A cron run was blocked *before execution* because the loaded skill text contained a literal secret-file inspection example. Hermes' cron prompt scanner treated it as a `read_secrets`-style risk. The fix was not to add more agent logic, but to make the prompt surface safer and the sync path more deterministic.

## Lessons encoded in the workflow

- Prefer **previous completed day** semantics for a 2:00 AM local cron job.
  - This avoids partial-day ambiguity and reduces the chance of importing an in-progress day.
- Keep the default workflow **model-optional**.
  - The sync job should not require a local model to do its core work.
- Use **atomic state writes**.
  - Write to a temp file, flush/fsync, then replace the state file.
- Avoid `shell=True` for Telegram delivery.
  - Pass argv directly to `telegram-notify`.
- Keep cron-loaded docs free of sensitive-file examples.
  - Use generic wording or safe inspection commands instead.

## Verification commands

```bash
# Check current review semantics
hermes skill run quickthoughts-daily-sync --status

# Syntax check the sync script
python3 -m py_compile ~/.hermes/skills/note-taking/quickthoughts-daily-sync/scripts/sync.py
```

## Related references

- `references/cron-scan-pitfalls.md` — safe wording patterns for cron-loaded docs
- `references/daily-session-review-notes.md` — separate local-model session-review workflow
