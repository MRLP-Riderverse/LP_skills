---
name: regional-news-monitoring
description: Monitor regional news sources (Acadian/NB example), generate weekly briefings, and identify consulting opportunities from news patterns.
category: research
tags: [news, monitoring, regional, acadian, briefing, rss, telegram]
version: 1.0
---

# Regional News Monitoring & Weekly Briefing

**Trigger:** User asks for news monitoring from a specific region, weekly news summaries, or identifying business/consulting opportunities from local news patterns.

**Context:** 
- This workflow was developed for monitoring Acadian/Nouveau-Brunswick region (Péninsule acadienne, Caraquet, Bathurst)
- Sources in both French and English required
- Output format: Weekly summary appended to archive file + Telegram notification
- Key insight: When browser tools unavailable, use RSS feeds + curl + regex parsing

## Sources by Region

### Acadian/NB Region (Example)
| Source | Language | URL | Type |
|--------|----------|-----|------|
| CBC New Brunswick | EN | https://www.cbc.ca/news/canada/new-brunswick | Mainstream |
| Radio-Canada Acadie | FR | https://radio-canada.ca/aci | Public broadcaster |
| Acadie Nouvelle | FR | https://www.acadienouvelle.com/ | Local daily |
| Google News RSS | FR/EN | `https://news.google.com/rss/search?q=Acadie+Nouveau-Brunswick&hl=fr-CA&gl=CA&ceid=CA:fr` | Aggregator |

### Acadiana / Louisiana Cajuns
| Source | Language | Query / URL | Type |
|--------|----------|-------------|------|
| Google News RSS | EN | `"Cajun" "Louisiana" after:YYYY-MM-DD` | Aggregator |
| Google News RSS | EN | `Acadiana Lafayette Louisiana after:YYYY-MM-DD` | Aggregator |
| The Advocate | EN | https://www.theadvocate.com | Regional daily |
| WWLTV | EN | https://www.wwltv.com | NOLA TV |
| Lafourche Gazette | EN | Local parish paper | Community |
| KPEL / KADN | EN | Acadiana radio | Local radio |

**Note:** French-language RSS queries for Cadiens return near-zero results. See `references/acadiana-nouvelle-aquitaine-sources.md`.

### Nouvelle-Aquitaine / Old Roots Region
| Source | Language | Query / URL | Type |
|--------|----------|-------------|------|
| Google News RSS | FR | `Dax Landes after:YYYY-MM-DD` | Dax-specific |
| Google News RSS | FR | `Tarbes Hautes-Pyrénées after:YYYY-MM-DD` | Tarbes-specific |
| Google News RSS | FR | `Béarn Basque Pau after:YYYY-MM-DD` | Pau/Béarn triangle |
| Google News RSS | FR | `Nouvelle-Aquitaine after:YYYY-MM-DD` | Regional |
| Sud Ouest | FR | https://www.sudouest.fr | Regional daily |
| La Dépêche | FR | https://www.ladepeche.fr | Toulouse/SW daily |
| La Semaine des Pyrénées | FR | https://www.lasemainedespyrenees.fr | Pyrénées local |
| La République des Pyrénées | FR | https://www.larepubliquedespyrenees.fr | Pau/Béarn |
| Placéco | FR | https://www.placeco.fr | Béarn economy |
| AquitaineOnLine | FR | https://www.aquitaineonline.com | NA tech/business |

**Note:** Gascon/Occitan language queries return zero results. The absence itself is a finding. See `references/acadiana-nouvelle-aquitaine-sources.md`.

### General Pattern for Any Region
1. Identify 2-3 mainstream sources (CBC, CTV, Global for Canada)
2. Identify 2-3 local/regional sources (community papers, local radio)
3. Find RSS feeds (often `/rss`, `/feed`, or via Google News RSS)
4. Use Google News RSS as fallback: `https://news.google.com/rss/search?q=[REGION_KEYWORDS]&hl=[LANG]&gl=[COUNTRY]&ceid=[LOCALE]`

## Workflow

### Step 0: Compare Against Local Notes Before Writing
When the user wants a "what might I not know yet" report, always do a local novelty pass *before* summarizing:
- Search `~/Documents/Notes/notecore/inbox/QuickThoughts.txt` with simple, broad keywords first
- Search GBrain with `PATH="$HOME/.bun/bin:$PATH" gbrain search "<keyword>"`
- Use multiple queries for the same topic if needed (broad topic, proper noun, related phrase)
- Treat **no hit** as a strong signal the topic is likely new to the user
- Treat weak or partial hits as "possibly related" rather than known
- Prefer a short Telegram-friendly report with only the highest-signal items
- If a topic is only supported by headline-level evidence, say so and avoid overclaiming details

