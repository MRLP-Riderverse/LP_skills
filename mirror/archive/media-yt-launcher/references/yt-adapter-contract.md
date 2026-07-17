# yt Adapter Contract

## Purpose

Preserve the original YouTube launcher script while giving Hermes a stable, machine-readable layer for agent use.

## Layers

- **Upstream launcher**: `/home/midnight/ExoCortex/Agentic/Scripts/yt`
- **Hermes adapter**: `/home/midnight/ExoCortex/Agentic/Scripts/yt-hermes`
- **Skill**: routes `yt` intent to the adapter

## Contract

The Hermes adapter should emit **one JSON object on stdout** and avoid banner text there.

Recommended fields:

- `tool`: `yt`
- `query`: original query string
- `private`: boolean
- `status`: `ok` or `error`
- `opened_url`: resolved URL opened by the launcher
- `upstream`: preserved upstream path
- `exit_code`: upstream exit code

## stdout / stderr rules

- `stdout`: JSON result only
- `stderr`: human commentary, usage errors, warnings, debug logs

## Routing rules

- `yt <query...>` → normal search
- `yt -p <query...>` → private/incognito mode

## Preservation rule

Do **not** modify the upstream launcher when the problem can be solved in the adapter layer.

## Verification

- Run the adapter with a known query and confirm valid JSON output.
- Confirm the upstream launcher still opens the browser and remains unchanged.
- Confirm private mode forwards `-p` without altering the upstream script.