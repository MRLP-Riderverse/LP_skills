# Exact Counting and Routing

## Counting rule

GBrain retrieval is for recall, not exact arithmetic. For a topic/media/entity count:

1. Search GBrain for candidate pages and index coverage.
2. Scan canonical `~/brain/sources/` Markdown files with a deterministic, case-insensitive matcher.
3. Parse entry boundaries rather than counting matching lines when possible.
4. Deduplicate overlapping daily pages and raw snapshots by timestamp plus normalized body.
5. Report matched rows, unique entries, unique dates, and extracted entities separately.
6. Treat explicit preference language as distinct from positive reaction or repeated exposure.

## Routing rule

Keep QuickThoughts append-only and raw. Use literal provisional markers as breadcrumbs, then derive organized files without deleting or rewriting the source. Minimum source classes:

- human reality/status
- pulse/activity/friction/endday observations
- tasks and someday items
- development/system notes
- Hermes summaries
- cron/sync status
- research or GPT-transfer material

Every derived record should retain its source path, timestamp, and original text or a reversible pointer. Parser changes should be able to regenerate the derived collection.

## Interpretation rule

Separate direct observation from inference. Report sparse coverage, automation contamination, burst-day effects, and the difference between captured activity and total activity. Use hypotheses about state transitions rather than deterministic personality or capacity claims.
