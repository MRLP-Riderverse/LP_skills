# Novelty-Pass Digest

Use this when the user wants a vague "what happened lately?" or "give me highlights I might have missed" report.

## Workflow
1. Collect headline candidates from the last 7 days from reliable sources.
2. Compare each candidate against local knowledge before summarizing:
   - `grep -i` / broad keyword search on `~/Documents/Notes/notecore/inbox/QuickThoughts.txt`
   - `PATH="$HOME/.bun/bin:$PATH" gbrain search "<keyword>"`
3. If needed, rerun local search with a broader phrase or a nearby synonym.
4. Classify each item:
   - **No hit**: likely new to the user
   - **Weak hit**: possibly related, mention cautiously
   - **Clear hit**: skip unless there is a meaningful update
5. Keep the final report short and high-signal.

## Query heuristics
- Start with broad topic words, then try proper nouns and synonyms.
- Prefer headline + source + date when article text is unavailable.
- Do not overclaim from headline-only evidence.

## Output cues
- Focus on what seems genuinely new or surprising.
- Explain briefly why each item matters.
- Use a concise, Telegram-friendly format.