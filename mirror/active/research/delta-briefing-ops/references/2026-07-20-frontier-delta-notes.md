# Frontier Delta Probe Notes — 2026-07-20

## Window and source strategy

- Use an explicit UTC window before collection; this run covered 2026-07-06 through 2026-07-20.
- Probe GitHub releases first for Ollama and LangGraph, then inspect release bodies rather than relying on tags alone.
- Probe GitHub commits with `since=` for sparse-release projects. OpenJarvis's canonical repository is `open-jarvis/OpenJarvis`; recent substantive commits included model-switch chat preservation, hermetic tests, Rust-extension fallback, and provider-key lookup repair.
- Solana's weekly changelog is a strong primary aggregation point: it combines Agave/Firedancer/Frankendancer, SDKs, LiteSVM, Mollusk, and Surfpool, and often includes proposals not represented by release tags.
- Simon Willison's Atom feed and Matt Webb's RSS feed provide reliable dated posts; fetch the article page for context after confirming the feed item.

## Dedup and synthesis

- The last delivered brief had Solana/WSOP, Ollama provider/cache hardening, LangGraph state fixes, and Simon's WebRTC post. New releases on those exact projects qualify as follow-ups only when they materially advance the topic.
- Do not re-confirm previously quiet Oxide, x402, or Open Wallet areas. Omit them unless they move.
- Prefer a cross-stack pattern grounded in the cycle's new evidence. This cycle's strongest pattern was bounded, inspectable execution: explicit local-agent context/tooling, graph-state correctness, reproducible validator configuration, and deliberately single-purpose voice interfaces.

## Operational reminder

- If the requested output is a cron-delivered delta brief, the brief must be the final assistant message: no postscript, delivery confirmation, or research log.