See `references/headline-digest-comparison.md` for the compact comparison recipe and query heuristics.

### Step 1: Fetch News from Multiple Sources
```python
from hermes_tools import terminal
import re

# English sources (CBC example)
result = terminal('curl -s -A "Mozilla/5.0" -L "https://www.cbc.ca/news/canada/new-brunswick" --connect-timeout 15')
content = result.get('output', '')

# Extract headlines from JSON metadata
headlines = re.findall(r'"headline"\s*:\s*"([^"]+)"', content)

# French sources (Google News RSS)
result = terminal('curl -s -A "Mozilla/5.0" -L "https://news.google.com/rss/search?q=Acadie+Nouveau-Brunswick&hl=fr-CA&gl=CA&ceid=CA:fr"')
rss_content = result.get('output', '')

# Parse RSS items
items = re.findall(r'<item>(.*?)</item>', rss_content, re.DOTALL)
```

**If the RSS shortlist is noisy:**
1. Run a second pass with narrower combinations such as `Caraquet`, `Bathurst`, `Péninsule acadienne`, and `Nouveau-Brunswick` rather than single broad terms.
2. Search the local publication directly with its site search (for example `?s=Caraquet` on *Acadie Nouvelle*).
3. Open the matched article page and pull `og:title`, `og:description`, and `article:published_time` to build a grounded summary.
4. Prefer these source-grounded items over ambiguous aggregator hits.

### Step 2: Categorize Stories
Categorize each story into:
- **Economic**: fisheries, tourism, local business, employment, trade
- **Infrastructure**: connectivity, water, energy, transportation, healthcare
- **Cultural/Identity**: language, heritage, demographics, community events
- **Environmental**: weather, fisheries, forestry, conservation, climate

### Step 3: Generate Weekly Summary
Format following existing archive conventions:
```
================================================================================
ACADIAN NEWS SUMMARY - WEEK OF [DATE RANGE]
Péninsule acadienne, Caraquet, Bathurst, Nouveau-Brunswick
Generated: [Date]
================================================================================

[DATE]
• [Headline in original language]
 - English translation if French
 - Key details (who, what, when, where)
 - Relevance to region
 - Source: [Publication]

[Repeat for 3-5 top stories per category]

================================================================================
CONSULTING OPPORTUNITY - TECH GAPS IDENTIFIED
================================================================================

1. [CATEGORY NAME]
 - Problem statement from news
 - Opportunity: [solution type]
 - Market: [target customers]

[Repeat for 4-8 opportunities]
```

### Step 4: Append to Archive

**IMPORTANT: Do NOT use `read_file()` output as the source for a full-file rewrite.** The normal `read_file` tool prefixes lines like `12|...`. If you write that content back unchanged, you will corrupt the archive with baked-in line numbers.

**Preferred approach (cron-safe, no python pipe):**
```bash
cat >> /path/to/archive/highlights.txt << 'EOF'
[summary content here]
EOF
```

**Alternative (when you need to read+modify existing content):**
```bash
# Read raw content (no line prefixes)
cat /path/to/archive/highlights.txt > /tmp/backup.txt
# Then use write_file with modified content
```

**If `execute_code` is available (non-cron context):**
```python
from hermes_tools import write_file, terminal

file_path = '/path/to/archive/highlights.txt'

# Use raw shell read, NOT read_file() which adds line prefixes
result = terminal(f'cat {file_path}')
existing_content = result.get('output', '')

# Append new summary
new_content = existing_content + "\n" + summary

# Write back
write_file(file_path, new_content)
```

**⚠️ Cron pitfall:** The `python3 - <<'PY'` pattern and `curl | python3` pipes are blocked in cron mode. Always use `cat >> file << 'HEREDOC'` for appends in cron jobs.

