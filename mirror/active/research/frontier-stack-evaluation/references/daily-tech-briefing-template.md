# Daily Tech Briefing Template

Use this structure for the daily frontier-stack briefing output.

---

⚡ **DAILY TECH BRIEFING — [DATE]**

---

## 🔗 SOLANA ECOSYSTEM
[2-4 items max. If no signal from RSS, note the feed gap and what was attempted. Don't pad with stale news.]

- Item → **Action:** [builder-facing next step]

---

## 🤖 AI/AGENT INFRASTRUCTURE
[3-5 items. Cover Ollama, LangGraph, x402, OWS, and any new entrants.]

### [Tool/Protocol Name] — [One-line headline]
- Key detail (numbers, version, capability)
- **→ Action:** [specific integration/evaluation step]

---

## 🧠 SOVEREIGN BUILDER INTELLIGENCE
[3-5 items across Willison, Oxide/Cantrill, Webb, and any new sovereign-infrastructure voices.]

### [Source Author] — [Topic]
- Signal detail
- Implication for sovereign builders
- **→ Action:** [concrete step]

---

## 🏠 LOCAL-FIRST & DIY AUTOMATION
[2-3 items. If automated searches return empty, synthesize from other sections' edge/local signals rather than reporting "nothing found."]

- Item → **→ Action:** [step]

---

## 🎯 CROSS-CUTTING SIGNALS

- **[Signal 1]** → [One-line implication]
- **[Signal 2]** → [One-line implication]
- **[Signal 3]** → [One-line implication]

*(Use labeled bullet pairs instead of markdown tables — Telegram strips tables.)*

**Thread for the week:** *[Single sentence synthesizing the dominant theme across all sections]*

---

## Format rules
- Target: 800-1200 words total
- Every item that makes the cut gets an **→ Action:** line
- If you can't find an actionable angle, reconsider including the item
- Emoji section headers for quick scanning in Telegram
- Bold for tool names, version numbers, and key metrics
- No filler — if a section is genuinely quiet, say so briefly and move on
- **Use bullet lists instead of markdown tables** — Telegram strips/garbles pipe tables. For cross-cutting signals, use labeled bullet pairs: `- **Signal:** X → **Implication:** Y`
- **English only** — never duplicate sections in another language regardless of source language. Translate first.

## Cron delivery rules (CRITICAL)
- The briefing IS the final response. Never append a "Briefing delivered" or wrap-up message after the briefing.
- The delivery system captures the LAST assistant message. Any post-briefing output will replace the full briefing.
- If you track progress with the todo tool, do NOT emit a "all tasks complete" message as your final response.
- Write the briefing, end with the thread sentence, stop.
