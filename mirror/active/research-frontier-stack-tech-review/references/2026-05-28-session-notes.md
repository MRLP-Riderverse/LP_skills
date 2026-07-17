# 2026-05-28 session notes

## Source behavior observations
- Solana news RSS updated (lastBuildDate May 27). Chiliz/sports on Solana (May 27) is the only new item in the 7-day window; rest is Bits to Bricks podcast episodes from May 18-20.
- Agave v4.0.0 stable since May 16; v4.1.0-beta.1 on testnet since May 22 — fast cadence continues.
- Ollama v0.24.0 shipped May 14 (stable) — adds Codex App support, MLX sampler rework, model recommendations. v0.30.0-rc28 (pre-release since May 13) continues the major architecture shift track. Blog RSS stale (latest March 30); GitHub releases are primary signal.
- LangGraph 1.2.2 shipped May 26 — stable ID fix for DeltaChannel checkpoint writes. 1.2.1 (May 21) added `before_builtins` for stream transformers. SDK 0.3.15 and checkpoint 4.1.1 also released May 22.
- x402 had no tagged releases; very active commits on May 27 (6+ commits): Solana cache dedup, Aptos gas price vuln fix, ERC-6492 factory call fix, Bazaar middleware validation, Python service metadata. Commit activity remains the only freshness signal.
- Open Wallet Standard: no new releases since v1.3.2 (Apr 20); no commits in 7-day window. OWF blog active: GDC Task Forces and KEYRING posts from May 21.
- Simon Willison: extremely prolific (May 19-27). Dominant themes: AI security/safety (curl pressure, Copilot exfiltration, coding agent shields-up), OSS maintainer defense (SQLite AGENTS.md, Armin Ronacher slop issues), enterprise pricing PMF analysis. Datasette approaching 1.0; datasette-agent launched May 21.
- Matt Webb: Resident post (May 20) confirmed as top sovereign-builder item. No new posts since.
- Oxide blog: still dormant since Feb 2026 ($200M Series C). RFDs unverifiable via scraping (React SPA).
- Ink & Switch: Tenfold Playground (May 18) and Progressions notebook (May 12). Lab Day at Local-First Conf July 14.
- Automerge: fragments pre-releases (3.3.0-fragments.0/.1 on May 20-21) — new CRDT feature.
- Yjs: v14.0.0-rc.17 released May 26 — approaching stable major version.

## Synthesis pattern
- Cross-stack pattern: "sandbox as sovereign primitive" continues — x402's Bazaar middleware validation, Matt Webb's Resident Lua sandbox, and SQLite's AGENTS.md all treat constrained execution environments as the answer to autonomous AI safety.
- AI security is the dominant sovereign-builder theme for the second consecutive week — the defense posture is now formalizing (AGENTS.md, Copilot exfiltration patches, OSS maintainer pushback).
- Solana's real-world use case narrative hardens: sports/fan tokens + merchant settlement + Pay.sh/Google Cloud = stablecoin payments stack becoming concrete.
- Ollama v0.24.0 with Codex App support is significant: local-first coding agent now has a desktop app with browser annotation and review mode — reduces dependence on cloud coding agents.
- LangGraph's checkpoint stability improvements (stable IDs in 1.2.2) directly serve crash-resume patterns that sovereign builders need.
