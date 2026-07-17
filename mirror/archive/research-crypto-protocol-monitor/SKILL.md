---
name: crypto-protocol-monitor
description: Monitor Ethereum, Bitcoin, and alternative L1/L2 protocols for protocol upgrades, DeFi developments, scaling solutions, regulatory news, security incidents, and developer tools. Produce structured weekly briefings for builders.
category: research
aliases: [crypto-weekly-briefing, ethereum-monitor, bitcoin-protocol-watch, defi-infrastructure-monitor]
---

# Crypto Protocol Monitoring & Weekly Briefing

This is the **class-level skill** for monitoring blockchain protocol developments across Ethereum, Bitcoin, and alternative L1/L2 ecosystems. It covers protocol upgrades, DeFi infrastructure, scaling solutions, regulatory developments, security incidents, and developer tool updates.

**Trigger:** User requests weekly crypto protocol updates, needs monitoring of specific chains/protocols, wants security incident alerts, or requires structured briefings on blockchain infrastructure developments for builders/developers.

---

## Core Monitoring Targets

### Protocol Layers
- **Ethereum**: EIPs, core dev updates, EF blog, EthResearch, Vitalik's blog
- **Bitcoin**: BIPs, Bitcoin Core mailing list, Bitcoin Magazine technical sections
- **L2 Scaling**: Arbitrum, Optimism, Base, Polygon, zkSync, Starknet, Mantle
- **Alternative L1s**: Solana, Avalanche, Cosmos ecosystems, Sui, Aptos

### Infrastructure Categories
1. **Protocol Upgrades**: EIPs, BIPs, network upgrades, hard forks, devnet progress
2. **DeFi & Infrastructure**: New protocols, TVL shifts, lending/borrowing innovations, oracle updates
3. **Scaling Solutions**: Rollup tech, bridging infrastructure, L2Beat metrics
4. **Regulatory & Institutional**: ETF news, regulatory rulings, institutional adoption, custody solutions
5. **Security**: Exploits, hacks, audit findings, vulnerability disclosures
6. **Developer Tools**: SDKs, frameworks, testing tools, account abstraction updates

---

## Standard Workflow

### Step 1: Gather Protocol Development Data

**Ethereum GitHub:**
```bash
# Check ethereum/go-ethereum recent commits
curl -s "https://api.github.com/repos/ethereum/go-ethereum/commits?per_page=15" | grep -E '"message"|"html_url"|"date"'

# Check EIP repository
curl -s "https://api.github.com/repos/ethereum/EIPs/commits?per_page=15" | grep -E '"message"|"html_url"|"date"'
```

**Bitcoin GitHub:**
```bash
# Check bitcoin/bitcoin recent commits
curl -s "https://api.github.com/repos/bitcoin/bitcoin/commits?per_page=15" | grep -E '"message"|"html_url"|"date"'
```

**L2 Development:**
```bash
# Optimism
curl -s "https://api.github.com/repos/ethereum-optimism/optimism/commits?per_page=10" | grep -E '"message"|"date"'

# zkSync (if active)
curl -s "https://api.github.com/repos/matter-labs/zksync/commits?per_page=10"
```

### Step 2: Gather News & Analysis

**RSS Feeds (prioritize technical sections):**
```bash
# Decrypt (technical/crypto infrastructure)
curl -s "https://decrypt.co/feed" | grep -E "<title>|<link>|<pubDate>|<description>"

# The Block (if accessible)
curl -s "https://www.theblock.co/rss/news"

# Coindesk (may require redirect handling)
curl -sL "https://www.coindesk.com/arc/outboundfeeds/rss/"
```

**Key Sources to Check:**
- Ethereum Foundation blog: `https://blog.ethereum.org/` (RSS/feed endpoint is currently `https://blog.ethereum.org/en/feed.xml`, not `/rss.xml`)
- EthResearch: `https://ethresear.ch/`
- Bitcoin Magazine technical sections
- Bitcoin Optech newsletter: `https://bitcoinops.org/en/newsletters/` (high-signal technical coverage for BIPs, wallet/interoperability changes, and node/networking proposals when the raw mailing-list thread is harder to summarize)
- L2Beat: `https://l2beat.com/` (scaling metrics; `https://l2beat.com/api/scaling/summary` returns a dict keyed by project slug, not a flat list)
- DeFiLlama: `https://api.llama.fi/` (TVL data)
- GitHub releases for clients/rollups/SDKs: Prysm, Erigon, Nitro, Optimism, zkSync, Solana SDKs (often better than RSS/blogs for operator-relevant release notes)

### Step 3: Extract TVL & Market Metrics

**DeFiLlama API:**
```bash
# Get chain TVL data
curl -s "https://api.llama.fi/chains" | head -500

# Get specific chain (e.g., Ethereum, Base, Arbitrum)
curl -s "https://api.llama.fi/chains/Ethereum"

# Get protocol data
curl -s "https://api.llama.fi/protocols" | head -2000
```

### Step 4: Security Incident Tracking

**Monitor for:**
- Exploit announcements (Kelp DAO, Solv Protocol, etc.)
- Bridge vulnerabilities (LayerZero, Chainlink, etc.)
- Audit findings from major firms
- DAO governance responses to incidents

