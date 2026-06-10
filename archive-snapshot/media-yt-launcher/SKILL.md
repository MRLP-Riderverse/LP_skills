---
name: yt-launcher
description: Use when the user wants to search YouTube with `yt <query>` or `yt -p <query>`. This is for YOUTUBE only — NOT movies/shows (use 123m-launcher for those). Route to /home/midnight/ExoCortex/Agentic/Scripts/yt-hermes adapter.
version: 1.4.0
author: Hermes Agent
license: MIT
metadata:
 hermes:
 tags: [youtube, video, music, yt]
 related_skills: []
---

# yt Launcher Routing Skill

## Overview

This skill teaches Hermes how to treat `yt` as a **routing intent** rather than a new service.

There are now two layers:

- **Upstream launcher**: `/home/midnight/ExoCortex/Agentic/Scripts/yt`
- **Hermes adapter**: `/home/midnight/ExoCortex/Agentic/Scripts/yt-hermes`

Do **not** edit the upstream launcher from this skill. The purpose here is to make Hermes recognize `yt topicXYZ` as a command-like request and to invoke the adapter with the right arguments.

## When to Use

Use when the user:

- types `yt <topic>` in chat and wants YouTube search/open behavior
- asks for a private/incognito YouTube search via `yt -p <topic>`
- wants Hermes to use the existing local script instead of inventing a new implementation
- asks how to make a CLI tool AI-readable without changing the tool itself

## Disambiguation: yt vs 123m

These are **completely separate tools** with no overlap:

| Signal | Route to | Adapter |
|--------|----------|---------|
| `yt` keyword, YouTube, music video, "listen to", tutorial | **yt-launcher** | `yt-hermes` |
| `123m` keyword, movie/show title, "Blockbuster", "watch [film]" | **123m-launcher** | `123m-hermes` |

**If the user explicitly says `123m`, always route to 123m-launcher — never fall through to yt.** Conversely, `yt` always means YouTube. These keywords are unambiguous routing signals. Do not load the other skill when one intent is clear.

Do **not** use this skill to:

- rewrite the `yt` script
- introduce a new YouTube backend
- replace the shell command with a separate agent service
- handle movie/show searches (that is 123m-launcher's job)

## Routing Contract

Treat `yt` as a local command wrapper around the existing launcher.

### Default search

```bash
/home/midnight/ExoCortex/Agentic/Scripts/yt-hermes <query...>
```

### Private mode

```bash
/home/midnight/ExoCortex/Agentic/Scripts/yt-hermes -p <query...>
```

### Hermes contract

The adapter emits a single JSON object on stdout so Hermes can read the result without parsing banner text:

- `tool`: always `yt`
- `query`: original query string
- `private`: boolean
- `status`: `ok` or `error`
- `opened_url`: resolved URL the launcher opened
- `upstream`: the preserved OG launcher path
- `exit_code`: upstream exit code

### In chat

If the user says something like:

- `yt superman`
- `yt topicXYZ`
- `yt -p lo-fi study`

interpret it as a request to run the adapter command, then report the JSON result or summarize it for the user.

## Best-Practice Architecture

This setup works best as a **wrapper + skill** pair:

- **The upstream script** stays the source of truth and keeps doing the actual browser/opening work.
- **The Hermes adapter** adds a stable JSON contract for agent consumption.
- **The skill** teaches Hermes how to route natural language into that adapter.
- **A shell alias/wrapper** is optional if the user later wants the same UX outside Hermes.

A skill by itself is **not** a standalone service and does **not** bypass the CLI. It is instruction/routing metadata for Hermes.

See `references/yt-adapter-contract.md` for the preserved two-layer design and the stdout/stderr contract.

## Practical Notes About the Current Script

The existing script is already serviceable for human use because it:

- validates dependencies (`curl`, `python3`, `xdg-open`)
- URL-encodes the query
- falls back to search if a first result cannot be found
- supports a private mode flag

However, it is still primarily **human-readable output**, not machine-structured output. For AI use, the skill should rely on the command itself and the observed effect, not on parsing the banner text.

## Response Format

When delivering the result in Telegram chat, format the response so the **query text itself is the clickable hyperlink** — no bare URL, no separate link line:

```
Searching YouTube for [Query Title](opened_url)
```

Example for query "lo-fi study":
```
Searching YouTube for [Lo-Fi Study](https://www.youtube.com/watch?v=xyz&autoplay=1)
```

Capitalize the query title-style for presentation. Ensure `telegram.disable_link_previews: true` is set in `~/.hermes/config.yaml` so Telegram does not generate URL preview embed cards — just clean tappable text. Set via:
```bash
hermes config set telegram.disable_link_previews true
```

## Common Pitfalls

1. **Trying to make the skill do the work directly.** Skills do not execute commands by themselves; they guide Hermes on what command to run.
2. **Changing the script when a routing layer is enough.** Keep the original script untouched unless you explicitly want to modernize its interface.
3. **Expecting machine-readable stdout from the script.** The current command prints friendly banners; if you later want JSON, add a separate wrapper in another layer.
4. **Confusing a skill with a shell alias.** A shell alias helps in terminals; a Hermes skill helps inside agent sessions.

## Verification Checklist

- [ ] Hermes recognizes `yt <query>` as a YouTube search intent
- [ ] Hermes runs `/home/midnight/ExoCortex/Agentic/Scripts/yt-hermes <query...>` when asked
- [ ] The upstream launcher `/home/midnight/ExoCortex/Agentic/Scripts/yt` remains unchanged
- [ ] Private mode is routed with `-p` when requested
- [ ] The adapter emits JSON on stdout with the documented fields
- [ ] Any future shell alias/wrapper is kept separate from this skill
