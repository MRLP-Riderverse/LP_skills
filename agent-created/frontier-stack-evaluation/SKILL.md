---
name: frontier-stack-evaluation
description: Evaluate frontier builder tooling, agent infrastructure, and sovereign/open workflows through a practical, local-first, provider-agnostic lens. Consolidates stack auditing, tech review, and news investigation.
category: research
aliases: [frontier-stack-reviewer, frontier-stack-tech-review, frontier-agent-stack-audit, frontier-tech-news-investigation]
---

# Frontier Stack Evaluation Umbrella

This is the **class-level skill** for evaluating frontier AI/agent tooling, infrastructure, and technology developments. It consolidates stack auditing, tech review, news investigation, and practical evaluation workflows.

**Trigger:** User wants to evaluate new AI/agent tools, compare frontier infrastructure, audit their current stack, investigate breaking tech news, or monitor technology developments (Solana, blockchain, Linux, AI tooling).

---

## Subsections

### A. Stack Reviewer Framework (from `frontier-stack-reviewer`)
Evaluate frontier builder tooling, agent infrastructure, and sovereign/open workflows through a practical, local-first, provider-agnostic lens.

**When to use:** Need structured analysis for decision-making on new tools, compare tools by practical utility rather than hype, assess portability/resilience/lock-in risks.

**Evaluation Framework:**
- **Maturity**: Is it usable today or experimental?
- **Portability**: Can work be moved between systems?
- **Resilience**: Local/offline fallback capabilities
- **Lock-in Risk**: Dependency on specific providers
- **Recoverability**: Session export/import after crashes
- **Wallet Safety**: Policy-aware signing controls
- **Payment Potential**: Native tool/agent payment rails
- **Orchestration Fit**: Multi-agent workflow suitability
- **Real-world Usability**: Practical adoption readiness

**Standard analysis targets:** OpenCode, OpenHarness, OpenSpace, MassGen, Open Wallet Standard (OWS), x402, OpenJarvis, OpenClaw, NemoClaw, OpenShell.

**x402** (Coinbase → LF Projects, 2025-2026) — HTTP 402 payment protocol for agent-to-agent and agent-to-API payments. Production traction: 75M+ transactions/month, $24M+ volume (as of Jun 2026). Supports USDC on Base, Ethereum, Arbitrum, Solana. Integration: `@x402/express`, `@x402/next` — single middleware line. Ships MCP tool (`get-x402-info`) for LLM agent discovery. **Batch Settlement** (May 2026) enables sub-cent agentic transactions with cryptographic vouchers and bulk onchain redemption. Key for sovereign builders: zero KYC, zero API keys, per-request stablecoin payments. **Enterprise backing**: Visa, MasterCard, Amex, Amazon, Google, Stripe, Shopify, Cloudflare, Coinbase, Circle, Solana = Premier Foundation members. See `references/x402-ecosystem-members.md` for full member list. See `references/daily-tech-briefing-sources.md` for sourcing details.

**Ollama 0.30.7 + `ollama launch`** (Jun 2026) — `ollama launch` is a single-command setup for coding agents (Claude Code, OpenCode, Codex) with local or cloud models, no env vars or config files. Ollama 0.30.x adds improved GGUF compatibility via llama.cpp, better multi-GPU scheduling, fewer OOM crashes, and cloud model preview. **MLX Performance update** (11 Jun): up to 20% faster on Apple Silicon via fused Metal kernels, NVFP4 quantization for higher quality, and a **snapshot system** for agent workflows that saves model state at branch points and intervals — enabling stateful long-running agent sessions without cloud prefix caching. This is the local-first answer to LangSmith's server-side session persistence. Blog URL pattern: `https://ollama.com/blog/<slug>` — blog homepage lists slugs via `grep -ioP 'href="/blog/[^"]*"'`.

**micropython-wasm** (Willison, Jun 2026) — MicroPython compiled to WASM for safe Python plugin execution. Host-function bridging, persistent interpreter state across calls. The local-first alternative to cloud microVM sandboxes (LangSmith Sandboxes). WASM isolation guarantees: "if the C turns out to be fatally flawed the worst that can happen is the WebAssembly execution will fail with an exception."

