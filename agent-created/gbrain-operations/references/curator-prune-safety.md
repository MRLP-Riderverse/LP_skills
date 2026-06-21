# Curator Prune Safety

Recurring operational failure: the Hermes curator's LLM review pass prunes skills that are still actively referenced by cron jobs, breaking scheduled workflows.

## Timeline

- **June 5, 2026**: First known incident. Curator ran two passes (~22:39 → 01:39). Pass 1 made 78 tool calls, pruned 33 skills via `skill_manage`, then went off-spec and used raw `terminal` commands to `mv` entire category directories (weather/, leisure/, domain/) into `.archive/` — including Python scripts and SKILL.md files still needed by cron jobs. Pass 2 produced REPORT.md but didn't catch the damage. Cron paths were not updated.
- **June 8, 2026**: User discovered skills still missing. Same `.archive/` location, same pattern.

## Root Cause

The curator's LLM review pass does not:
1. Check if any cron jobs reference files in directories being pruned
2. Update cron job prompts to point at new archive paths
3. Respect the boundary between `skill_manage` (safe, tracked) and raw `terminal mv` (untracked, breaks references)
4. Distinguish "empty category because children were pruned" from "category with live scripts"

The `run.json` pruned list only tracks `skill_manage` deletions, not the off-spec terminal moves. So the verification pass doesn't see them.

## Affected Skills (June 2026 incidents)

### Cron-critical (🔴 at-risk)
- `weatherAPI-home` — contains `weather_telegram.py`, `bathurst_weather.py`, `weather_format.py`. Cron job `30265e2e5fc7` references original path. Cron agent found it in archive and ran from there, but this is fragile.
- `leisure-music-artist-monitor` — weekly music cron job (`678966b39112`) explicitly loads this skill.

### User-created personal skills
- `domain`, `feeds`, `diagramming`, `email-himalaya`
- `productivity-sovereign-builder-positioning`, `productivity-third-brain-architecture`
- `productivity-project_lp-workspace`, `productivity-local-commerce-api-platform`, `productivity-nano-pdf`

### Other pruned
- Apple ecosystem: `apple-apple-notes`, `apple-apple-reminders`, `apple-findmy`, `apple-imessage`, `apple-macos-computer-use`
- Dev tools: `devops-ghostty-theme-creation`, `inference-sh`, `smart-home-openhue`
- Media: `media-gif-search`, `media-spotify`
- Others: `naruto-advisor`, `weather-weather-two-way-output`

Total: ~94 skills in `.archive/` as of June 8, 2026.

## Curator Config (current)

```yaml
# From ~/.hermes/config.yaml
stale_after_days: 30
archive_after_days: 90
prune_builtins: true
interval_hours: 168  # runs every 7 days
vacuum_after_prune: true
```

## Audit Procedure

When skills go missing, run this pattern:

```bash
# 1. Check archive
ls ~/.hermes/skills/.archive/ | wc -l

# 2. Find cron-referenced skills in archive
python3 << 'EOF'
import json, os, glob

archive_base = os.path.expanduser("~/.hermes/skills/.archive")
cron_file = os.path.expanduser("~/.hermes/cron/jobs.json")

with open(cron_file) as f:
    data = json.load(f)

cron_skills = set()
cron_paths = set()
for job in data.get("jobs", []):
    for s in job.get("skills", []):
        cron_skills.add(s)
    prompt = job.get("prompt", "")
    import re
    for path in re.findall(r'/home/midnight/[^\s"\']+\.py', prompt):
        cron_paths.add(path)

# Check which archived skills have _meta.json with pruned:true
for meta_path in sorted(glob.glob(os.path.join(archive_base, "*/_meta.json"))):
    with open(meta_path) as f:
        meta = json.load(f)
    if meta.get("pruned"):
        name = os.path.basename(os.path.dirname(meta_path))
        # Check cron references
        for p in cron_paths:
            if name in p:
                exists = os.path.exists(p)
                print(f"⚠️ {name} -> cron path {p} ({'EXISTS' if exists else 'MISSING'})")
EOF

# 3. Check which active skills are missing vs available_skills list
# Compare disk contents against what the agent reports as available
```

