---
name: person-monitor
description: Monitor public intellectuals, researchers, and thought leaders who don't self-publish — people whose output appears in other people's media (interviews, podcast appearances, op-eds, talks). Feed discovery, cron job setup, and briefing delivery.
category: research
aliases: [thought-leader-monitor, public-intellectual-tracker, person-of-interest-feed]
---

# Person Monitor

Monitor public figures whose output is scattered across external media rather than their own blog/feed. This is the "appears in other people's media" pattern — talks, interviews, podcast guest spots, op-eds in major outlets, arXiv papers, music releases, etc.

**Trigger:** User says "keep an eye on [person]", "track [person]'s appearances", "make a cron for [person]", "find [person]'s feeds", or wants to set up monitoring for a public intellectual/thought leader.

**When NOT to use:** The person has a single canonical blog with RSS — use `blogwatcher` instead.

---

## Feed Discovery Procedure

### Step 1: Check for personal site + RSS

```bash
curl -sL "https://[personname].com" | grep -ioP 'href="[^"]*(rss|feed|atom|xml)[^"]*"'
```

- If RSS/Atom found → add to blogwatcher, skip to Step 4
- If no RSS but site exists → note as secondary manual-check source

### Step 2: Google News RSS (primary catch-all)

This is the **single best feed** for "appears-in-others-media" figures:

```
https://news.google.com/rss/search?q=[Person+Name]&hl=en-US&gl=US&ceid=US:en
```

- Catches articles, interviews, podcast coverage, event talks, music releases
- Returns items across all outlets (Guardian, Atlantic, NYT, TechCrunch, university news, etc.)
- No API key needed, works via simple curl

### Step 3: Supplementary feeds (person-dependent)

Check these if relevant to the person's output:

- **The Atlantic** (contributing writers): `https://www.theatlantic.com/author/[slug]/` — no author-specific RSS, but Google News catches their pieces
- **arXiv** (researchers): `https://arxiv.org/search/?query=au:[Name]&searchtype=author` — no author RSS, but papers are infrequent; Google News usually catches them
- **YouTube** (if they have a channel): `https://www.youtube.com/feeds/videos.xml?channel_id=[ID]` — many public intellectuals don't have personal channels
- **Spotify/Apple Podcasts** (if they host a podcast): search by name — many "appear on" podcasts rather than hosting their own
- **Substack**: `https://substack.com/@[handle]` — check if active

### Step 4: Assess cadence

Before setting up a cron, determine how often the person appears publicly:

- **1-2 items/quarter** → monthly cron is sufficient
- **3-5 items/quarter** → weekly cron (most common for public intellectuals)
- **Daily+ output** → daily cron (only for prolific self-publishers)

---

## Cron Job Setup Pattern

### Standard weekly person-monitor cron

```
action: create
schedule: every monday 9:00
prompt: |
  Fetch Google News RSS for [Person Name]:
  curl -sL "https://news.google.com/rss/search?q=[Person+Name]&hl=en-US&gl=US&ceid=US:en"
  
  Extract new items published in the last 7 days.
  For each item, provide:
  - Title
  - Source outlet
  - Date
  - 1-2 sentence summary (fetch the article if accessible)
  
  If no new items, say "No new [Person Name] appearances this week."
  
  Format as a compact Telegram-friendly briefing.
```

### Thematic monitor (optional enhancement)

If the user has specific philosophical alignment with the person, add a relevance filter:

```
Flag items that touch on: [user's key themes]
Downrank: [topics user doesn't care about]
```

---

## Delivery Format

For Telegram delivery, keep it compact:

```
🧠 [Person Name] — Weekly Monitor

📰 [N] new appearances this week:

1. **Title** — Outlet, Date
   Brief summary sentence.

2. **Title** — Outlet, Date
   Brief summary sentence.

📌 Thematic relevance: [if any items align with user's framework]

---
No new appearances = "No new [Name] items this week. 🤷"
```

---

## Pitfalls

1. **Don't assume a personal YouTube channel exists** — most public intellectuals appear *on* other channels, they don't run their own
2. **Don't rely on Substack** — many have placeholder accounts with no posts; verify activity before adding
3. **Google News RSS may have Google-proxy URLs** — the actual article URL is obscured; use the title + source to find the canonical URL if you need full text
4. **The Atlantic has no author-specific RSS** — don't waste time trying to construct one; Google News catches their pieces
5. **arXiv author feeds don't exist** — you can search by author but there's no subscription RSS; rely on Google News
6. **Static personal sites without RSS** are common for this class of person — don't treat the absence of RSS as a failure, just note it as a manual-check source
7. **Cadence varies wildly** — a university professor might have 1 talk/month, a pundit might have 5 appearances/week. Assess before choosing cron frequency.

---

## Related Skills

- `blogwatcher` — for people who DO have their own RSS/blog (use instead of this skill when applicable)
- `adaptive-research-system` — methodology for building monitoring systems that evolve with feedback
- `frontier-stack-tech-review` — for technology-specific monitoring (overlaps when the person is a tech figure)
- `regional-news-monitoring` — for geographic/community-specific news monitoring

---

## Reference Files

- `references/jaron-lanier-feeds.md` — Full feed discovery research for Jaron Lanier (May 2026). Template for how to assess a person's feed landscape.

---

*Created: May 2026*
*Origin: Jaron Lanier feed discovery session — classic "appears in others' media" pattern*
