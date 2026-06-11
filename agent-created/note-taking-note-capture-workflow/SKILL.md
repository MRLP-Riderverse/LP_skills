---
name: note-capture-workflow
description: "MANDATORY — activate whenever the user starts a message with note, remember, capture, or log, or explicitly asks to save/note/record something. On trigger: immediately run the echo wrapper script, then present ONLY the captured entry block in a code block — no conversational preamble, no Logged., no markdown bullets, no extra wrapping. The stored entry IS the reply."
category: note-taking
aliases: [note-capture, note-capture-flow-audit, note-routing-policy]
---

# Note Capture Workflow

This skill defines the reliable Hermes protocol for capturing notes into the user's local QuickThoughts inbox.

The goal is simple: preserve `QuickThoughts.txt` as an append-only running log, and always route capture through the user's `note` CLI.

## ⚡ TRIGGER + RESPONSE PROTOCOL (READ FIRST)

**When to capture:** Anytime the user starts a message with "note", "remember", "capture", "log", or explicitly asks to save/record something. This is NOT optional — it is a mandatory action.

**What to do on trigger:**
1. Run the echo wrapper: `NOTE_SOURCE_LABEL=Hermes ~/.hermes/skills/note-taking/note-capture-workflow/scripts/note_capture_echo.sh "..."`
2. Present the echo wrapper output as a **code block** — that IS your entire response.
3. **DO NOT** add conversational text before or after (no "Logged.", no "Captured as:", no "Done.", no bullet summary).
4. **DO NOT** save to Hermes memory instead of running the note CLI — memory ≠ note capture.
5. The stored entry block in the code block is the single source of truth for the user's visual review.

**Correct Telegram response shape:**
```
⁜ HH:MM:SS | DD.MM.YY > Notes, by Hermes : the note content
 ########
```

**WRONG — do not do this:**
- "Logged. ⁜ ..." (redundant preamble)
- "Captured as: • Notes, by Hermes : ..." (markdown bullets instead of code block)
- Saving to Hermes memory and replying conversationally without running note CLI at all

## Core Rule

Use the `note` CLI for QuickThoughts capture.

Never write to `~/Documents/Notes/notecore/inbox/QuickThoughts.txt` directly with `write_file`, `patch`, heredocs, redirect appends, Python scripts, or any other manual file edit. `write_file` is the most dangerous: it replaces the ENTIRE file with no rollback. One `write_file` call on QuickThoughts.txt destroys the cumulative inbox permanently.

Why:
- The user wants QuickThoughts treated like a diary/log: new entries only go to the bottom.
- The canonical capture path is `~/ExoCortex/Agentic/Scripts/note`.
- That script owns the timestamp and separator format.
- Direct writes bypass the script's formatting and make the workflow less trustworthy.

### CRITICAL PITFALL: "File already open" shortcut bias

If you have already read QuickThoughts.txt (via read_file, patch, or any other tool), you may feel tempted to just patch/write the new entry directly since the file content is already in your context. **DO NOT DO THIS.** The fact that the file is open does NOT change the capture path. Always close the loop through the `note` CLI regardless.

Why this matters:
- `write_file` replaces the ENTIRE file — one call erases the full cumulative inbox with no rollback (this actually happened — see `references/file-overwrite-incident-may-2026.md`)
- `patch` does find-and-replace. A fuzzy or wrong `old_string` match can **corrupt or overwrite existing entries** — data that cannot be recovered.
- Even a "clean" direct edit produces a format-inconsistent entry (wrong timestamp style, wrong separators) that breaks downstream parsing and GBrain sync.
- The `note` CLI is append-only by design. It **cannot** mutate existing content. That is the entire safety model.

**Pre-capture gate:** Before any QuickThoughts capture, this skill MUST be loaded (via skill_view). If you are about to write to QuickThoughts and have not loaded this skill, stop and load it first. The skill exists because direct writes are dangerous enough to need a protocol — skipping the protocol defeats the purpose.

