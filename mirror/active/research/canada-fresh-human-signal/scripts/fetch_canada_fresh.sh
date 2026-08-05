#!/usr/bin/env bash
# Callable entry point for the Canada Fresh research skill.
# Run this from a shell, CI job, or an external scheduler.
# Hermes cron jobs should normally preload the skill directly instead of
# recursively invoking this wrapper.
set -euo pipefail

prompt="${*:-Fetch Canada Fresh. Use the default scope and output format in the attached skill.}"

exec hermes chat \
  --query "$prompt" \
  --skills canada-fresh-human-signal \
  --toolsets web \
  --quiet
