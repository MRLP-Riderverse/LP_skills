# High-Signal Crypto Protocol Monitoring Sources

## Primary Sources (GitHub)

### Ethereum Ecosystem
- **go-ethereum**: https://api.github.com/repos/ethereum/go-ethereum/commits
- **EIPs**: https://api.github.com/repos/ethereum/EIPs/commits
- **EF Blog**: https://blog.ethereum.org/
- **EthResearch**: https://ethresear.ch/
- **Vitalik's Blog**: https://vitalik.ca/

### Bitcoin
- **Bitcoin Core**: https://api.github.com/repos/bitcoin/bitcoin/commits
- **Bitcoin Magazine**: Technical sections only
- **Bitcoin Core Mailing List**: https://lists.linuxfoundation.org/pipermail/bitcoin-dev/

### Layer 2 Scaling
- **Optimism**: https://api.github.com/repos/ethereum-optimism/optimism/commits
- **Arbitrum**: https://api.github.com/repos/OffchainLabs/arbitrum/commits
- **zkSync**: https://api.github.com/repos/matter-labs/zksync/commits
- **Polygon**: https://api.github.com/repos/0xPolygon/polygon-edge/commits
- **Base**: Check Coinbase announcements and Base ecosystem repos

## News & Analysis (RSS Feeds)

### Technical News (Priority)
- **Decrypt**: https://decrypt.co/feed
- **The Block**: https://www.theblock.co/rss/news (may require redirect handling)
- **Coindesk**: https://www.coindesk.com/arc/outboundfeeds/rss/ (may require redirect handling)

### Security-Focused
- **SlowMist**: https://slowmist.medium.com/feed/
- **CertiK**: Check blog RSS
- **OpenZeppelin**: https://blog.openzeppelin.com/feed/

## APIs & Data Sources

### TVL & Market Data
- **DeFiLlama Chains**: https://api.llama.fi/chains
- **DeFiLlama Protocols**: https://api.llama.fi/protocols
- **L2Beat**: https://l2beat.com/ (web scraping required)

### Protocol-Specific APIs
- **Ethereum**: Various RPC endpoints
- **Bitcoin**: Blockchain explorers, mempool.space API

## Search Patterns for Monitoring

### Security Incidents
```bash
curl -s "https://decrypt.co/feed" | grep -i -E "hack|exploit|vulnerability|audit|security"
```

### Regulatory/Institutional
```bash
curl -s "https://decrypt.co/feed" | grep -i -E "etf|sec|regulation|institutional|custody|stablecoin"
```

### DeFi Infrastructure
```bash
curl -s "https://decrypt.co/feed" | grep -i -E "defi|tvl|lending|protocol|migration"
```

## Key Indicators to Track

### Protocol Upgrades
- EIP status changes (Draft → Review → Final → Merged)
- SFI (Standard for Inclusion) designations
- CFI (Consider for Inclusion) markings
- Devnet deployment announcements
- Hard fork coordination calls

### Security
- Exploit announcements with dollar amounts
- Bridge vulnerabilities (LayerZero, Chainlink, etc.)
- DAO treasury responses
- Court orders/legal complications
- Migration decisions (e.g., Solv → Chainlink)

### Developer Experience
- Documentation changes affecting compatibility (e.g., Bitcoin Core `script_flags`)
- SDK/framework releases
- Account abstraction updates (ERC-4337)
- Testing tool improvements

### Institutional Adoption
- Banking charter applications
- ETF filings/approvals
- Custody solution launches
- Major corporate treasury moves

## Date Range Best Practices

- **Weekly briefings**: 7-day rolling window
- **Always specify**: `May 4, 2026 – May 11, 2026` format
- **TVL data timestamp**: Note exact date of snapshot
- **News article dates**: Use `pubDate` from RSS, verify against article metadata

## Output Guidelines

- **Word count**: 400-600 words max
- **Tone**: Builder-focused, technical but accessible
- **Sources**: Link to primary sources, avoid paywalls
- **Structure**: Date range → Top 3-5 developments → Watch space → Action items → TVL metrics
