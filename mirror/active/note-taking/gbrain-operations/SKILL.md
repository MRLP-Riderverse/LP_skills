---
name: gbrain-operations
description: Complete GBrain operations workflow — setup, troubleshooting, raw import, and search fidelity optimization for local-first PKM with hybrid RAG search.
category: note-taking
aliases: [gbrain-setup-troubleshooting, gbrain-raw-import]
---

# GBrain Operations Umbrella

This is the **class-level skill** for all GBrain operations. It consolidates setup, troubleshooting, raw import workflows, and search fidelity optimization for local-first personal knowledge management (PKM) with hybrid RAG search.

**Trigger:** User needs to set up or troubleshoot GBrain, import raw notes for full-fidelity search, verify installation, or optimize search results.

---

## Subsections

### A. Setup & Troubleshooting (from `gbrain-setup-troubleshooting`)
Verify and troubleshoot an existing GBrain installation, local brain repo, and common setup warnings.

**What to Check First:**
1. `gbrain --version` - Verify installed version
2. Confirm command is on PATH - On this system the wrapper may live at `~/.bun/bin/gbrain`, but it still requires `bun` to be reachable
3. If `gbrain` errors with `/usr/bin/env: 'bun': No such file or directory`, test with `PATH="$HOME/.bun/bin:$PATH" gbrain stats`
4. Verify bun itself is present at `~/.bun/bin/bun` before assuming the wrapper is usable
5. If `bun` is not installed, use Node-based fallbacks:
 - `npm install` in the gbrain repo to bootstrap dependencies
 - `npx tsx src/cli.ts stats`
 - `npx tsx src/cli.ts doctor`
 - `npx tsx src/cli.ts search <term>`
6. `gbrain init` - Initialize if needed
7. `gbrain doctor --json` - Get diagnostic JSON
8. `gbrain stats` - Check page count
9. Confirm the separate brain repo exists for markdown files
10. Import markdown only after the repo is ready

**Local Setup Pattern:**
GBrain code and the user's brain repo are separate:
- code/install repo: `~/gbrain`
- brain content repo: `~/brain` or another user-chosen directory

**CRITICAL: npm Package Name Collision:**
There are TWO different packages named `gbrain` on npm:
- `gbrain` v0.12.3 = Personal knowledge brain with hybrid RAG search (the PKM tool you want)
- `gbrain` v1.3.1 = GPU JavaScript Library for Machine Learning/WebGL by `stormcolor` (NOT what you want)

**Symptom:** `bun update gbrain` installs the wrong package, or `gbrain --version` shows unexpected version

**Fix:** If you see `gbrain@1.3.1` in `bun pm ls -g` but your local repo is `0.12.3`, run `bun uninstall -g gbrain` to remove the wrong package. Your actual gbrain CLI may be running from a local repo (e.g., `~/gbrain`) via a symlink at `~/.bun/bin/gbrain`.

**Prevention:** For locally-developed gbrain, use the local repo directly rather than installing from npm. Check `which gbrain` and `cat ~/.bun/bin/gbrain` to verify the source.

**Common Pitfalls:**
- If `gbrain doctor --json` says it cannot find the skills directory, ensure the brain repo exposes a `skills` path. A symlink to the installed skills directory is often the quickest fix.
- If `gbrain import` runs in a brand-new git repo and prints `fatal: ambiguous argument 'HEAD'`, check whether the import still succeeded. A successful page count with exit code 0 means the warning is usually benign.
- If `gbrain sync --repo <path>` prints that there is no tracking information or "No commits in repo", make an initial git commit in the brain repo first; then rerun sync.
- If a page is skipped with a frontmatter slug/path mismatch, either remove the `slug:` field or move/rename the file so the slug matches the path-derived slug.
- If you only want local ingestion and do not want embedding/API dependencies, use `gbrain import --no-embed <repo>` for the first pass.
- If embeddings are missing, that is expected until `OPENAI_API_KEY` is set. That only affects vector/semantic search; local keyword search can still work without it.

**Verification Commands:**
```bash
gbrain doctor --json
gbrain stats
gbrain import --no-embed <repo>
gbrain search "some known imported term"
```

**Decision Rules:**
- If the user only needs keyword search, proceed without API keys.
- If semantic/vector search matters, ask for `OPENAI_API_KEY`.
- If the setup is failing in a weird way, trust `gbrain doctor --json` over individual partial warnings.
- Prefer a small sanitized source page first, then import locally with `--no-embed` before attempting broader sync.

