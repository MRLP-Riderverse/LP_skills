# Session Transcript Analysis with Local Models

Use this when the user wants to mine recent Hermes sessions for themes, patterns, or cross-session connections with a local model.

## Recommended workflow

1. Work from `~/.hermes/sessions/` and prefer `session_*.json` files over `.jsonl` when you want the full structured message list.
2. Exclude cron/session-noise unless the user explicitly wants it:
   - skip `session_cron_*.json`
   - skip sessions whose first user message is scheduler boilerplate
3. Expect many near-duplicate files from resumes/branches/compaction forks.
   - Do **not** blindly send every file to the local model first.
   - Group files by normalized first user prompt and keep the latest representative file from each group for the first pass.
4. Good two-stage local pipeline:
   - Stage 1: summarize each representative session into compact JSON
   - Stage 2: synthesize cross-session connections from those summaries
5. Treat local-model outputs as thematic guidance, not exact bookkeeping.
   - Verify counts/dates/file totals yourself before reporting them as facts.
   - Granite 4.1 8B was useful for pattern-sensemaking but drifted on strict structure/date fidelity.
   - Qwen-class models may be better for constrained JSON/format obedience.

## Practical notes

- In one live pass, 66 non-cron session files from the last 3 days collapsed into 20 unique opening-prompt groups. Deduping first made the local-model experiment much cheaper and more legible.
- Keep transcripts bounded before sending them to local models. A compact prefix of user/assistant messages is often enough for first-pass topical summaries.
- Save both:
  - a human-readable markdown report
  - a JSON artifact with counts, selected files, and per-session summaries

## When to choose models

- GPT-5.4: orchestration, verification, file selection, truth-checking
- Granite 4.1 8B: local thematic synthesis, recurring-thread detection, rough connection finding
- Qwen 3 8B: stricter structured outputs and formatting-constrained transforms