**OpenJarvis** (Stanford SAIL, May 2026) — local-first personal AI framework. **Companion to Hermes, not competitor.** Five primitives: Intelligence (model catalog), Engine (hardware-aware inference), Agents (constrained reasoning), Tools & Memory (MCP + A2A + semantic indexing), Learning (local trace fine-tuning via GRPO/LoRA). Key distinction vs Ollama: OpenJarvis is a model *system* (auto-selects, tracks efficiency, learns), Ollama is a model *runner* (serves weights). Architecture: Hermes = orchestration layer, OpenJarvis = inference layer. Already imports Hermes skills. **v1.0 released Jun 2026** with Ollama support built-in. **Commit activity on the canonical `open-jarvis/OpenJarvis` repo is now a primary freshness signal; check it even when releases lag.** See `references/openjarvis-evaluation.md` for full evaluation.

****LangChain Labs**

**NVIDIA Nemotron 3 Ultra** (Jun 2026) — 550B params (55B active MoE), open model on Ollama Cloud. Built for long-running agentic workflows. Up to 30% cost savings vs other leading open models for tool-call-heavy workloads. Test as high-volume subagent model where GPT-5.5 is overkill and local models too slow.

**datasette 1.0a33** (11 Jun 2026) — Approaching the long-anticipated 1.0 stable release. When it ships, it becomes the default local-first data tool for Hermes memory/query interfaces. Previous alpha: 1.0a32 (31 May). (Launched 10 Jun 2026) — Applied research arm for continual learning in agents. Partners: Harvey, NVIDIA, Prime Intellect, Fireworks, Baseten. Research directions: prompt optimization across models, harness engineering, fine-tuning open models (Nemotron) as cost-efficient subagents, converting trace data into training signal. Converges with OpenJarvis' local GRPO/LoRA learning loop — both aim at agents that improve from their own execution history. The open-research angle matters: if evals/datasets are published, Hermes can integrate them as quality benchmarks.

**See original:** Full evaluation framework preserved from `frontier-stack-reviewer` skill.

---

### B. Tech Review & Monitoring (from `frontier-stack-tech-review`)
Evaluate technology developments including Solana, blockchain, Linux, and real-world tech usage through a practical, builder-focused lens.

**When to use:** Stay updated on Solana ecosystem, track blockchain/Web3 infrastructure, monitor Linux/open-source advancements, evaluate real-world tech adoption.

**High-signal sources:**
- **Solana**: `https://solana.com/news/rss.xml` (official), individual article pages for metadata
- **Ollama**: `https://ollama.com/blog/rss.xml` (RSS still broken via curl Jun 2026; homepage scrape works)
- **LangChain/LangGraph**: `https://www.langchain.com/blog/rss.xml` (RSS returns valid items with titles/descriptions as of Jun 2026 — Cloudflare gate resolved). **Pitfall: direct blog URLs 404 on curl** — LangChain's blog is JS-rendered Webflow. Individual post URLs (e.g. `/blog/the-missing-link-between-agents-and-applications`) return 404 on curl/HTTP fetch. RSS titles and descriptions are the reliable extraction path; falling back to individual article pages requires a browser/rendering engine.
- **Simon Willison**: `https://simonwillison.net/atom/everything/` — AI tooling patterns, Datasette, LLM security, open-source norms
- **Matt Webb / Interconnected**: `https://interconnected.org/home/feed` — agentive design, ESP32 firmware (Resident, Courier), vibe-coding hardware, AI psychosis risk, RSS for app distribution. **"Wet thoughts" (12 Jun 2026):** Webb coins "wet words" for human-authored words, by analogy with wet lab, wet hire, wet lease, wetware — all meaning "includes humans." As most words become non-human-made, "wet" specifies the human-governed. Sovereignty framing: wet inference, wet memory, wet policy = human-governed AI.
- **Oxide**: `https://oxide.computer/blog/feed` — infrastructure sovereignty, Rust/firmware safety, rack-scale computing, $200M Series C (Jun 2026). Dormant since 2 Jun 2026 (last post: iddqd/unsafe Rust).
- **x402**: `https://x402.org` homepage + `/writing` — production stats, MCP tool, integration middleware
- **Open Wallet Standard**: the public `.org` / `.com` sites may still be offline, but the canonical `open-wallet-standard/core` repo is active and should still be checked for commits/doc updates (especially x402-related payment + policy examples). Do not treat the website being offline as a signal to stop monitoring the codebase.

