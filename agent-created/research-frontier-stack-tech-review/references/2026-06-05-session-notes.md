# 2026-06-05 session notes

## Source behavior observations
- Solana news RSS: New item today — May 2026 Ecosystem Roundup (RWA ATH $2.8B+, 97% tokenized equities share, $16.4B stablecoin supply, record ETF inflows). Last 5 items: Jun 5, Jun 2, Jun 1, May 28, May 27.
- Agave: v4.1.0-beta.2 (Jun 1, prerelease) still latest release. Jun 5 commit: xtask pipeline generator repo info fix (#12914). Jun 4 commits: p-token tag update (#12948), XDP setup docs (#12818), Block type alias→struct (#12929), staked validator spawn in multinode-demo (#12395), remove simple vote static cost after feature activation (#12902), Revert "fix(votor): only add vote to vote_history if voting" (#12953), alpenglow leader abort quiet log (#12933).
- Ollama: v0.30.5 (Jun 4, stable) — fixes gemma4:12b FPE crash, adds Hermes Windows install integration. This is the 4th release in 2 days (v0.30.2–0.30.5). Blog RSS had title "?" for nemotron-3-ultra post (Jun 4) — extraction issue with encoding.
- LangGraph: v1.2.4 (Jun 2) is latest. Jun 3 commits are all dependency bumps (TypeScript 6.0.3, mypy 2.1.0). Cadence continues to be hardening/maintenance.
- x402: Very active Jun 2-5. Key PR #2553 (merged Jun 5): adds x402 v1 support to Python/Go MCP modules — previously only TypeScript SDK supported v1+v2. Other activity: v1 path param preservation (#2508, Jun 4), partial money string rejection (#2530, Jun 3), Schema v2 support (#2329, Jun 2), SVM smart wallet e2e test (#2504), Swig smart wallet allowlist fix (#2509). No tagged releases.
- OWF: Still quiet. Last release v1.3.2 (Apr 20), last commit May 5.
- OpenJarvis: Active Jun 4-5. Jun 5: outcome-first gallery tier (#500), leaderboard quarantine filter (#501), clone traffic. Jun 4: leaderboard telemetry pipeline fix (#498), AppImage env-strip + server attach (#496), Discord conversation_id reply fix (#495), MCP Authorization:Bearer auto-load (#494).
- Simon Willison: Jun 4 — "AI enthusiasts are in a race against time, AI skeptics are in a race against entropy" (quoting Charity Majors on the gap between AI enthusiast and skeptic engineers — no natural feedback loop connecting them). Jun 3 — Uber AI tool cost caps ($1,500/mo per tool). Jun 2 — Microsoft MAI models, datasette-agent-micropython 0.1a0, Pasted File Editor, micropython-wasm.
- Matt Webb: No new posts since May 30 (FedEx personal agents essay).
- Oxide: Dormant since Feb 2026. Not re-fetched.

## Synthesis
- Dominant theme: **"MCP as the connective tissue"** — x402 adding v1 support to Python/Go MCP modules (#2553, merged today) and OpenJarvis auto-loading MCP tools with Bearer auth (#494) are both advancing MCP as the standard agent-to-tool interface. Ollama's Cline CLI auto-install (v0.30.2) and Hermes Windows integration (v0.30.5) extend the same pattern: local inference → MCP → agent tool use.
- Second theme: **"The cost-feedback gap"** — Simon Willison's quote of Charity Majors crystallizes the organizational problem: AI enthusiasts and skeptics lack natural feedback loops. Uber's $1,500/mo cap is the first corporate attempt to create one (a budget constraint as feedback). The sovereign builder version: your own spending data becomes the feedback loop.
- Third theme: **"Solana's institutional arrival"** — May roundup shows RWA at ATH ($2.8B+), 97% tokenized equities market share, $16.4B stablecoin supply, record ETF inflows. The ecosystem has shifted from DeFi-native to institutional-grade. Subscriptions & Allowances (Jun 2) add recurring payment rails.
- Agave's SIMD-0525 revert (Jun 4, from yesterday) and the voter vote_history revert (#12953) show Alpenglow consensus is still being actively debugged — slot time reductions and voting fixes are being tried and rolled back.
