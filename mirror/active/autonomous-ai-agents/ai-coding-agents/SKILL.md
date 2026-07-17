---
name: ai-coding-agents
description: "Delegate coding to autonomous AI CLI agents — Claude Code, OpenAI Codex, OpenCode — one-shot tasks, PRs, parallel work, and session management."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [AI, coding, agents, claude-code, codex, opencode, delegation, autonomous]
    related_skills: [hermes-agent, kanban-orchestrator, kanban-worker]
---

# AI Coding Agents — Delegation Guide

Class-level skill for delegating coding tasks to autonomous AI CLI tools. Covers the three primary agents: OpenCode, Claude Code, and OpenAI Codex. Each subsection covers usage, pitfalls, and agent-specific workflows.

## Choosing an Agent

| Agent | Best for | Key feature | Cost model |
|-------|----------|-------------|------------|
| **OpenCode** | Open-source projects, iterative work | Local, configurable | Free (uses your API key) |
| **Claude Code** | Complex multi-file refactors, PRs | Anthropic's coding model | Anthropic API |
| **Codex** | OpenAI-native workflows | Codex CLI sandbox | OpenAI API |

General rules:
- Prefer **OpenCode** for local/iterative tasks and when you need session continuation
- Prefer **Claude Code** for large refactors with complex cross-file reasoning
- Prefer **Codex** for OpenAI-integrated workflows and sandboxed execution
- All three support one-shot (`run`) and interactive modes

---

## OpenCode

### One-Shot Tasks

```bash
opencode run "Add a /health endpoint to the FastAPI app in src/main.py"
opencode run "Fix the flaky test in tests/test_auth.py — it fails intermittently on CI"
```

### Interactive Sessions

```bash
# Start interactive (background PTY)
opencode  # starts TUI

# Prefer continuation via run -s instead of resuming TUI
opencode run -s <session-id> "Continue: add tests for the health endpoint"
```

### Session Management

```bash
# List sessions
opencode sessions list

# Continue a session (preferred over resuming TUI)
opencode run -s <session-id> "Now add error handling for the case where the database is down"
```

### PR Review Workflow

```bash
opencode run "Review PR #42 for the current repo — check for security issues, test coverage, and code style"
```

### Parallel Work Pattern

```bash
# Run multiple tasks in parallel via background terminal sessions
opencode run "Implement feature A in src/feature_a.py" &
opencode run "Write tests for feature B in tests/test_b.py" &
wait
```

### Pitfalls (OpenCode)

- **PATH mismatches** — OpenCode may not see the same PATH as your shell. Use absolute paths for tools.
- **`/exit` not valid** — Don't try to send `/exit` to an interactive session. Use Ctrl+C or close the PTY.
- **Bun segfaults on resumed sessions** — Avoid resuming TUI sessions; use `opencode run -s <id>` instead.
- **Session continuation** — Always prefer `opencode run -s <id> '...'` over resuming an interactive TUI.
- **Opencode delegation pattern** — For reliable QR code generation or dependency-heavy tasks, delegate to Opencode to handle environment issues.

### OpenCode Delegation Pattern

When encountering dependency or environment issues that the main agent can't resolve, delegate to OpenCode:

```bash
opencode run "Install the qrcode Python library and generate a QR code for https://example.com, saving to /tmp/qr.png"
```

This is especially useful when:
- Python dependency installation requires venv manipulation
- A tool needs to be compiled or built
- Environment-specific paths need resolution

### Static Site Iteration Pattern

When iterating on a static concept website:
1. Start with a minimal OpenCode task to scaffold
2. Refine with focused follow-up tasks
3. Reduce noise before adding complexity
4. Prefer one stable visible surface over collapsible mode stacks when the UX needs to feel "organic" or low-friction.
5. If a control is only a compatibility shim or state switch, keep its visible surface minimal and deterministic.

See `references/mobile-ui-verification.md` for a compact verification loop for mobile UI changes.

---

## Claude Code

### One-Shot Tasks

```bash
claude-code "Implement user authentication with JWT tokens in src/auth.py"
claude-code "Fix the memory leak in the WebSocket handler — see src/ws.py"
```

### PR Workflow

```bash
# Create a feature branch and implement
claude-code "Create a branch feat/auth, implement login/register endpoints, add tests, and open a PR"

# Review an existing PR
claude-code "Review PR #42 — check for security issues, missing tests, and code style"
```

### Interactive Sessions

```bash
claude-code  # Start interactive mode
# Continue conversation naturally
# Use Ctrl+C to exit
```

### Pitfalls (Claude Code)

- **API key required** — Needs `ANTHROPIC_API_KEY` set in environment
- **Context limits** — For very large codebases, specify the relevant files/directories explicitly
- **Cost awareness** — Complex multi-file tasks can consume significant tokens

---

## OpenAI Codex

### One-Shot Tasks

```bash
codex "Add input validation to the /api/users endpoint"
codex "Refactor the database connection pool in src/db.py"
```

### Kanban Codex Lane

When using Codex within a Hermes Kanban workflow, follow the Kanban Codex Lane pattern:

1. **Worker ownership** — Hermes keeps ownership of task lifecycle, reconciliation, testing, and handoff
2. **Codex as implementation lane** — Codex runs as an isolated implementation worker
3. **Worktree isolation** — Use git worktrees to isolate Codex's changes
4. **Reconciliation** — After Codex completes, Hermes reconciles and tests before marking complete

### Pitfalls (Codex)

- **Sandbox execution** — Codex runs in a sandbox; it may not have access to all local tools
- **OpenAI API key** — Needs `OPENAI_API_KEY` set
- **Network access** — Codex sandbox may have restricted network access

---

## General Delegation Tips

1. **Be specific** — Include exact file paths, function names, and expected behavior
2. **One task per run** — Don't bundle unrelated changes in a single delegation
3. **Verify output** — Always review the agent's changes before committing
4. **Session reuse** — For iterative work, continue sessions rather than starting fresh
5. **Cost management** — Monitor token usage, especially for complex tasks
6. **Fallback** — If an agent fails, try another or fall back to manual implementation
