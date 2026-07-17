# Acadian/NB News Sources - Reference

This file contains the specific sources, URLs, and techniques for monitoring news in the Acadian/Nouveau-Brunswick region (Péninsule acadienne, Caraquet, Bathurst).

## Primary Sources

### English-Language
| Source | URL | RSS | Notes |
|--------|-----|-----|-------|
| CBC New Brunswick | https://www.cbc.ca/news/canada/new-brunswick | N/A (JSON metadata) | Mainstream, reliable, JSON headlines in page metadata |
| The Telegraph-Journal | https://www.telegraphjournal.com/ | N/A | Saint John-based, provincial coverage |
| The Daily Gleaner | https://www.gleaner.co.uk/ | N/A | Fredericton-based |

### French-Language
| Source | URL | RSS | Notes |
|--------|-----|-----|-------|
| Radio-Canada Acadie | https://radio-canada.ca/aci | Via Google News RSS | Public broadcaster, Acadian focus |
| Acadie Nouvelle | https://www.acadienouvelle.com/ | N/A | Local daily, Caraquet-based |
| Le Devoir | https://www.ledevoir.com/ | N/A | Quebec-based, covers Acadian issues |

### Aggregators
| Source | URL | Notes |
|--------|-----|-------|
| Google News RSS | `https://news.google.com/rss/search?q=Acadie+Nouveau-Brunswick&hl=fr-CA&gl=CA&ceid=CA:fr` | Best for French content |
| Google News RSS (EN) | `https://news.google.com/rss/search?q=Acadie+New+Brunswick&hl=en-CA&gl=CA&ceid=CA:en` | English coverage |

## Search Keywords

### French
- "Acadie"
- "Acadien"
- "Péninsule acadienne"
- "Caraquet"
- "Bathurst"
- "Shippagan"
- "Tracadie"
- "Nouveau-Brunswick"

### English
- "Acadia"
- "Acadian"
- "Acadian Peninsula"
- "Caraquet"
- "Bathurst"
- "New Brunswick"
- "Northeast NB"

## Fetching Techniques

### CBC New Brunswick (JSON Metadata)
CBC embeds article metadata in JSON format within the HTML:
```python
import re
content = terminal('curl -s -A "Mozilla/5.0" -L "https://www.cbc.ca/news/canada/new-brunswick"').get('output', '')
headlines = re.findall(r'"headline"\s*:\s*"([^"]+)"', content)
```

### Google News RSS (Best for French Content)
```python
rss_url = "https://news.google.com/rss/search?q=Acadie+Nouveau-Brunswick&hl=fr-CA&gl=CA&ceid=CA:fr"
content = terminal(f'curl -s -A "Mozilla/5.0" -L "{rss_url}"').get('output', '')
items = re.findall(r'<item>(.*?)</item>', content, re.DOTALL)

for item in items:
    title = re.search(r'<title>([^<]+)', item).group(1)
    link = re.search(r'<link>([^<]+)', item).group(1)
    date = re.search(r'<pubDate>([^<]+)', item).group(1)
```

### Radio-Canada Acadie (JSON Metadata)
Similar to CBC, but French:
```python
content = terminal('curl -s -A "Mozilla/5.0" -L "https://radio-canada.ca/aci"').get('output', '')
titles = re.findall(r'"title"\s*:\s*"([^"]+)"', content)
# Unescape Unicode: \u00e9 = é, \u00e8 = è, etc.
```

## Date Handling

RSS dates come in RFC 822 format:
```python
from datetime import datetime

date_str = "Thu, 30 Apr 2026 22:50:36 GMT"
pub_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
days_ago = (datetime.now() - pub_date).days
```

Filter for recent stories:
```python
recent = [a for a in articles if a['days_ago'] <= 7]  # Last week
```

## Archive Format

