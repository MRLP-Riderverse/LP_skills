---
name: 123m-launcher
description: Use when the user wants to search for a movie, show, or video on 123movies ("Blockbuster") via the `123m <query>` command. This is for MOVIES/SHOWS only — NOT YouTube. Route to /home/midnight/ExoCortex/Agentic/Scripts/123m-hermes adapter.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
 hermes:
 tags: [movies, shows, 123movies, blockbuster, video-streaming]
 related_skills: []
---

# 123m Launcher Routing Skill

## Overview

This skill teaches Hermes how to treat `123m` as a **routing intent** — when the user says `123m <title>` or asks to watch/search a movie, Hermes should invoke the adapter directly instead of overthinking or attempting web searches.

There are two layers:

- **Upstream launcher**: `/home/midnight/ExoCortex/Agentic/Scripts/123m`
- **Hermes adapter**: `/home/midnight/ExoCortex/Agentic/Scripts/123m-hermes`

Do **not** edit the upstream launcher from this skill. The purpose here is to make Hermes recognize `123m <title>` as a command-like request and invoke the adapter with the right arguments.

## When to Use

Use when the user:

- types `123m <title>` in chat (e.g. `123m social dilemma`, `123m the matrix`)
- asks to search/watch a movie on 123movies / "Blockbuster"
- says anything that maps to "look up a movie on the user's movie site"
- references a movie title with clear intent to find it on 123m

## Disambiguation: 123m vs yt

These are **completely separate tools** with no overlap:

| Signal | Route to | Adapter |
|--------|----------|---------|
| `123m` keyword, movie/show title, "Blockbuster", "watch [film]" | **123m-launcher** | `123m-hermes` |
| `yt` keyword, YouTube, music video, "listen to", tutorial | **yt-launcher** | `yt-hermes` |

**If the user explicitly says `123m`, always route to 123m-launcher — never fall through to yt.** The `123m` keyword is an unambiguous routing signal. Do not load yt-launcher or attempt YouTube search when 123m intent is present.

Do **not** use this skill to:

- rewrite the `123m` script
- introduce a new movie search backend
- replace the shell command with a separate agent service
- attempt web searches or browser navigation when the user clearly wants `123m`
- route to yt-launcher (that is a completely different tool for YouTube)

## Routing Contract

Treat `123m` as a local command wrapper around the existing launcher.

### Search command

```bash
/home/midnight/ExoCortex/Agentic/Scripts/123m-hermes <query...>
```

### Hermes contract

The adapter emits a single JSON object on stdout so Hermes can read the result without parsing banner text:

- `tool`: always `123m`
- `query`: original query string
- `status`: `ok` or `error`
- `opened_url`: resolved URL the launcher opened on 123moviesfree
- `upstream`: the preserved OG launcher path
- `exit_code`: upstream exit code

### In chat

If the user says something like:

- `123m social dilemma`
- `123m the matrix`
- `watch oppenheimer on 123m`
- `find interstellar on blockbuster`

interpret it as a request to run the adapter command, then report the result in chat.

### Response format

Always format the chat response as:

```
Searching Blockbuster for [query](opened_url)
```

Where the **query text itself is the clickable hyperlink** to the 123movies search URL. Do **not** show the raw URL separately. The movie title is the link.

Example output for query "social dilemma":
```
Searching Blockbuster for [Social Dilemma](https://ww8.123moviesfree.net/search/?q=social+dilemma)
```

Capitalize the query title-style (first letter of each major word) for presentation, even if the user typed it lowercase.

**Important:** ensure `telegram.disable_link_previews: true` is set in `~/.hermes/config.yaml` so Telegram does not generate URL preview embed cards — the response should be just the text with a tappable title, no thumbnail/description card. Set via:
```bash
hermes config set telegram.disable_link_previews true
```

## Architecture (mirror of yt-launcher)

This setup works as a **wrapper + skill** pair:

- **The upstream script** stays the source of truth and keeps doing the actual browser/opening work.
- **The Hermes adapter** adds a stable JSON contract for agent consumption.
- **The skill** teaches Hermes how to route natural language into that adapter.

A skill by itself is **not** a standalone service and does **not** bypass the CLI. It is instruction/routing metadata for Hermes.

See `references/adapter-architecture.md` for the two-layer design, JSON contract, and rationale.

## Common Pitfalls

1. **Overthinking the request.** If the user says `123m <title>`, just run it. Don't search the web, don't ask clarifying questions, don't try to find the movie elsewhere.
2. **Trying to make the skill do the work directly.** Skills do not execute commands; they guide Hermes on what command to run.
3. **Changing the upstream script when a routing layer is enough.** Keep the original script untouched unless explicitly asked.
4. **Expecting machine-readable stdout from the upstream script.** The upstream prints friendly banners; the adapter converts that to JSON.
5. **Confusing a skill with a shell alias.** A shell alias helps in terminals; a Hermes skill helps inside agent sessions.

## Verification Checklist

- [ ] Hermes recognizes `123m <query>` as a 123movies search intent
- [ ] Hermes runs `/home/midnight/ExoCortex/Agentic/Scripts/123m-hermes <query...>` when asked
- [ ] The upstream launcher `/home/midnight/ExoCortex/Agentic/Scripts/123m` remains unchanged
- [ ] The adapter emits JSON on stdout with the documented fields
- [ ] Any future shell alias/wrapper is kept separate from this skill