**Operational sourcing tactics:**
- Prefer official pages and release notes over third-party commentary
- Extract metadata (`og:title`, `meta name="description"`, `article:published_time`) instead of full article when possible
- Use Google News RSS with `when:1d` for daily briefings when canonical feeds are stale
- Cross-verify key developments from multiple sources
- Focus on practical utility over price speculation

**Community adoption / blockchain-choice lens:**
- When the user is evaluating BTC vs ETH vs SOL for onboarding a real community, frame the question around participation, identity, fees, merchant/event utility, and future builder composability — not token speculation
- Use cultural namespace precedents (`.cat`, `.gal`, `.bzh`) plus wallet-native precedents (ENS subnames, POAP-style attendance) to show how names can become community infrastructure
- `references/cultural-namespace-and-wallet-onboarding.md`
- `references/frontier-stack-system-prompt.md`
- `references/daily-tech-briefing-template.md`
- `references/stack-status-2026-06.md` — session-derived stack snapshot (versions, status, key developments)
- `references/cron-provider-routing.md` — verified provider-id behavior for cron briefs (`openai-api` vs `openai-codex`)
- `references/2026-06-12-session-notes.md` — delta-brief source behavior notes, commit-first signals, and June 12/13 freshness examples


**See original:** Full sourcing notes and extraction tactics preserved from `frontier-stack-tech-review` skill.

---

### C. Agent Stack Audit (from `frontier-agent-stack-audit`)
Audit and compare a user's current AI agent stack against the 2026 frontier landscape. Identify gaps, redundancies, and learning priorities for local-first, privacy-focused workflows.

**When to use:** User wants to audit their current tool stack, identify gaps in their setup, or understand the frontier architecture.

**Core Stack Layers (Reference Architecture):**
```
YOU (User) → Thunderbolt (POS Interface) → [Hermes | Opencode | NemoClaw] → GBrain (Curated Memory) → mempalace (Raw Memory) → NoteCore (Inbox)
```

**Stack Component Status (April 2026):**
- **Hermes Agent**: ✅ Best-in-class for local-first orchestration
- **Opencode**: ✅ v1.14.18, anomalyco/opencode, daily driver
- **GBrain**: ✅ PGLite/Postgres backend, active
- **mempalace**: ✅ Filesystem-based (JSONL/SQLite), QuickThoughts.txt
- **OpenClaw**: ✅ 375K+ ⭐, 78K forks. Personal AI assistant, 50+ integrations. Steinberger → OpenAI Feb 2026. ClawHub marketplace. `references/openclaw-nemoclaw-openshell.md`
- **NemoClaw**: ⚠️ Alpha (v0.0.55), NVIDIA. Reference stack for OpenClaw + Hermes in OpenShell sandboxes. 20K+ ⭐. `references/openclaw-nemoclaw-openshell.md`
- **OpenShell**: ⚠️ NVIDIA sandbox runtime. 6.3K ⭐. Seccomp/Landlock isolation. `references/openclaw-nemoclaw-openshell.md`
- **Thunderbolt**: ⚠️ UI layer only, not OS builder
- **Claude Code CLI / Codex CLI**: ✅ Alternatives to Opencode

**Audit Procedure:**
1. Inventory current tools (`which hermes`, `opencode --version`, etc.)
2. Map to core layers (Orchestration, Coding Agent, Memory/Search, Sandbox/Runtime, UI/Client, Packaging)
3. Identify gaps & redundancies
4. Create learning priority matrix

**High Priority Learning (May 2026):**
1. **MCP (Model Context Protocol)** - Tool discovery standard
2. **Structured Output** - Outlines/Guidance for guaranteed JSON/XML
3. **vLLM Serving** - High-throughput self-hosted inference
4. **GGUF Quantization** - Run larger models on consumer hardware
5. **OpenJarvis** - Local-first inference backbone with learning loop (complements Hermes orchestration)

**See original:** Full audit procedure and MCP integration pattern preserved from `frontier-agent-stack-audit` skill.

---

### D. Tech News Investigation (from `frontier-tech-news-investigation`)
Investigate and verify breaking tech/AI news when search tools return conflicting results - extract primary sources, handle date discrepancies, and compile multi-angle narratives.