**Real incident 1 (early May 2026):** Agent read QuickThoughts.txt to check state, then patched a new entry directly instead of using the `note` CLI. The entry landed with wrong format ([2026-05-31] prefix and [4/1] chunk label instead of `⁜ HH:MM:SS | DD.MM.YY >` + `########`). It also risked overwriting existing entries on a bad match. The user caught it and confirmed: this is exactly the kind of mistake that could destroy important data.

**Real incident 2 (late May 2026):** Agent used `write_file` on QuickThoughts.txt during a memory offload + GPT transfer report session. `write_file` replaces the ENTIRE file contents. The result: the cumulative inbox (~690+ lines, ~46KB, months of data) was replaced with only the entries from that one session. A second overwrite later in the same week wiped even those recovery entries. By May 31, the file contained only that day's notes — everything from May 25-30 was gone. This is the most destructive variant of the bug because `write_file` has no rollback, no append mode, and the auto-backup script had only run once (April 19). GBrain daily pages were the only recovery path. See `references/file-overwrite-incident-may-2026.md` for full timeline and recovery procedure.

## Canonical Paths

- Inbox file: `~/Documents/Notes/notecore/inbox/QuickThoughts.txt`
- Capture CLI: `~/ExoCortex/Agentic/Scripts/note`
- Notes root default: `~/Documents/Notes/notecore`

## Actual Capture Behavior

As currently implemented, the `note` script appends entries like this:

```text
⁜ HH:MM:SS | DD.MM.YY > <content>
 ########
```

For multiline notes, it appends:

```text
⁜ HH:MM:SS | DD.MM.YY > -- multiline below --
-- | ***first line***
-- | second line
-- | *** end of multiline ***
 ########
```

Important facts confirmed from the live script:
- The `note` wrapper delegates normal captures to Python `notecore.storage.append_note()` when available.
- Python storage is the canonical formatter for multiline entries; the shell wrapper should pass raw note text through unchanged.
- Capture is append-only for normal note submission.
- The skill should not claim a 3-column `line_num|note_num|content` format.
- The skill should not claim stdin piping works for capture right now.

## How Hermes Should Capture Notes

### Single-line note

```bash
note "Your note text here"
```

### Multiline note

Use a command that passes a real newline character as one argument.

Safe examples:

```bash
note "$(printf 'Line 1\nLine 2\nLine 3')"
```

```bash
note $'Line 1\nLine 2\nLine 3'
```

Do not assume this works:

```bash
echo "Line 1\nLine 2" | note
```

The current script does not read stdin for note capture. With no arguments, it launches the UI flow instead of capturing piped text.

### Pitfall: bash quoting with printf multiline

When the multiline content contains single quotes, double quotes, or special characters, the `$(printf '...')` form wrapped in double quotes can produce `unexpected EOF while looking for matching '"'` errors in bash. The `$'...'` syntax is more reliable for complex multiline content because it avoids nesting quote layers.

**Safe for complex content (contains quotes, apostrophes, special chars):**
```bash
NOTE_SOURCE_LABEL=Hermes note $'Multi-line with apostrophes: it\'s done.\nSecond line with "quotes" inside.'
```

**Fails when content has unescaped double quotes inside `$(printf "...")`:**
```bash
# This can break if the note text contains unescaped double quotes
NOTE_SOURCE_LABEL=Hermes note "$(printf 'Line with "nested quotes" inside\nSecond line')"
```

Rule of thumb: if the note text contains any quote marks, reach for `$'...'` syntax first and escape internal single quotes with `\'`.

## Source Labels

The script can add a source label through `NOTE_SOURCE_LABEL`.

Use this when the source matters:

```bash
NOTE_SOURCE_LABEL=Hermes note "Your note text here"
```

Behavior:
- `NOTE_SOURCE_LABEL=Hermes` becomes `Notes, by Hermes : `
- `NOTE_SOURCE_LABEL=Telegram` becomes `Notes, by Telegram : `
- If the content already starts with `Notes, by ... : `, the script does not add a second label
- If no env var is set, no source label is added automatically