**Search patterns:**
```bash
# Check Decrypt for security headlines
curl -s "https://decrypt.co/feed" | grep -i -E "hack|exploit|vulnerability|audit|security"

# Check for exploit relief/DAO responses
curl -s "https://decrypt.co/feed" | grep -i -E "dao votes|treasury|exploit relief"
```

### Step 5: Regulatory & Institutional Developments

**Track:**
- ETF approvals/rejections
- Regulatory rulings (SEC, ECB, etc.)
- Institutional adoption (custody solutions, banking charters)
- Stablecoin legislation

**Search patterns:**
```bash
# Regulatory news
curl -s "https://decrypt.co/feed" | grep -i -E "etf|sec|regulation|institutional|custody|stablecoin"
```

### Step 6: Compile Structured Report

**Output Format:**
```markdown
# Crypto Protocol Weekly Report
**Date Range:** [YYYY-MM-DD] – [YYYY-MM-DD]

---

## Top Critical Developments

### 1. [Headline]
[Description with technical detail]
**Impact:** [High/Medium/Low] – [Brief assessment]
**Source:** [Primary source link]

[Repeat for 3-5 developments]

---

## Watch This Space: [Emerging Trend]
[Analysis of emerging trend with 12-18 month outlook]

---

## Regulatory & Institutional Briefs
- Bullet points on regulatory developments
- Institutional adoption news
- ETF/custody updates

---

## Action Items for Developers

| Priority | Action |
|----------|--------|
| **HIGH** | [Urgent security patches, migrations] |
| **MEDIUM** | [Compatibility updates, monitoring] |
| **LOW** | [Long-term planning items] |

---

## TVL & Market Metrics (as of [date])
- **Chain/Protocol:** $X.XXB TVL
- **Notable shifts:** [Explain significant changes]

*Data: DeFiLlama*

---

*Report generated autonomously via cron job. Primary sources linked throughout.*
```

---

## Common Pitfalls

1. **Relying on paywalled content** - Always prioritize primary sources and free-tier accessible links
2. **Missing security context** - Security stories often show up first on news wires, but the report should anchor to protocol/vendor postmortems or official advisories when available
3. **Overlooking source endpoint changes** - The Ethereum Foundation blog feed is currently `/en/feed.xml`; do not assume `/rss.xml`
4. **Misreading L2Beat API shape** - `https://l2beat.com/api/scaling/summary` returns a project-slug-keyed object under `projects`, not a flat array
5. **Not distinguishing TVL impact** - Exploits affect TVL differently than organic shifts or market-wide risk-off moves
6. **Skipping protocol-vs-price separation** - A weekly builder briefing should separate code/protocol progress from macro-driven token/liquidity moves
7. **Using generic news sources** - Prioritize technical sections of crypto news sites
8. **Not checking GitHub directly** - RSS feeds may lag actual commits/merges
9. **Treating feeds as the only primary source** - for client/operator changes, GitHub Releases pages are often the clearest canonical source within the 7-day window
10. **Using L2Beat/API calls without a browser-like User-Agent** - some endpoints may reject default library clients; prefer `requests`/`curl` with an explicit UA before assuming the endpoint is unavailable

---

## Verification Checklist

After compiling report, verify:
- [ ] Date range is explicit (7-day window)
- [ ] 3-5 critical developments with impact assessment
- [ ] "Watch this space" trend identified with timeline
- [ ] Primary sources linked (GitHub, official blogs, APIs)
- [ ] No paywalled content as primary sources
- [ ] Action items categorized by priority
- [ ] TVL data sourced and dated
- [ ] Builder-focused language (avoid hype, focus on implementation)
- [ ] Length: 400-600 words max

---

## Example Commands

```bash
# Full weekly monitoring workflow
DATE_RANGE="May 4, 2026 – May 11, 2026"

# 1. Check Ethereum EIPs
curl -s "https://api.github.com/repos/ethereum/EIPs/commits?per_page=15" | grep '"message"'

# 2. Check Bitcoin Core
curl -s "https://api.github.com/repos/bitcoin/bitcoin/commits?per_page=15" | grep '"message"'

# 3. Check L2s
curl -s "https://api.github.com/repos/ethereum-optimism/optimism/commits?per_page=10" | grep '"message"'

# 4. Get news
curl -s "https://decrypt.co/feed" | grep -E "<title>|<link>" | head -60

# 5. Get TVL data
curl -s "https://api.llama.fi/chains" | head -500

# 6. Check security
curl -s "https://decrypt.co/feed" | grep -i "exploit\|hack\|vulnerability"
```

---

## Related Skills

- `frontier-stack-evaluation` - Broader tech stack evaluation (includes some blockchain)
- `polymarket` - Query prediction markets on crypto events
- `blogwatcher` - RSS/Atom feed monitoring (general purpose)
- `adaptive-research-system` - Research methodology framework

---

## Support Files

- `references/sources.md` - Curated list of high-signal crypto news sources and APIs with search patterns
- `scripts/monitor-weekly.sh` - Automated weekly monitoring script that gathers GitHub commits, RSS feeds, and TVL data

---

*Created: May 2026*
*Based on: Weekly crypto protocol monitoring workflow for builder-focused briefings*
