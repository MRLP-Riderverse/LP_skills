# Homepage attention hierarchy and mobile decluttering

## Current Home architecture

Use one intentional sequence instead of a launcher dashboard:

1. quiet identity
2. one owner-controlled LIVE signal
3. one featured photo/album
4. one community door
5. one quiet updates/archive exit

The mobile dock already owns primary route navigation. Home should communicate identity and current attention, not repeat Directory, Events, Search, and Menu as content cards.

## Correction captured

A desktop composition can feel appropriately infrastructural while the same card stack feels cluttered on mobile. Do not solve this by redesigning desktop or merely shrinking every card.

For a restrained mobile-only pass:

- remove duplicate top chrome on Home when identity and the bottom dock already frame the page;
- flatten the welcome surface into a short identity line rather than another bordered card;
- keep LIVE as the only visually dominant attention card;
- shorten the photo surface and hide nonessential teaser copy;
- hide duplicate actions already present in the dock (for example Events);
- reduce secondary community/archive surfaces to one action or a plain text row;
- lower padding, shadow depth, and radius together so the page feels calmer rather than miniaturized.

Preserve desktop intentionally with `<900px` mobile overrides and verify computed visibility on both sides of the breakpoint.

## Verification pattern

Before changing CSS, add computed-style assertions for the elements that should disappear on mobile and remain visible on desktop. Run once red, apply the mobile override, then run green.

Minimum viewport sweep:

- 320px phone
- 390–430px phone
- 820px tablet/touch shell
- 900px desktop-shell boundary
- 1280px desktop

Check:

- no horizontal overflow;
- dock visible and desktop nav hidden below 900px;
- dock hidden and desktop nav visible at/above 900px;
- intentional mobile-only elements compute to `display: none`;
- desktop content remains visible;
- no browser console errors or uncaught exceptions.

## Shipping verification

When the user explicitly supplies a commit message, use it exactly even if it is not conventional-commit format. Selectively stage intended files so unrelated local media is not swept into the commit.

After push:

1. compare local `HEAD` to `git ls-remote origin refs/heads/main`;
2. verify the latest GitHub Pages build references that commit and reaches `built`;
3. fetch `https://acadie.sol.site/?v=<short-sha>` and verify a unique marker from the change, not merely HTTP 200;
4. only then tell the user the mobile build is ready for self-testing.

## Delayed-review corrections

A fixed dock and page-local tablet layout rules can disagree even when phone and desktop screenshots look correct. In this shell, the dock remains active below `900px`, while editorial/gallery layouts start their tablet rules at `760px`. Do not let those tablet rules reduce bottom padding to desktop values between `760–899px`.

Regression assertion:

```text
computed page padding-bottom >= computed dock height + 16px
```

Run it against editorial, gallery-index, and album shells at an intermediate width such as `820px`, not only at 390 and 900.

Label-based menu launchers need an explicit keyboard contract because the checkbox itself is visually hidden:

- `role="button"` and `tabindex="0"`;
- `aria-controls` pointing to the drawer;
- synchronized `aria-expanded` on every launcher;
- Enter/Space toggles the checkbox and dispatches its change event;
- Escape closes and restores focus to the launcher that opened the drawer.

Finally, when specific local media is intentionally excluded from publication, selective staging is necessary for the current release but not sufficient as a durable guard. Add explicit `.gitignore` paths and verify them with `git check-ignore -v`.
