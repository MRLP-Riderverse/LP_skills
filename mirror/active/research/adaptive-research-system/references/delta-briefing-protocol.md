# Delta briefing protocol

Use this when producing a recurring monitoring brief.

## Source of truth for deltas
1. Find the most recent delivered brief.
2. Read the whole brief, not just the search snippet.
3. Treat items from the last 3 briefings as stale unless there is a concrete new release/post/commit/status change.

## If the search query misses
- If a query like `frontier stack daily briefing` returns no results, browse recent sessions and open the named cron run directly.
- Prefer the latest cron session title plus full-session read when the discovery query is noisy.

## Output rules
- Keep only genuinely new items.
- If a topic has no verified update, say silence for that section rather than re-explaining prior coverage.
- Use concise bullets with dates and URLs.
- For cron-delivered briefs, the last assistant message is what gets delivered, so do not append a closing summary.

## Practical watchlist pattern
- Track source-specific “alive/quiet” status once, then skip until it changes.
- Separate “new item” from “new angle on an old item.”
- Prefer primary sources and commit/release feeds over secondary summaries.
