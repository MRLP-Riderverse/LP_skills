# Crypto weekly briefing notes — 2026-07-06

## Source map that worked
- **Ethereum Foundation blog:** fetch RSS with a browser-like User-Agent header if the feed blocks plain requests.
- **Vitalik:** `https://vitalik.eth.limo/feed.xml`
- **EthResearch:** `https://ethresear.ch/latest.rss` and `https://ethresear.ch/posts.rss`
- **Bitcoin Optech:** `https://bitcoinops.org/feed.xml` (Atom) plus the dated newsletter page for section-level parsing.
- **GitHub releases/commits:** GitHub API was the fastest way to confirm protocol/operator releases and recent commits for:
  - `ethereum/go-ethereum`
  - `bitcoin/bitcoin`
  - `ethereum/EIPs`
  - `OffchainLabs/nitro`
  - `ethereum-optimism/optimism`
  - `matter-labs/zksync-era`
  - `solana-foundation/solana-web3.js`
  - `near/nearcore`
  - `celestiaorg/celestia-app`
- **DeFiLlama:** use `/protocols` for protocol movers and `/v2/historicalChainTvl/{chain}` for chain-level TVL deltas.
- **L2Beat:** if the JSON/API endpoint is protected, use the public `/scaling/summary` HTML page and extract the embedded metrics instead.

## Retrieval quirks
- GitHub release notes often contain the decisive operational signal; scan the first 10 lines before digging into commit logs.
- For Bitcoin, Bitcoin Optech newsletters frequently summarize the most actionable wallet/core changes faster than media coverage.
- For Ethereum, research posts can be more signal-dense than EF blog posts during protocol-heavy weeks.

## What to extract for the final brief
- Protocol upgrade / release candidates / hardfork dates
- Node-operator actions and compatibility notes
- Security fixes or advisories
- TVL or value-secured deltas that indicate real flow rotation
- One builder-relevant trend, not a market recap
