# 2026-05-30 session notes

## Source behavior observations
- Solana news RSS (lastBuildDate May 27): only new item in 7-day window remains Chiliz/sports on Solana (May 27). Rest is Bits to Bricks podcast episodes (May 18-20).
- Agave v4.0.1 released May 29 (marked prerelease). Key fixes: WS pubsub subscription cap bypass (PR #12594 — duplicate params circumvented operator-set limits), secondary index memory regression (PR #12726 — OOM on RPC nodes upgrading from 3.1.14→4.0.0), ChannelSend blocking send footgun (PR #12832). v4.1.0-beta.1 still on testnet since May 22.
- Ollama stable v0.24.0 (May 14): Codex App support with built-in browser annotation. v0.23.0-0.23.4 rapid cadence (May 3-13): Claude Desktop, Gemma 4 MTP speculative decoding, OpenCode vision model support. v0.30.0-rc31 (May 13): architecture shift to direct llama.cpp support (still pre-release). Blog RSS updated with OpenJarvis post (May 28) — Stanford Hazy Research/Scaling Intelligence labs build local-first personal AI framework with Ollama support.
- LangGraph SDK 0.4.0 (May 28): websocket stream transports, streaming reconnect hardening, sync subgraphs, sync messages/tool calls, thread stream helpers. CLI 0.4.27 (May 28). LangGraph 1.2.2 (May 26): stable ID fix for DeltaChannel checkpoint writes.
- x402 extremely active: v2.14.0 Go release (May 29), v2.13.0 Go release (May 29), TypeScript release (May 29), Python package versioning (May 29). Key features: auth-capture client scheme for refundable payments (TypeScript PR #2486), simulation-based smart wallet verification — wallet-agnostic, works for Squads/Swig/SPL Governance/Crossmint (PR #1527), Bazaar service metadata plumbing for discovery (PR #2496), Concordium chain spec review (PR #2389), Go module v2 path suffix for major version compliance.
- Open Wallet Standard: no new releases since v1.3.2 (Apr 20). Last commit May 5 (NEAR Protocol chain support). OWF blog: GDC Task Forces update and KEYRING peer-to-peer credentials demo (both May 21). Quiet otherwise.
- Simon Willison (May 26-29): datasette 1.0a31 with write SQL queries + stored queries (May 29), Anthropic $47B run-rate / $65B Series H (May 29), Claude Opus 4.8 "modest but tangible improvement" (May 28), llm-anthropic 0.25.1 (May 28), markdown-svg-renderer tool (May 28), SQLite AGENTS.md (May 27), AI coding agents have found PMF (May 27), curl pressure from AI-assisted security reports (May 26), Copilot Cowork file exfiltration (May 26), Paul Graham quote on AI-written founder emails (May 26).
- Matt Webb: Resident (May 20) remains latest. No new posts since.
- Oxide blog: dormant since Feb 2026 ($200M Series C). RFD page is SPA-rendered, unverifiable via scraping. 80 RFDs total (Bryan Cantrill has 14).
- Ink & Switch: Dispatch 017 (May 28) — Patchwork progress ahead of Local-First Conf Berlin. bijou64 variable-length integer encoding (May 26). Tenfold Playground (May 18).
- Automerge: fragments pre-releases 3.3.0-fragments.0/.1 (May 20-21).
- Yjs: v13.6.31 stable (May 28) — fixes undo+setAttribute+delete data corruption (PR #757). v14.0.0-rc.17 (May 26) continuing.

## Synthesis pattern
- Cross-stack pattern: "payment protocol maturity" is the new dominant thread — x402 shipped two Go major releases + TypeScript/Python releases in a single day (May 29), added auth-capture refundable payments and wallet-agnostic smart wallet verification. Solana stack solidifying with sports/fan tokens + merchant settlement + Agave hardening.
- Agave v4.0.1 is significant: WS pubsub bypass fix (security) + secondary index memory fix (ops) directly address validator pain points from the v4.0.0 upgrade. These are sovereign infra hardening commits.
- Ollama's OpenJarvis + rapid v0.23-0.24 cadence = local-first AI agent stack accelerating. `ollama launch` became the universal on-ramp (Claude Desktop, Codex App, OpenCode). OpenJarvis from Stanford is the academic sovereign-AI counterpart.
- x402 auth-capture is a new primitive for sovereign commerce: agents can now sign refundable payment payloads, enabling "try before you commit" economics for API access.
- Datasette 1.0 approaching with write SQL + stored queries = sovereign data tool reaching full CRUD capability. Combined with AGENTS.md trend and OpenJarvis, the "self-hosted AI agent with its own data" stack is becoming real.
- Willison's PMF analysis + Anthropic $47B run-rate confirms: AI coding agents have crossed the chasm. The sovereign builder question shifts from "can agents work?" to "which agents can I run on my own hardware?"
- CRDT ecosystem: Yjs data corruption fix in v13.6.31 is operationally important; bijou64 from Ink & Switch eliminates canonicalisation attack surface.
