---
name: github
description: "GitHub workflow: auth, repos, issues, PRs, code review, CI — full lifecycle via gh CLI and REST API."
version: 2.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Git, PR, Issues, Code-Review, CI/CD, gh-cli, REST-API]
    related_skills: [requesting-code-review, subagent-driven-development]
---

# GitHub — Complete Workflow Guide

Class-level skill covering the full GitHub lifecycle: authentication setup, repository management, issue triage, pull request workflow, and code review. Each section shows the `gh` way first, then the `git` + `curl` fallback for machines without `gh`.

## 0. Authentication Setup

Before any GitHub operation, determine the auth method:

```bash
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
  AUTH="gh"
else
  AUTH="git"
  if [ -z "$GITHUB_TOKEN" ]; then
    if [ -f ~/.hermes/.env ] && grep -q "^GITHUB_TOKEN=" ~/.hermes/.env; then
      GITHUB_TOKEN=$(grep "^GITHUB_TOKEN=" ~/.hermes/.env | head -1 | cut -d= -f2 | tr -d '\n\r')
    elif grep -q "github.com" ~/.git-credentials 2>/dev/null; then
      GITHUB_TOKEN=$(grep "github.com" ~/.git-credentials 2>/dev/null | head -1 | sed 's|https://[^:]*:\([^@]*\@.*|\1|')
    fi
  fi
fi
echo "Using: $AUTH"
```

### HTTPS Token Setup (no sudo needed)

1. User creates token at https://github.com/settings/tokens with `repo`, `workflow`, `read:org` scopes
2. `git config --global credential.helper store`
3. Test with `git ls-remote https://github.com/<user>/<repo>.git` — enter token as password
4. Set identity: `git config --global user.name "Name"` + `git config --global user.email "email"`

### SSH Key Setup

```bash
ssh-keygen -t ed25519 -C "email" -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub  # Add at https://github.com/settings/keys
ssh -T git@github.com      # Verify
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

### gh CLI Auth

```bash
echo "<TOKEN>" | gh auth login --with-token
gh auth setup-git
gh auth status  # Verify
```

### Troubleshooting Auth

| Problem | Solution |
|---------|----------|
| `git push` asks for password | GitHub disabled password auth — use PAT as password |
| `remote: Permission denied` | Token may lack `repo` scope — regenerate |
| `fatal: Authentication failed` | Cached credentials stale — `git credential reject` then re-auth |
| SSH port 22 refused | Use SSH over HTTPS port 443: `Hostname ssh.github.com` + `Port 443` in `~/.ssh/config` |
| Credentials not persisting | Must set `credential.helper` to `store` or `cache` |

---

## 1. Repository Management

### Extract Owner/Repo from Remote

```bash
REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\.com[:/]||; s|\.git$||')
OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO" | cut -d/ -f2)
```

### Clone / Create / Fork

**With gh:**

```bash
gh repo clone owner/repo
gh repo create my-project --public --clone
gh repo fork owner/repo --clone
```

**With curl:**

```bash
# Create a new repo
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user/repos -d '{"name":"my-project","private":false}'

