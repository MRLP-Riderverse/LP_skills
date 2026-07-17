# Echo Script Optimization — June 2026

## Problem

The `note_capture_echo.sh` wrapper used `path.read_text()` to load the **entire** QuickThoughts.txt file into Python memory, then scanned bottom-up for the latest `⁜` block. For a growing inbox (700+ lines, ~46KB+), this is O(n) and adds unnecessary latency to every capture+echo call.

## Root Cause

Original Python inline script:

```python
lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
for idx in range(len(lines) - 1, -1, -1):
    if lines[idx].startswith("⁜ "):
        ...
```

This reads every line ever written just to find the last entry.

## Fix

1. Replace full-file read with `tail -n 50` piped to Python via stdin
2. Fall back to `tail -n 100` if the latest entry isn't in the first 50 lines
3. Write the Python scanner to a **temp `.py` file** instead of a heredoc (see below)

```python
# scanner reads from stdin (piped from tail)
lines = sys.stdin.read().splitlines()
for i in range(len(lines) - 1, -1, -1):
    if lines[i].startswith("\u205c "):  # ⁜ as unicode escape
        print("Captured entry:")
        print("\n".join(lines[i:]))
        sys.exit(0)
sys.exit(1)
```

## Bash Pitfall: Pipe + Heredoc Stdin Conflict

**`tail ... | python3 <<'PY'` silently fails.** Both the pipe and the heredoc compete for Python's stdin — the heredoc wins, and tail output is lost. The Python script receives its own source code as input instead of the tail output.

**Fix:** Write the Python scanner to a temp `.py` file and run `tail ... | python3 "$echo_py"`. This frees stdin for the pipe while the script is read from the filesystem.

```bash
echo_py="$(mktemp --suffix=.py)"
cat > "$echo_py" <<'PY'
import sys
lines = sys.stdin.read().splitlines()
...
PY

tail -n 50 "$NOTE_FILE" | python3 "$echo_py"
```

## User Guidance

User preference: the echo wrapper should stay lean. The `note` CLI is near-perfect and append-only by design — it doesn't need heavy verification scaffolding. Reserve the echo for testing/debugging, not routine capture.

## LP_skills Mirror

The echo script also exists at:
`/home/midnight/ExoCortex/websites/projects/LP_skills/agent-created/note-taking-note-capture-workflow/scripts/note_capture_echo.sh`

Both copies were patched in the same session. Committed as `908afd7` with message "optimized latency" and pushed to `origin/main`.
