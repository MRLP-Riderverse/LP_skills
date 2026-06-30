# Export `.ics` DTSTAMP churn

## Symptom
Running `python3 scripts/export_to_site.py --all --site ...` rewrites `assets/calendar/*.ics` even when no event source changed.

Typical diff:

```diff
-DTSTAMP:20260619T015604Z
+DTSTAMP:20260619T235028Z
```

## Cause
In `acadie_sol_directory/scripts/export_to_site.py`, `write_calendar_files()` emits:

```py
f"DTSTAMP:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
```

That makes calendar output nondeterministic: every export run changes the file contents.

## Operational rule
Until the exporter is made deterministic, treat `DTSTAMP`-only `.ics` diffs as noise:

1. Inspect `git diff -- assets/calendar/*.ics`
2. If the only changes are `DTSTAMP` lines, revert them before committing the site repo
3. If event fields like `SUMMARY`, `DTSTART`, `DTEND`, `DESCRIPTION`, or `LOCATION` changed, keep the `.ics` update

## Better long-term fix
Prefer one of these when doing a cleanup pass:

- derive `DTSTAMP` from stable event/source modification time instead of `datetime.now()`
- or compare generated content to the existing file and only rewrite when the meaningful body changed

This keeps export commits readable and prevents timestamp-only calendar churn from polluting site publishes.
