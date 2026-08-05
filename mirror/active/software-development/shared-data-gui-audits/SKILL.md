---
name: shared-data-gui-audits
description: "Use when a GUI shares storage with a proven CLI."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [debugging, gui, cli, shared-storage, local-first, regression-safety]
    related_skills: [software-dev-workflow, note-capture-workflow]
---

# Shared-Data GUI Audits

Use this skill when a desktop or standalone GUI feels unreliable while a CLI, script, or capture workflow is known to work. The goal is to distinguish application drift from storage/backend failure without damaging the trusted path.

## Operating contract

- Treat the existing CLI/capture workflow as a protected reference implementation unless the user explicitly authorizes changes to it.
- Assume there may be multiple GUIs or launchers until the entry points are enumerated.
- Prefer evidence from live files, imports, logs, process behavior, and isolated probes over architectural assumptions.
- Diagnose first when the user asks to “look into” a problem and explicitly says not to break working behavior.
- Never write test probes into the user’s real data store; use a temporary root or temporary target file.

## Audit sequence

1. **Map entry points.** Locate launchers, scripts, package entry points, GUI modules, and parallel/legacy implementations. Record which command starts which UI.
2. **Trace data flow.** For each path, follow launcher → process → input handler → read/write code → storage files. Mark whether it delegates to the canonical backend or bypasses it.
3. **Establish storage authority.** Inspect dependencies and actual file formats before assuming a database. Check for SQLite files, plaintext logs, JSON staging records, and environment-variable path overrides.
4. **Compare implementations.** Search for recent fixes such as bounded tail reads, caches, retry queues, formatting rules, and path discovery. A fork may be missing a fix even when it points to the same files.
5. **Inspect state without mutation.** Check file sizes/timestamps, queue contents, ignored staging artifacts such as `.tmp`, and logs. Preserve orphaned evidence until its recovery semantics are understood.
6. **Run isolated probes.** Exercise imports, syntax, focused tests, GUI startup, and a capture/readback probe against a temporary target. Keep the real inbox untouched.
7. **Report before patching when scope is ambiguous.** Name the likely failing layer, state what is proven, and identify which GUI the proposed change would affect.
8. **Patch only the app layer when requested.** Keep the CLI, capture scripts, and known-good shared backend unchanged unless the user expands scope. Add a regression test for the app behavior and rerun the focused suite.
9. **Verify launch context.** Check whether the app is installed globally, only in a virtual environment, or dependent on `PYTHONPATH`; treat launcher ambiguity as a separate application issue, not proof of storage failure.
10. **Separate perceived slowness by interaction.** Measure launch, typing/rendering, save, and resize independently. Do not infer that a large plaintext file is the cause merely because the user notices the slowdown after growth.
11. **Preserve valued motion by default.** If the user says animation makes typing enjoyable and typing is generally responsive, do not disable motion as the first fix. Optimize redundant redraws, resize work, and blocking saves first.
12. **Use size-controlled probes.** Compare representative temporary files (small through multi-megabyte) for GUI initialization and app-mediated save. If timings remain flat, focus on interpreter/Tk startup, subprocess/import/fsync, border construction, or filesystem integration rather than replacing the storage format.
13. **Model a low-friction sidecar explicitly.** When the GUI exists to capture notes while the user works elsewhere, treat responsiveness and attention preservation as product requirements: input should return immediately, save completion should be asynchronous, and preview refresh should happen only after confirmed success.
14. **Coalesce event-loop work before redesigning visuals.** Route input and animation through one pending-render request, remove sequential calls that already redraw, and debounce resize-triggered full rebuilds. Preserve valued motion unless measurement shows it is the primary interaction bottleneck.
15. **Keep asynchronous saves serial and recoverable.** Use one worker/queue so submissions preserve order; clear the input immediately only after placing the capture in the queue; refresh recent content on success; restore failed content without discarding text typed while the save was running. Keep the existing CLI/backend call unchanged for the first GUI refactor.


## Evidence and interpretation

Report findings in four buckets:

- **Proven healthy:** tests, imports, startup smoke tests, or isolated writes that actually passed.
- **Proven divergent:** code paths where one UI has behavior absent from another.
- **Observed state:** queue files, timestamps, logs, or file contents; do not overinterpret them.
- **Unresolved:** questions requiring the user to identify the exact UI or reproduce a specific friction.

Do not call a storage problem a database problem without evidence. Do not call a GUI healthy merely because the data file contains the expected note: stale reads, slow redraws, launcher/environment drift, and bypassed retry logic can all produce user-facing friction while storage remains intact.

## Safety checklist

- [ ] Canonical CLI/capture path identified and left unchanged.
- [ ] Every GUI/launcher path enumerated.
- [ ] Actual storage format verified.
- [ ] Real data only read, not rewritten, during diagnosis.
- [ ] Temporary probes use a temporary target.
- [ ] Orphaned staging files preserved unless explicit cleanup is requested.
- [ ] Focused tests and startup smoke test completed.
- [ ] Any proposed patch is limited to the authorized app layer.

## References

- `references/standalone-gui-vs-cli-audit.md` — condensed audit pattern and evidence examples from a local plaintext notes application.
