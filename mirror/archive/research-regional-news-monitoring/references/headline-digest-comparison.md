# Headline Digest Comparison

Use this when producing a weekly "outside the echo chamber" digest.

## Workflow
1. Gather headline candidates from the past 7 days using Google News RSS and major outlets.
2. Compare each candidate against the user's local notes and GBrain.
3. Search locally with simple keywords first:
   - `grep -i` on `~/Documents/Notes/notecore/inbox/QuickThoughts.txt`
   - `PATH="$HOME/.bun/bin:$PATH" gbrain search "<keyword>"`
4. If the first pass is inconclusive, try a second query with a broader phrase or a nearby synonym.
5. Treat outcomes as follows:
   - **No hit**: strong signal the topic is new/unmentioned
   - **Weak hit**: mention it as possibly related but not clearly discussed
   - **Clear hit**: deprioritize unless it changed materially this week
6. Prefer a short report with only the highest-signal items.

## Query heuristics
- Start broad (`"drought"`, `"grid capacity"`) then narrow (`"Bathurst drought"`, `"Canada security bill"`).
- Use proper nouns when they matter; use topical phrases when the headline is generic.
- If browser/article resolution fails, rely on RSS title + source + date and mark it as headline-level evidence only.

## Output cues
- Call out Atlantic / New Brunswick relevance if present.
- Explain why the item matters in 1–2 sentences.
- Keep the final digest concise enough for Telegram.