For Hermes-triggered note capture, prefer setting `NOTE_SOURCE_LABEL=Hermes` unless the user wants the raw note text with no label.

### Source Label Registry

Known label conventions (extend when new source types emerge):

| Label | `NOTE_SOURCE_LABEL` | Renders as | Purpose |
|---|---|---|---|
| Raw | *(unset)* | `⁜ ... > content` | User's own direct notes, no attribution |
| Hermes | `Hermes` | `Notes, by Hermes : content` | Agent-captured notes, analysis, summaries |
| GPT Transfer | `Hermes · GPT Transfer` | `Notes, by Hermes · GPT Transfer : content` | Reports pasted from GPT/ChatGPT sessions (see `gpt-transfer-report` skill) |

The `·` suffix pattern (`Hermes · <Source>`) can be extended for other AI contexts (e.g., `Hermes · Claude`, `Hermes · Gemini`) if the user adds more cross-context transfer workflows. The key design principle: same append-only protocol, same QuickThoughts source of truth — the label is a legibility layer for human scanning, not a separate storage path.

## Memory Offload Workflow

When Hermes memory nears capacity (≈90%+ of the 2,200 char limit), relocate less-critical entries to QuickThoughts before adding new ones:

1. **Identify candidates** — entries that are concepts, research details, procedural data, or session-specific context (not active config, preferences, or high-stakes facts)
2. **Capture to QuickThoughts** — use `NOTE_SOURCE_LABEL=Hermes note $'<content>'` to preserve the data
3. **Remove from memory** — use `memory(action='remove', old_text='...')` targeting the relocated entry
4. **Verify** — confirm the QuickThoughts entry landed and memory is under capacity

**What belongs where:**
- **Memory (hot cache):** active config, user preferences, tool quirks, current project stakes, environment facts that affect every session
- **QuickThoughts (warm storage):** concepts, research findings, session outcomes, philosophical insights, external reference data — anything true and useful but not needed *in every prompt*
- **GBrain (cold storage):** deep searchable knowledge, indexed after QuickThoughts sync cron runs at 2AM

Nothing is lost — only relocated. The user's principle: "We aren't trying to move truth, but share truth."

Do NOT offload: timezone, PKM policy, GBrain path, tool-critical quirks, or anything the user explicitly said to keep in memory.

For QuickThoughts capture, append-only means:
- New notes are only added at the bottom through `note`
- Existing QuickThoughts entries are never edited, deleted, reordered, or rewritten as part of note capture
- Capture and verification may read the file, but must not mutate it directly

Do not use these as part of normal capture:
- `write_file` on QuickThoughts.txt (DESTROYS entire file — most dangerous variant)
- direct edits to `QuickThoughts.txt`
- overwrite-style scripts
- cleanup passes that rewrite old entries
- archive or recap actions unless the user explicitly asks for them

### CRITICAL PITFALL: write_file on QuickThoughts.txt

`write_file` is the nuclear option — it replaces the ENTIRE file contents with whatever string you pass. There is no append mode, no undo, no backup before write. If you `write_file` on QuickThoughts.txt, you erase months of accumulated notes in one call.

This is not theoretical. It happened in late May 2026 during a memory offload session. The agent used `write_file` instead of `note` CLI to capture entries. The result: ~690 lines / ~46KB of notes were replaced with a handful of entries from that one session. The auto-backup script had not run since April 19, so there was no recent backup. GBrain daily pages (synced by the 2AM cron) were the only recovery path.

**If you find yourself about to call `write_file` with path containing `QuickThoughts`: STOP. Use `note` CLI instead.**

### Recovery procedure (if overwrite happens)

If QuickThoughts.txt is discovered to be truncated or overwritten:

