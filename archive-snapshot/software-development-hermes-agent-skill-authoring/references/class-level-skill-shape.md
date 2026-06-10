# Class-Level Skill Shape

Use this as a quick rubric when deciding whether to extend an existing skill or create a new one.

## Preferred shape
- One skill should cover a *class* of work, not a single session artifact.
- The SKILL.md should explain the repeatable workflow, decision points, pitfalls, and verification.
- Session-specific examples, transcripts, and edge cases belong in `references/`.
- Copyable scaffolds belong in `templates/`.
- Deterministic probes, fix-verification helpers, and re-runnable commands belong in `scripts/`.

## Good signals for patching an existing umbrella
- The user corrected a workflow, tone, format, or sequence.
- A repeatable workaround or debugging path emerged.
- The new learning applies to the same class of task as an existing skill.
- A one-off narrow skill would duplicate an existing umbrella.

## Good signals for creating a new umbrella
- No current skill covers the work class.
- The task recurs across sessions.
- The workflow benefits from a clear trigger, pitfalls, and verification checklist.

## Anti-patterns
- One-session-one-skill naming.
- PR numbers, error strings, or dated task artifacts in skill names.
- Overwriting an umbrella with transcript noise instead of moving detail to `references/`.
- Adding a new sibling skill when the right move is to broaden an existing one.