# Fork
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/forks
```

### Repo Operations

| Action | gh | curl endpoint |
|--------|-----|--------------|
| List repos | `gh repo list` | `GET /user/repos` |

### Public Repo Hygiene Audit

Use this when the user asks "is my GitHub hygiene okay?" or wants a quick exposure review across public repos.

### Static-site audit checklist

When the repo is a GitHub Pages / static HTML site, pair the repo audit with `references/static-site-audit-checklist.md`.

### GitHub Pages Static Site Sync

Use this when one repo generates a payload that another GitHub Pages repo serves publicly.

1. Identify the source-of-truth repo and the Pages repo.
2. If the Pages repo needs a helper script, commit it first so the automation is tracked.
3. Update the source repo content.
4. Run the export/generation step that writes the Pages payload.
5. Commit the generated payload in the Pages repo.
6. If `git push` is rejected, fetch and rebase onto `origin/main` before retrying.
7. Verify the payload landed in the Pages repo working tree and is ready to deploy.
8. Remember GitHub Pages root behavior:
   - a repo root with no `index.html` falls back to `README.md`
   - a repo with a tiny placeholder `index.html` will publish that placeholder until the real file is committed

Reference: `references/github-pages-static-site-sync.md`

1. Enumerate public repos with the correct gh flag:
   ```bash
   gh repo list <owner> --public --limit 100 --json name,nameWithOwner,isPrivate,url,defaultBranchRef
   ```
   **Pitfall:** `gh repo list` uses `--public`, not `--visibility public`.
2. For each repo, inspect root contents for baseline hygiene:
   - `README.md`
   - `.gitignore`
   - license presence
3. Check current tree for suspicious filenames (for example `.env`, `*.pem`, `*.key`, `*secret*`, `*token*`, `*.db`).
4. Check recent commit history for the same suspicious filename patterns.
5. Query GitHub secret scanning alerts:
   ```bash
   gh api repos/<owner>/<repo>/secret-scanning/alerts?state=open
   ```
6. Report findings in three buckets:
   - confirmed risk
   - likely false positives
   - hygiene gaps / hardening opportunities

### Repo Operations

| Action | gh | curl endpoint |
|--------|-----|--------------|
| List repos | `gh repo list` | `GET /user/repos` |
| View repo | `gh repo view owner/repo` | `GET /repos/{o}/{r}` |
| Delete repo | `gh repo delete owner/repo --yes` | `DELETE /repos/{o}/{r}` |
| Rename | `gh repo rename new-name` | `PATCH /repos/{o}/{r}` with `{"name":"new-name"}` |
| List branches | `gh api repos/{o}/{r}/branches` | `GET /repos/{o}/{r}/branches` |
| List releases | `gh release list` | `GET /repos/{o}/{r}/releases` |
| Create release | `gh release create v1.0 --title "v1.0"` | `POST /repos/{o}/{r}/releases` |

### GitHub Pages / Static Site Publishing

Use this for repo-root Pages sites that are generated locally or exported from a data repo.

1. Treat the site repo as the deployable artifact; keep the data source in a separate repo when that is the design.
2. If the site is fed by an export step from a source repo, run the export from the source repo first, then switch to the site repo and commit the generated payload there.
3. Commit helper scripts that perform the export when they are part of the repeatable workflow; do not leave them as untracked local-only glue.
4. Inspect the generated root files before pushing.
5. Remember GitHub Pages behavior at repo root:
   - `index.html` is the public entry point.
   - If `index.html` is absent, Pages may show `README.md` instead.
   - A placeholder `index.html` will be served exactly as committed, even if your working tree has richer uncommitted files.
6. If `git push` is rejected with `fetch first`, don't force-push by habit. First `git fetch origin` and `git rebase origin/main`, then push again.
7. After export + commit + push, verify both repos:
   - source repo has the new content committed and pushed
   - site repo has the generated payload committed and pushed
   - the exported payload actually contains the new entry/data before claiming the site is live
8. For custom domain / identity rails (including SNS-style `.sol.site` setups), separate the naming layer from the hosting layer:
   - confirm the Pages site works at its GitHub URL first
   - confirm the custom domain actually resolves to the Pages target
   - do not assume a dashboard UI has completed the DNS handoff just because the name appears there

See `references/github-pages-static-site.md` for a concise sequence and pitfalls.
See `references/pages-custom-domain-and-sns.md` for the Acadie.sol custom-domain/SNS lesson.
See `references/hermes-skill-backup-sync.md` for a normalized mirror workflow for agent-made Hermes skills.

### Hermes Skill Backup Mirror Sync

Use this when a sibling repo is the restore point for agent-made Hermes skills.

1. Identify the live skill tree and the backup repo root.
2. Restrict the comparison to agent-made skills; skip bundled/base Hermes content.
3. Normalize skill names before matching so hyphenated and underscored layouts line up.
4. Compare the whole skill directory, not just `SKILL.md`.
5. Verify support files under `references/`, `templates/`, and `scripts/` with hashes or `diff -qr`.
6. If the backup includes shared runtime helpers, verify those files too.
7. Commit the mirror refresh as a single chore, then push.
8. Re-run a read-only verification after push and expect a clean tree.

Pitfall:
- `SKILL.md` parity alone is not enough; support files can drift independently.

### Two-repo Pages sync pattern

When a source repo exports into a sibling GitHub Pages repo, the safe order is:

1. Commit/push the source repo change.
2. Run the export script from the source repo.
3. Verify the generated payload in the site repo working tree.
4. Commit/push the site repo change.
5. Only then report the site as updated.

Pitfall:
- Export success does **not** mean the site repo is published yet; the generated payload still needs its own commit and push.

### Deterministic generated artifacts

For static site exports, generated artifacts should be deterministic so repeat exports do not create false git diffs.

Checklist:
- Do **not** stamp generated `.ics` calendar files with wall-clock export time when the event data did not change.
- Prefer a stable source-derived value such as the event record's `source_modified_at` for `DTSTAMP`.
- When writing generated files, compare the new body to the existing file and skip the write if content is identical.
- Treat intentionally volatile files (for example a `site-meta.json` with `generated_at` or refresh counters) separately from content artifacts; do not let that volatility justify noisy diffs in calendar or payload files.

Why this matters:
- timestamp-only diffs hide real changes
- repeat exports look dirty even when nothing changed
- accidental commits become more likely in two-repo publish flows

### API Cheatsheet

For full API reference, see `references/github-api-cheatsheet.md`.

---

## 2. Issues — Create, Triage, Manage

### Create an Issue

**With gh:**

```bash
gh issue create \
  --title "Login redirect ignores ?next= parameter" \
  --body "## Description\nAfter logging in, users always land on /dashboard.\n\n## Steps to Reproduce\n1. Navigate to /settings while logged out\n2. Get redirected to /login?next=/settings\n3. Log in\n4. Actual: redirected to /dashboard" \
  --label "bug,backend" \
  --assignee "username"