**Rate-limit resilience for cron briefs:** if a delta briefing dies after source collection with an HTTP 429 / Too Many Requests from the synthesis model, treat it as a provider throttle rather than a source failure. Trim the prompt, retry with backoff once, and if it repeats, split collection from synthesis or move the cron to a less rate-limited provider. See `references/cron-rate-limit-resilience.md`.

**When to use:** User asks about recent tech/AI news, acquisitions, or industry developments; initial web searches return conflicting or "not found" results; need to verify breaking news not yet indexed.

**Step-by-Step Instructions:**
1. **Start with user-provided sources FIRST** - fetch URLs directly before running general web searches.
2. **Prefer official feeds and canonical article pages** - use RSS/Atom where available, then fetch the article page for metadata and lead paragraphs.
3. **Extract key entities** - people names, company names, dates, timelines, technical details, quotes.
4. **Run targeted follow-up searches** - use extracted entities for secondary research and corroboration.
5. **Handle search/tool inconsistencies** - trust primary source articles over search engine "not found" results or stale snippets.
6. **Extract maximum context from limited sources** - fetch related articles, expert quotes, technical details, and release notes.
7. **Compile a concise multi-angle narrative** - structure as: what changed, why it matters, what to do next.

**Critical:** Web search tools may return "not found" or misleading results for very recent news (past few days/weeks), future-dated events, or regional/niche publications. Trust primary source articles fetched directly over search engine output.

**Daily briefing workflow:**
1. Check official RSS/Atom first for all canonical sources (see `references/daily-tech-briefing-sources.md`). Before drafting, compare against the last 3 frontier-stack briefings; repeated items are stale unless there is a concrete new release/post/commit/status change.
2. If a feed returns empty/1-line output (common with Cloudflare-gated feeds like Solana, Ollama, LangChain), fall back to: (a) direct article page fetch with User-Agent header, (b) Google News RSS with `when:1d`, (c) the site's HTML homepage scraped for recent post links.
3. Extract content per-source: Willison → article page (Atom for discovery only), Oxide → Atom feed works, Webb → RSS works with full content, x402 → homepage + `/writing` page.
4. Synthesize into four sections: (1) Solana ecosystem, (2) AI/Agent infrastructure, (3) Sovereign Builder Intelligence, (4) Local-first/DIY automation.
5. Close with cross-cutting signals as labeled bullet pairs (NOT markdown tables — Telegram strips them) and a single thematic thread.
6. Every item gets an **→ Action:** line — builder-facing, not just informational.
7. **The briefing itself must be the final output.** Never append a post-briefing summary, confirmation, or "done" message. Cron delivery captures the LAST assistant response — any follow-up message will replace the briefing.
8. **Write in English only.** Translate non-English source material before including it. Never create parallel-language sections or tables.

**Briefing output format (see `references/daily-tech-briefing-template.md`):**
- 4 numbered sections matching the briefing categories
- Cross-cutting signals table at the bottom
- One "Thread for the week" sentence synthesizing the dominant theme
- Each item: signal → implication → action (where actionable)
- Emoji section headers for quick scanning
- Concise — target 800-1200 words total

**Example commands:**
```bash
# Fetch article paragraphs
curl -sL "URL" | grep -oP '<p[^>]*>[^<]*</p>' | head -25

# Extract headlines from related articles
curl -sL "URL" | grep -oP '"headline":"[^"]*"' | head -5

# Get full article metadata
curl -sL "URL" | grep -oP '"(headline|description|datePublished)":"[^"]*"'
```

**See original:** Full investigation workflow preserved from `frontier-tech-news-investigation` skill.

---

### E. Cross-Context Analysis (from GPT/Hermes divergence pattern)

When the user shares a report, summary, or insight from another AI context (GPT, Claude, Perplexity, etc.), perform a structured cross-reference against Hermes session history to surface what's genuinely new vs already-explored, and flag any tensions between the other context's framing and prior Hermes decisions.

**When to use:** User shares output from another AI session, says "I was chatting with GPT about..." or pastes a session report/summary from another tool.

