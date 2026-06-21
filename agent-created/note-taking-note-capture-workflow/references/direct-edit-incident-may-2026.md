# Direct-Edit Incident — May 2026

## What happened

During a session where the user asked to capture a note to QuickThoughts, the agent had already read `QuickThoughts.txt` via `read_file` to check the file's current state. Instead of routing the capture through the `note` CLI, the agent used the `patch` tool to insert a new entry directly into the file.

## Why it happened

- The file content was already in the agent's context from a prior `read_file` call.
- The `note-capture-workflow` skill had not been loaded yet — it was only loaded later when the user said "nnote", which triggered a skill lookup.
- The agent took the path of least resistance: direct edit on the open file instead of reaching for the canonical tool first.
- The skill list instructs agents to "load relevant skills before acting," but the agent did not proactively load the note-capture skill before making the capture.

## What went wrong

1. **Format inconsistency** — The patched entry used `[2026-05-31]` prefix and `[4/1]` chunk label instead of the canonical `⁜ HH:MM:SS | DD.MM.YY > content ########` format. This creates a structurally inconsistent file that breaks downstream parsing and GBrain sync.

2. **Data corruption risk** — The `patch` tool does find-and-replace. If the `old_string` match had been fuzzy or matched the wrong block, existing entries could have been overwritten or corrupted. The `note` CLI is append-only and cannot mutate existing content — that is its entire safety model.

3. **No guardrail on the shortcut path** — The `note` CLI is the guardrail. Bypassing it removes all structural protections.

## What the user said

The user identified the format discrepancy between the two captures in the same session, asked why it happened, and confirmed that the direct-edit path "could destroy something important because of a simple mistake." The user emphasized that this needs a reliable safeguard.

## Corrective actions taken

1. Added "CRITICAL PITFALL: File already open shortcut bias" section to the skill's Core Rule, with the full reasoning and this incident reference.
2. Added a pre-capture gate: "Before any QuickThoughts capture, this skill MUST be loaded."
3. Added a durable memory entry: "QuickThoughts capture: ALWAYS use `note` CLI, NEVER patch/write_file directly."
4. Skill patch is the primary safeguard; memory entry is the safety net for when the agent is moving fast.

## Lesson

Having the file open in context is NOT a reason to bypass the `note` CLI. The append-only constraint exists precisely because direct writes are dangerous. The skill must be loaded before acting, even if the agent thinks it already knows what to do.

## Related incident

A more destructive variant of this same bug class happened later in May 2026: the agent used `write_file` (full file replacement) instead of `note` CLI, destroying the entire cumulative inbox. See `references/file-overwrite-incident-may-2026.md` for that incident's full timeline and recovery procedure.
