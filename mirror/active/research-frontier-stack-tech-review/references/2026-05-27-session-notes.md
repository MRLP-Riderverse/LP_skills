# 2026-05-27 session notes

## Source behavior observations
- Solana news RSS is current (lastBuildDate May 20) but primarily Bits to Bricks podcast episodes this week; April Roundup is the most substantive item.
- Agave v4.0.0 went stable on May 16; v4.1.0-beta.1 already on testnet by May 22 — fast cadence.
- Ollama had a burst of releases (v0.23.2–v0.24.0 in one week, plus v0.30.0-rc27 as a separate RC track). The v0.30 RC signals a major architecture shift to llama.cpp/MLX.
- Ollama blog RSS is stale (latest entry March 30); GitHub releases and commits are the primary signal.
- LangGraph shipped 1.2.0→1.2.2 in two weeks; the durable error-handler/crash-resume feature in 1.2.0 is the most significant for sovereign builders.
- x402 had no tagged releases; 10+ commits in 2 days (May 26-27) covering Go/Java payment fixes, maxValue ceiling, dev tools docs, and docs site navbar. Commit activity is the only usable freshness signal.
- Open Wallet Standard: NEAR chain support merged May 5; no releases since v1.3.2 (Apr 20). OWF blog has GDC Task Forces and KEYRING posts from May 21.
- Simon Willison's Atom feed is very active; key pattern this week is AI security/safety concern (curl pressure, Copilot exfiltration, coding agent shields-up metaphor). Datasette approaching 1.0 with datasette-agent plugin.
- Matt Webb's Resident post (May 20) is the most actionable sovereign-builder item: open-source ESP32 sandbox for AI-authored device code, combining on-device sandboxes + AI code generation.
- Oxide blog has had no new posts since Feb 2026 ($200M Series C). No new RFDs surfaced in the 14-day window.
- Ink & Switch celebrating 10th anniversary; hosting Lab Day at Local-First Conf (July 14). No new research publications this window.
- Automerge blog is stale (last post July 2025 for v3.0).

## Synthesis pattern
- Cross-stack pattern: the "sandbox as primitive" concept appears in both x402 (payment middleware sandbox) and Matt Webb's Resident (on-device code sandbox). Both treat sandboxing as the answer to "how do I let AI act safely in the real world?"
- AI security is the dominant sovereign-builder theme this week — from curl's flood of AI-found vulnerabilities to Copilot's data exfiltration to the "shields up" metaphor for coding agents.
- Solana's stablecoin/payment narrative continues to harden: Pay.sh + Google Cloud for agent payments, Bits to Bricks series on merchant settlement and banking evolution.