1. **Do NOT write anything else to the file** — any new write makes forensic recovery harder
2. **Check GBrain** — `~/.bun/bin/gbrain list | grep quickthoughts-2026` shows all daily pages synced before the wipe. These are the primary recovery source.
3. **Check auto-backups** — `ls -lt ~/Documents/Notes/notecore/.auto_backups/` for timestamped copies
4. **Check manual backups** — `QuickThoughts.txt.backup2` and any other copies in the notecore directory
5. **Check pipeline windows** — `~/Documents/Notes/opencode_based/quickthoughts_pipeline/windows/` for date-windowed extracts
6. **Reconstruct by merging** — pull GBrain daily pages for the lost period, extract raw ⁜ entries, and re-append them via `note` CLI in chronological order
7. **Preserve current entries** — save any entries added after the overwrite before reconstruction, then re-append them at the end
8. **Run a backup immediately after recovery** — `bash ~/Documents/Notes/notecore/scripts/backup_quickthoughts.sh`
9. **Verify** — `wc -l` and `tail` the file to confirm entry count and format consistency

Important nuance:
- The broader `note` tool contains non-capture commands such as archive/recap flows.
- This skill should treat those as separate operations, not part of default QuickThoughts capture.
- If the user says they never want QuickThoughts to go backwards, do not proactively use archive flows on that file.

## Routing Policy

When the user wants something captured:
1. Decide whether they want a durable note or just a normal conversational response.
2. If they want durable capture, use the `note` CLI.
3. Keep the note concise, readable, and useful later.
4. If the content is too long, split it into multiple notes rather than shortening away meaning.
5. Prefer shorthand references over full noisy paths when that preserves meaning.

Capture by default when the user explicitly asks to:
- note something
- remember something
- log something
- save a recap of what just happened
- preserve a durable workflow correction or preference

Avoid over-capturing:
- noisy debugging chatter
- repetitive back-and-forth without durable value
- private internal reasoning
- huge raw logs when a compact summary would do
- near-duplicate captures of the same moment, especially casual activity/status notes already logged earlier in the session

## Ambient / Life-Log Capture Rule

For casual status notes like "I'm listening to X while doing Y," preserve the user's real-world moment without inflating it into a formal recap.

## Concept / Pattern Capture Rule

When the user says to note a concept they want to keep developing later, capture the idea as one compact durable proposition rather than a chatty recap.

Preferred shape:
- one sentence when possible
- preserve the ladder or structure the user discovered (for example: daily -> weekly -> monthly -> yearly)
- keep the user's core claim intact
- lightly normalize grammar for future readability
- do not bury the concept inside session-specific context unless that context is essential

Examples:
- Good: `Daily posts carry the raw data; weekly, monthly, and yearly recaps progressively trade raw technical detail for broader patterns.`
- Bad: `We had a long talk and then realized this might maybe be useful for a blog and social and other things later.`

If the user explicitly says they want to work on it later, optimize the note for future retrieval and expansion, not for narrative completeness.

Preferred shape:
- one short line
- keep the concrete nouns the user gave you
- preserve the parallel structure when present (for example: listening to X while doing Y)
- do not add interpretation, sentiment, or motivational framing unless the user asked for it
- do not turn a tiny life-log note into a multi-line summary unless the user explicitly wants a richer capture

Examples:
- Good: `Listening to a Pattern Weaver video on YouTube while clearing a few leaves in the backyard.`
- Bad: `Reflecting on digital pattern-weaving ideas while doing peaceful yard cleanup in the backyard this evening.`

If the user gave a fragmentary note in chat, normalize it just enough for readability, but stay close to their wording.

## Reflective Media / Culture Capture Rule

When the user wants to capture a thought sparked by music, a band, a film, or a cultural artifact, preserve three elements in one compact note when possible:
- the source artifact
- the emotional or energetic quality it carried
- the user's deeper interpretation or metaphor

Preferred shape:
- one compact sentence
- keep the concrete cultural reference intact for searchability
- preserve unusual phrasing if it carries the insight
- do not flatten it into generic sentiment like "this was meaningful"
- if the user supplied a metaphor or philosophical twist, keep that twist rather than replacing it with summary language

Example:
- Good: `Panic at the Disco-type teen energy stays etched in the soul: pop-punk's anti-authoritative yet humane aura sparked an internal riot that shielded us from outside chaos, and the name now feels like a wake-up metaphor.`
- Bad: `Remember that old music used to feel powerful and emotionally important.`

