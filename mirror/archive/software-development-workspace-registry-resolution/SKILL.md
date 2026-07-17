---
name: workspace-registry-resolution
description: Resolve local project roots from ~/.hermes/workspaces.yaml before using hardcoded paths, and use the `workspace` helper command to list or resolve aliases.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [workspace, paths, hermes, local-dev]
---

# Workspace Registry Resolution

Use this skill when the task involves local project roots, notes roots, or any user-owned directory that may move over time. Prefer the workspace registry over hardcoded absolute paths.

## Registry location

- Primary registry: `~/.hermes/workspaces.yaml`
- Resolver command: `workspace`

Current registry is expected to contain simple alias-to-path mappings such as:

```yaml
websites: /home/midnight/ExoCortex/websites
notes: /home/midnight/Documents/Notes
gbrain: /home/midnight/.gbrain
```

## Rules

1. **Consult the registry first** when you need a user workspace root.
2. **Prefer aliases in reasoning/workflow** (`websites`, `notes`, `gbrain`) and resolve them only when acting.
3. **Avoid introducing new hardcoded absolute paths** in notes, scripts, or skills when an alias is sufficient.
4. **If the alias is missing**, either:
   - inspect `~/.hermes/workspaces.yaml`, or
   - ask the user whether to add it.
5. **Do not store secrets in `workspaces.yaml`**. It is for directory roots only.

## Fast commands

### List aliases

```bash
workspace
# or
workspace --list
```

### Resolve an alias

```bash
workspace websites
workspace notes
```

### Resolve a subpath within an alias

```bash
workspace websites projects/strays_silly_webpage
workspace notes notecore/inbox/QuickThoughts.txt
```

### Machine-friendly output

```bash
workspace websites --json
workspace --list --json
```

### Require existence

```bash
workspace websites projects/strays_silly_webpage --exists
```

## Recommended agent workflow

1. Read or resolve the alias before operating in a workspace.
2. Use the resolved path for file reads/writes/terminal work.
3. When sharing a reusable procedure, mention the alias first and the current resolved path second.

Example:

```bash
PROJECT_ROOT="$(workspace websites projects/strays_silly_webpage)"
cd "$PROJECT_ROOT"
```

## Pitfalls

- `workspace` prints a path; it cannot change the parent shell's current directory by itself.
- The registry parser is intentionally simple; keep entries as one-line `alias: /path` mappings.
- If a path moves, update `~/.hermes/workspaces.yaml` instead of editing many downstream scripts.

## Verification

- `workspace` should list aliases.
- `workspace <alias>` should print an absolute path.
- `workspace <alias> <subpath> --exists` should exit nonzero when the target does not exist.
