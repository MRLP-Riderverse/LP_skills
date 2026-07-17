# Daily Tech Briefing Delta Protocol

Use this when producing the frontier-stack daily briefing.

## Dedup protocol
1. Find the most recent session with `session_search(query="frontier stack daily briefing", sort="newest")`.
2. Read the last delivered brief’s content, not just the session title.
3. Compare against the last 3 briefings; items repeated across that window are stale unless there is a concrete new release, post, commit, or status change.
4. If a source has no verified new delta, report silence for that section.

## Source freshness signals verified in June 2026
- **Solana**: official RSS can be live enough to use directly; keep a fallback ready.
- **Ollama**: RSS provides usable release deltas; watch MLX, tool-call parsing, and launch/agent UX changes.
- **LangGraph**: release notes are the best signal for state/overwrite semantics and subgraph behavior.
- **Simon Willison**: Atom feed is reliable for small tools, agentic coding, and local-first patterns.
- **Oxide**: Atom feed is stable; use it as the canonical signal for infrastructure sovereignty and Rust/firmware topics.
- **Matt Webb**: RSS is useful for conceptual framing; prefer posts that shift the model of product form or human/agent boundaries.
- **x402**: the `/writing` page plus repo commits is the best freshness pair; releases may lag.
- **Open Wallet Standard**: releases and commits both matter because provenance/trusted-publishing changes often land in small patches.
- **OpenJarvis**: the canonical `open-jarvis/OpenJarvis` repo commits are the freshness signal; desktop release tags can lag behind active fixes.

## Briefing hygiene
- Keep the final output in English only.
- Use bullet lists, not tables.
- The briefing itself must be the last output when delivering it.
- Include an action line only for genuinely new items.