**Success Criteria:**
A setup is good enough when:
- the brain database is initialized
- the content repo exists
- imported pages are visible to `gbrain doctor --json` or `gbrain stats`
- the remaining warnings are explainable and non-blocking
- a first sanitized source page can be imported locally without cloud embeddings

**See original:** Full troubleshooting workflow preserved from `gbrain-setup-troubleshooting` skill.

---

### B. Raw Import Workflow (from `gbrain-raw-import`)
Import raw, un-sanitized notes into GBrain for full-fidelity local search while maintaining cloud-safe workflows.

**Problem:** Over-sanitizing notes before importing into GBrain destroys search fidelity:
- Names (e.g., "Jasper4420") get collapsed to generic terms
- Specific contexts (e.g., "ArcRaiders sessions") become unfindable
- Pattern recognition across time becomes impossible
- User ends up with 70% less searchable content than they actually wrote

**Example from production:**
- Raw QuickThoughts file: **10 mentions** of "ArcRaiders"
- Sanitized GBrain import: **3 mentions** found
- **Loss rate: 70%** of valuable context

**Solution: "Raw In, Redacted Out" Architecture:**

Keep **full-fidelity raw notes** in your local GBrain instance (which is secure), and only redact **on-demand** when sending data to cloud AI models.

```
Raw Note (Local GBrain) → Search finds everything
 ↓
On-Demand Redaction → Cloud AI sees [REDACTED]
 ↓
You get reasoning without PII leakage
```

**Step-by-Step Import Process:**

1. **Locate Your Sources Folder**
 **CRITICAL:** GBrain expects files in `~/brain/sources/` (plural), NOT `inbox/` or `source/` (singular).
 
 **Common Mistake:** Creating new folders like `raw_quickthoughts/` or looking in `inbox/` (which may be empty). Always use the existing `sources/` folder where your other dated entries live.

2. **Prepare Raw Files for Import**

 **Option A: Daily QuickThoughts import (extract new entries since last import)**
 ```bash
 # Extract entries from a specific date
 grep '⁜.*20.04.26' ~/Documents/Notes/notecore/inbox/QuickThoughts.txt
 
 # Create markdown file with new entries
 # Write to ~/brain/sources/quickthoughts-YYYY-MM-DD.md
 ```

 **Option B: Full QuickThoughts file copy**
 ```bash
 # Copy raw notes to GBrain sources folder (rename to .md)
 cp ~/Documents/Notes/notecore/inbox/QuickThoughts.txt \
 ~/brain/sources/quickthoughts-RAW-2026-04-19.md
 ```

 **Option C: Batch import project files (.txt → .md conversion)**
 ```bash
 # Convert all project .txt files to .md and copy to sources
 cd ~/Documents/Notes/notecore/projects
 for f in $(find . -name "*.txt" -type f); do
 mkdir -p ~/brain/sources/projects/$(dirname "$f")
 cp "$f" ~/brain/sources/projects/"$f".md
 done
 ```

 **Critical:**
 - Files must have `.md` extension (GBrain ignores `.txt`)
 - Use existing `sources/` folder structure, don't create parallel folders
 - Preserve original files; only copy/convert for import

3. **Import Without Embeddings**
 ```bash
 cd ~/brain
 PATH="$HOME/.bun/bin:$PATH" gbrain import --no-embed ~/brain/sources/
 ```

 **Why `--no-embed`:**
 - Avoids OpenAI API calls for local-only data
 - Faster import (keyword search only)
 - Sufficient for personal PKM retrieval

4. **Verify Import and Search**
 ```bash
 # Check stats (should see increased page count)
 gbrain stats
 
 # Test search for known terms
 gbrain search "Jasper"
 gbrain search "ArcRaiders"
 
 # If search output is truncated (common), grep the raw file directly:
 grep -i "jasper" ~/brain/sources/quickthoughts-RAW-2026-04-19.md
 ```

**Expected Results:**

**Before (Over-Sanitized):**
- Search "Jasper" → No results
- Search "ArcRaiders" → 3 generic mentions
- **Loss rate: ~70%** of searchable context

**After (Raw Import to Correct Folder):**
- Search "Jasper" → 7 specific mentions with timestamps
- Search "ArcRaiders" → 10 mentions with full context
- **Recovery: 100%** of original data searchable

**File Format Requirements:**
GBrain import expects:
- ✅ `.md` extension (Markdown)
- ✅ Directory of files (not single file import)
- ✅ Files in `~/brain/sources/` folder (or configured source folder)
- ❌ `.txt` files are ignored (must rename to `.md`)
- ❌ Single-file import doesn't work (expects directory)
- ❌ Wrong folders (`inbox/`, `source/`, `raw_quickthoughts/`) won't be found

