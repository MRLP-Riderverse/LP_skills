---
name: third-brain-architecture
description: Design and implement a "Third Brain" local-first architecture where GBrain serves as the central memory core, Thunderbolt.io (or similar) acts as the Personal Operating System (POS) interface, and agents (Hermes, Opencode) route through it. Includes patterns for data flow, sanitization, and empire-scale isolation.
version: 1.0.0
author: Hermes Agent
license: MIT
dependencies: ["gbrain", "excalidraw"]
metadata:
  hermes:
    tags: [Architecture, GBrain, Thunderbolt, Local-First, Empire, PKM]
    related_skills: ["excalidraw", "note-capture", "weather-two-way-output"]
---

# Third Brain Architecture

This skill defines the architecture and workflow for a **Third Brain** system: a local-first, sovereign AI stack where memory is centralized (GBrain), the interface is dynamic (Thunderbolt.io/POS), and agents are ephemeral workers.

## Core Concepts

1. **First Brain**: Biological (You).
2. **Second Brain**: Static storage (Notes, Files).
3. **Third Brain**: **Active Agent Layer** that listens, structures, and executes.

## Architecture Diagram

The flow is: `User` → `POS (Thunderbolt)` → `Agents (Hermes/Opencode)` ↔ `GBrain (Memory)` → `NoteCore (Inbox)`.

```
       ┌─────────────────┐
       │   YOU (User)    │
       └────────┬────────┘
                │
                ▼
┌───────────────────────────────────┐
│   POS Interface (Thunderbolt.io)  │
└────────────────┬──────────────────┘
                 │
         ┌───────┴────────┐
         ▼                ▼
┌─────────────────┐  ┌─────────────────────┐
│  Hermes Agent   │  │   Opencode          │
└────────┬────────┘  └──────────┬──────────┘
         └──────────┬───────────┘
                    ▼
         ┌─────────────────────┐
         │   GBRAIN            │
         │  (Memory Core)      │
         └──────────┬──────────┘
                    ▼
         ┌─────────────────────┐
         │   NoteCore          │
         └─────────────────────┘
```

## Installation Strategy

### Division of Labor
1. **User (Main PC)**: Installs GBrain core (`bun install`, `bun run init`), runs Postgres/PGLite, hosts Thunderbolt.io.
2. **Agent (Hermes)**: Installs GBrain skills, configures MCP client to point to local GBrain instance, creates `SOUL.md`/`USER.md`.

### Step-by-Step

**1. User installs GBrain (Main PC):**
```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain
bun install
bun run src/commands/init.ts  # Initializes local PGLite
bun run src/commands/serve.ts # Starts MCP server
```

**2. Agent configures Hermes:**
- Install GBrain skill pack.
- Add MCP config to `config.yaml`:
  ```yaml
  mcpServers:
    gbrain:
      command: "bun"
      args: ["run", "src/commands/serve.ts"]
      cwd: "/path/to/gbrain"
  ```
- Create `SOUL.md` and `USER.md` in GBrain.

## Data Flow Patterns

### Pattern A: Quick Capture
`User Voice/Text` → `POS` → `NoteCore` → `GBrain (Auto-Link)`

### Pattern B: Agent Query
`User Question` → `Hermes` → `GBrain Query Skill` → `Synthesize Answer` → `Telegram`

### Pattern C: Research Loop
`Opencode Session` → `Summarize to GBrain` → `Link to Entities` → `Update Timelines`

## Security & Isolation (Empire Mode)

When monetizing, split the stack:
- **Personal Brain**: Local, raw, sensitive (Your home server).
- **Sanitization Gateway**: Custom skill to strip PII.
- **Production Brain**: Dockerized, public-facing, client data.

## Troubleshooting

- **Excalidraw Link Fails on Mobile**: Use `image_generate` or ASCII fallback. Send both interactive link and static text representation.
- **GBrain Connection Refused**: Ensure `serve.ts` is running and port is exposed (use `ngrok` if Hermes is remote).
- **Token Bloat**: Use `nvidia/qwen3.6` for local summarization tasks before sending to GBrain.

## Reusable Artifacts

1. **`SOUL.md` Template**: Defines agent identity ("I am a Third Brain executor...").
2. **`USER.md` Template**: User profile, preferences, empire goals.
3. **Excalidraw JSON**: Standard diagram for the architecture (saved as `.excalidraw`).

## Notes

- **Thunderbolt.io**: Use as the primary UI layer for dashboarding GBrain data.
- **Sanitization**: Critical before moving data from Personal to Production brain.
- **Minions**: Use GBrain's `minion-orchestrator` for deterministic background jobs (e.g., daily digest, entity enrichment).
