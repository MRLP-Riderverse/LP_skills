---
name: debugging
description: "Debug Python and Node.js — pdb, debugpy, node inspect, CDP — plus systematic root-cause investigation methodology."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [debugging, python, nodejs, pdb, debugpy, CDP, root-cause, troubleshooting]
    related_skills: [systematic-debugging, test-driven-development]
---

# Debugging — Python, Node.js, and Root-Cause Methodology

Class-level skill covering debugging tools and methodology. Three sections: (1) Systematic root-cause investigation, (2) Python debugging with pdb/debugpy, (3) Node.js debugging with inspect/CDP.

---

## Section 1: Systematic Root-Cause Investigation

**Iron law: NO FIXES WITHOUT ROOT CAUSE.**

### Phase 1: Root Cause Investigation

1. Reproduce the issue reliably
2. Isolate: narrow the scope (which module, which function, which line)
3. Collect evidence: logs, error messages, stack traces, state snapshots
4. Form initial hypothesis

### Phase 2: Pattern Analysis

1. Check for similar failures in other tests/modules
2. Identify temporal patterns (always? intermittent? after specific changes?)
3. Map the failure to a code path

### Phase 3: Hypothesis & Testing

1. Rank hypotheses by likelihood
2. Test the most likely first with minimal probes
3. Rule of 3: if 3 fixes fail, question the architecture
4. Document what you ruled out and why

### Phase 4: Implementation

1. Make the smallest possible fix
2. Add a test that would have caught the original bug
3. Verify the fix doesn't break anything else
4. Document the root cause in the commit message

### Anti-Patterns

- **Shotgun debugging** — changing multiple things at once without understanding
- **Symptom fixing** — treating the error message, not the cause
- **Assumption debugging** — "I think it's X" without evidence
- **Cargo-cult fixes** — copying fixes from StackOverflow without understanding

### Front-end / static HTML+JS regressions

When debugging menu/search/theme behavior in static pages:
- Preserve existing markup when updating labels. If a button uses nested spans/icons, update attrs/state instead of replacing the element's contents.
- Treat "same button should bring me back" as an in-place focus/scroll action, not a reset or page reload.
- Use an explicit clear/reset control only when the user asks to clear state.
- If a dock disappears on only one page, inspect page-local CSS overrides and media-query-specific hiding rules first.
- For fast-click bugs, verify the state machine order: render current state, then apply the new state, then focus/scroll.

See `references/front-end-ui-regressions.md` for a condensed pattern note.

---

## Section 2: Python Debugging

### Tools by Situation

| Tool | When to use | How |
|------|-------------|-----|
| `breakpoint()` + pdb | Quick local debug | Add `breakpoint()` in code, run normally |
| `python -m pdb` | Launch under debugger from start | `python -m pdb script.py` |
| `debugpy` | Remote/attach debugging | `python -m debugpy --listen 5678 script.py` |

### pdb Quick Reference

```
(Pdb) h          # Help
(Pdb) n          # Next line (step over)
(Pdb) s          # Step into
(Pdb) c          # Continue execution
(Pdb) b 42       # Set breakpoint at line 42
(Pdb) b func     # Set breakpoint at function
(Pdb) p var      # Print variable
(Pdb) pp var     # Pretty-print variable
(Pdb) w          # Show stack trace
(Pdb) u          # Go up one frame
(Pdb) d          # Go down one frame
(Pdb) l          # List source around current line
(Pdb) q          # Quit
```

### Common Recipes

**Local breakpoint:**
```python
# In your code:
breakpoint()  # Python 3.7+
# Or: import pdb; pdb.set_trace()
```

**Debug pytest test:**
```bash
python -m pdb -m pytest tests/test_auth.py::test_login -x
# Or with debugpy:
python -m debugpy --listen 5678 -m pytest tests/test_auth.py::test_login -x
```

**Post-mortem (debug after crash):**
```bash
python -m pdb -c continue script.py
# Drops into debugger at the point of crash
```

### debugpy Remote Debugging

```bash
# Start program with debugpy listener
python -m debugpy --listen 5678 --wait-for-client script.py

# Connect with DAP client (VS Code, etc.)
# Or use the DAP script approach for CLI-based debugging
```

### Pitfalls (Python)

- **xdist + pdb** — pytest-xdist captures output; use `-s` flag or disable xdist for debugging
- **CI hangs** — debugpy `--wait-for-client` will hang CI; only use in local dev
- **PYTHONBREAKPOINT** — set `PYTHONBREAKPOINT=0` to disable all breakpoints (useful in CI)
- **ptrace_scope** — on Linux, `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope` needed for attach
- **Threads** — pdb is single-threaded; use `threading.settrace()` for multi-threaded debugging
- **Asyncio** — use `aiomonitor` or `pdb++` with asyncio support

### Hermes-Specific Debugging

For debugging Hermes agent internals:
- Tests: `python -m debugpy --listen 5678 -m pytest tests/`
- `run_agent.py`: `python -m debugpy --listen 5678 run_agent.py`
- TUI Gateway: attach to running PID
- `_SlashWorker`: set breakpoints in slash command handlers

---

## Section 3: Node.js Debugging

### Tools

| Tool | When to use | How |
|------|-------------|-----|
| `node inspect` | Built-in CLI REPL (preferred) | `node inspect script.js` |
| `chrome-remote-interface` | Scriptable CDP | `npm install chrome-remote-interface` |

### node inspect Quick Reference

```
> c              # Continue
> n              # Next (step over)
> s              # Step into
> o              # Step out
> pa             # Pause
> sb('file.js', 10)  # Set breakpoint at file:line
> .exit          # Quit
```

### Attaching to Running Process

```bash
# Send SIGUSR1 to enable inspector on a running Node process
kill -USR1 <PID>
# Then connect:
node inspect localhost:9229
```

### CDP (Chrome DevTools Protocol)

```javascript
// driver.js — scriptable CDP client
const CDP = require('chrome-remote-interface');

async function debug() {
  const client = await CDP({port: 9229});
  const {Runtime, Debugger} = client;
  await Runtime.enable();
  await Debugger.enable();
  // Set breakpoints, evaluate expressions, etc.
}
debug();
```

### Hermes TUI Debugging

The Hermes UI (Ink-based) can be debugged via:
```bash
node --inspect ~/.hermes/ui-tui/index.js
# Then connect with node inspect or CDP
```

### Heap Snapshots & CPU Profiles

```bash
# Take heap snapshot via CDP
# Connect to the inspector, then:
const {HeapProfiler} = client;
await HeapProfiler.enable();
await HeapProfiler.takeHeapSnapshot();
```

### Pitfalls (Node.js)

- **Source maps** — TypeScript/ESM may need `--enable-source-maps` flag
- **Forked processes** — child processes need their own `--inspect` flag with unique ports
- **Ink components** — React/Ink DevTools require separate setup; prefer `console.log` + CDP
- **Vitest tests** — use `node --inspect vitest run --no-threads` for single-threaded debugging