**Procedure:**
1. **Session search** — query Hermes session DB for each major theme in the shared content
2. **Classify coverage** — tag each theme as: ✅ heavily explored, ⚠️ partially explored, ❌ entirely new
3. **Flag tensions** — identify places where the other AI's recommendations contradict concrete prior decisions (e.g., payment choice, framing language, cloud vs local stance)
4. **Deliver the delta** — focus the response on what's genuinely new and what tensions need user decision, not on re-validating what Hermes already established

**Why this matters:** The user values seeing where different AI contexts diverge. They use multiple AI tools and want Hermes to be the "ground truth check" — not just another opinion, but the one backed by actual session history and prior decisions. This is the "federated cognition" advantage: each context contributes, Hermes anchors.

**Example tension patterns to watch for:**
- Other AI pushes cloud-dependent solution → Hermes has local-first stance
- Other AI uses heavier control language → Hermes has softer "guided/stewarded" framing
- Other AI recommends web3-native early → Hermes chose simpler V1-first approach
- Other AI treats conversation history as ongoing cloud memory → Hermes stance is export→local

**See also:** `note-capture-workflow` for routing cross-context insights into QuickThoughts.

### F. Smol Web / Small Web Movement

The smol web movement (minimal markup, no tracking, human-scale web) aligns with local-first sovereign AI philosophy. The "small AI" intersection — local models, sovereign compute, AI as personal amplifier — is a natural bridge, not a conflict. ~40% of Gemini community is anti-AI-content, ~40% pragmatic-if-labeled, ~20% pro-experimental. Relevant for community content delivery (low-bandwidth Gemini channels) and cultural alignment with Acadie.sol's AI-as-infra vision. See `references/smol-web-research.md`.

---

## Common Pitfalls

