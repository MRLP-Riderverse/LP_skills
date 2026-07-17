# Current source map for cron delta briefings

This note captures the current high-signal source layout and a few probe quirks observed while assembling frontier-stack briefs.

## Canonical sources currently worth checking
- **Solana news RSS**: https://solana.com/news/rss.xml
- **Agave releases**: https://github.com/anza-xyz/agave/releases
- **Ollama blog RSS**: https://ollama.com/blog/rss.xml
- **LangGraph releases**: https://github.com/langchain-ai/langgraph/releases
- **Simon Willison Atom feed**: https://simonwillison.net/atom/everything/
- **Interconnected feed**: https://interconnected.org/home/feed
- **Oxide blog feed**: https://oxide.computer/blog/feed
- **x402 repo commits**: https://github.com/x402-foundation/x402/commits
- **Open Wallet Standard core releases**: https://github.com/open-wallet-standard/core/releases
- **OpenJarvis commits/releases**: https://github.com/open-jarvis/OpenJarvis

## Probe notes
- **Open Wallet Standard**: the relevant repo is `open-wallet-standard/core`; the organization homepage is not a useful discovery surface.
- **x402**: recent signal is in commits, not tags/releases.
- **Simon Willison**: Atom feed parsing by regex is still the safest path for reliable extraction.
- **Solana RSS**: CDATA-aware title parsing avoids missing current items.
- **Ollama RSS**: feed can be a strong signal when populated; if it ever goes empty again, fall back to the blog or releases.
- **Oxide**: do not assume dormancy without a current feed check if the cycle specifically needs it; otherwise skip if already established as quiet.
