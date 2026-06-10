# 2026-05-19 session notes

This note captures durable workflow lessons from the 2026-05-19 frontier-stack briefing run.

## Proven source strategy
- Establish the UTC date first, then use a 14-day recency window for daily briefing items.
- For sparse essay/blog sources, widen to ~30 days and label them as thematic signals rather than core-window news.
- Prefer primary sources: official blogs, RSS/Atom feeds, GitHub releases/commits, and public APIs.

## Fetching / parsing lessons
- Some feeds require a browser-like User-Agent to avoid 403s.
- If direct piping into an interpreter is blocked, download to a temp file first, then parse locally.
- When `feedparser` is unavailable, manual RSS/Atom parsing with `xml.etree.ElementTree` is sufficient for daily monitoring.
- Treat missing results carefully: an empty window can be a signal, not a failure (for example, no Oxide posts in-window).

## Evidence hierarchy used successfully
1. Dated release/commit/news items inside the recency window.
2. Thematic essays or posts slightly outside the window when they strongly match the topic.
3. GitHub commits/releases when blogs or feeds are sparse.
4. Absence of recent activity, when verified, should be reported explicitly.

## Useful classification heuristics
- Solana: ecosystem adoption, stablecoins, enterprise payments, AI-agent-friendly infra.
- AI/agent infra: local runners, durable checkpoints/resume, payment plumbing, wallet interoperability.
- Sovereign builder intelligence: feed-first distribution, headless services, local spend controls, observability, and portability.
- Local-first/DIY automation: offline-capable models, small tools, RSS/Atom, and explicit control surfaces for cost and state.

## Reporting pattern
- Lead with the most actionable signal.
- Call out quiet/no-activity sources when verified.
- End with one or two concrete moves a nomadic builder can take immediately.