### Step 5: Send Telegram Notification
```python
from hermes_tools import terminal

telegram_script = "/home/midnight/.hermes/hermes-agent/scripts/telegram_notify.py"
top_headline = "🔴 [REGION] NEWS BRIEF - [Date]\n\nTop Story: [Headline]\n\nOther highlights:\n• [Story 2]\n• [Story 3]\n\nFull archive: [file_path]\n\nSources: [List]"

# In cron jobs, prefer a dry-run first when formatting is new or the message contains paths/links.
terminal(f'python3 {telegram_script} --target telegram --dry-run "{top_headline}"')
result = terminal(f'python3 {telegram_script} --target telegram "{top_headline}"')
```

## Key Insights & Pitfalls

### ✅ What Works:
- **RSS feeds when browser unavailable**: Google News RSS provides reliable access even when direct site scraping fails
- **Multiple source triangulation**: Cross-reference between English and French sources for complete picture
- **Structured categorization**: Economic/Infrastructure/Cultural/Environmental framework captures all story types
- **Consulting opportunity extraction**: News gaps reveal tech opportunities (connectivity, traceability, data management)
- **Telegram integration**: Use existing `telegram_notify.py` script for notifications
- **Local novelty filtering**: Compare headlines against QuickThoughts + GBrain first; no hit is a strong signal of newness
- **Local-site search as grounding fallback**: When Google News RSS gives a promising headline but weak article resolution, search the local publication directly (for example `https://www.acadienouvelle.com/?s=<keyword>`) and extract `og:title`, `og:description`, and `article:published_time` from the article page. This gives short, source-grounded summaries without needing a browser session.

### ⚠️ Pitfalls to Avoid:
- **JavaScript-heavy sites**: Modern news sites (Radio-Canada, CBC) use React/frameworks - can't parse HTML directly, need JSON metadata or RSS. In practice (June 2026), CBC and Radio-Canada both returned empty/null from curl — the JSON metadata extraction documented in `references/acadian-nb-sources.md` is unreliable in cron/headless contexts. Prefer RSS + WordPress site search.
- **Date parsing**: RSS dates in GMT, convert to local timezone; some items may have no date
- **Google News RSS limitations**: Returns historical results mixed with recent - filter by date, sort by recency. In practice, a June 2026 query for "Acadie Nouveau-Brunswick" returned items from 2014–2025 mixed with current ones. Always parse `<pubDate>` and filter ≤7 days. Discard items older than the reporting window before categorization.
- **Archive format consistency**: Follow existing format in target file; don't invent new structure
- **Archive corruption via line-numbered reads**: Never feed `read_file()` presentation output directly into `write_file()` for a full-file rewrite; strip prefixes or use raw file I/O first
- **Language handling**: Preserve original language headlines, provide translations for cross-reference
- **Headline-only overreach**: If article body resolution fails, summarize conservatively and label claims as headline-level evidence only
- **Cron delivery semantics**: Cron auto-delivery does not replace an explicitly requested secondary Telegram ping; when the task asks for both, send the extra brief separately via the notifier script
- **Over-broad keyword collisions**: Queries like `Bathurst` and `Acadia` can pull in irrelevant results from Australia, Nova Scotia, or product/company names. Use regional combinations (`Caraquet`, `Bathurst`, `Péninsule acadienne`, `Nouveau-Brunswick`) and verify locality against the source site before promoting a headline into the weekly top stories.
- **Cron security blocks `execute_code` and `curl|python3` pipes**: Cron jobs block `execute_code` entirely (policy restriction) and flag `curl | python3` pipe patterns as high-risk (tirith guard). Workaround: use raw shell heredoc for file appends (`cat >> file << 'EOF'`) and `grep -oP` / `sed` for HTML extraction instead of piping to python. The `python3 - <<'PY'` pattern from Step 4 of the workflow also fails under cron — use `cat >> file << 'HEREDOC'` instead.
- **Subagent timeouts under cron**: `delegate_task` subagents with heavy terminal/web toolsets may time out (600s default) when fetching multiple RSS feeds sequentially. Prefer direct `terminal()` calls from the parent agent for news fetching — it's faster and avoids the timeout risk.