The weekly summary should follow this structure:
```
================================================================================
ACADIAN NEWS SUMMARY - WEEK OF [DATE RANGE]
Péninsule acadienne, Caraquet, Bathurst, Nouveau-Brunswick
Generated: [Date]
================================================================================

[DATE]
• [Headline]
 - Key details
 - Relevance
 - Source: [Publication]

[Repeat for each story]

================================================================================
CONSULTING OPPORTUNITY - TECH GAPS IDENTIFIED
================================================================================

1. [CATEGORY]
 - Problem from news
 - Opportunity: [solution]
 - Market: [customers]

[4-8 opportunities]

================================================================================
SOURCES CONSULTED
================================================================================
- [List of sources with URLs]
```

## Telegram Notification Format

Keep it brief (under 4000 chars for Telegram limit):
```
🔴 ACADIE NEWS BRIEF - [Date]

Top Story: [Headline]

Other highlights:
• [Story 2]
• [Story 3]
• [Story 4]

Full archive: [file_path]

Sources: [List]
```

## Common Story Categories

### Economic
- Fisheries (lobster, crab quotas, processing plants)
- Tourism (season extension, attractions, events)
- Local business (openings, closures, expansions)
- Employment (workforce development, layoffs, hiring)

### Infrastructure
- Connectivity (broadband, cellular coverage)
- Water (treatment, advisories, infrastructure)
- Energy (power outages, renewable projects)
- Transportation (roads, Maritime Bus, airports)
- Healthcare (vet services, dental, hospitals)

### Cultural/Identity
- Language rights and education
- Demographic changes (population decline, immigration)
- Cultural events and festivals
- Acadian identity and heritage

### Environmental
- Weather events (storms, rainfall, snow)
- Fisheries conservation (whales, plovers, quotas)
- Forestry (fires, management, climate impact)
- Coastal erosion and protection

## Consulting Opportunity Patterns

From this region's news, recurring opportunities include:

1. **Rural Connectivity**: Mesh networks, satellite backup, community ISP
2. **Fisheries Tech**: Traceability, GPS logging, compliance automation
3. **French-Language Tech**: EdTech, training platforms, content management
4. **Environmental Monitoring**: Water quality, erosion tracking, weather alerts
5. **Tourism Platforms**: Booking systems, digital experiences, multilingual content
6. **Healthcare Access**: Telemedicine, scheduling optimization, patient management
7. **Civic Engagement**: Voting info, candidate profiles, issue tracking
8. **Community Platforms**: Event management, crisis communication, resource sharing

## Session Notes (June 2, 2026)

This session revealed several operational constraints under cron mode:
- `execute_code` is entirely blocked in cron jobs (policy restriction)
- `curl | python3` pipe patterns trigger tirith security guard (HIGH risk)
- `delegate_task` subagent timed out at 600s fetching multiple RSS feeds
- CBC and Radio-Canada JSON metadata extraction returned empty from curl (both sites fully JS-rendered now)
- Google News RSS returned items spanning 2014–2026 unsorted — date filtering is essential, not optional

**Working techniques:**
1. Direct `terminal()` calls for curl → raw RSS XML (no python pipe) — reliable
2. Acadie Nouvelle WordPress search: `curl .../?s=KEYWORD | grep -oP '<h2[^>]*>.*?</h2>' | sed 's/<[^>]*>//g'` — solid headline extraction
3. `cat >> file << 'HEREDOC'` for archive append — cron-safe, no python needed
4. Telegram notify: `python3 scripts/telegram_notify.py --target telegram "message"` — works in cron, but always `--dry-run` first

**Failed approaches:**
- `delegate_task` for parallel RSS fetching — timed out
- CBC/Radio-Canada JSON metadata — empty in headless curl
- `python3 -c` one-liners — blocked by tirith in cron
- `execute_code` — blocked entirely in cron

**Top stories this week:**
1. Téléjournal Acadie reduced by 30 min (Radio-Canada → web shift, community backlash)
2. Supreme Court to hear closed courthouses case (French justice access)
3. 10th Rendez-Vous Acadie-Québec (economic partnerships)
4. NB considers 2nd nuclear plant + consumer advocate at NB Power
5. Dry summer forecast + wildfire preparedness
