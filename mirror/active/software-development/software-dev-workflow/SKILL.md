---
name: software-dev-workflow
description: "Software development workflow — plan, spike, TDD, code review, and subagent execution. From idea to verified commit."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [planning, TDD, code-review, spiking, workflow, implementation, delegation]
    related_skills: [debugging, test-driven-development, hermes-agent]
---

# Software Development Workflow — Plan → Spike → Test → Review → Execute

Class-level skill covering the full development workflow from planning through execution. Each subsection is a phase that can be used independently or as part of the complete pipeline.

---

## Phase 1: Planning

### Writing Implementation Plans

Output: actionable markdown plan saved to `.hermes/plans/YYYY-MM-DD_HHMMSS-<slug>.md`

**Plan structure:**
```markdown
# Goal
<what we're building and why>

# Context
<relevant background, constraints, dependencies>

# Approach
<high-level strategy>

## Steps
1. [bite-sized task, 2-5 min, with exact file paths and complete code]
2. [next task]

# Files
- `path/to/file.py` — <what it does>

# Tests
- `tests/test_thing.py` — <what it verifies>

# Risks
- <what could go wrong and mitigation>
```

### Planning Craft

- **Bite-sized tasks** — each step should take 2-5 minutes
- **Exact file paths** — no ambiguity about where code goes
- **Complete, copy-pasteable code** — no `...` or `// implement this`
- **TDD cycle per task** — write test first, then implement
- **DRY/YAGNI/TDD** — don't repeat, don't over-engineer, test first
- **No execution** — plans are plan-only; execution happens in Phase 5

### Common Planning Mistakes

- Vague task descriptions ("improve the API")
- Missing file paths
- Tasks that are actually multiple tasks
- No test strategy
- No risk assessment

---

## Phase 2: Spiking

### What is a Spike?

A throwaway experiment to validate feasibility before committing to build.

### Spike Workflow

1. **Decompose** the question into testable hypotheses
2. **Research** — check docs, existing code, similar projects
3. **Build** — minimal code to test the hypothesis
4. **Verdict** — document: works / doesn't work / needs more investigation

### Comparison Spikes

When evaluating two approaches, create parallel spikes:
```
002a-spike-redis-caching/
002b-spike-memcached-caching/
```

### Spike Rules

- **Throwaway** — spike code is NOT production code
- **Time-boxed** — set a limit (30 min, 1 hour)
- **Document verdict** — always record what you learned
- **Adapted from GSD** — spikes validate, they don't deliver

---

## Phase 3: Debugging and Root Cause Investigation

### Debugging Workflow

When something fails, do not start by changing code at random. Use a root-cause loop:

1. Reproduce the issue reliably.
2. Narrow the scope to the smallest failing path.
3. Collect evidence: logs, stack traces, screenshots, snapshots, or state dumps.
4. Form one hypothesis at a time and test it with the smallest probe.
5. Fix the smallest cause, then add a regression test or verification step.

### Debugging Rules

- No symptom-only fixes.
- No shotgun changes.
- If three fixes fail, question the architecture or assumptions.
- Preserve useful evidence before changing the state.
- Prefer targeted probes over broad rewrites.

### Debugging Tools

- Python: `pdb`, `debugpy`, `breakpoint()`.
- Node.js: `node inspect`, inspector ports, CDP.
- Browser/UI issues: inspect the DOM, accessibility tree, and console errors before guessing.

### Debugging Anti-Patterns

- Changing several things at once.
- Trusting the first error message without checking the cause.
- Fixing the visible symptom but not the failing invariant.
- Ignoring the exact reproduction path.

## Phase 4: Test-Driven Development

### Iron Law: No Production Code Without a Failing Test First

### RED-GREEN-REFACTOR Cycle

1. **RED** — Write a failing test that describes the desired behavior
2. **GREEN** — Write the minimum production code to make the test pass
3. **REFACTOR** — Clean up while keeping all tests green

### Rationalizations to Reject

- "I'll add tests later" → No, write them now
- "This is too simple to test" → If it's simple, the test is simple too
- "I need to see it work first" → That's what the test is for
- "Testing frameworks are slow" → Fix the framework, not the process

### Anti-Patterns