### 🔑 Critical Techniques:
| Challenge | Solution |
|-----------|----------|
| Site uses JavaScript rendering | Use RSS feeds or extract JSON metadata from HTML |
| Need both French and English sources | Google News RSS with locale params + direct source scraping |
| Date filtering in RSS | Parse `<pubDate>` and calculate days ago, filter threshold |
| Telegram notification | Use `~/.hermes/hermes-agent/scripts/telegram_notify.py` with `--target telegram` |
| WordPress sites (Acadie Nouvelle, CHNC) return no JSON/RSS | `curl -s -A "Mozilla/5.0" "https://www.acadienouvelle.com/?s=KEYWORD" \| grep -oP '<h2[^>]*>.*?</h2>' \| sed 's/<[^>]*>//g'` — extracts headlines reliably from WordPress search pages |
| Cron blocks `execute_code` and `curl\|python3` pipes | Use raw shell: `cat >> file << 'HEREDOC'` for appends, `grep -oP` + `sed` for extraction, avoid piping curl to python interpreters |
| Radio-Canada/CBC return empty JSON from curl | Fall back to Google News RSS (reliable) + WordPress site search; don't depend on CBC/R-C JSON metadata in cron context |

## Example Commands

```bash
# Use the fetch_news.py script (recommended)
python3 ~/.hermes/skills/research/regional-news-monitoring/scripts/fetch_news.py --region acadian --days 7

# Custom RSS feed
python3 ~/.hermes/skills/research/regional-news-monitoring/scripts/fetch_news.py --rss "https://news.google.com/rss/search?q=..." --days 7

# Fetch CBC New Brunswick headlines manually
curl -s -A "Mozilla/5.0" -L "https://www.cbc.ca/news/canada/new-brunswick" | grep -o '"headline":"[^"]*"'

# Fetch Google News RSS for region
curl -s -L "https://news.google.com/rss/search?q=Acadie+Nouveau-Brunswick&hl=fr-CA&gl=CA&ceid=CA:fr"

# Send Telegram notification
python3 ~/.hermes/hermes-agent/scripts/telegram_notify.py --target telegram "Message text"

# Append to archive
cat existing.txt > archive.txt
echo "$new_summary" >> archive.txt
```

## Consulting Opportunity Framework

When extracting consulting opportunities from news, look for:

1. **Connectivity Gaps**: Rural broadband, cellular coverage, digital divide
2. **Data Management**: Supply chain tracking, regulatory compliance, market transparency
3. **Infrastructure Monitoring**: Water systems, energy grids, transportation networks
4. **Cultural/Linguistic Tech**: French-language platforms, heritage preservation, community engagement
5. **Environmental Monitoring**: Weather tracking, resource management, conservation compliance
6. **Service Access**: Healthcare, education, government services in rural areas

Format each opportunity as:
- **Problem**: Specific gap identified in news
- **Opportunity**: Type of solution (platform, monitoring, automation)
- **Market**: Who would pay (municipalities, businesses, community orgs)

## Resources & Sources

### Support Files
- **Acadian/NB Sources**: `references/acadian-nb-sources.md` — Detailed source list, keywords, and session notes
- **Fetch Script**: `scripts/fetch_news.py` — Reusable Python script for fetching regional news
- **Digest comparison recipe**: `references/headline-digest-comparison.md` — Local-notes/GBrain novelty check and concise Telegram report rules
- **Acadiana & Nouvelle-Aquitaine Sources**: `references/acadiana-nouvelle-aquitaine-sources.md` — RSS queries, key sources, cross-relation patterns for the "same patch" Acadian roots triangle (Acadie ↔ Acadiana ↔ Nouvelle-Aquitaine)

### External Sources
- **Google News RSS**: `https://news.google.com/rss/search?q=[KEYWORDS]&hl=[LANG]&gl=[COUNTRY]`
- **CBC New Brunswick**: https://www.cbc.ca/news/canada/new-brunswick
- **Radio-Canada Acadie**: https://radio-canada.ca/aci
- **Acadie Nouvelle**: https://www.acadienouvelle.com/
- **Telegram Notify Script**: `~/.hermes/hermes-agent/scripts/telegram_notify.py`

## Cross-Relation Sweeps ("Same Patch" Workflow)

When the user asks to monitor multiple culturally-linked regions together (e.g., Acadie ↔ Acadiana ↔ Nouvelle-Aquitaine), run each region independently using the queries documented in region-specific reference files, then add a **Cross-Relation** section to the briefing.

### Cross-Relation Section Format
```
CROSS-RELATION: [Region A] ↔ [Region B] ↔ [Region C]
1. Pattern name — shared evidence across regions
2. Pattern name — shared evidence across regions
...
```

### What to Surface
- **Shared structural fights** — rural isolation, infrastructure, education access, language erosion
- **Cultural transmission parallels** — festivals, music, pageants as cultural diplomacy
- **Divergences** — where one branch is thriving and another is struggling (e.g., French-language media gradient)
- **Economic identity shifts** — workforce branding, tech corridors, sovereignty pivots