1. **Assuming tools are interchangeable** - GBrain ≠ mempalace (curated vs raw)
2. **Skipping MCP** - reinventing tool discovery for each agent
3. **Cloud-first thinking** - contradicts local-first, privacy goals
4. **Over-engineering memory** - start with append-only QuickThoughts, add structure later
5. **Ignoring persistence** - NemoClaw sandboxes are ephemeral without proper volume mounts
6. **Don't rely on generic web search snippets** for current-state reporting if canonical source is accessible
7. **Don't overstate "latest"** if only older but still relevant posts are available
8. **Avoid using broad hype language** - keep output builder-facing and implementation-oriented
9. **If a source blocks default view**, try plain/simplified variant before giving up
10. **Treat breaking-release headlines cautiously** until they match canonical upstream status
11. **RSS feeds silently fail** — Solana, Ollama, and LangChain RSS commonly return empty/1-line output via curl due to Cloudflare or JS-rendered content. Always have a fallback path (direct page scrape, Google News RSS, or site homepage). Don't treat empty RSS as "no news."
12. **Google News RSS often returns zero results** for niche/technical queries (CRDT, local-first, specific protocols). This means the query format doesn't match indexed content, not that there's nothing happening. Fall back to canonical project blogs/repos directly.
13. **Solana RSS works intermittently** — as of Jun 2026, the Solana RSS feed returned full items with titles, descriptions, and dates via curl (no Cloudflare block). This is an improvement; don't assume it's always broken, but still have the homepage-scrape fallback ready because it has failed in prior cycles.
14. **`execute_code` blocked in cron mode** — when running as a scheduled cron job without user present, `execute_code` is blocked (requires approval). Use separate `terminal()` calls for each source fetch instead of batching them in a Python script. This means cron-based briefings need N separate curl calls rather than 1 consolidated script. Plan the sourcing sequence accordingly.
15. **LangChain blog posts are JS-rendered Webflow** — individual blog post URLs (e.g. `/blog/the-missing-link-between-agents-and-applications`) return 404 on curl/HTTP fetch because the site is a single-page Webflow app. RSS titles and descriptions are the reliable extraction path. If you need article body content, you need a browser/rendering engine — curl alone cannot extract it.
13. **Cloud model output integrity is not guaranteed** — Anthropic's Claude Fable 5 silently corrupts replies on certain topics (e.g., "ML accelerator design") without disclosure (confirmed by Willison, Jun 2026). **Update (11 Jun 2026):** Anthropic walked back the invisible aspect — flagged requests now visibly fall back to Opus 4.8, and the API returns a refusal reason. Willison's take: good they're visible, but wants the entire category of refusals dropped. The sovereignty gap remains: you still don't control the intervention policy. Local/open-weight models are the only path where you do. Flag this in any stack audit comparing cloud vs local models. **Willison also documented Fable's "relentless proactivity"** (11 Jun): Fable 5 + Claude Code autonomously built test infrastructure (scratch HTML pages, Safari screenshot capture, custom CORS web app for measurements, local server, injected JS into test templates) without human direction. Cost: ~$12 in tokens per unsupervised debug session. Claude Max plan ($100/month) includes Fable access only until June 22 2026, after which full API pricing applies. The autonomy vs cost tradeoff is now concrete: cloud gives relentless autonomy at $12/session, local gives controlled autonomy at inference cost.
14. **Every briefing item needs an action line** — a briefing without "→ Action:" prompts is information, not intelligence. If you can't find an actionable angle, reconsider including the item.
16. **Cron delivery captures the LAST assistant message, not the biggest** — when running as a scheduled cron job, the delivery system saves and delivers the *final* assistant response. If the model produces a full briefing and then appends a follow-up "Briefing delivered" or wrap-up summary, that follow-up becomes the saved/delivered output and the full briefing is lost. **Rule: the briefing itself MUST be the last thing you output. Never add a post-briefing summary, confirmation, or "done" message.** If you need to track internal progress, use the todo tool — never emit a closing message after the briefing.
17. **Language contamination from non-English sources** — when source material is in another language (e.g., Dutch ForkLog articles, French Acadian press), the model may spontaneously duplicate output sections in that language. This is a context-window bleed issue, not a feature. **Rule: write the entire briefing in English. Translate non-English source material before including it. Never create parallel-language sections or tables.**
18. **Telegram strips markdown tables** — markdown pipe tables render as garbled text or get completely stripped in Telegram delivery. **Rule: use bullet lists (labeled key: value pairs) instead of tables for Telegram-bound briefings.** The cross-cutting signals section should use labeled bullet pairs, not a table.
19. **Skill alias resolution fails with skill_view** — this skill has aliases (`frontier-stack-tech-review`, `frontier-stack-reviewer`, etc.) in its YAML frontmatter, but `skill_view(name='frontier-stack-tech-review')` returns "not found." The aliases are metadata only, not resolvable by the tool. **Rule:** always use the canonical skill name (`frontier-stack-evaluation`) when calling `skill_view`. If a cron job or prompt references an alias, translate it before the tool call. Do not rely on alias resolution working.
20. **x402 ecosystem is enterprise-grade** — as of Jun 2026, x402 Foundation members include Visa, MasterCard, American Express, Amazon, Google, Stripe, Shopify, Adyen, Cloudflare, Coinbase, Circle, Fiserv, and Solana (Premier), plus 10+ general members. See `references/x402-ecosystem-members.md` for the full list. Do not frame x402 as "emerging" or "early-stage" in briefings — it has enterprise backing.
21. **429 during synthesis is usually a provider throttle, not a source bug** — if the cron makes it through collection and then fails on the final model response, shrink the prompt and retry once before changing source logic. For recurring cases, split collection and synthesis into separate jobs or switch providers. See `references/cron-rate-limit-resilience.md`.
22. **Cron/provider ids can drift independently of the model** — `gpt-5.4-mini` may remain correct while the persisted job still points at a stale provider (`openai`). In that case, verify the job record and update the provider explicitly; for this stack, `openai-api` and `openai-codex` both validated, while plain `openai` failed.

---

## Verification Checklist

After evaluation or audit, you should be able to answer:
- [ ] What layer does each tool occupy?
- [ ] What's the single source of truth for notes? (QuickThoughts.txt)
- [ ] How do agents discover tools? (MCP or custom?)
- [ ] What's the learning priority for next 30 days?
- [ ] Where is PII preserved vs sanitized?
- [ ] Are sources current (within last 24-48 hours for daily briefings)?
- [ ] Have you cross-verified from multiple sources when possible?

---

## Related Skills

- `native-mcp` - MCP server configuration
- `gbrain-operations` - GBrain setup and raw import
- `note-capture-workflow` - Note capture and routing
- `third-brain-architecture` - Local-first architecture design

---

*Consolidated: May 2026*
*Source skills: frontier-stack-reviewer, frontier-stack-tech-review, frontier-agent-stack-audit, frontier-tech-news-investigation*
