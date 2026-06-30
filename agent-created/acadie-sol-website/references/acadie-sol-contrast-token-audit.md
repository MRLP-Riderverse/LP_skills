# Acadie.sol Contrast and Token Audit

Use this reference when the user asks for light/dark visual tuning, contrast cleanup, or “make it readable.”

## User expectation
- Legibility beats subtle aesthetic tinting.
- Light mode: offwhite/paper surfaces with dark ink text.
- Dark mode: charcoal/blackboard surfaces with light parchment text.
- Links, descriptions, notes, footer text, placeholders, quick cards, drawers, and event/detail rows must remain visibly readable in both modes.

## Token pattern
Prefer one shared semantic palette across public pages:

```css
:root {
  --paper: #fffaf2;
  --paper-soft: #fbf3e7;
  --ink: #2f261d;
  --ink-strong: #1a1410;
  --muted: #5f5247;
  --link: #0d2f5e;
  --link-hover: #174b8e;
  --blue-deep: #0d2f5e;
  --blue-ink: #fffaf2;
}
[data-theme="dark"] {
  --paper: #2a2520;
  --paper-soft: #332e27;
  --ink: #f2eadf;
  --ink-strong: #fff8ec;
  --muted: #d1c2ad;
  --link: #9fc7ff;
  --link-hover: #cfe3ff;
  --blue-deep: #9fc7ff;
  --blue-ink: #0d2f5e;
}
```

## Audit commands
Run from the project root after CSS edits:

```bash
# Catch hardcoded text/link colors that often break theme contrast.
rg -n "color: #[0-9a-fA-F]{3,8}|color: rgba|a \\{ color: inherit|a \\{ color: #fff|\\.description .*rgba|\\.notes .*rgba|\\.desc .*rgba" *.html

# Check scripts embedded in HTML.
python3 - <<'PY'
import re, subprocess, tempfile
from pathlib import Path
for html in ['index.html','events.html','directory.html','entry.html','recents.html']:
    text=Path(html).read_text()
    scripts=re.findall(r'<script>([\s\S]*?)</script>', text)
    for i,script in enumerate(scripts):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
            f.write(script); path=f.name
        r=subprocess.run(['node','--check',path], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f'{html} script {i} FAIL\n{r.stderr}')
    print(f'{html}: {len(scripts)} script(s) ok')
PY
```

## Browser verification
Use Puppeteer or browser tools to verify actual computed styles, not just CSS text. Do not trust grep alone: malformed trailing CSS or later token overrides can make the visible page differ from the intended palette.

For directory dark mode, confirm representative elements resolve to semantic tokens:

- `.card-title`, `.description`: `--ink`
- `.notes`, `.note-list`, `.detail-value`: `--muted` or `--ink` depending importance
- `.detail-link`, normal links: `--link`
- card/panel/drawer backgrounds: `--paper`, `--paper-soft`, or tokenized `color-mix(...)`

For events / “What’s Happening” dark mode, explicitly inspect:

- `.event-main h2`: should resolve near `--ink-strong` (`#fff8ec`)
- `.description`: should resolve near `--ink` (`#f2eadf`)
- `.event-subline`, `.side-note`: should resolve near readable `--muted` (`#d1c2ad`), not dim brown/gray
- `.event-card`, `.empty`, `.site-dock`, `.drawer`: should use tokenized charcoal/glass surfaces, not hardcoded offwhite `rgba(255,250,242,...)`

## Common blockers
- Multiple `:root` / `[data-theme="dark"]` blocks defining different token systems in the same file.
- Malformed leftover CSS blocks near `</style>` (example: a dangling `[data-theme="dark"] { --page-bg: ...`) that do not show up as JS errors but can still corrupt CSS parsing/cascade.
- Global `a { color: inherit; }` making links blend into context.
- Hardcoded offwhite backgrounds left in dark mode under light text.
- Hardcoded `color: rgba(...)` on descriptions/notes/footer copied from old dark-only designs.
- Public-but-secondary pages like `recents.html` lagging behind the main token system.
