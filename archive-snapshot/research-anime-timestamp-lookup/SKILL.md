---
name: anime-timestamp-lookup
description: Reusable workflow for finding the exact episode, timestamp, and cause of an anime character death using web search plus subtitle/transcript sources.
---
# Anime timestamp lookup

Use this skill when a user wants the exact episode, timestamp, and circumstances of a scene in an anime and the answer requires web research.

## Goal
Find a scene precisely, not just the episode number.

## Reliable workflow
1. Search the web for the episode number first.
   - Use broad queries with the character name, event, and series.
   - Prefer search engines that expose raw HTML results if browser tooling is unavailable.

2. Look for a transcript/subtitle source for the exact episode.
   - Good sources are subtitle archives and episode transcript sites.
   - If a transcript page has timecoded lines, use that to locate the scene.

3. Extract the timestamp from the transcript.
   - On some subtitle archive pages, lines appear as `[MM:SS] --- dialogue`.
   - Use regex or text search around the character/event name to get the surrounding lines.
   - The scene is often a few lines before or after the first mention of the character’s name.

4. Cross-check the episode title and scene details with a second source.
   - Wiki/fandom pages are good for confirming episode title/number.
   - A transcript source is best for the timestamp.

5. Summarize carefully.
   - State the episode and title.
   - Give the timestamp range if the exact second is not obvious.
   - Explain how the character died in one or two sentences.

## Practical search tactics
- Try queries like:
  - `"character name" death episode timestamp anime`
  - `site:transcript_site episode number character name`
  - `"episode title" transcript character name`
- If a subtitle export endpoint rate-limits or blocks access, fetch the main page HTML and parse the embedded transcript instead.

## Common pitfalls
- Do not rely on random fan articles for exact timestamps unless they cite a transcript or video timestamp.
- If a source only confirms the episode but not the timestamp, keep searching; do not invent a time.
- Some subtitle sites return 429 or Cloudflare challenges on export links; the main page often still contains usable transcript text.

## Verification pattern
- Episode number/title from wiki or episode index.
- Timestamp from transcript lines.
- Death method from the surrounding dialogue/action lines.
