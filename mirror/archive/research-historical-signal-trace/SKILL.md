---
name: historical-signal-trace
description: Structured approach for tracing lineages, surnames, and cultural signals across deep time (900-1600 AD), handling gaps, variants, and silences.
category: research
triggers:
  - lineage tracing
  - surname origin
  - historical signal reconstruction
  - genealogical mystery
  - heritage research
---

# Historical Signal Trace & Lineage Reconstruction

## Core Philosophy
1.  **Silence is Data:** Gaps in records (e.g., unknown parents) are often intentional survival strategies, not just missing data.
2.  **Variants are Keys:** Searching only the modern spelling misses 90% of the trail. Dialect, Latinization, and phonetic shifts are critical.
3.  **Context > Confirmation:** Place the subject in their historical context (wars, schisms, migrations) to explain *why* records disappear.
4.  **Tiered Verification:** Clearly distinguish between **Verified** (archival proof), **Plausible** (contextual fit), and **Folklore** (oral tradition/myth).

## Workflow Steps

### 1. Define the Anchor Points
Identify the **confirmed facts** (dates, locations, roles) vs. the **mysteries** (gaps, unknown parents).
*   *Example:* Bishop Geraldus (1378, Dax) = Verified. Germain's parents = Unknown.

### 2. Expand the Search Net (Naming Variants)
Never search just one name. Generate a list of variants based on:
*   **Root Meaning:** (e.g., "Doux" = gentle/sweet)
*   **Dialects:** (e.g., Occitan: *Dols*, Gascon: *Dos*)
*   **Latinization:** (e.g., *Dulcis*, *Dulcetius*)
*   **Phonetic Shifts:** (e.g., *Duce*, *Dous*, *Le Doux*)
*   **Action:** Use these variants in ALL search queries.

### 3. Contextualize the "Silence"
If a lineage disappears or lacks records during a specific period, check for:
*   **Religious Conflicts:** (e.g., Schisms, Wars of Religion, Persecution)
*   **Political Upheaval:** (e.g., Regime change, Exile)
*   **Strategy:** Families often "went silent" to survive. This is a **feature**, not a bug.

### 4. Heraldic & Symbolic Verification
*   Search for standard coats of arms first.
*   If user claims a *different* symbol (e.g., "Double-headed eagle" vs. standard "Crowns"), investigate:
    *   Maternal lineage (quartered shields).
    *   Specific grants (imperial service).
    *   Modern embellishment/folklore.
*   *Heuristic:* Anomalies often point to a specific, hidden historical event or alliance.

### 5. Delegation Strategy (Sub-Agent Protocol)
When delegating this task:
*   **Avoid:** "Write a comprehensive report to a file" (often fails on large context).
*   **Use:** "Search for X, Y, Z variants. Return top 3 findings per variant. Output a concise summary to stdout."
*   **Fallback:** If file writing fails, have the agent output the summary to stdout, then write it yourself.

### 6. Output Structure
Always structure findings as:
*   **Verified:** (Archival proof)
*   **Plausible/Theoretical:** (Fits context, lacks direct proof)
*   **Folklore/Myth:** (Oral tradition, meaningful but unverified)
*   **The Gap:** (What is missing and why)
*   **Next Action:** (Specific archive, DNA test, or community call)

## Example Commands
*   `Search for "[Surname]" AND "[Variant 1]" AND "[Variant 2]" in "[Region]" during "[Period]"`
*   `Check heraldry databases for "[Surname]" standard arms vs. user claims.`
*   `Contextualize "[Period]" in "[Region]" for reasons of record loss (war, schism, exile).`

## Pitfalls to Avoid
*   **Presentism:** Assuming modern borders/nationalities applied then.
*   **Literalism:** Treating oral tradition as fact, or dismissing it as fiction. It's *memory*, which serves a different function.
*   **Single-Name Search:** Missing the "Dols" because you only searched "Doucet".
*   **Over-reliance on Digital Records:** Pre-1600 data often requires physical archive access (e.g., Archives Départementales).

## Reusable Prompts
*   "Trace the lineage of [Name] from [Year A] to [Year B], accounting for dialect variants and historical silences."
*   "Verify the heraldic claim of [Symbol] for [Family], comparing against standard grants."
*   "Identify historical events in [Region] between [Year X] and [Year Y] that would cause a family to obscure their origins."
