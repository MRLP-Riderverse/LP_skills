# 2026-06-02 session notes

## Source behavior observations
- Solana news RSS: New item Jun 1 — "Build Fully Onchain Perps on Solana". Also May 28 gold tokenization (Oro), May 27 sports/Chiliz. Ecosystem content picking up slightly vs. last briefing.
- Agave: v4.1.0-beta.2 released Jun 1 (testnet). Key backports: secondary index memory fix (#12666), RPC perf fix for stakes (#12863), tx-v1 binary encoding fix (#12591). June 2 master commits: SIMD-0232 feature key, snapshot storage rebuilder refactor, vote history reconciliation with hard forks, Alpenglow hashes_per_tick=None, safe-to-notar snapshot root fix.
- Ollama: No new releases in 7-day window. v0.30.0 (May 13, stable) remains latest — direct llama.cpp support, wider hardware/model range. Blog RSS had OpenJarvis post (May 28) but no Ollama-specific content since.
- LangGraph: Rapid release cadence continues. Jun 1: core 1.2.3 (RemoteGraph.interleave, v3 streaming, named tool-dispatched subagents, ProtocolEvent rename, config merge fix), SDK 0.4.2 (percent-encode thread_id in v3 stream), SDK 0.4.1 (stream decoders, interleave_projections, stateless tools_agent). May 28: SDK 0.4.0, CLI 0.4.27.
- x402: Three new commits Jun 2 after 4-day post-release silence — TypeScript wildcard pattern hardening (#2541), Python failure hook fix (#2540), EVM batch-settlement explicit gas limit (#2375). Post-May-29-release absorption + bugfix phase.
- Open Wallet Standard: Still quiet. No releases since v1.3.2 (Apr 20), no commits since May 5 (NEAR chain support). OWF blog: GDC Task Forces update and KEYRING demo (May 21).
- OpenJarvis: Extremely active Jun 1 — 9 commits in one day. Highlights: API key Bearer token fix for /v1 + /api (#471), parallelized engine discovery + async version check for faster startup (#470), SSRF Python fallback + Rust detection at import time (#467), SOUL.md/USER.md context in streaming chat (#449), temperature retry for gpt-5 (#466), Apple FM cumulative→delta conversion (#464), MSRV pinned to 1.88 (#469). Jun 2: clone traffic data update. Desktop v1.0.2 still latest stable.
- Simon Willison: Jun 2 — "Pasted File Editor" (built with Codex desktop, paste detection → file attachment, drag-drop, image thumbnails). Jun 1 — "Hackers Simply Asked Meta AI" (Meta wired account recovery to AI chatbot, one-shot account takeover via prompt), May newsletter. May 31 — datasette 1.0a32, ADHD amplifier essay. May 30 — Claude containment (gVisor/Seatbelt/Bubblewrap/VMs), Pyodide ASGI service worker.
- Matt Webb: No new posts since May 30 FedEx personal agents essay. Feed unchanged.
- Oxide: Dormant since Feb 2026. Not re-fetched (confirmed by 3+ prior briefings).
- Yjs: v13.6.31 (May 28, stable — undo+setAttribute+delete data corruption fix), v14.0.0-rc.17 (May 26). No new releases in June.
- Automerge: fragments pre-releases (May 20-21) remain latest. No June activity.
- Ink & Switch: Dispatch page SPA-rendered, unscrapable via curl. Last known: Dispatch 017 (May 28, Patchwork/Local-First Conf Berlin).

## Synthesis
- Dominant theme: **"Agent infra hardening week"** — LangGraph shipped 3 SDK releases in 5 days (interleave, v3 streaming, thread_id encoding), x402 entered post-release bugfix mode, OpenJarvis patched SSRF, auth, and streaming bugs in a single day. The agent stack is getting production-grade reliability patches, not features.
- Second theme: **"Containment lessons go mainstream"** — Willison's Meta AI hack post crystallizes the pattern: wiring AI to infrastructure without sandboxing enables one-shot takeovers. Same week, OpenJarvis adds SSRF protection, Agave adds vote-history reconciliation, x402 hardens wildcard matching. Across the stack, the question shifts from "can agents do X?" to "what happens when they do X wrong?"
- Third theme: **"Solana ecosystem content, not infra"** — New Solana RSS items are use-case articles (onchain perps, gold tokenization, sports), not validator/protocol changes. The infra story is Agave v4.1.0-beta.2 backporting v4.0.1 fixes while Alpenglow features land on master.
- OpenJarvis Jun 1 burst (9 commits) signals the desktop app reaching daily-driver maturity — startup perf, auth, streaming reliability, and SSRF protection all in one day.
- Ollama is in a quiet period post-v0.30.0. No new releases for 20 days. May indicate a larger feature cycle.