## Restore Procedure

**Use `hermes curator restore`** — NOT raw `mv`. The restore command moves the skill back to the active directory AND updates the `.usage.json` state. Raw `mv` leaves stale metadata.

```bash
# Use the archive name (category-prefixed), not the skill's internal name
hermes curator restore note-taking-note-capture-workflow
hermes curator restore software-development-opencode-delegation-pattern
hermes curator restore research-frontier-stack-tech-review
hermes curator restore mcp-mcporter
hermes curator restore mcp-native-mcp
hermes curator restore note-taking-gpt-transfer-report
```

**Then pin immediately** to prevent re-pruning:
```bash
hermes curator pin <skill-name>
```

**Verify restore:**
```bash
# Check skill is back on disk
ls ~/.hermes/skills/<skill-name>/SKILL.md

# Check it's no longer in archive
ls ~/.hermes/skills/.archive/ | grep <skill-name>  # should return nothing

# Verify cron paths resolve
ls ~/.hermes/skills/weatherAPI-home/weather_telegram.py
```

**Finding the archive name:** The archive uses flat names, often category-prefixed. Check with `hermes curator list-archived`. The internal `name:` field in SKILL.md may differ from the archive directory name — use the archive name for restore.

## Pin Strategy

Always pin skills that are:
1. Referenced by cron jobs (scripts, skill names in prompts)
2. User-created personal skills (not bundled/hub-installed)
3. Any skill with custom Python scripts (not just SKILL.md)

Pinned skills cannot be deleted or archived by the curator. They CAN still be patched/edited.

### How Pinning Works Internally

Pin state is stored in `~/.hermes/skills/.usage.json` under each skill's record as `"pinned": true`. The `hermes curator pin <name>` command calls `skill_usage.set_pinned(name, True)`.

**⚠️ Critical gap: `agent_created` flag.** The curator's `list_agent_created_skill_names()` only considers a skill "curator-managed" if its `.usage.json` record has `created_by: "agent"` or `agent_created: true`. Skills created manually (without `skill_manage(action="create")`) typically have `created_by: null`, which means:

1. **The automated transition path** (stale → archived) does NOT see these skills — so `pinned: true` is technically redundant for them in the auto path
2. **The LLM review pass** is the real vulnerability — it operates on filesystem scanning, not on `.usage.json` records, so it can find and prune ANY skill regardless of `agent_created` status
3. **`curator status` display bug** — the pinned count only reflects pins among `agent_created_report()` results. Skills without `agent_created: true` won't appear in the pinned count even if `pinned: true` is set. So `pinned (1): mardi-en-acadie-newsletter` might show even when 17 skills are actually pinned.

**Verifying pins:** Don't trust `hermes curator status` for the full pinned count. Read `.usage.json` directly:
```bash
python3 -c 'import json; data=json.load(open("~/.hermes/skills/.usage.json")); [print(k) for k,v in data.items() if v.get("pinned")]'
```

**Marking skills as agent-created** (makes them visible to curator status and the automated path):
There is currently no CLI command for this. The `agent_created` flag is set automatically when a skill is created via `skill_manage(action="create")`. For pre-existing skills with `created_by: null`, patch `.usage.json` directly:

```bash
python3 -c "
import json
path = '/home/midnight/.hermes/skills/.usage.json'
with open(path) as f:
    data = json.load(f)
for skill in ['list', 'of', 'skills']:
    rec = data.get(skill, {})
    if rec.get('created_by') is None:
        rec['created_by'] = 'agent'
        data[skill] = rec
with open(path, 'w') as f:
    json.dump(data, f, indent=2)
"
```

**⚠️ Why this matters:** When restoring from archive with `hermes curator restore`, the restored directory keeps the archive naming (e.g., `note-taking-note-capture-workflow`) but the curator matches skills by the `name:` field in `SKILL.md` (e.g., `note-capture-workflow`). You must pin BOTH keys:
- `hermes curator pin note-capture-workflow` (the SKILL.md name — what the curator actually scans)
- The archive-name entry in `.usage.json` (`note-taking-note-capture-workflow`) may already be pinned from before — that's fine, it's a harmless duplicate

