---
name: opencode
description: Delegate coding tasks to OpenCode CLI agent for feature implementation, refactoring, PR review, and long-running autonomous sessions. Requires the opencode CLI installed and authenticated.
version: 1.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Coding-Agent, OpenCode, Autonomous, Refactoring, Code-Review]
    related_skills: [claude-code, codex, hermes-agent]
---

# OpenCode CLI

Use [OpenCode](https://opencode.ai) as an autonomous coding worker orchestrated by Hermes terminal/process tools. OpenCode is a provider-agnostic, open-source AI coding agent with a TUI and CLI.

## When to Use

- User explicitly asks to use OpenCode
- You want an external coding agent to implement/refactor/review code
- You need long-running coding sessions with progress checks
- You want parallel task execution in isolated workdirs/worktrees

## Prerequisites

- OpenCode installed: `npm i -g opencode-ai@latest` or `brew install anomalyco/tap/opencode`
- If the npm install fails during postinstall with `spawn sh ENOENT` or a similar script error, retry with `npm i -g opencode-ai@latest --ignore-scripts`, then verify the binary still works with `opencode --version`
- Auth configured: `opencode auth login` or set provider env vars (OPENROUTER_API_KEY, etc.)
- Verify: `opencode auth list` should show at least one provider
- Git repository for code tasks (recommended)
- `pty=true` for interactive TUI sessions

## Binary Resolution (Important)

Shell environments may resolve different OpenCode binaries. If behavior differs between your terminal and Hermes, check:

```
terminal(command="which -a opencode")
terminal(command="opencode --version")
```

If a GitHub release URL 404s, search for the current canonical org/repo before assuming the version is missing. In one live check, `github.com/sst/opencode` 404'd and the current release source was `github.com/anomalyco/opencode`.

If needed, pin an explicit binary path:

```
terminal(command="$HOME/.opencode/bin/opencode run '...'", workdir="~/project", pty=true)
```

## One-Shot Tasks

Use `opencode run` for bounded, non-interactive tasks:

### Continue the same session, but as a bounded one-shot

When you want to keep the same OpenCode session lineage/context **without** reopening the full interactive TUI, prefer `opencode run -s <session_id> '...'`.

This is especially useful when:
- you already have a good prior session to build on
- you want a fresh bounded implementation pass
- the interactive PTY/TUI route is awkward to monitor from Hermes

Example:

```
terminal(command="opencode run -s ses_abc123 'Continue this mockup. Add a wallet actions panel and improve the village interactions.'", workdir="~/project", timeout=300)
```

Observed reliable behavior on this system:
- `opencode -s <session_id>` in an interactive PTY can be harder to drive/monitor cleanly from Hermes for a bounded follow-up request
- `opencode run -s <session_id> '...'` preserved the same session lineage while producing a clear, self-contained result and edit summary
- This worked well for "second pass" refinement tasks on an existing static website mockup

```
terminal(command="opencode run 'Add retry logic to API calls and update tests'", workdir="~/project")
```

Attach context files with `-f`:

```
terminal(command="opencode run 'Review this config for security issues' -f config.yaml -f .env.example", workdir="~/project")
```

Show model thinking with `--thinking`:

```
terminal(command="opencode run 'Debug why tests fail in CI' --thinking", workdir="~/project")
```

Force a specific model:

```
terminal(command="opencode run 'Refactor auth module' --model openrouter/anthropic/claude-sonnet-4", workdir="~/project")
```

## Interactive Sessions (Background)

For iterative work requiring multiple exchanges, start the TUI in background:

```
terminal(command="opencode", workdir="~/project", background=true, pty=true)
# Returns session_id

# Send a prompt
process(action="submit", session_id="<id>", data="Implement OAuth refresh flow and add tests")

# Monitor progress
process(action="poll", session_id="<id>")
process(action="log", session_id="<id>")

# Send follow-up input
process(action="submit", session_id="<id>", data="Now add error handling for token expiry")

# Exit cleanly — Ctrl+C
process(action="write", session_id="<id>", data="\x03")
# Or just kill the process
process(action="kill", session_id="<id>")
```

**Important:** Do NOT use `/exit` — it is not a valid OpenCode command and will open an agent selector dialog instead. Use Ctrl+C (`\x03`) or `process(action="kill")` to exit.

### TUI Keybindings

| Key | Action |
|-----|--------|
| `Enter` | Submit message (press twice if needed) |
| `Tab` | Switch between agents (build/plan) |
| `Ctrl+P` | Open command palette |
| `Ctrl+X L` | Switch session |
| `Ctrl+X M` | Switch model |
| `Ctrl+X N` | New session |
| `Ctrl+X E` | Open editor |
| `Ctrl+C` | Exit OpenCode |

### Resuming Sessions

After exiting, OpenCode prints a session ID. Resume with:

```
terminal(command="opencode -c", workdir="~/project", background=true, pty=true)  # Continue last session
terminal(command="opencode -s ses_abc123", workdir="~/project", background=true, pty=true)  # Specific session
```

### Stable continuation pattern from Hermes

If you want to keep the same session lineage but only need a bounded follow-up pass, prefer:

```
terminal(command="opencode run -s ses_abc123 'Continue from the prior session. Implement the next pass and summarize changes.'", workdir="~/project", timeout=300)
```

Observed in live Hermes use:
- `opencode run -s <session_id> '...'` was the most reliable way to continue an existing session from Hermes
- it preserved session context while giving a clean one-shot result and edit summary
- this worked especially well for iterative website/UI refinement passes where each pass could be phrased as a self-contained next step

Use this as the default continuation strategy unless you truly need a long-lived interactive back-and-forth.

### Iterative static website/UI refinement pattern

For iterative mockup work on a static site, the most reliable pattern observed in live use was:

1. Re-read the current `index.html`, `css/styles.css`, and `js/script.js` before each pass so the next instruction is grounded in the real state.
2. Before a major simplification or reduction pass, make a full project snapshot copy (for example `project_name_v0.0.01`) so aggressive cuts are reversible and you retain a stable exploratory milestone.
3. Continue the same OpenCode lineage with a bounded prompt via `opencode run -s <session_id> '...'`.
4. If the workspace policy or project conventions mention a styling/layout specialist (for example `@css-master`), explicitly instruct OpenCode to ask that agent for feedback first.
5. Phrase each pass around one high-impact theme instead of a vague “improve it” prompt — e.g. gameplay legibility, public-vs-holder actions, dossier/profile clarity, pet visual integration, lightweight interaction polish, or reduction-first cleanup.
6. Keep constraints explicit in the prompt:
   - static HTML/CSS/JS only
   - no frameworks or external dependencies
   - preserve the existing tone/branding
   - run `node --check js/script.js` before finishing
6. After OpenCode finishes, verify independently:
   - read the changed files
   - check JS syntax yourself
   - verify the local server still returns HTTP `200 OK`
   - optionally measure size with `wc -c` when the user cares whether the page stayed lightweight
   - if the task includes exact public-facing copy, author handles, IDs, URLs, or visible labels, verify those literal strings directly in the output files instead of trusting the agent summary
   - for HTML pages, spot-check critical markup blocks because an otherwise successful pass can still leave a garbled text node or malformed visible line that needs manual cleanup

Why this is worth encoding:
- CSS/layout specialist guidance noticeably improved the quality of visual hierarchy and pet/UI integration
- bounded “next pass” prompts worked better than open-ended interactive steering from Hermes
- repeated verification caught regressions and gave concrete answers about whether the mockup remained lightweight

## Common Flags

| Flag | Use |
|------|-----|
| `run 'prompt'` | One-shot execution and exit |
| `--continue` / `-c` | Continue the last OpenCode session |
| `--session <id>` / `-s` | Continue a specific session |
| `--agent <name>` | Choose OpenCode agent (build or plan) |
| `--model provider/model` | Force specific model |
| `--format json` | Machine-readable output/events |
| `--file <path>` / `-f` | Attach file(s) to the message |
| `--thinking` | Show model thinking blocks |
| `--variant <level>` | Reasoning effort (high, max, minimal) |
| `--title <name>` | Name the session |
| `--attach <url>` | Connect to a running opencode server |

## Procedure

1. Verify tool readiness:
   - `terminal(command="opencode --version")`
   - `terminal(command="opencode auth list")`
2. **Always verify your current working directory** before delegation:
   - `terminal(command="pwd")`
   - `terminal(command="ls -la")` to confirm expected files exist
3. For bounded tasks, use `opencode run '...'` (no pty needed).
   - Attach relevant context files with `-f` flag if needed
4. For iterative tasks, start `opencode` with `background=true, pty=true`.
5. Monitor long tasks with `process(action="poll"|"log")`.
6. If OpenCode asks for input, respond via `process(action="submit", ...)`.
7. Exit with `process(action="write", data="\x03")` or `process(action="kill")`.
8. Summarize file changes, test results, and next steps back to user.

## PR Review Workflow

OpenCode has a built-in PR command:

```
terminal(command="opencode pr 42", workdir="~/project", pty=true)
```

Or review in a temporary clone for isolation:

```
terminal(command="REVIEW=$(mktemp -d) && git clone https://github.com/user/repo.git $REVIEW && cd $REVIEW && opencode run 'Review this PR vs main. Report bugs, security risks, test gaps, and style issues.' -f $(git diff origin/main --name-only | head -20 | tr '\n' ' ')", pty=true)
```

## Parallel Work Pattern

Use separate workdirs/worktrees to avoid collisions:

```
terminal(command="opencode run 'Fix issue #101 and commit'", workdir="/tmp/issue-101", background=true, pty=true)
terminal(command="opencode run 'Add parser regression tests and commit'", workdir="/tmp/issue-102", background=true, pty=true)
process(action="list")
```

## Session & Cost Management

List past sessions:

```
terminal(command="opencode session list")
```

Check token usage and costs:

```
terminal(command="opencode stats")
terminal(command="opencode stats --days 7 --models anthropic/claude-sonnet-4")
```

## Pitfalls

- Interactive `opencode` (TUI) sessions require `pty=true`. The `opencode run` command does NOT need pty.
- `/exit` is NOT a valid command — it opens an agent selector. Use Ctrl+C to exit the TUI.
- PATH mismatch can select the wrong OpenCode binary/model config.
- OpenCode may simply not be installed on the machine. Verify with `which -a opencode` or `opencode --version` first; if missing, fall back to `delegate_task`/web research instead of burning time on a dead command.
- If OpenCode appears stuck, inspect logs before killing:
  - `process(action="log", session_id="<id>")`
- Avoid sharing one working directory across parallel OpenCode sessions.
- Enter may need to be pressed twice to submit in the TUI (once to finalize text, once to send).
- On this Hermes/Bun setup, an interactive resumed session (`opencode -s <session_id>` in background PTY) proved less stable than one-shot continuation and surfaced a Bun segfault during a resumed interactive attempt. When you already know the next bounded instruction, prefer `opencode run -s <session_id> '...'` over reopening the TUI.

## Policy-managed scaffold workflow

When the task is to create a new local website/app inside a user-managed workspace, do not jump straight into OpenCode.

Observed reliable sequence:
1. Inspect the local workspace policy/scripts first (for example project-specific scaffold commands, required destination folders, and logging rules).
2. Create the project with the approved scaffold flow rather than ad-hoc file creation.
3. Only after the scaffold exists, hand the bounded implementation pass to OpenCode in that project directory.
4. After OpenCode finishes, verify the result yourself:
   - confirm the expected files exist
   - confirm HTML references CSS/JS correctly when relevant
   - start or use a local server and verify an HTTP `200 OK`
   - update any required append-only project log/policy artifacts
5. Report both the project path and a direct local-open path/URL back to the user.

Why this matters:
- user workspaces may have non-obvious conventions that matter more than generic code quality
- OpenCode is best used for the implementation pass, not for discovering local policy from scratch
- explicit post-run verification catches cases where files were edited but not actually wired together

## Verification

Smoke test:

```
terminal(command="opencode run 'Respond with exactly: OPENCODE_SMOKE_OK'")
```

Success criteria:
- Output includes `OPENCODE_SMOKE_OK`
- Command exits without provider/model errors
- For code tasks: expected files changed and tests pass

## Rules

1. Prefer `opencode run` for one-shot automation — it's simpler and doesn't need pty.
2. Use interactive background mode only when iteration is needed.
3. Always scope OpenCode sessions to a single repo/workdir.
4. For long tasks, provide progress updates from `process` logs.
5. Report concrete outcomes (files changed, tests, remaining risks).
6. Exit interactive sessions with Ctrl+C or kill, never `/exit`.