## Philosophical / Self-Alignment Capture Rule

When the user wants to capture a personal philosophy, maturity insight, or alignment statement, preserve it as a clean, durable line they can return to later.

Preferred shape:
- one sentence when possible
- keep the user's moral or existential framing intact
- preserve key words like truth, humanity, stewardship, responsibility, maturity, cosmos, alignment when they carry the point
- lightly normalize grammar for readability, but do not flatten the user's voice into sterile self-help language
- prefer a statement of orientation or commitment over a chatty summary of the conversation

Examples:
- Good: `I have abstained from chasing responsibilities while nurturing my maturity, so that I may later carry more in alignment with truth, humanity, and the wider cosmos.`
- Good: `I am aligning into a stewardship role rooted in truth, maturity, and care for the whole, so I can carry more wisely when the time comes.`
- Bad: `We had a deep talk and I felt more human and responsible afterward.`

If the user asks to save a persona-flavored reflection (for example, a Naruto-style take), capture the underlying principle in a searchable way while keeping the persona cue if it adds retrieval value.

## Duplicate-Capture Guard

Before capturing a short status/life-log note (for example: what the user is listening to, doing in the yard, or casually observing), do a quick duplicate check against the most recent QuickThoughts entries or against notes you already captured earlier in the same session.

If the new note is materially the same as a recent one:
- do not blindly append a paraphrased duplicate
- either skip the capture and tell the user it was already logged
- or capture only the new delta if something meaningfully changed

Use this especially for low-stakes ambient notes, where duplicate paraphrases add noise faster than value.

## Audit Procedure

Use this when the user wants the note workflow checked end-to-end.

1. Verify the current inbox path and script path still match the user's real setup.
2. Inspect `~/ExoCortex/Agentic/Scripts/note` for QuickThoughts capture behavior.
3. Confirm normal capture appends to the inbox rather than overwriting it.
4. Check whether multiline capture is still supported the way the skill claims.
5. Check for misleading docs that mention stale formats or unsupported flows.
6. Distinguish *capture* from *sync*: a note landing in `QuickThoughts.txt` does **not** by itself prove it reached GBrain.
7. If the user asks to verify a note in GBrain, inspect the indexed page / daily page directly rather than inferring from the inbox file or search hits alone.
8. Flag any command that can rewrite, truncate, rotate, or archive QuickThoughts so it is not confused with basic capture.

What to report:
- whether the live implementation matches the documented protocol
- whether QuickThoughts capture is append-only
- whether multiline instructions are accurate
- whether any docs still describe old behavior
- whether the note is present in GBrain proper or only in the QuickThoughts inbox
- what should change to keep Hermes reliable

## Verification Checklist

After a note capture, verify as needed:
- the note was routed through `note`
- the new entry appears at the bottom of `QuickThoughts.txt`
- the entry starts with `⁜ HH:MM:SS | DD.MM.YY >`
- the entry ends with ` ########`
- multiline notes use the `-- multiline below --` block structure when applicable
- no older QuickThoughts content was modified during capture

## Scaling Reads: Tail vs Full Read

For growing QuickThoughts logs, use the smallest read mode that fits the task:
- `tail`-style reads for recent-note verification, formatting checks on the newest entry, and quick UI previews
- full reads only for recap/archive/search jobs that truly need the whole inbox or a wide historical window

Implementation guidance:
- keep append-only capture on the `note` CLI path
- avoid reading the entire inbox just to show the latest few entries
- prefer a bounded tail window or cached recent preview for UI and verification
- full scans are acceptable for recap/archive workflows, but should not be the default for glance checks
- if a recent-preview path starts to become slow, consider adding a small index or mtime-based cache before optimizing the heavier recap paths

### Tail-report requests

