# LP_skills — Pinned & Cron-Critical Backup

Backup of MidnightRider.sol's crucial Hermes skills — the ones that keep the machine running.

## Why This Exists

The Hermes curator has pruned skills twice (June 5, June 8 2026) — including cron-critical ones.
This repo is the restore point. If something gets pruned, copy it back.

## Tier 1 — Cron-Critical (will break scheduled jobs if pruned)
- weatherAPI-home — daily Bathurst weather → Telegram
- quickthoughts-daily-sync — daily QT sync to GBrain
- leisure-music-artist-monitor — music industry monitoring
- acadian-community-tech — Acadian community briefing
- research-frontier-stack-tech-review — daily frontier stack tech briefing
- mardi-en-acadie-newsletter — periodic Acadian newsletter

## Tier 2 — Pinned, Important (breaks workflows if pruned)
- gbrain-operations — GBrain infra + curator prune safety docs
- gpt-transfer-report — GPT session transfer pattern
- note-taking-note-capture-workflow — note capture routing
- note-capture-workflow — current live note capture skill path/name
- note-taking-gpt-transfer-report — variant of transfer report
- software-development-opencode-delegation-pattern — opencode delegation
- local-browser-accessibility-automation — browser automation

## Tier 3 — Agent-Created, Nice to Have
- frontier-stack-evaluation — research evaluation
- acadie-sol-website — Acadie.sol site workflow and references
- community-event-directory-linking — event ↔ directory linking workflow
- cron-job-reliability — Hermes cron failure / provider-routing notes
- git-secrets-hygiene — secret exposure verification and remediation
- hermes-provider-config — provider/local model config sync notes
- mcp, mcp-mcporter, mcp-native-mcp — MCP tooling

## How to Restore

1. Find the skill in agent-created/
2. Copy back to ~/.hermes/skills/ (correct category path)
3. Ensure created_by: "agent" + pinned: true in .usage.json
4. Verify: `hermes curator pin <name>`
5. Check cron jobs that reference it still work

## Update

Run backup after significant skill changes. Cron-critical skills change rarely.

Author: MidnightRider.sol — created June 9 2026
