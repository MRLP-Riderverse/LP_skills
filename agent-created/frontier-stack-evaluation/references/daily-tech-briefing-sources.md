# Daily Tech Briefing Sources & Quirks

Use this when producing the daily frontier-stack briefing.

## Priority sources

### Solana ecosystem
- Solana RSS: `https://solana.com/news/rss.xml`
- **STATUS (Jun 2026):** RSS feed returned full items with titles, descriptions, and dates via curl. Previously blocked by Cloudflare — now intermittently working. Still keep the homepage-scrape fallback ready as it has failed in prior cycles.
- Fallback: scrape `https://solana.com/news` homepage for recent article links, or use Helius/Rpc provider changelogs.
- Solana Stack Exchange for community-surfaced issues.

### AI/Agent infrastructure
- Ollama blog RSS: `https://ollama.com/blog/rss.xml`
 - **QUIRK:** RSS still returns empty via curl as of Jun 2026. Fallback: scrape `https://ollama.com/blog` for post list (homepage returns `<p>` summaries of recent posts), then fetch individual posts.
- LangChain blog RSS: `https://www.langchain.com/blog/rss.xml`
 - **STATUS (Jun 2026):** RSS now returns full items with titles, descriptions, and dates. Cloudflare gate appears resolved. Rich feed — 20+ items going back months.
- x402: `https://x402.org` homepage + `https://x402.org/writing` for blog posts
 - Site ships a Model Context Protocol tool (`get-x402-info`) — LLM agents can natively discover x402 endpoints.
 - Production stats visible on homepage (transactions, volume, buyers, sellers — last 30 days).
 - Integration: `@x402/express`, `@x402/next` middleware. Supports Base, Ethereum, Arbitrum, Solana with USDC.
 - GitHub: `https://github.com/x402-foundation/x402` (may block curl).
 - **Key posts:** "Introducing x402 Batch Settlement" (May 2026), "Introducing x402 V2" (Dec 2025).
- Open Wallet Standard: **CONFIRMED OFFLINE** as of Jun 2026
 - Both `.org` and `.com` return connection refused (HTTP 000). Successor is x402 V2's wallet-based identity layer. Stop monitoring these domains.

### Sovereign Builder Intelligence
- Simon Willison Atom: `https://simonwillison.net/atom/everything/`
 - **RELIABLE:** Atom feed works for headline discovery. Article pages have the real content — always fetch the article page for summaries.
 - High-signal topics: AI tooling patterns, Datasette updates, LLM security, open-source contribution norms, WASM sandboxing, llm CLI releases.
 - **Also track:** `llm` CLI tool releases (appears in Atom feed as versioned entries, e.g. "llm 0.32a3").
- Oxide blog feed: `https://oxide.computer/blog/feed`
 - **RELIABLE:** Atom feed returns titles and dates. Individual posts have deep technical content.
 - High-signal topics: infrastructure sovereignty, Rust/firmware safety, rack-scale computing, observability.
 - **Note:** Feed doesn't expose `<title>` in a grep-friendly way — entries show as `<link>` + `<updated>` pairs. Use the link URL slug to infer the post title.
- Matt Webb / Interconnected: `https://interconnected.org/home/feed`
 - **RELIABLE:** RSS returns full content — can extract complete post text with `<description>` tags.
 - **QUIRK:** May block generic fetches with 403 unless request uses a browser-like User-Agent. Always set `User-Agent: Mozilla/5.0`.
 - High-signal topics: agentive design, ESP32 firmware (Resident, Courier), vibe-coding hardware, RSS for app distribution, personal agent adoption friction.

### Local-first / DIY automation
- No single canonical feed. Monitor: Ink&Switch blog, Automerge releases, CRDT community, self-hosted AI projects.
- **QUIRK:** Google News RSS returns zero results for niche queries (CRDT, local-first, Automerge, ink-and-switch, personal server). Fall back to GitHub repos and project blogs directly.
- Converging stack signals: Ollama (local inference) + ESP32/Courier (edge agents) + WASM sandboxes (compute anywhere).
- **Emerging:** micropython-wasm (Willison, Jun 2026) — WASM sandbox for Python plugin code. Local-first alternative to cloud microVM sandboxes.

## Useful fallbacks
- Google News RSS search for very recent announcements or missing canonical coverage (but expect zero results for niche queries)
- Direct article fetch + metadata extraction (`title`, `description`, `og:description`, first paragraphs)
- GitHub release pages for projects with no blog RSS
- Discord/Matrix community channels for real-time updates (not automatable via curl)

## Briefing emphasis
- Builder utility over hype
- Sovereign/local-first control
- Payment rails for agents
- Observability and feedback loops
- Headless/service APIs over GUI-only products
- Every item needs an **→ Action:** line — builder-facing, not just informational

## Observed quirks (general)
- Search snippets can be stale for brand-new protocol or tooling announcements; verify with the canonical page before reporting.
- Some blog RSS feeds expose empty fields even when the item link and pubDate are valid.
- If a source blocks default view, try `User-Agent: Mozilla/5.0` header before giving up.
- Empty RSS output ≠ "no news." Always attempt a fallback before reporting silence.
- Solana and LangChain RSS feeds have improved reliability as of Jun 2026 — don't assume they're always broken, but keep fallbacks.
- Oxide feed doesn't include `<title>` tags in a grep-friendly format — extract post slugs from `<link>` URLs instead.
