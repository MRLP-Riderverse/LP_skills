# Stack Status Snapshot — June 2026

Session-derived stack status for the frontier builder ecosystem. Update monthly or when major version bumps land.

## AI/Agent Infrastructure

- **Ollama** — 0.30, ✅ Production. GGUF compatibility via llama.cpp, MLX on Apple Silicon, `ollama launch` (zero-config coding agent setup), cloud models in preview
- **OpenJarvis** — v1.0, ✅ Released. Local-first personal AI framework. Ollama support built-in. Auto-selects models, tracks efficiency, learns from traces. Companion to Hermes (orchestration layer), not competitor.
- **LangGraph** — 1.2, ✅ Production. Delta Channels (diff-only checkpointing → flat storage cost for long-running agents). Fault tolerance: RetryPolicy, TimeoutPolicy, error_handler with SAGA pattern.
- **Deep Agents** — v0.6, ✅ Production. Code interpreter, harness profiles, streaming v3, delta channels, ContextHub. Rubrics middleware for self-evaluation.
- **LangSmith Sandboxes** — GA, ✅ Production. Kernel-isolated microVMs, snapshots, parallel forks, service URLs, auth proxies. Cloud-only.
- **LangSmith Engine** — New, ✅ Production. Auto-clusters agent failures into named issues, proposes targeted fixes. "Agent for improving agents."
- **LangChain Labs** — Launched 10 Jun 2026. Applied research for continual learning. Partners: Harvey, NVIDIA, Prime Intellect, Fireworks, Baseten. Research: prompt optimization across models, harness engineering, fine-tuning Nemotron as cost-efficient subagents, trace→training signal conversion.
- **x402** — V2 + Batch, ✅ Production. Batch settlement (May 2026) for sub-cent agentic transactions. V2 adds wallet identity, discovery, dynamic recipients. Zero protocol fees, zero KYC. **Enterprise backing**: Visa, MasterCard, Amex, Amazon, Google, Stripe, Shopify, Cloudflare, Coinbase, Circle, Solana are Premier Foundation members. See `x402-ecosystem-members.md`.
- **Open Wallet Standard** — ❌ Offline (confirmed Jun 2026). Successor: x402 V2 wallet identity.

## Sovereign Builder Intelligence — Key Developments

### Simon Willison (Jun 2026)
- **micropython-wasm** (6 Jun) — MicroPython compiled to WASM for sandboxed Python plugin execution. Host-function bridging, persistent interpreter state across calls. Local-first alternative to cloud microVMs.
- **datasette-agent 0.2a0** (10 Jun) — Fast iteration from 0.1a0. Agent-editable Datasette. Built using Claude Code + datasette-agent itself (self-modifying-agent pattern).
- **llm 0.32a3** (9 Jun) — CLI tool for LLM interaction. Track releases via Atom feed.
- **Anthropic Fable 5 silent interventions** (9-11 Jun) — Willison flagged Anthropic's invisible refusal/corruption of replies on "ML accelerator design" topics. **Walk-back (11 Jun):** Anthropic is making safeguards visible (flagged requests fall back to Opus 4.8 visibly; API returns refusal reason). Willison: good they're visible, but wants the entire category dropped.
- **Quoting Jeremy Howard** (10 Jun) — Restricting AI capabilities doesn't prevent them, it concentrates them. Better to advance openly, avoiding power imbalance.
- **AgentsView custom model pricing** (9 Jun) — Used Fable 5 to reverse-engineer AgentsView pricing database. Per-model cost observability tool.
- **DiffusionGemma** (10 Jun) — Google's diffusion-based language model. Novel architecture, early signal.

### Oxide Computer (Jun 2026)
- **"iddqd, or the hardest kind of unsafe Rust"** (2 Jun) — Soundness reasoning for unsafe Rust abstractions. Key insight: safe abstractions' soundness depends on reasoning about surrounding safe code too. Layered validation framework.
- **$200M Series C** (Feb 2026) — Infrastructure sovereignty fully funded.
- No new posts since 2 Jun (dormant as of 11 Jun).

### Matt Webb / Interconnected (Jun 2026)
- **"How global logistics got me over my fear of personal agents"** (30 May) — Adopted an agent under pressure (15 FedEx customs worksheets). Agents adopted when drowning, not from curiosity.
- **"Self-driving legs"** (5 Jun) — EMS body augmentation. Cognitive offloading through body outsourcing.
- **"We need RSS for sharing abundant vibe-coded apps"** (29 Apr) — RSS as sovereign distribution layer.
- No new posts since 5 Jun (dormant as of 11 Jun).

## Solana Ecosystem (Jun 2026)
- **WSOP Partnership** (10 Jun) — Solana is official Presenting Sponsor of World Series of Poker 2026. Players buy in with USDC/USDT/SOL, zero processing fees. WSOP Paradise (Dec) offers stablecoin tournament settlements. ESPN broadcast, 130+ countries.
- **Native Subscriptions & Allowances** (2 Jun) — Recurring payments and delegated spending as shared onchain primitives.
- **May 2026 Roundup** (5 Jun) — RWA ATH $2.8B+, 97% tokenized equities share, $16.4B stablecoin supply, record ETF inflows.
- **Onchain Perps program** (1 Jun) — Foundation supporting fully onchain derivatives.

## Convergence Signals
- **WASM sandbox convergence:** Willison's micropython-wasm + LangSmith microVMs + OpenShell seccomp/Landlock = three independent solutions to safe agent code execution. WASM is the only fully local-first path.
- **Ollama + OpenJarvis:** Local inference backbone + agent framework = zero-config sovereign agent stack.
- **Solana subscriptions + x402 batch:** Onchain recurring payments + micropayment settlement = full agent payment rails.
- **Anthropic visible interventions:** Partial win — cloud models self-report refusals, but still intervene. Local/open-weight models remain the only fully sovereign path.
- **LangChain Labs + OpenJarvis learning loops:** Two independent efforts converging on agents that improve from their own traces. The question is now "where does learning data live, and who controls it?"
- **x402 enterprise backing:** Visa/MC/Amex/Amazon/Google + Solana as Foundation member. x402 is production-grade, not emerging.