```

**With curl:**

```bash
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/issues \
  -d '{"title":"Bug title","body":"Description","labels":["bug"],"assignees":["user"]}'
```

### Issue Quick Reference

| Action | gh | curl endpoint |
|--------|-----|--------------|
| List issues | `gh issue list` | `GET /repos/{o}/{r}/issues` |
| View issue | `gh issue view N` | `GET /repos/{o}/{r}/issues/N` |
| Search | `gh issue list --search "term"` | `GET /search/issues?q=...` |
| Add labels | `gh issue edit N --add-label "bug"` | `POST /repos/{o}/{r}/issues/N/labels` |
| Assign | `gh issue edit N --add-assignee user` | `POST /repos/{o}/{r}/issues/N/assignees` |
| Comment | `gh issue comment N --body "text"` | `POST /repos/{o}/{r}/issues/N/comments` |
| Close | `gh issue close N` | `PATCH /repos/{o}/{r}/issues/N` state=closed |
| Reopen | `gh issue reopen N` | `PATCH /repos/{o}/{r}/issues/N` state=open |

### Triage Workflow

1. List untriaged: `gh issue list --label "needs-triage" --state open`
2. Read and categorize each issue
3. Apply labels and priority
4. Assign if owner is clear
5. Comment with triage notes

### Issue Templates

- Bug report: `templates/bug-report.md`
- Feature request: `templates/feature-request.md`

---

## 3. Pull Request Workflow

### Branch and Commit

```bash
git fetch origin && git checkout main && git pull origin main
git checkout -b feat/add-user-authentication
# ... make changes with file tools ...
git add src/auth.py tests/test_auth.py
git commit -m "feat: add JWT-based user authentication

- Add login/register endpoints
- Add User model with password hashing"
```

Commit format (Conventional Commits): `type(scope): short description`
Types: `feat`, `fix`, `refactor`, `docs`, `test`, `ci`, `chore`, `perf`

### Create a PR

**With gh:**

```bash
git push -u origin HEAD
gh pr create \
  --title "feat: add JWT-based user authentication" \
  --body "## Summary
- Adds login and register API endpoints
- JWT token generation and validation

## Test Plan
- [ ] Unit tests pass

Closes #42"
```

**With curl:**

```bash
BRANCH=$(git branch --show-current)
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/$OWNER/$REPO/pulls \
  -d "{\"title\":\"feat: add auth\",\"body\":\"Summary\",\"head\":\"$BRANCH\",\"base\":\"main\"}"
```

### PR Quick Reference

| Action | gh | curl endpoint |
|--------|-----|--------------|
| List PRs | `gh pr list` | `GET /repos/{o}/{r}/pulls` |
| View diff | `gh pr diff` | `git diff main...HEAD` |
| Add comment | `gh pr comment N --body "..."` | `POST /repos/{o}/{r}/issues/N/comments` |
| Request review | `gh pr edit N --add-reviewer user` | `POST /repos/{o}/{r}/pulls/N/requested_reviewers` |
| Close PR | `gh pr close N` | `PATCH /repos/{o}/{r}/pulls/N` state=closed |
| Checkout PR | `gh pr checkout N` | `git fetch origin pull/N/head:pr-N` |

### PR Body Templates

- Feature PR: `templates/pr-body-feature.md`
- Bugfix PR: `templates/pr-body-bugfix.md`

---

## 4. Monitoring CI and Auto-Fix

### Check CI Status

```bash
# With gh
gh pr checks
gh pr checks --watch  # Poll every 10s

