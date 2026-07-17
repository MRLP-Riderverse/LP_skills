---
name: youtube-content
description: "YouTube transcripts to summaries, threads, blogs."
platforms: [linux, macos, windows]
---

# YouTube Content Tool

## When to use

Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, or wants to extract and reformat content from any YouTube video. Transforms transcripts into structured content (chapters, summaries, threads, blog posts).

Extract transcripts from YouTube videos and convert them into useful formats.

## Setup

```bash
pip install youtube-transcript-api
```

## Helper Script

`SKILL_DIR` is the directory containing this SKILL.md file. The script accepts any standard YouTube URL format, short links (youtu.be), shorts, embeds, live links, or a raw 11-character video ID.

```bash
# JSON output with metadata
python3 SKILL_DIR/scripts/fetch_transcript.py "https://youtube.com/watch?v=VIDEO_ID"

# Plain text (good for piping into further processing)
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only

# With timestamps
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --timestamps

# Specific language with fallback chain
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --language tr,en
```

## Output Formats

After fetching the transcript, format it based on what the user asks for:

- **Chapters**: Group by topic shifts, output timestamped chapter list
- **Summary**: Concise 5-10 sentence overview of the entire video
- **Chapter summaries**: Chapters with a short paragraph summary for each
- **Thread**: Twitter/X thread format — numbered posts, each under 280 chars
- **Blog post**: Full article with title, sections, and key takeaways
- **Quotes**: Notable quotes with timestamps

### Example — Chapters Output

```
00:00 Introduction — host opens with the problem statement
03:45 Background — prior work and why existing solutions fall short
12:20 Core method — walkthrough of the proposed approach
24:10 Results — benchmark comparisons and key takeaways
31:55 Q&A — audience questions on scalability and next steps
```

## Workflow

1. **Fetch** the transcript using the helper script with `--text-only --timestamps`.
2. **Validate**: confirm the output is non-empty and in the expected language. If empty, retry without `--language` to get any available transcript. If still empty, tell the user the video likely has transcripts disabled.
3. **Chunk if needed**: if the transcript exceeds ~50K characters, split into overlapping chunks (~40K with 2K overlap) and summarize each chunk before merging.
4. **Transform** into the requested output format. If the user did not specify a format, default to a summary.
5. **Verify**: re-read the transformed output to check for coherence, correct timestamps, and completeness before presenting.

## Transcript Archiving & Note Capture

When the user watches a YouTube video they found insightful or wants to keep for later reference, archive the full transcript locally and capture an indexed note. This is the "high-signal media consumption" workflow: extract → archive → index.

### Archive transcript locally

```bash
# Save full timestamped transcript to the references directory
python3 SKILL_DIR/scripts/fetch_transcript.py "URL" --text-only --timestamps \
  > ~/Documents/Notes/notecore/references/transcripts/yt-VIDEO_ID-slug.txt
```

- Directory: `~/Documents/Notes/notecore/references/transcripts/`
- Filename pattern: `yt-{VIDEO_ID}-{descriptive-slug}.txt`
- Prepend a header with video ID, URL, channel info, and capture date before the transcript content (use `write_file` for the combined header + transcript)

### Capture indexed note to QuickThoughts

After archiving, capture a note via the `note` CLI (see `note-capture-workflow` skill) that includes:

1. **Source**: "YouTube —" + brief creator/channel context
2. **Key insights**: distilled frameworks, quotable lines, or personal sparks the user mentioned
3. **Applications**: any connections the user drew to their own projects (e.g., "Maps Merch pattern → Acadie.sol")
4. **URL**: the original YouTube URL
5. **Transcript ref**: absolute path to the saved transcript file

Example note shape:
```bash
NOTE_SOURCE_LABEL=Hermes note $'YouTube — [creator context]. Core thesis: [distilled]. Key frameworks: [numbered]. Personal spark: [user\'s own realization]. Applications: [project connections]. URL: https://youtu.be/VIDEO_ID | Transcript: ~/Documents/Notes/notecore/references/transcripts/yt-VIDEO_ID-slug.txt'
```

This ensures future sessions can search QuickThoughts for the video's insights and trace back to the full transcript file.

### When to archive

Archive + note when the user:
- Says the video was insightful, inspiring, or worth keeping
- Draws connections to their own projects or philosophy
- Explicitly asks to capture or note the content
- Mentions they want to reference it later

Don't archive every video — only ones the user signals as high-signal.

## How the transcript extraction works (for users who ask)

The skill uses the `youtube-transcript-api` Python library under the hood. No API key or browser needed — it hits YouTube's internal caption endpoints directly. If a user asks how to build a local skill or do this themselves, the core is ~10 lines:

```python
from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcript("VIDEO_ID", languages=['en'])
for entry in transcript:
    print(f"{entry['start']:.0f}:{entry['text']}")
```

Each entry is a dict with `start` (seconds), `duration`, and `text`. The library handles caption track selection and language fallback.

Gotchas:
- Some videos have captions disabled → `NoTranscriptFound`
- Auto-generated captions can be messy (raw artifacts like `[singing]`, `[music]`)
- No API key needed, but YouTube could rate-limit under heavy use
- Live streams may lack transcripts until post-processing

## Error Handling

- **Transcript disabled**: tell the user; suggest they check if subtitles are available on the video page.
- **Private/unavailable video**: relay the error and ask the user to verify the URL.
- **No matching language**: retry without `--language` to fetch any available transcript, then note the actual language to the user.
- **Dependency missing**: run `pip install youtube-transcript-api` and retry.
- **Output truncated**: the script may produce long output that gets truncated in terminal. Pipe to a file directly (`> file.txt`) or re-fetch with offset if needed for full transcript archiving.
