# 2026-05-29 session notes

## Source behavior observations
- Solana news RSS updated (lastBuildDate May 27). Only new item in 7-day window: Chiliz/sports on Solana (May 27). Rest is Bits to Bricks podcast episodes (May 18-20).
- Agave v4.1.0-beta.1 shipped May 22 (testnet); v4.0.0 stable since May 16. Fast cadence continues.
- Ollama v0.24.0 stable since May 14 (Codex App support). v0.30.0-rc29 continues the major architecture shift. Blog RSS now shows "OpenJarvis: a local-first personal AI" post dated May 28 — first blog update since March.
- LangGraph SDK 0.4.0 released May 28 — major SDK update with websocket streaming, reconnect hardening, sync subgraphs, thread stream helpers. LangGraph 1.2.2 (May 26) fixes stable IDs for DeltaChannel. CLI 0.4.27 also May 28.
- x402 extremely active: 10+ commits May 27-29. Key items: simulation-based smart wallet verification, Bazaar service metadata, ERC-6492 factory call fix, Aptos gas price vuln fix, Solana cache dedup. No tagged releases.
- Open Wallet Standard: no new releases since v1.3.2 (Apr 20). NEAR Protocol chain support merged May 5 (Ed25519 + Borsh + NEP-413) — last commit in window but just outside 7-day.
- Simon Willison: datasette 1.0a31 (May 29) adds write SQL queries and stored queries. Claude Opus 4.8 review (May 28). SQLite AGENTS.md (May 27). Copilot Cowork file exfiltration (May 26). curl pressure (May 26). Vatican encyclical on AI (May 25). Datasette Agent launch (May 21). Memory shortage repricing (May 22).
- Matt Webb: Resident (May 20) remains top item. No new posts since.
- Oxide blog: still dormant since Feb 2026.
- Ink & Switch: Dispatch 017 (May 28), bijou64 (May 26), Tenfold Playground (May 18).
- Automerge: Fragments prereleases (3.3.0-fragments.0/.1 May 20-21).
- Yjs: v14.0.0-rc.17 (May 26), v13.6.31 stable (May 28) with undo+setAttribute+delete data corruption fix.

## Synthesis pattern
- Cross-stack pattern: "sandbox as sovereign primitive" continues to strengthen — x402 Bazaar middleware validation, Matt Webb's Resident Lua sandbox, SQLite AGENTS.md, and Ink & Switch's bijou64 all reinforce constrained execution as the answer to autonomous AI safety.
- AI coding agents hitting critical mass: Willison argues PMF found via Claude Code/Codex; Datasette Agent is the sovereign self-hosted answer; Ollama blog now features OpenJarvis (local-first personal AI).
- LangGraph SDK 0.4.0 is a major release for sovereign builders: websocket streaming, reconnect hardening, and sync subgraphs directly serve crash-resume and offline-capable agent workflows.
- Solana narrative hardening: sports/fan tokens + smart wallet verification on x402 = payments stack becoming concrete.
- CRDT ecosystem maturing: bijou64 eliminates canonicalisation attack surface; Yjs v14 RCs accelerating; Automerge Fragments approaching partial doc sync.