# With curl
SHA=$(git rev-parse HEAD)
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/commits/$SHA/status \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'Overall: {d[\"state\"]}')"
```

### Auto-Fix Loop

1. Check CI → identify failures
2. Read failure logs: `gh run view <RUN_ID> --log-failed`
3. Fix with `patch`/`write_file`
4. `git add . && git commit -m "fix: ..." && git push`
5. Re-check CI (max 3 attempts, then ask user)

### CI Troubleshooting

See `references/ci-troubleshooting.md` for common CI failure patterns and fixes.

---

## 5. Merging

```bash
# Squash merge + delete branch (recommended for feature branches)
gh pr merge --squash --delete-branch

# Enable auto-merge (merges when all checks pass)
gh pr merge --auto --squash --delete-branch

# With curl
curl -s -X PUT -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/merge \
  -d '{"merge_method":"squash","commit_title":"feat: add auth (#N)"}'
```

Merge methods: `"merge"` (merge commit), `"squash"`, `"rebase"`

---

## 6. Code Review

### Review a PR

**With gh:**

```bash
# View the diff
gh pr diff N

# Approve
gh pr review N --approve --body "LGTM — clean implementation"

# Request changes
gh pr review N --request-changes --body "Please add tests for the auth middleware"

# Comment without approving/requesting changes
gh pr review N --comment --body "Just a note: consider using bcrypt instead"
```

**With curl (inline comments):**

```bash
# Submit review with inline comments
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/N/reviews \
  -d '{
    "body": "Overall review comment",
    "event": "REQUEST_CHANGES",
    "comments": [{
      "path": "src/auth.py",
      "position": 15,
      "body": "This should use constant-time comparison"
    }]
  }'
```

### Review Workflow

1. Get the diff: `gh pr diff N` or fetch the PR branch
2. Check for: security issues, test coverage, code style, logic errors
3. Leave inline comments for specific lines
4. Approve, request changes, or comment

### Review Output Template

See `references/review-output-template.md` for structured review output format.

---

## Codebase Inspection (pygount)

Use `pygount` for quick LOC/language analysis of a repo:

```bash
# Install
pip install pygount

# Analyze a directory
pygount --format=summary /path/to/project

# Output as CSV
pygount --format=csv /path/to/project > loc_report.csv
```

Useful for: understanding codebase size, language distribution, and identifying large files to refactor.

---

## Pitfalls

- **Auth detection block** — every GitHub skill repeats the same auth detection. This umbrella consolidates it at section 0. Always check auth before proceeding.
- **PRs in issues endpoint** — GitHub's `/issues` API returns PRs too. Filter with `'pull_request' not in i`.
- **filterByFormula URL encoding** — always URL-encode special characters in search queries.
- **Auto-merge via REST** — auto-merge requires GraphQL API, not REST. Use `gh pr merge --auto` instead.
- **Token scopes** — `repo` scope covers most operations; `workflow` needed for Actions.
- **Rate limits** — authenticated: 5000 req/hr; unauthenticated: 60 req/hr. Use `gh` when possible (handles pagination automatically).

## References

- `references/github-api-cheatsheet.md` — REST API quick reference
- `references/ci-troubleshooting.md` — CI failure patterns
- `references/conventional-commits.md` — Commit message format guide
- `references/review-output-template.md` — Structured review template
- `references/public-repo-hygiene-checklist.md` — Fast audit checklist for public repo hygiene and exposure review
- `references/github-pages-static-site.md` — Pages root behavior, static-site split, and push/rebase verification notes
- `references/github-pages-static-site-sync.md` — Two-repo export/publish order and verification checklist
- `references/hermes-skill-backup-sync.md` — Agent-made Hermes skill mirror workflow and verification checklist
- `scripts/gh-env.sh` — Auth environment setup script
- `templates/bug-report.md` — Issue bug report template
- `templates/feature-request.md` — Feature request template
- `templates/pr-body-feature.md` — Feature PR body template
- `templates/pr-body-bugfix.md` — Bugfix PR body template