- Writing tests after implementation (not TDD)
- Testing implementation details instead of behavior
- Mock-heavy tests that verify mocks, not code
- Skipping the refactor step
- Shared-shell drift: one page uses a different dock class, one template keeps an old icon after the new one lands, one page loses the background language, or a separate overlay/filter layer still exposes its own close icon after the drawer/menu was simplified.
- Shared-shell contract bugs: if the user says a dock "should always be the same," treat the dock as site-wide chrome and verify every page against the same contract. Don’t leave one page with a page-local active state, hidden icon sizing, or a different menu path.
- Icon-as-navigation bugs: if a centered icon in the menu is supposed to open a specific page, make it a real link/button to that target and verify the click target on every page. Don’t assume the visual glyph alone is enough.
- Mobile input zoom traps: if a search/text field auto-zooms on focus, check whether the font size is below the mobile browser threshold and verify the field at real device width before shipping.

### Verification Checklist

- [ ] Every function/method has at least one test
- [ ] Tests describe behavior, not implementation
- [ ] All tests pass before committing
- [ ] No commented-out or skipped tests
- [ ] Test coverage meets project threshold

### Static Site / Data-Driven UI Pattern

When a website page renders from generated JSON rather than direct content files, treat UI changes and exporter changes as one unit of work.

**Use this pattern when:**
- adding "recently added" / "latest items" / chronological views
- adding cross-links from dashboard widgets into rendered cards
- the page needs ordering that the current payload does not encode explicitly
- the content model has both a human-authored file and a structured metadata file (for example `entry.md` + `meta.json`)

**Contract reminder:**
- `entry.md` is often live input to the exporter, not just dev-facing prose.
- `short_description` should stay a plain string when the quick card needs reliability.
- Multilingual/public-facing prose belongs in a localized field like `summary`.
- Slugs and foreign keys are different: the folder slug identifies the entry, while `location_id` should only change with its dependent location/event refs.

**Use this pattern when:**
- adding "recently added" / "latest items" / chronological views
- adding cross-links from dashboard widgets into rendered cards
- the page needs ordering that the current payload does not encode explicitly

**Implementation rule:**
1. Inspect the renderer first to see what fields the page already consumes.
2. If the UI depends on recency or sort order, add an explicit sortable field to the exported payload (`*_ts`, ISO timestamp, sequence number) instead of relying on filename order or current array order.
3. Re-export the JSON immediately after changing the exporter.
4. Verify both layers:
   - exporter: compile/syntax check if applicable and confirm the new fields exist in generated JSON
   - renderer: confirm the new UI markup and logic exist, and that links/anchors resolve to the intended card or section
5. For public-facing static mirrors, run a copy/UX pass that strips internal data-model language from the rendered UI. Do not expose implementation labels like `source repo`, `generated from`, `published`, `active`, `placeholder`, or `event feed` unless they are explicitly visitor-facing.
6. For website repos that consume generated JSON from a source repo, treat source edits, export regeneration, and rendered-page verification as one unit of work. If the user reports missing content, check the source record first, re-export the payloads, then confirm the public assets and rendered page both contain the item.
7. When events or tabs disagree, check whether the split is an intentional computed-status filter (`all` vs `upcoming`/`active`) before chasing routing bugs.
8. For page transitions that briefly reveal shell ghosts, add a route-pending cloak (`html.route-pending`) or equivalent loading gate and remove it in both success and failure paths after data resolves.
9. For mobile public pages, verify the first screen before clicks. Overlapping intents such as discover/search/explore should usually collapse into one clear search/browse path with optional lenses.
10. When working from user-provided visual mockups, treat the image as design direction, not a literal screenshot to over-query. Use vision once when the user sends/references the photo; if vision is rate-limited, inspect local image dimensions/crops or make a contact sheet and proceed from visible/user-stated direction instead of repeatedly retrying.
11. For "recent items" affordances, prefer a compact collapsible panel near the top of the page instead of permanently expanding more chrome into the main result list.
12. When recent items should jump to full cards lower on the page, give each rendered card a stable `id` and open/scroll to it from hash links.
13. For user-reviewed visual/product work, treat “make it look like the mockup” as interaction/surface design, not just color theming. Rework information hierarchy, navigation surfaces, app shell/drawer/dock states, card anatomy, empty media placeholders, and first-screen flow before tweaking palette.
14. When the user wants Telegram screenshot review, generate and send screenshots directly without vision-analyzing them first unless they explicitly ask for analysis. Use vision only when the user sends/references a photo or when visual inspection is necessary to act.
15. For Acadie.sol-style mobile public pages, prefer an OS/product surface model over a generic website model: home as launch surface, search as app state, drawer as navigation state, events/directory as compact surfaces inside one system.
16. For shared shells, treat the bottom dock as a permanent cross-page component. Verify and edit it as one site-wide contract, not as page-by-page local chrome.
17. For stripped memorial/obituary pages, preserve enough of the shared branded surface (background, gradient, type rhythm, framing) that the page still reads as part of the same unit.

