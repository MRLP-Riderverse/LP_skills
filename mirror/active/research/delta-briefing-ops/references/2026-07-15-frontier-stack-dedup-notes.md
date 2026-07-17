# Frontier Stack Dedup Notes — 2026-07-15

This reference captures the current delta-briefing workflow and source-map details observed during the July 15 run.

## Dedup protocol that worked
- Use session_search to find the most recent briefing session for the topic.
- Treat the most recent rendered cron output as the canonical delivered brief when it exists.
- Use the last 3 briefings as the staleness window.
- If a source area has no verified new item in the window, leave it silent instead of rephrasing older items.
- Keep the final brief short, bullet-only, and English-only.

## Current source map and extraction notes
### Solana
- Primary feed: https://solana.com/news/rss.xml
- Also useful: https://solana.com/rss.xml
- GitHub releases/commits: https://github.com/anza-xyz/agave/releases and recent commits
- RSS titles use CDATA; pubDate uses GMT suffix.
- Current verified items in the latest cycle:
  - Agave v4.1.2 stable and v4.2.0-beta.1
  - July 9 Solana changelog
  - $SKHY launch on Solana

### Ollama
- Blog: https://ollama.com/blog
- Releases: https://github.com/ollama/ollama/releases
- Blog RSS can lag or return empty; GitHub releases/commits are the safer primary signal.
- Current verified items in the latest cycle:
  - v0.31.2 release
  - commit work on actionable web auth errors and Gemma4 template alignment

### LangGraph
- Releases: https://github.com/langchain-ai/langgraph/releases
- Commits: https://github.com/langchain-ai/langgraph/commits
- Current verified item in the latest cycle:
  - v1.2.9 release
  - sdk-py cron end_time clearing via update(end_time=None)

### x402 / Open Wallet Standard / OpenJarvis
- x402 commits often carry the freshest signal; release cadence may lag.
- OWS release notes are a primary source for provenance / publishing / chain-support changes.
- OpenJarvis commit stream is worth checking every run; it often has more signal than traditional “core” repos.
- Current verified items in the latest cycle:
  - x402 XRPL onboarding/docs/facilitator expansion
  - OWS provenance and trusted-publishing hardening in prior cycle
  - OpenJarvis model-list refresh and async streaming work

### Sovereign-builder / local-first
- Simon Atom feed: https://simonwillison.net/atom/everything/
- Matt Webb feed: https://interconnected.org/home/feed
- Oxide feed: https://oxide.computer/blog/feed
- Oxide is active again after the quiet spell; do not treat it as dormant.
- Current verified items in the latest cycle:
  - Simon on DRI + small deterministic tooling
  - Matt on voice interfaces that stay on task
  - Oxide: Performance Has Layers (reopened signal)

## Briefing shape reminder
- What's new
- What changed
- Cross-stack signal
- Actionable

## Delivery reminder
- The brief itself must be the final output.
- No summary line after the brief.
- If there is no delta across all sources, return exactly [SILENT].