### French-Language Media Gradient (durable finding, Jun 2026)
| Region | Media Health | Evidence |
|--------|-------------|----------|
| Acadie (NB/NS) | Healthy | Radio-Canada, Acadie Nouvelle |
| Acadiana (LA) | Thin | Near-zero French RSS; English-only dominant |
| Nouvelle-Aquitaine | Near-zero | Gascon/Occitan invisible in news |

This gradient is a useful anchor for cross-relation briefings — the further from the Dérangement, the quieter the mother tongue in public media.

### Pitfall: Regional-Language RSS Returns Nothing
When querying Google News RSS for regional/minority languages (Gascon, Occitan, Cadien French), expect **zero results**. Don't waste multiple retry queries — after one empty return, note the gap and move on. The absence itself is a finding worth reporting.

## Cron Scheduling & Naming Conventions

### Morning Clustering Preference
When setting up recurring news briefing crons for the same user, **cluster them within the same ~30-minute window** rather than spacing them across the day. The user explicitly prefers this to maintain a single morning headspace and mental context — receiving all briefings together rather than fragmented throughout the day.

Example (the "Mardi en Acadie" block):
- 6:00 AM — Mardi en Acadie
- 6:15 AM — Mardi en Acadiana
- 6:30 AM — Mardi en Nouvelle-Aquitaine

**Do not** schedule related briefings hours apart unless the user explicitly requests it.

### Naming Convention
The "Mardi en [Region]" pattern is the established naming convention for this user's weekly regional news crons. Follow it for any new regional briefings:
- French-language naming ("Mardi en…") for Francophone-connected regions
- Job names: `Mardi en [Region] - Weekly [Description] Brief`

### Post-Briefing Note Capture
Every cron-run briefing should conclude by capturing key findings to QuickThoughts via the `note` CLI. This ensures the data persists for the 2AM GBrain sync cron. Use `NOTE_SOURCE_LABEL=Hermes` and the multiline format documented in the `note-capture-workflow` skill.

```bash
NOTE_SOURCE_LABEL=Hermes note $'[REGION] — Week of [date range]\n-- | [key items]\n-- | *** end of multiline ***'
```

### Cron Model/Provider Pinning (Required)
All news cron jobs **must** pin both `model` and `provider` at creation time. Unpinned jobs inherit whatever the current session provider is at fire time, which can cause silent model flips or provider mismatches. The original "Mardi en Acadie" job was pinned (`z-ai/glm-5.1` + `nvidia`); the 3 new jobs were initially unpinned and had to be patched after audit. Always set:

```yaml
model:
  model: z-ai/glm-5.1
  provider: nvidia
```

When creating new regional briefing crons, verify model pinning matches the existing block before declaring the job done.

### Manual One-Off Runs
User may request a manual run of a region's briefing before the cron fires (e.g., "just grab a surface-level relation so I'm not too out of touch"). This is a lightweight variant:
1. Use the same RSS queries from the region's reference file with a 7-day `after:` filter
2. Skip the full consulting-opportunity framework — surface-level only
3. Compare against QuickThoughts/GBrain for novelty (Step 0)
4. Deliver directly in chat (no archive append needed for manual runs)
5. Optionally capture to QuickThoughts via `note` CLI if findings are significant

### Québec-Acadie Bridge Region (4th Cron)
The "Mardi en Québec-Acadie" job covers the bridge between Québec and Acadie — stories where both communities intersect (language politics, cultural exchange, federal-provincial dynamics, cross-border identity). Queries should target both `Québec Acadie` and `Acadie Québec` combinations, plus `francophonie Canada` and `minorité francophone`.

Schedule slot: 6:45 AM ADT (after the 3 other Mardi briefings at :00, :15, :30).

## Philosophy

> *"News isn't just information — it's a map of problems waiting for solutions."*

Regional news monitoring serves three purposes:
1. **Awareness**: Keep user informed of local developments
2. **Pattern Recognition**: Identify recurring themes (infrastructure gaps, demographic shifts)
3. **Opportunity Identification**: Translate problems into consulting opportunities
4. **Cross-Relation**: Connect culturally-linked regions to surface shared struggles, divergences, and identity patterns

The goal isn't just to summarize — it's to **surface signal from noise** and connect daily events to larger trends that create business opportunities and cultural understanding.
