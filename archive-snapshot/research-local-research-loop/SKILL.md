---
name: local-research-loop
description: Execute research tasks using local AI (Ollama) to scrape, analyze, and format findings without burning cloud tokens, then route to QuickThoughts + GBrain
category: research
triggers:
 - "research"
 - "scrape"
 - "compare"
 - "analyze locally"
 - "zero-token research"
---

# Local Research Loop

Execute research tasks using **local AI (Ollama + Qwen)** to scrape, analyze, and format findings without burning cloud tokens, then route outputs to QuickThoughts inbox and GBrain for indexing.

## When to Use

- User asks to research/compare tools, platforms, or technologies
- Need to gather technical specs from multiple sources
- Want to avoid cloud API costs for research tasks
- Need structured output formatted for both human reading and machine indexing
- Building "Sovereign Operator" style intelligence workflows

## Core Workflow

### Phase 1: Scrape (Gather Raw Data)
1. Identify target URLs (GitHub READMEs, official docs, comparison articles)
2. Use `curl` or `terminal()` to fetch raw content
3. Limit fetched content to relevant sections (e.g., `head -n 2000`)
4. Store raw data in `/tmp/research_raw.json` for processing

```python
from hermes_tools import terminal
import json

urls_to_scrape = [
    ("Platform A", "https://github.com/org/repo/raw/main/README.md"),
    ("Platform B", "https://example.com/docs"),
]

scraped_data = {}
for name, url in urls_to_scrape:
    result = terminal(f"curl -s -L '{url}' | head -n 2000")
    scraped_data[name] = result.get("output", "")[:3000]

with open("/tmp/research_raw.json", "w") as f:
    json.dump(scraped_data, f)
```

### Phase 2: Reason (Local AI Analysis)
1. Construct a prompt with specific criteria (deployment, features, sovereignty, etc.)
2. Write prompt to `/tmp/ollama_prompt.txt` to avoid shell escaping
3. Run `ollama run qwen2.5-coder:7b` with the prompt file
4. Capture structured output (Markdown table + recommendations)

```python
context_prompt = """
Analyze the following platforms against criteria:
1. Deployment (Docker, resources)
2. Features (UI, bot API, encryption)
3. Sovereignty (federation, data portability)

RAW DATA:
""" + json.dumps(scraped_data)

with open("/tmp/ollama_prompt.txt", "w") as f:
    f.write(context_prompt)

result = terminal("ollama run qwen2.5-coder:7b \"$(cat /tmp/ollama_prompt.txt)\"")
analysis = result.get("output", "")
```

### Phase 3: Format (Structure for Human + Machine)
1. Parse local AI output into clean Markdown
2. Add metadata headers (`# Tags`, `# Date`, `# Status`)
3. Include comparison tables, sovereign scores, and actionable recommendations
4. Save to `/tmp/research_report.md`

```markdown
# [Topic] Research (YYYY-MM-DD)
# Tags: #research/[topic] #sovereign-stack
# Status: Complete

## Executive Summary
[Winner + runner-up with scores]

## Comparison Table
| Criteria | A | B | Notes |
|----------|---|---|-------|

## Recommendation
[Clear guidance with trade-offs]

## Revenue Angle
[Why this matters for newsletter/SOP]
```

### Phase 4: Route (Multi-Destination Output)
1. **QuickThoughts**: Append full report to `~/Documents/Notes/notecore/inbox/QuickThoughts.txt`
2. **GBrain**: Use `gbrain put "research/[slug]" < /tmp/research_report.md`
3. **Optional Alert**: Send Telegram/Signal notification: "✅ Research complete: [Topic]"

```python
from hermes_tools import terminal

# Append to QuickThoughts
with open("~/Documents/Notes/notecore/inbox/QuickThoughts.txt", "a") as f:
    f.write(f"\n\n---\n# {timestamp} - Research: [Topic]\n{report}\n")

# Index in GBrain
terminal('~/.bun/bin/gbrain put "research/[slug]" < /tmp/research_report.md')
```

## Key Rules

1. **Always use local Ollama** for analysis to avoid token costs
2. **Write prompts to files** to avoid shell escaping issues with multi-line strings
3. **Structure output for both humans and machines** (Markdown + metadata tags)
4. **Route to multiple destinations** (QuickThoughts for inbox, GBrain for search)
5. **Include "Revenue Angle"** section to identify monetization potential

## Pitfalls

- **Shell escaping**: Multi-line strings in bash commands fail. Use file-based prompts (`$(cat file.txt)`) instead of inline strings.
- **GBrain command syntax**: `gbrain put` requires input via stdin redirect (`< file.md`), not as an argument.
- **Token limits**: Truncate raw scraped data to ~12k chars before sending to local LLM.
- **Model availability**: Ensure `qwen2.5-coder:7b` (or similar) is installed via `ollama pull`.
- **Concurrent writes**: If multiple research tasks run simultaneously, use unique temp files (`/tmp/research_[topic]_[timestamp].md`).

## Example Usage

```python
# Full research loop for comparing chat platforms
# 1. Scrape docs for Revolt, Matrix, Fluxer
# 2. Analyze with local Qwen model
# 3. Format as structured Markdown report
# 4. Save to QuickThoughts + GBrain
```

## Success Criteria

- Research completed using **zero cloud tokens**
- Output is structured with comparison tables and clear recommendations
- Report is indexed in both QuickThoughts (inbox) and GBrain (searchable)
- "Revenue Angle" section identifies potential for newsletter/SOP content
- User can immediately act on findings (e.g., "Deploy Matrix Synapse")

## Related

- `note-capture`: For simple note-taking to QuickThoughts
- `gbrain-raw-import`: For importing raw notes into GBrain
- `weather-one-shot`: Example of one-shot script pattern
- User's QuickThoughts: `~/Documents/Notes/notecore/inbox/QuickThoughts.txt`
- GBrain CLI: `~/.bun/bin/gbrain`

## Revenue Integration

This pattern directly supports the "Sovereign Operator" business model:
1. Research a painful decision (e.g., "Which chat platform?")
2. Document the process and findings
3. Publish as newsletter issue #1
4. Offer paid setup guide or done-for-you service

Each research loop becomes a potential product.
