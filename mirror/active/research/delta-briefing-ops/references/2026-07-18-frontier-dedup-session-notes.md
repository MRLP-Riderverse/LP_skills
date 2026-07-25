# 2026-07-18 Frontier Delta Dedup Notes

## Retrieval lesson

The required topic query can return an unrelated conversational session instead of the newest cron delivery. When that happens:

1. Browse recent sessions without a query.
2. Locate sessions titled like `frontier-stack-morning-brief · <date>`.
3. Read the newest session directly.
4. Treat a session containing only the cron prompt as an empty/failed attempt, not as a delivered brief.
5. Continue backward until finding assistant content, then read the last three delivered briefs for dedup.

This distinction matters: deduplication must be based on what the user actually received, not on a job that started or on a draft that was generated but never delivered.

## Probe lesson

For a fast-moving frontier stack, combine:

- Solana RSS for dated ecosystem/changelog items.
- GitHub release APIs for Ollama, LangGraph, and Agave; check `prerelease` before calling a release stable.
- GitHub commit APIs for OpenJarvis, x402, and Open Wallet Standard when tagged releases lag.
- Simon Willison and Matt Webb feeds for dated essays and tooling posts.

Use release/commit bodies for the actionable sentence, but keep the final brief to the smallest set of genuinely new items.

## Output lesson

When a source has no qualifying change, omit it or mark the relevant section silent; do not re-confirm a known dormant source. The final cron response must end with the briefing itself, with no delivery note appended.
