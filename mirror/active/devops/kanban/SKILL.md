---
name: kanban
description: "Hermes Kanban multi-agent workflow — orchestration, worker execution, decomposition, anti-temptation rules, and session management."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [kanban, multi-agent, orchestration, routing, collaboration, workflow]
    related_skills: [ai-coding-agents, hermes-agent]
---

# Hermes Kanban — Orchestration + Worker Guide

Class-level skill for the full Hermes Kanban multi-agent workflow. Covers both roles: **orchestrator** (decomposes, routes, reviews) and **worker** (executes, reports, heartbeats). A single agent may play both roles depending on the task.

---

## Orchestrator Role

### Step 0 — Discover Profiles

```bash
hermes profile list
```

Or ask the user which profiles are available. The dispatcher silently fails on unknown assignees — always verify.

### When to Use the Board

- Multi-specialist coordination needed
- Crash survival (tasks persist across sessions)
- Human-in-the-loop approval gates
- Parallel work streams
- Review loops required
- Audit trail needed

### Anti-Temptation Rules

1. **Don't execute yourself** — create a card and assign it
2. **Create cards for every task** — no implicit work
3. **Split multi-lane requests** — one card per workstream
4. **Run independent lanes in parallel** — don't serialize
5. **Never create dependent work without `parents=[...]`** — enforce ordering

### Decomposition Playbook

1. Understand the goal
2. Sketch the task graph (dependencies, parallelism)
3. Create cards + link dependencies
4. Complete your own orchestrator task
5. Report back with summary

### Common Patterns

- **Fan-out/fan-in** — dispatch N workers, collect results
- **Parallel + validation** — run N workers, validate with separate reviewer
- **Pipeline with gates** — sequential stages with approval checkpoints
- **Same-profile queue** — serialize work for a single specialist
- **Human-in-the-loop** — block on user review before proceeding

### Goal-Mode Cards

Use `goal_mode=True` for persistent workers that run a judge loop until the goal is met.

### Recovering Stuck Workers

- Reclaim the card: `kanban_update status=todo`
- Reassign to a different profile
- Change model: switch to a stronger/weaker model as needed

---

## Worker Role

### Workspace Handling

| Type | Use for | Path |
|------|---------|------|
| `scratch` | Temporary, discardable work | Auto-generated temp dir |
| `dir:<path>` | Persistent shared workspace | Explicit path |
| `worktree` | Git worktree isolation | `.worktrees/<branch>` |

### Tenant Isolation

Prefix memory entries with tenant identifier to avoid cross-contamination.

### Good Summary + Metadata Shapes

**Coding tasks:**
- `changed_files`: list of modified files
- `tests_run`: test results summary
- `decisions`: key decisions made

**Review-required tasks:**
- Block with `reason="review-required: ..."`
- Put detailed metadata in comments, not in the block reason

**Research tasks:**
- `findings`: key findings
- `sources`: where information came from
- `confidence`: high/medium/low

### Claiming Created Cards

Only pass IDs from captured `kanban_create` return values. **Never invent IDs.**

### Block Reasons

Specific one-sentence decisions. Longer context goes in comments.

### Heartbeats

Report **measurable progress only** — not "still working" or "thinking about it".

### Retry Scenarios

| Status | Meaning | Action |
|--------|---------|--------|
| `timed_out` | Worker exceeded time limit | Retry with more time or simpler scope |
| `crashed` | Worker process crashed | Check logs, retry |
| `spawn_failed` | Couldn't start worker | Check profile, model config |
| `reclaimed` | Orchestrator took back the card | Accept, don't fight it |
| `blocked` | Worker hit a dependency | Resolve blocker, retry |

### DO NOTs

- **No `delegate_task` as kanban substitute** — use the board, not direct delegation
- **No modifying outside workspace** — stay in your assigned area
- **No self-assigned follow-ups** — create new cards instead
- **No completing unfinished work** — block if work isn't done

### CLI Fallback Equivalents

All `kanban_*` tool operations have equivalent `hermes kanban` CLI commands for use in terminals.

---

## Heartbeat Cheatsheet

| Signal | When to use | Example |
|--------|-------------|---------|
| Heartbeat | Making measurable progress | "Implemented auth middleware, 3/5 endpoints done" |
| Block | Cannot proceed without input | "Blocked: need API key for external service" |
| Complete | Task fully done | "All endpoints implemented + tested, PR opened" |

Bad heartbeat: "Still working on it" (no measurable progress)
Good heartbeat: "Refactored 2/4 modules, test coverage at 78%"
