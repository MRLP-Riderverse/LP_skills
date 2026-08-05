# Standalone GUI vs. CLI Audit Pattern

## Reproduction shape

A local plaintext notes system had two GUI paths:

- a legacy GUI launched by the canonical `note` script;
- a newer standalone desktop package with its own Tk shell and direct storage imports.

Both targeted the same inbox and project files, but their behavior differed. The legacy path already used bounded tail reads and delegated submission through the proven shell backend. The standalone fork reread the whole notes file for each recent-panel refresh and directly called the shared storage module.

## Evidence to collect

```text
launcher → GUI module → submit/read function → backend/storage → actual path
```

Inspect:

- `which`/entry-point availability and virtual-environment context;
- environment overrides such as `NOTES_DIR`, `NOTECORE_DIR`, and `NOTE_TARGET_FILE`;
- actual file extensions and dependencies before assuming a database;
- queue directories for both `*.json` and orphaned `*.json.tmp` files;
- file size/mtime and focused recent-entry reads;
- syntax, focused unit tests, and a GUI startup smoke test;
- a temporary-target write/readback probe, never the real inbox.

## Interpretation rules

- A healthy plaintext file and passing storage tests do not prove the standalone GUI is behaviorally current.
- An orphaned `.tmp` record is evidence of an interrupted staging write, not automatically a lost note or a reason to delete the file.
- A pending counter that only counts `*.json` does not account for orphaned temporary records.
- A package that imports only after activation or `PYTHONPATH` setup indicates launcher drift, not necessarily storage corruption.
- If the user says “the app” while multiple GUI paths exist, diagnose the ambiguity before patching.

## Performance diagnosis pattern

When the user reports that the GUI becomes slower as the shared plaintext file grows, split the measurement by interaction rather than assuming a full-file scan:

- **Launch:** include interpreter/Tk startup, initial Canvas construction, border/logo creation, and recent-preview loading.
- **Typing:** count redraws per key plus timer-driven animation frames; preserve motion if it is part of the tool's value.
- **Save:** inspect whether the GUI blocks on a shell subprocess, Python import, queue staging, append, or `fsync`; compare against a CLI save.
- **Resize:** inspect debounced `<Configure>` handling and whether full static decoration is rebuilt repeatedly.

Use temporary files at several sizes, including multi-megabyte fixtures. A bounded tail reader and append-only writer should produce roughly flat timings as the historical file grows. Flat save timings point toward process startup/import/fsync rather than file parsing. Repeated full Canvas deletion and recreation, especially symbol-by-symbol borders, is a common resize bottleneck. Prefer resize debouncing, cached/static decoration, and coalesced redraws before removing valued animation.

If the GUI delegates saving to a proven CLI, keep that path intact for the first fix. Make the GUI wait asynchronously only after success/error ordering is specified; do not silently bypass the canonical writer merely to shave process-startup time.

## Safe conclusion format

Separate the report into:

1. what is proven healthy;
2. what differs between implementations;
3. observed state that needs cautious interpretation;
4. interaction-specific measurements (launch, typing, save, resize);
5. unresolved reproduction questions;
6. an app-only repair proposal that explicitly leaves the CLI/capture path untouched.