When the user explicitly asks for a recent-window review such as "tail 100" on QuickThoughts:
- treat it as a bounded recent-read request, not a whole-file read
- read only the tail window needed to cover the last N lines
- default the response to a compact report or synthesis unless the user explicitly asks for the raw lines verbatim
- preserve concrete recent entries, timestamps, and themes when summarizing so the report remains audit-friendly

Support files:
- `references/tail-vs-read-scaling.md` for the current scaling rationale and implementation notes
- `references/direct-edit-incident-may-2026.md` for the first incident (patch on open file, early May 2026)
- `references/file-overwrite-incident-may-2026.md` for the second incident (write_file full overwrite, late May 2026) — includes timeline, root cause, and 9-step recovery procedure
- `references/gbrain-sync-verification.md` for the QuickThoughts vs GBrain verification distinction and direct-check workflow
- `references/echo-optimization-june-2026.md` for the tail -50 echo fix, pipe+heredoc stdin conflict pitfall, and lean-by-default guidance
- `scripts/note_capture_echo.sh` for a re-runnable capture wrapper that prints the latest stored entry after a successful note write (uses `tail -n 50` + fallback `tail -n 100`, temp .py file for scanner)

## Latest-Entry Echo Wrapper

When the user wants the *actual captured note* echoed back after a successful write, use the wrapper script rather than manually rereading the whole inbox.

Behavior:
- runs the normal `note` CLI first
- reads only the last 50 lines of `QuickThoughts.txt` via `tail -n 50`, scans bottom-up for the latest `⁜` block, and prints it
- falls back to `tail -n 100` if the entry wasn't in the first 50 lines
- for Telegram-facing wrapper output, omit the CLI confirmation line and show only the stored entry block so the timestamp/content block is the single source of truth

Use cases:
- verify the exact stored text after capture
- show the user the final persisted entry, not a paraphrase
- check multiline formatting without manually scanning the whole file

Pitfalls:
- this wrapper is for readback after capture, not for editing or rewriting the inbox
- if no new `⁜` entry is found, treat it as a failed verification and inspect the note file directly
- **NEVER read the full QuickThoughts.txt for echo readback.** The old implementation used `path.read_text()` on the entire file — this is O(n) for a growing inbox. Always use bounded `tail -n 50` with `tail -n 100` fallback. (Fixed June 2026 — see `references/echo-optimization-june-2026.md`)
- **Pipe + heredoc stdin conflict:** `tail ... | python3 <<'PY'` silently fails because the pipe feeds tail output to Python's stdin *and* the heredoc also tries to send the script to stdin. The fix: write the Python scanner to a temp `.py` file and run `tail ... | python3 "$echo_py"` so stdin is free for the pipe. Never combine pipe input with heredoc input to the same process.

### When to use the echo wrapper vs bare `note` CLI

The echo wrapper adds a subprocess (temp .py file + python3 scan). For routine captures where the user just wants the note saved, bare `NOTE_SOURCE_LABEL=Hermes note "..."` is sufficient — the `note` CLI is append-only and reliable by design. Reserve the echo wrapper for:
- testing / debugging capture formatting
- confirming a multiline note landed correctly
- auditing the note workflow

**Lean by default.** Don't add readback overhead unless the user needs verification.

## Examples

Correct:

```bash
NOTE_SOURCE_LABEL=Hermes note "Remember to audit multiline capture in the note CLI"
```

```bash
NOTE_SOURCE_LABEL=Hermes note "$(printf 'Workflow update:\nQuickThoughts must stay append-only.\nDo not use direct file edits.')"
```

Wrong:

```bash
echo "some note" >> ~/Documents/Notes/notecore/inbox/QuickThoughts.txt
```

```bash
python some_script.py # that manually appends or rewrites QuickThoughts.txt
```

```bash
echo "Line 1\nLine 2" | note
```

## Short Operating Rule

If the task is QuickThoughts capture, the safe default is:

```bash
NOTE_SOURCE_LABEL=Hermes note "..."
```

If the content must be multiline, pass a real newline in the argument. Do not pipe stdin unless the script is later upgraded to support that explicitly.

*Updated: May 2026 after checking the live `note` script behavior.*
