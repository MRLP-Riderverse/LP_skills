#!/usr/bin/env bash
set -euo pipefail

NOTE_SCRIPT="${NOTE_SCRIPT:-/home/midnight/ExoCortex/Agentic/Scripts/note}"
NOTE_FILE="${NOTE_TARGET_FILE:-$HOME/Documents/Notes/notecore/inbox/QuickThoughts.txt}"

if [[ $# -eq 0 ]]; then
  exec "$NOTE_SCRIPT"
fi

note_stdout="$(mktemp)"
cleanup() {
  rm -f "$note_stdout"
}
trap cleanup EXIT

if "$NOTE_SCRIPT" "$@" >"$note_stdout"; then
  true
else
  status=$?
  cat "$note_stdout" >&2 || true
  exit "$status"
fi

python3 - "$NOTE_FILE" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
if not path.exists():
    raise SystemExit(f"note file not found: {path}")

lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
for idx in range(len(lines) - 1, -1, -1):
    if lines[idx].startswith("⁜ "):
        print("Captured entry:")
        print("\n".join(lines[idx:]))
        break
else:
    raise SystemExit("latest capture not found in note file")
PY