Reference: see `references/acadie-mobile-os-ui.md` for the session-derived Acadie.sol mobile OS surface pattern.
Reference: see `references/shared-surface-regression-checks.md` for shared dock/nav regression checks and focus-state pitfalls.
Reference: see `references/shared-shell-menu-regression-checks.md` for centered drawer labels, separate Support/About destinations, and subtitle cleanup notes.
Reference: see `references/permanent-shared-dock-and-memorial-page.md` for the permanent dock and memorial-page branding notes.
Reference: see `references/menu-drawer-overlay-regressions.md` for stale drawer-item, duplicate-close, and shared-dock regression checks.
Reference: see `references/static-site-audit-checklist.md` for a reusable checklist covering URL validation, hash hardening, class/selector drift, and dark-mode coherence on public static sites.
Reference: see `references/acadie-directory-export-routing.md` for source→export→render verification, route-pending cloaking, and search/tab split pitfalls.
Reference: see `references/acadie-search-filter-overlay.md` for right-aligned shortcut pills and modal filter-sheet behavior on the Acadie.sol search surface.
Reference: see `references/acadie-mobile-search-surface-followups.md` for Enter-to-blur search, right-aligned full-page links, and hidden-drawer hitbox fixes.

**Pitfall:**
- Do not fake recency from display order. If recency matters, encode it in the payload and sort against that field in the client.
- Do not “light-mode” a dashboard and call it a redesign. If the critique is dashboard vibes, remove dashboard structures: stats chrome, admin labels, oversized hero cards, separate overlapping modes, and website nav clutter.
- Do not assume a shared dock is fine because one page looks right. Search every related template for class drift, duplicate selectors, and page-specific hide rules before calling it consistent.
- Do not leave a second close affordance hiding in a secondary overlay (for example a filter popover, modal, or side panel) after simplifying the main drawer/menu. Count the visible close controls across the whole shell.
- Do not patch a shared shell from stale paginated reads when another pass may be editing the same files. Re-read the live blocks first, then patch the shared component once and verify the change across every page.
- Do not let click focus masquerade as toggle selection. Keep `:focus-visible` separate from the selected-state visuals; use icon/color contrast for the selected mode itself.
- On public mobile search surfaces, keep shortcut pills compact and right-biased for one-handed use, and treat filter launchers as modal sheets with a backdrop blur/backwall rather than floating inline panels.
- If a search page keeps the keyboard up after Enter, blur the input after rendering so the user can see the result set immediately.
- If a "view full page" affordance feels visually lost, move it to the right edge of the card and make it a right-aligned block rather than a left-floating chip.

Reference: see `references/acadie-mobile-os-ui.md` for the session-derived Acadie.sol mobile OS surface pattern.
Reference: see `references/shared-surface-regression-checks.md` for shared dock/nav regression checks and focus-state pitfalls.
Reference: see `references/shared-shell-menu-regression-checks.md` for centered drawer labels, separate Support/About destinations, and subtitle cleanup notes.
Reference: see `references/permanent-shared-dock-and-memorial-page.md` for the permanent dock and memorial-page branding notes.
Reference: see `references/menu-drawer-overlay-regressions.md` for stale drawer-item, duplicate-close, and shared-dock regression checks.
Reference: see `references/static-site-audit-checklist.md` for a reusable checklist covering URL validation, hash hardening, class/selector drift, and dark-mode coherence on public static sites.

**Pitfall:**
- Do not fake recency from display order. If recency matters, encode it in the payload and sort against that field in the client.
- Do not “light-mode” a dashboard and call it a redesign. If the critique is dashboard vibes, remove dashboard structures: stats chrome, admin labels, oversized hero cards, separate overlapping modes, and website nav clutter.
- Do not assume a shared dock is fine because one page looks right. Search every related template for class drift, duplicate selectors, and page-specific hide rules before calling it consistent.
- Do not leave a second close affordance hiding in a secondary overlay (for example a filter popover, modal, or side panel) after simplifying the main drawer/menu. Count the visible close controls across the whole shell.
- Do not patch a shared shell from stale paginated reads when another pass may be editing the same files. Re-read the live blocks first, then patch the shared component once and verify the change across every page.
- Do not let click focus masquerade as toggle selection. Keep `:focus-visible` separate from the selected-state visuals; use icon/color contrast for the selected mode itself.
- On public mobile search surfaces, keep shortcut pills compact and right-biased for one-handed use, and treat filter launchers as modal sheets with a backdrop blur/backwall rather than floating inline panels.
- If a search page keeps the keyboard up after Enter, blur the input after rendering so the user can see the result set immediately.
- If a "view full page" affordance feels visually lost, move it to the right edge of the card and make it a right-aligned block rather than a left-floating chip.