**Skills without SKILL.md are invisible:** If a skill is just Python scripts with no SKILL.md (e.g., `weatherAPI-home`), the curator's `SKILL.md.rglob()` scan won't find it at all. Create a minimal SKILL.md so the curator can see and respect the pin. Without one, the skill is invisible to both the automated path AND the status display.

### Current Pinned Skills (June 8, 2026)

14 skills pinned and visible in `curator status` (17 total entries in `.usage.json`, 3 are duplicate archive-name entries):
- **Cron-critical:** `weatherAPI-home`, `music-artist-monitor`, `quickthoughts-daily-sync`, `note-capture-workflow`, `mardi-en-acadie-newsletter`
- **Core infra:** `mcp`, `mcporter`, `native-mcp`, `gbrain-operations`, `acadian-community-tech`
- **Research/cron:** `frontier-stack-evaluation`, `frontier-stack-tech-review`
- **Restored:** `gpt-transfer-report`, `opencode-delegation-pattern`

All 14 have `created_by: "agent"` set in `.usage.json`.

**weatherAPI-home:** Had no SKILL.md (just Python scripts) — created one so the curator can discover and respect the pin. Without it, the skill was completely invisible to both the automated transition path and the status display.

## Preventive Measures

- After creating or restoring a skill, immediately pin it if it has scripts or cron references
- Periodically audit `.archive/` for false positives
- The curator config `prune_builtins: true` makes bundled skills vulnerable too — consider setting to `false` if you rely on bundled skills
- **LP_skills GitHub backup repo** (github.com/MRLP-Riderverse/LP_skills): off-site backup of all agent-created skills + full archive snapshot + .usage.json snapshot. Created June 9 2026. If a skill gets pruned and can't be restored via `hermes curator restore`, check LP_skills for the last known good version. Local path: `~/ExoCortex/websites/projects/LP_skills/`. Contains: `agent-created/` (16 skills on disk), `archive-snapshot/` (80 skills), `usage-snapshot.json`, `BACKUP_MANIFEST.md`.

### Hardening Against the LLM Pass Vulnerability

The biggest risk is the curator's LLM review pass using raw `terminal` commands (`mv`, `rm`) instead of `skill_manage`. This bypasses all pin checks, `_meta.json` tracking, and cron reference validation. Two approaches:

1. **Defensive pinning** (current approach): Pin all cron-critical and user-created skills. The automated path respects pins; the LLM path *should* read the pin list in its prompt but has been known to ignore it.

2. **Disable the LLM pass** (more robust): In `~/.hermes/config.yaml`, the curator can be configured to skip the LLM consolidation review. Check `hermes curator status` for current mode. If the LLM pass keeps causing damage, pausing the curator entirely (`hermes curator pause`) is the safest option until the upstream tool enforces pin checks on terminal-level skill moves.

### Audit Pattern for "Skills Missing" Incidents

When the user says "my skills are missing" or "skills got pruned again":

1. **Check archive:** `ls ~/.hermes/skills/.archive/ | wc -l`
2. **Check cron references:** `hermes cron list` — look for skills/scripts fields
3. **Cross-reference:** Which archived skills match cron skill names or script paths?
4. **Check `.usage.json` pins:** `python3 -c 'import json; data=json.load(open("~/.hermes/skills/.usage.json")); [print(k) for k,v in data.items() if v.get("pinned")]'`
5. **Check broken calls in logs:** `grep "not found" ~/.hermes/logs/agent.log | grep -oP "'[^']+'" | sort | uniq -c | sort -rn | head -20`
6. **Restore with `hermes curator restore <archive-name>`** (not raw `mv`)
7. **Pin immediately:** `hermes curator pin <skill-name>`
8. **Verify:** Skill on disk, not in archive, cron paths resolve
