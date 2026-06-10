# Jaron Lanier — Feed Research (May 2026)

## Person Profile

- **Who:** "Creator of VR" / "Godfather of Virtual Reality", computer scientist, musician, tech ethicist, Microsoft Researcher
- **Key thesis:** "There is no AI, just humans" — AI as human collaboration endpoints, like Wikipedia
- **Philosophical alignment with user:** Data dignity, human-first tech, cultural resilience, community sovereignty
- **Output pattern:** Public intellectual who *appears in other people's media* — talks, interviews, podcast guest spots, op-eds. Not a self-publisher.
- **Cadence:** ~3-4 public appearances per quarter (talks, interviews, articles, music)

## Feed Assessment

### 🟢 Google News RSS (PRIMARY — USE THIS)

```
https://news.google.com/rss/search?q=Jaron+Lanier&hl=en-US&gl=US&ceid=US:en
```

**Verified working.** Catches:
- University talks (Brown Apr 2026, TCNJ Nov 2025, Arcata/Humboldt Apr 2026)
- Podcast coverage (The Ten Reckonings Jan 2026 — TechRadar)
- Press interviews (Guardian, Atlantic, NYT op-eds, MusicTech, Business Insider)
- Music releases (Instruments of Change album/video May 2026, Santa Cruz Symphony Apr 2026)
- Film/entertainment (Natasha Lyonne AI film collaboration Apr 2025)

### 🟡 jaronlanier.com (SECONDARY — manual check only)

- Static HTML, no RSS/Atom feed
- Has a "general" page linking to press appearances
- Manually maintained bibliography, not recent-first
- Useful for: finding older canonical pieces, arXiv paper links

### 🟡 The Atlantic (contributing writer)

- Author page: `https://www.theatlantic.com/author/jaron-lanier/` (200 OK)
- **No author-specific RSS** — general feed only at `/feed/all/`
- Google News catches Atlantic pieces anyway

### 🟡 arXiv (occasional co-author)

- Search: `https://arxiv.org/search/?query=Jaron+Lanier&searchtype=author`
- Papers are infrequent; Google News catches major ones
- Found on jaronlanier.com: arxiv.org/abs/2211.05875, arxiv.org/abs/2310.17838, and others

### 🔴 YouTube — no personal channel

- `@JaronLanier` → 404
- `c/JaronLanier` → 404
- Appears *on* other channels (StarTalk with Neil deGrasse Tyson, etc.)
- YouTube search RSS doesn't work for arbitrary queries

### 🔴 "The Ten Reckonings" podcast (Jan 2026)

- RSS feed not found on common platforms (megaphone, buzzsprout)
- May be platform-locked (Apple/Spotify only)
- Google News caught the TechRadar coverage of it

### 🔴 Substack

- `@jaronlanier` → exists (HTTP 200) but appears to be placeholder/inactive
- Not a reliable source

## Recommended Cron Setup

**Frequency:** Weekly (Monday mornings)
**Primary feed:** Google News RSS
**Filter:** Items from last 7 days only
**Thematic relevance tags:** data dignity, human collaboration, AI accountability, cultural resilience, music+tech
**Deliver:** Compact Telegram briefing

## Key Works (for context)

- "There Is No A.I." — The New Yorker (canonical version of his core thesis)
- *You Are Not a Gadget* (2010) — early critique of algorithmic culture
- *Dawn of the New Everything* (2017) — VR memoir
- *Ten Arguments for Deleting Your Social Media Accounts Right Now* (2018)
- "Data Dignity" concept — the economic-justice version of what user's Acadie.sol is building
- "Instruments of Change" (2026) — music album/video series
- Santa Cruz Symphony compositions (2026)

---
*Researched: May 31, 2026*
