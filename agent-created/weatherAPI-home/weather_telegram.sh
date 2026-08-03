#!/usr/bin/env bash
set -euo pipefail

WEATHER_DIR="/home/midnight/.hermes/skills/weatherAPI-home"
ENV_FILE="$HOME/.hermes/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

cd "$WEATHER_DIR"

# Keep delivery deterministic: the weather report and its optional archival note
# are both produced locally. QuickThoughts capture failure must never suppress
# the Telegram weather delivery.
report="$(python3 "$WEATHER_DIR/weather_telegram.py" "$@")"
printf '%s\n' "$report"

if note_text="$(python3 "$WEATHER_DIR/bathurst_weather.py" --format note "$@" 2>/dev/null)"; then
  NOTE_SOURCE_LABEL=Weather "$HOME/ExoCortex/Agentic/Scripts/note" "$note_text" >/dev/null 2>&1 || true
fi
