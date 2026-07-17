# Search mobile keyboard lane + GitHub Pages PWA path

## Search bar jitter during iPhone editing

Use this when `search.html` has a bottom-fixed search bar and the user reports behavior like:
- the bar drops under or toward the keyboard while typing
- backspacing from many results to one result makes the bar jump
- empty/sparse result states seem to drag the bar around
- Safari works, but focused editing on iPhone feels unstable

### Root cause pattern
Do **not** compare `visualViewport.height` against the live current `window.innerHeight` to decide keyboard-open state.

On iPhone/Safari, `innerHeight` can wobble during editing/backspacing and address-bar transitions. That lets `keyboard-open` flip on/off mid-edit, which can yank the search bar between its resting dock lane and its keyboard lane.

### Durable fix pattern
1. Keep a stable layout-height baseline (`layoutViewportHeight`) captured when the keyboard is not open.
2. On `visualViewport.resize`, compute:
   - `keyboardInset = layoutViewportHeight - (visualViewport.height + visualViewport.offsetTop)`
3. Treat keyboard-open as true only when:
   - the search input is focused, and
   - the inset exceeds a real threshold (about `> 120px` worked here).
4. Feed that inset into CSS via a custom property such as `--keyboard-inset`.
5. In the focused + keyboard-open state, position the fixed search bar with:
   - `bottom: calc(var(--keyboard-inset) + gap + env(safe-area-inset-bottom))`
6. Do **not** synthesize keyboard-open on `focus`; let `visualViewport.resize` establish it.
7. When keyboard closes, reset the inset to `0` and refresh the stored layout baseline.

### Layout guardrails
- Reserve bottom space in active results (`padding-bottom`) so shrinking result sets do not visually fight the fixed search bar.
- Keep scroll-hide disabled while the input is focused.
- If swipe-down-to-dismiss is supported, ensure the touch delta matches a real downward drag (`currentTouchY - touchStartY > threshold`), not the opposite direction.

## GitHub Pages installed-app 404

Symptom:
- Safari browsing works
- installed homescreen/PWA app opens to GitHub 404

### Root cause pattern
For a GitHub Pages **project site**, manifest `start_url` must not be root-absolute like `/index.html`.

That can launch the installed app at the domain root instead of the repo subpath.

### Durable fix pattern
Use relative manifest paths such as:
- `"start_url": "./index.html"`
- `"scope": "./"`

Then reinstall the homescreen app because iOS caches manifest metadata aggressively.
