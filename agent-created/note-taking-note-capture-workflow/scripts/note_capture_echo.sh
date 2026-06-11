#!/usr/bin/env bash
set -euo pipefail

NOTE_SCRIPT="${NOTE_SCRIPT:-/home/midnight/ExoCortex/Agentic/Scripts/note}"
NOTE_FILE="${NOTE_TARGET_FILE:-$HOME/Documents/Notes/notecore/inbox/QuickThoughts.txt}"

if [[ $# -eq 0 ]]; then
  exec "$NOTE_SCRIPT"
fi

note_stdout="$(mktemp)"
echo_py="$(mktemp --suffix=.py)"
cleanup() { rm -f "$note_stdout" "$echo_py"; }
trap cleanup EXIT

# Write the echo scanner to a temp file (stdin must be free for tail pipe)
cat > "$echo_py" <<'PY'
import sys
lines = sys.stdin.read().splitlines()
for i in range(len(lines) - 1, -1, -1):
    if lines[i].startswith("\u205c "):
        print("Captured entry:")
        print("\n".join(lines[i:]))
        sys.exit(0)
sys.exit(1)
PY

if "$NOTE_SCRIPT" "$@" >"$note_stdout"; then
  if result=$(tail -n 50 "$NOTE_FILE" | python3 "$echo_py"); then
    printf '%s\n' "$result"
  elif result=$(tail -n 100 "$NOTE_FILE" | python3 "$echo_py"); then
    printf '%s\n' "$result"
  else
    echo "note captured (echo readback failed — entry is in QuickThoughts)" >&2
  fi
else
  status=$?
  cat "$note_stdout" >&2 || true
  exit "$status"
fi
