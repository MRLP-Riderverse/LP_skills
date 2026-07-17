# Mobile homepage discovery deck

## Intent
Acadie.sol Home should feel like discovering a small set of intentional surfaces, not consuming another top-to-bottom feed. On phones, native horizontal swiping can replace stacked feed behavior when each section is allowed to read as a full-page asset.

This remains a reversible, test-by-feel product experiment. The implementation should stay simple enough to flatten or revert after live review.

## Current composition contract
Home has three top-level semantic sections:

1. Welcome / identity and public pulse
2. Current notice / LIVE fallback
3. Recently added album

The current notice and recently added album are **separate sections**, not slides inside a nested carousel. This matters on desktop too: welcome occupies the left column while current and recent stack independently in the right column.

Do not restore autoplay merely because a prior version used it. The outer discovery deck is the interaction model now.

## Borderless surface language
When full-page mobile sections look like obvious cards pasted over a background, flatten them before adding more decoration:

- no panel border;
- no panel background fill;
- no panel shadow;
- no rounded outer card shell;
- use spacing, typography, the album image, and one restrained CTA to establish hierarchy;
- source foreground and action colors from shared light/dark tokens (`--ink-strong`, `--muted`, `--gold`, `--button-*`) rather than fixed navy/white card colors.

The page background is the shared visual field. An image can retain a moderate radius because it is content, not another container.

## Mobile responsive contract
Below `900px`:

- contain Home to the viewport and reserve clearance for the dock;
- make `.home-top` a horizontal flex scroller with `overflow-x:auto` and `scroll-snap-type:x mandatory`;
- use three direct child panels at `100vw` each with zero inter-panel gap so each reads as a full page;
- apply `scroll-snap-align:center` and `scroll-snap-stop:always`;
- preserve native touch behavior; do **not** force `touch-action:pan-x`, because short panels may need internal vertical scrolling;
- keep the footer above the dock instead of making utility links into panels;
- retain the localized cue `Swipe to discover →` / `Glissez pour découvrir →`.

### Short and landscape viewports
Document-level scrolling remains disabled, so each panel must fail open when content exceeds its available height:

- `overflow-y:auto` on welcome/current/recent panels;
- `overscroll-behavior-y:contain` to keep local scrolling controlled;
- never combine a clipped parent, absolutely positioned content, and disabled document scroll unless a browser test proves every CTA is reachable.

Verify reachability by scrolling each overflowing panel to its maximum and checking that its last meaningful action sits inside the panel viewport.

## Position dots
Add one bottom indicator per top-level section.

- The active indicator updates from the deck's real scroll position, not only from dot clicks.
- Dots are also buttons that scroll to their corresponding section.
- Use localized `aria-label` values and exactly one `aria-current="true"`.
- Keep the visible marks small, but give each button a larger stable hit target (for example a `40×28px` button with the visual dot rendered by `::before`).
- Do not change button width to indicate selection; expand only the pseudo-element so the control row does not shift.
- Honor reduced motion when dot-triggered scrolling requests smooth behavior.

## Desktop contract
At `>=900px`:

- use a two-column grid;
- let welcome span both rows in the left column;
- place current notice and recently added as separate stacked sections in the right column;
- hide mobile position dots;
- keep all three sections simultaneously visible and semantic;
- do not reintroduce an inner carousel just to reuse the mobile content model.

## Light/dark contract
The flat surfaces should remain transparent in both modes (`border:0`, transparent background, `box-shadow:none`). Theme differences come from the shared page field and tokenized text/action colors, not alternate card fills.

Audit computed styles for all three sections in both themes. Fixed white/navy copy from a prior always-dark carousel is a stale-style signal.

## Secondary mobile header
A phrase such as `Vive l’Acadie!` can stay if the header belongs to the page surface language. Prefer a translucent `var(--paper)` surface with `var(--ink-strong)` foreground, shared line treatment, and restrained blur. Do not pair `var(--gold)` with a semi-transparent medium-blue light-mode surface without measuring contrast.

## Browser verification matrix
At minimum test:

- `320×568` compact portrait;
- `375×667` portrait;
- `390×844` common mobile;
- `667×375` and `844×390` landscape;
- `820×900` tablet;
- `900×800` breakpoint boundary;
- `1280×900` desktop.

Assert:

- exactly three direct deck sections, all rendered and not hidden;
- mobile panel width equals viewport width and deck scroll width is three viewports;
- natural horizontal scrolling updates the active dot;
- tapping every dot lands on the expected scroll offset;
- no old carousel controls, timers, slide selectors, or autoplay code remain;
- flat border/background/shadow computed styles in light and dark mode;
- localized swipe cue, deck label, and all dot labels;
- no document overflow or console exceptions;
- internal vertical scrolling makes final CTAs reachable on short landscape phones;
- desktop is a grid with welcome left and current/recent stacked right.
