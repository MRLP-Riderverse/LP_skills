# Crypto weekly briefing source workflow

Use this when producing a 7-day builder-focused digest for Ethereum / Bitcoin / L2s.

## Source order
1. **Primary docs / repos**
   - Ethereum Foundation blog, Vitalik blog, EIPs
   - Bitcoin Core GitHub PRs / commits
   - L2 repos (OP Stack, geth, bitcoin, nitro, etc.)
2. **Metrics APIs**
   - DeFiLlama protocol and historical chain TVL endpoints
   - L2Beat summary API (`https://l2beat.com/api/scaling/summary`)
3. **News sites**
   - The Block, CoinDesk, Decrypt technical sections only

## Practical notes
- Prefer APIs over homepage RSS when feeds 403 or are behind anti-bot protection.
- Use GitHub PR/commit APIs to confirm whether a merge actually landed this week.
- For weekly windows, anchor on `date -Iseconds` and compute the cutoff in UTC.
- For TVL trends, compare the latest chain TVL to the nearest data point at the start of the window.
- When summarizing L2s, focus on rollup client changes, bridge flows, and fork-activation behavior, not just headline TVL.

## Useful endpoints observed
- `https://api.llama.fi/protocols`
- `https://api.llama.fi/v2/historicalChainTvl/<ChainName>`
- `https://l2beat.com/api/scaling/summary`
- `https://api.github.com/repos/<owner>/<repo>/commits?since=<ISO>`
- `https://api.github.com/repos/<owner>/<repo>/pulls/<number>`

## Pitfalls
- RSS/homepage fetches may return 403 even when the canonical feed exists.
- Some sites expose only HTML; in those cases, extract titles/meta or use official APIs instead of relying on feeds.
- TVL summaries often move faster than article coverage; cite the metric directly if it is the strongest signal.