**When to Use This Workflow:**

**✅ Use Raw Import When:**
- Your GBrain instance is **local-only** (disk encrypted, machine secure)
- You need **full search fidelity** for names, places, events
- You want to run **pattern recognition** over time (e.g., "How often do I game with Jasper?")
- You're comfortable managing PII exposure **on your own machine**

**❌ Don't Use Raw Import When:**
- Your brain repo is synced to a public GitHub repo
- You share your screen/notes with others frequently
- Your machine is shared/unencrypted
- You need cloud embeddings for semantic search (use `--embed` with API key)

**Security Model:**
This workflow assumes:
1. **Local GBrain DB** (`~/.gbrain/brain.pglite`) is secure (your machine, your control)
2. **Cloud AI** is the threat model (don't send PII to OpenAI/Claude/etc.)
3. **Redaction happens on-read**, not on-write

**Troubleshooting:**

**Issue: Import finds 0 pages**
- **Cause 1:** File extension is `.txt` instead of `.md` → **Fix:** Rename to `.md` and re-import
- **Cause 2:** Importing single file instead of folder → **Fix:** Use `gbrain import ~/brain/sources/` (folder path, not file path)
- **Cause 3:** Files in wrong folder (e.g., `inbox/` instead of `sources/`) → **Fix:** Move files to `~/brain/sources/` and re-import

**Issue: Search returns truncated results**
- **Cause:** GBrain displays snippets, not full context
- **Fix:** Use `grep` on raw file for full lines

**Issue: "Jasper" not found in search**
- **Cause:** Data not yet imported or imported from sanitized version
- **Fix:** Verify raw file exists, check GBrain stats, re-import if needed, confirm with grep

**Issue: Search works but query fails**
- **Cause:** GBrain query engine may not parse natural language well yet
- **Fix:** Use keyword `search` instead of semantic `query` for now

**Verification Checklist:**
After import, confirm:
- [ ] `gbrain stats` shows new page count increased
- [ ] `gbrain search "<recent-term>"` returns the new page
- [ ] `gbrain search "ArcRaiders"` returns more results than sanitized version
- [ ] Raw file grep shows expected matches
- [ ] No API calls made (if using `--no-embed`)
- [ ] New page appears in `gbrain list -n 10`

**Philosophy: Stream-First PKM:**
The goal isn't to create a perfect library of formatted notes. The goal is to build a **"good friend" memory system** that:
- **Listens** to today's chaos (raw, messy, unformatted)
- **Indexes** lightly (no heavy preprocessing, just capture the stream)
- **Recalls** contextually (search + grep finds exactly what you wrote)
- **Forgets** nothing (unless you explicitly delete)

**Day-by-day > Mass upload**
**Raw capture > Perfect formatting**
**Searchable chaos > Unfindable order**

**See original:** Full raw import workflow preserved from `gbrain-raw-import` skill.

---

## Identity / Profile Mining from PKM

When using GBrain or QuickThoughts to refresh the user's profile, treat notes as **evidence for durable identity/preferences**, not as profile entries to copy verbatim.

**Promote into profile/memory only when the pattern is durable:**
- self-descriptions that recur (`tech translator`, `bridge builder`, `sovereign builder`)
- stable work preferences (startup-style support, white-glove help, local-first workflows)
- durable framing of mission/direction (automation that helps humans be more present)
- long-lived project identity that keeps showing up across sessions (`acadie.sol` as stewardship / local digital home)

**Do NOT promote ephemeral operational state as identity:**
- cron job inventories
- exact scheduler times
- current enabled/paused jobs
- one-off session references / IDs
- transient system state that should be fetched live later

**Good extraction rule:**
1. Search QuickThoughts/GBrain for recurring self-description, values, and preferences.
2. Cross-check with recent session recall when available.
3. Elevate only what will still feel true/useful in a week or more.
4. Keep live operational state in the scheduler or source system, not in the user profile.

### D. Hot Memory → PKM Offload

When hot memory (MEMORY.md / USER.md) approaches capacity, offload project-spec and strategy content to GBrain. Keep only **identity + pointers** in hot memory.

**Principle:** Hot memory = who you are + where to find the details. GBrain = the details.

**What to offload:**
- Project architecture specs (stack details, phase descriptions, service flows)
- Strategic positioning content (GTM plans, market thesis, Coordination Era framing)
- Event logistics with expiry dates (wedding details, conference plans)
- Any content the agent can reconstruct by searching GBrain

**What stays in hot memory:**
- Identity core (translator, steward, bridge-builder)
- Cognitive cycle / operating mode patterns
- Active preferences and constraints
- One-line GBrain pointers to offloaded content ("Acadie.sol Directory Protocol → search GBrain")

**How to execute an offload:**
1. Read current MEMORY.md and USER.md via `read_file` on `~/.hermes/memories/MEMORY.md` and `~/.hermes/memories/USER.md`
2. Identify entries that are project/spec content, not identity/operating notes
3. Replace project specs with one-line GBrain pointer lines
4. Write compressed files via `write_file` (direct filesystem edit — see pitfall #12)
5. Verify the offloaded content exists in GBrain: `gbrain search "<project-term>"`

**Compression targets:** Aim for ~50% capacity on each file after offload. The agent fetches detail from GBrain on demand — it doesn't need full specs injected every turn.

**Before/after example (June 2026 session):**
- MEMORY.md: 2,212 → 493 chars (78% freed) — replaced Directory Protocol spec, AI Translator service flow, Coordination Era thesis with 3-line pointer list
- USER.md: 1,247 → 1,075 chars — replaced wedding logistics block with single GBrain pointer

---

## Common Pitfalls

1. **Wrong npm package** - gbrain v1.3.1 is GPU JS library, not PKM tool
2. **Wrong folder** - Use `sources/` (plural), not `inbox/` or `source/` (singular)
3. **Wrong extension** - Files must be `.md`, not `.txt`
4. **Single file import** - GBrain expects directory of files
5. **Missing bun** - Ensure bun is on PATH or use npx fallback
6. **Over-sanitization** - Import raw, redact on-demand for cloud
7. **Embedding dependency** - Use `--no-embed` for local-only search
8. **Git repo without commits** - Make initial commit before sync
9. **Profile pollution from ops state** - Do not mistake scheduler/job state for durable identity when mining PKM
10. **gbrain stats output format** - Output is `Label: N` (e.g. `Pages: 201`), NOT `N pages`. Regex: `[Pp]ages?\s*[:=]\s*(\d+)`
11. **Ollama thinking models in pipelines** - lfm2.5:8b embeds `<ȠϹ>` thinking tokens in API response body; `think:false` doesn't suppress. See `references/ollama-thinking-tokens.md`
12. **Memory tool can't delete entries** - The `memory` replace action requires non-empty `new_string` (empty string is rejected). There is no working delete action. To remove an entry, edit `~/.hermes/memories/MEMORY.md` or `USER.md` directly with `write_file`. Don't waste turns trying to replace-with-empty through the memory tool — it will loop.
13. **Curator prunes cron-referenced skills** - The curator's LLM review pass can go off-spec: it uses raw `terminal` commands to `mv` skill directories into `~/.hermes/skills/.archive/`, bypassing `skill_manage` and leaving cron job paths pointing at the now-missing original location. It does NOT update cron job prompts to match the new archive paths. **This has happened repeatedly** (June 5, June 8, 2026). **Key details:** (a) Pins are stored in `~/.hermes/skills/.usage.json` under `"pinned": true` — but `curator status` only displays pins among `agent_created_report()` results, which filters on `created_by: "agent"` or `agent_created: true`. Skills with `created_by: null` won't show in the pinned count even if pinned. (b) The LLM pass can bypass pin checks via raw terminal commands. (c) Skills without SKILL.md (e.g. script-only dirs like `weatherAPI-home`) are invisible to the curator's filesystem scan — create a minimal SKILL.md so pins work. (d) Restored skills keep archive directory names but the curator matches by SKILL.md `name:` field — pin BOTH keys. **Fix:** Pin cron-critical skills with `hermes curator pin <name>`; patch `created_by: "agent"` in `.usage.json` for visibility; verify pins with `python3 -c 'import json; data=json.load(open("~/.hermes/skills/.usage.json")); [print(k) for k,v in data.items() if v.get("pinned")]'` (not `curator status` which undercounts); restore with `hermes curator restore`. See `references/curator-prune-safety.md` for the full audit pattern, pin internals, and restore procedure.

---

## Verification Checklist

- [ ] `gbrain --version` shows correct version (v0.12.3)
- [ ] `gbrain doctor --json` returns valid diagnostics
- [ ] `gbrain stats` shows expected page count
- [ ] `gbrain search "test-term"` returns results
- [ ] Brain repo exists at `~/brain/` or specified path
- [ ] Sources folder populated with `.md` files
- [ ] No npm package collision (gbrain v0.12.3, not v1.3.1)

---

### C. Quick Note Capture via `note` CLI

The canonical way to capture notes into QuickThoughts is the `note` command at `/home/midnight/ExoCortex/Agentic/Scripts/note`.

**Single-line capture:**
```bash
note "some thought"
```

**Multi-line capture (preserves formatting as written):**
```bash
note $'Line 1\nLine 2\nLine 3'
```

**Key behavior:**
- Appends timestamped entry to QuickThoughts.txt
- Source label support: `NOTE_SOURCE_LABEL=Hermes note "captured by Hermes"`
- Multi-line notes are captured as a single entry with internal newlines preserved
- The content appears in QuickThoughts exactly as written — use `$'...'` bash syntax for literal newlines

**When to use:** Any time the user says "capture a note", "save this", "add to QuickThoughts", or wants content recorded for later GBrain sync.

**Project commands** (`note -new`, `note -open`, `note -ls`) are for structured project sessions, not quick capture.

---

**Architecture: Two cron jobs, one pipeline.**

```
2:00 AM  daily-quickthoughts-sync
         → Copies yesterday's QuickThoughts entries into ~/brain/sources/quickthoughts-YYYY-MM-DD.md
         → Runs gbrain import --no-embed
         → Sends Telegram sync summary

2:20 AM  daily-gbrain-sync-status
         → Checks sync file presence & size
         → Runs gbrain stats + gbrain doctor
         → Runs a gbrain search test for the target date
         → Appends a concise status note to QuickThoughts
         → Sends Telegram status report
```

**Design decision: GBrain IS the review.**

The old `daily-session-review-notes` cron used a local 8B model (qwen3:8b) to review session transcripts and produce topic blocks. This was abandoned because:
1. **qwen3:8b** produced garbage format — ignored the `Notes, by Hermes : [source | TOPIC]` template, hallucinated model comparison test plans instead of topic blocks
2. **lfm2.5:8b** embeds thinking tokens (`ƞϹϹ...`) directly in the API response body — Ollama's `/api/generate` does NOT separate them into a `thinking` field for models using the `lfm2-thinking` parser. The CLI flag `--hidethinking` works for terminal use but has no API equivalent on Ollama <0.6.
3. **Redundant pass** — the QuickThoughts sync already captures everything into GBrain. A second local-model summarization was adding noise, not intelligence.

**The replacement** (`daily_session_review_notes.py`) is fully deterministic — no model calls at all. It checks:
- Sync file exists for target date?
- GBrain stats (page count, chunks, tags)
- `gbrain doctor` health
- Search test (can GBrain find yesterday's entries?)

**If you want a daily digest**, the right approach is Option C: after sync, query GBrain for yesterday's entries and send the *indexed output* to a cloud model. The cloud model only sees what GBrain returns (already local + structured), not raw session transcripts.

**Script location:** `/home/midnight/.hermes/scripts/daily_session_review_notes.py`

**Key env vars:**
- `SESSION_REVIEW_MODEL` — no longer used (was `qwen3:8b`); kept in script signature for backward compat but ignored

**Ollama thinking-token pitfall (see `references/ollama-thinking-tokens.md`):**
Models using Ollama's `lfm2-thinking` parser (lfm2.5:8b, etc.) embed thinking in the `response` field of `/api/generate`. The `think: false` API parameter does NOT suppress these. The CLI `--hidethinking` flag works for interactive use but has no API equivalent. If you need a thinking model for a scripted pipeline, either:
- Use a custom Modelfile with `TEMPLATE {{ .Prompt }}` (no RENDERER/PARSER) to strip the thinking parser — but this may degrade output quality
- Use a non-thinking model (qwen3:8b, etc.) for scripted tasks
- Post-process the response with `re.sub(r'<ƞϹ>.*?ƞϹ>', '', raw, flags=re.DOTALL)` — but the closing tag may be absent if the model runs out of tokens

---

## Related Skills

- `note-capture-workflow` - Note capture and routing
- `native-mcp` - MCP server configuration
- `third-brain-architecture` - Local-first architecture design
- See `references/ollama-thinking-tokens.md` — Ollama lfm2-thinking parser behavior and workarounds
- See `references/curator-prune-safety.md` — curator off-spec pruning audit, restore procedure, and pin strategy

---

*Consolidated: May 2026*
*Updated: June 2026 — added nightly sync/status section, Ollama thinking-token pitfall, hot memory→PKM offload section, memory tool delete pitfall*
*Source skills: gbrain-setup-troubleshooting, gbrain-raw-import*