---

## Phase 4: Pre-Commit Code Review

### 8-Step Pipeline

1. **Get the diff** — `git diff` or `gh pr diff`
2. **Static security scan** — check for secrets, injection, eval, pickle, SQLi
3. **Baseline tests & linting** — ensure existing tests still pass
4. **Self-review checklist** — review your own changes first
5. **Independent reviewer** — use `delegate_task` for a second opinion. Treat the result as a commit barrier: background delegation is asynchronous, so do not commit or push while that reviewer is still running.
6. **Evaluate results** — wait for and weigh findings from both reviews before staging the final commit. If the runtime cannot synchronously wait for the delegated result, perform a complete local review and explicitly treat the background review as post-commit follow-up rather than claiming the commit was independently reviewed.
7. **Auto-fix loop** — max 2 cycles with a third agent if needed
8. **Commit with [verified] prefix** — indicate the review was done

### Static Public-Site Audit Pass

For public static sites, add a focused audit pass before commit that checks three things in parallel:

1. **Input/rendering safety**
   - Validate any data-driven `href`/`src`/URL fields before rendering.
   - Treat `location.hash`, query params, and generated JSON as untrusted input.
   - Guard `decodeURIComponent()` and selector-based hash handling against malformed fragments.

2. **Shell/renderer drift**
   - Look for duplicated theme/lang logic across pages when a shared shell already owns it.
   - Flag class mismatches where the CSS targets one class and the renderer emits another.
   - Flag stacked page-level overrides that repeatedly redefine the same selectors.

3. **Dark-mode coherence**
   - Check whether text accents still use a dark anchor token on dark/glass surfaces.
   - Check hard-coded borders/fills that disappear against the current palette.
   - Check browser chrome color (`theme-color`) against the actual dark-mode surface.

Use a delegated reviewer for the audit when the site is large enough that a single pass risks missing selector drift or color regressions.

### Fail-Closed Rules

- Any critical security finding → must fix before commit
- Any test regression → must fix before commit
- Lint errors → auto-fix if safe, otherwise block

### Common Patterns to Flag

| Pattern | Language | Risk |
|---------|----------|------|
| `eval()`, `exec()` | Python | Code injection |
| String formatting in SQL | Python | SQL injection |
| `subprocess` with shell=True | Python | Shell injection |
| `innerHTML` | JavaScript | XSS |
| `pickle.loads()` | Python | Arbitrary code execution |
| Hardcoded secrets | Any | Credential leak |

---

### Step 5: Subagent-Driven Execution

### 2-Stage Review Pattern

1. **Worker stage** — `delegate_task` spawns a subagent to implement
2. **Reviewer stage** — another subagent reviews the worker's output
3. **Integration** — main agent incorporates reviewed changes

### Parallel Cleanup / Simplify Pass

When the user asks to "simplify", "clean up my changes", or review recent changes for reuse, quality, and efficiency, use the parallel cleanup pattern rather than a single broad review:
- capture the relevant diff first
- split review into a few focused reviewers in parallel
- merge findings, drop weak nits, then apply only the survivors
- verify the touched tests or linters afterward

This is the umbrella version of the standalone simplify-code workflow.

### Execution Handoff

After planning (Phase 1), hand off to subagents for implementation:

```python
# Delegate the implementation
delegate_task(
    goal="Implement the authentication module per the plan in .hermes/plans/...",
    toolsets=["terminal", "file"]
)
```

### Key Principles

- Plans are plan-only; execution happens via subagents
- Review every subagent output before accepting
- Keep the main agent as the coordinator, not the implementer
- Use `delegate_task` for isolation; don't pollute the main context

---

## Complete Pipeline

```
Idea → Plan (Phase 1) → Spike if needed (Phase 2) → TDD (Phase 3) → Review (Phase 4) → Execute (Phase 5)
```

Not every task needs all phases. Use judgment:
- Simple bug fix: skip planning, TDD + review
- New feature: plan → TDD → review → execute
- Unknown approach: plan → spike → TDD → review → execute
