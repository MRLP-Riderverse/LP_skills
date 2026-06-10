---
name: opencode-release-research
description: Research the latest OpenCode (opencode.ai / anomalyco/opencode) release notes and summarize user-facing changes from GitHub releases, tags, and changelog clues.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [OpenCode, GitHub, Releases, Changelog, Research]
    related_skills: [opencode]
---

# OpenCode Release Research

Use this skill when the user asks what’s new in OpenCode, asks about the latest update, or wants clues from GitHub.

## Important repo note
There are multiple OpenCode repos in the ecosystem. For the terminal AI agent at opencode.ai, start with:
- `anomalyco/opencode` for the current release stream
- `opencode-ai/opencode` only if the user explicitly means that older repository

If the user says “opencode.ai” or gives a version like `1.14.x`, assume the `anomalyco/opencode` repo unless proven otherwise.

## Procedure

1. Identify the correct repository.
   - Prefer `anomalyco/opencode` for current OpenCode.ai releases.
   - Confirm with GitHub repo search if the user mentions a version or brand name that doesn’t match the older repo.

2. Check the latest release via GitHub API:
   - `GET /repos/anomalyco/opencode/releases/latest`
   - Or `GET /repos/anomalyco/opencode/releases?per_page=5`

3. Read the release body for user-visible changes.
   - Prefer summarized bullets from the release notes.
   - If the note is sparse, inspect nearby tags/releases and recent commits for context.

4. Look for practical impact categories:
   - Core behavior changes
   - TUI/UX changes
   - Provider/model support changes
   - Desktop/web integration fixes
   - SDK/API changes
   - Permission / safety / approval behavior changes

5. If the user asked for “what’s new,” summarize in plain English:
   - What changed
   - What a user would notice
   - Any breaking changes or workflow changes

6. If the latest release is unclear or there are multiple likely repos:
   - Say which repo you checked
   - State the latest confirmed tag
   - Mention any ambiguity explicitly instead of guessing

## Useful GitHub API endpoints
- Latest release: `/repos/anomalyco/opencode/releases/latest`
- Recent releases: `/repos/anomalyco/opencode/releases?per_page=5`
- Release by tag: `/repos/anomalyco/opencode/releases/tags/v1.4.1`
- Recent commits: `/repos/anomalyco/opencode/commits?per_page=10`
- Repository search: `/search/repositories?q=opencode.ai`

## Output style
- Keep the answer concise and practical.
- Focus on what users would actually notice.
- If the project is archived or moved, mention that as a major workflow clue.

## Pitfalls
- Do not assume `opencode-ai/opencode` is the current opencode.ai project.
- Do not report a version from the wrong repo.
- If a release exists but the body is tiny, supplement with adjacent release notes or recent commits.
- Avoid presenting speculative changes as confirmed facts.
