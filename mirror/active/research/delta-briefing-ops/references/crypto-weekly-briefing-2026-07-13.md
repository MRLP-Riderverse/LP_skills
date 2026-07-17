# Crypto weekly briefing source notes (2026-07-13)

Use this note when assembling 7-day Ethereum / Bitcoin / L1-L2 briefs.

## Primary-source map
- Ethereum Foundation blog feed: `https://blog.ethereum.org/feed.xml`
- Vitalik feed: `https://vitalik.eth.limo/feed.xml`
- EthResearch RSS: `https://ethresear.ch/latest.rss`
- Bitcoin Core releases: `https://api.github.com/repos/bitcoin/bitcoin/releases?per_page=10`
- Bitcoin Core release notes: `https://raw.githubusercontent.com/bitcoin/bitcoin/master/doc/release-notes/release-notes-<version>.md`
- Geth releases: `https://api.github.com/repos/ethereum/go-ethereum/releases?per_page=10`
- L2Beat scaling TVL API: `https://l2beat.com/api/scaling/tvs`
- DeFiLlama global TVL chart: `https://api.llama.fi/charts`
- DeFiLlama chain TVL charts: `https://api.llama.fi/charts/<ChainName>`
- DeFiLlama chain list: `https://api.llama.fi/v2/chains`
- OP Stack repo: `https://github.com/ethereum-optimism/optimism`
- zkSync Era repo: `https://github.com/matter-labs/zksync-era`
- Bor repo: `https://github.com/maticnetwork/bor`

## Retrieval notes
- The Ethereum Foundation RSS exposed the Jul 9 post: `The triage is the product: running AI agents against Ethereum's protocol code`.
- EthResearch had fresh posts in-window on lean execution, native UTXOs, incentive compatibility, and STARK backends; RSS is enough for title/date triage.
- GitHub release APIs were sufficient to catch Bitcoin Core v29.4, v30.3, v31.1 and Geth v1.17.4.
- For Bitcoin Core, the release notes are more useful than the GitHub release body; fetch the raw markdown for concise operator-impact bullets.
- L2Beat TVS API returns a chart that can be compared to a point ~7 days earlier for rough delta.
- DeFiLlama chain chart endpoints returned current-plus-historical daily TVL; enough to compute 7-day percentage deltas for major chains.
- Commit scans on key L2 repos surfaced recent operational changes even when no new release existed.

## 7-day findings from this run
- Ethereum: AI-assisted protocol security found a remotely-triggerable panic in libp2p gossipsub.
- Ethereum: Geth continued Amsterdam-related work, including block access list payload v2 handling and max blob cap enforcement.
- Bitcoin: v31.1 fixed a `-privatebroadcast` IP leak; v30.3 fixed excessive chainstate rewrites.
- L2: aggregate scaling TVL was down modestly; Base and Optimism were relatively firmer than Bitcoin and Solana TVL buckets.
- OP Stack: permissionless fault games at initial deploy merged.

## Extraction pattern
1. Pull RSS / release feeds first.
2. Use GitHub releases for date confirmation.
3. Read release notes markdown for operator impact.
4. Use L2Beat / DeFiLlama APIs for short-horizon TVL deltas.
5. Scan recent commits in core repos only after the feed pass.
