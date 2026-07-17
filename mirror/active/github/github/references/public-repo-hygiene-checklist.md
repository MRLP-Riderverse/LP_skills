# Public Repo Hygiene Checklist

Use for fast audits of a user's public GitHub footprint.

## Minimum checks
- Repo visibility confirmed public
- `README.md` present
- `.gitignore` present
- License decision present
- No obvious secret-like filenames in current tree
- No obvious secret-like filenames in recent commit history
- `secret-scanning/alerts?state=open` returns zero open alerts

## Common suspicious filename patterns
- `.env`, `.env.*`
- `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.crt`, `*.cer`
- `id_rsa`, `id_ed25519`
- names containing `secret`, `token`, `credential`, `password`, `private`
- `*.db`, `*.sqlite`, `*.sql`, `*.dump`

## Interpretation rules
- Treat filename hits as leads, not verdicts.
- Documentation can legitimately contain words like `token` or `secret`.
- Missing `.gitignore` is a future-risk signal, not evidence of exposure.
- Missing license is a stewardship/legal clarity issue, not a credential leak.
- If a real secret was ever pushed, rotate/revoke first; history cleanup comes second.

## Useful gh commands
```bash
gh repo list <owner> --public --limit 100 --json name,nameWithOwner,url,defaultBranchRef
gh api repos/<owner>/<repo>
gh api repos/<owner>/<repo>/contents?ref=<branch>
gh api repos/<owner>/<repo>/git/trees/<branch>?recursive=1
gh api repos/<owner>/<repo>/secret-scanning/alerts?state=open
```

## Output shape
Report:
1. Overall verdict
2. Good signals
3. Findings by repo
4. Immediate fixes
5. Optional hardening next steps
