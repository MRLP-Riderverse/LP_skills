# Homepage media card and GIF verification

Use this when adding a test image/GIF to the Acadie.sol homepage discovery deck.

## Asset inspection

```bash
file assets/images/example.gif
du -h assets/images/example.gif
python3 - <<'PY'
from PIL import Image
p = 'assets/images/example.gif'
im = Image.open(p)
print(im.size, getattr(im, 'n_frames', 1), im.info.get('duration'), im.info.get('loop'))
PY
```

Prefer an existing asset when it is visually suitable and reasonably small. Do not compress a small, legible glitch/text GIF automatically; preserve the animation for the design test unless weight is a real delivery problem.

## Ignored-media trap

A local asset can exist while `.gitignore` prevents deployment:

```bash
git check-ignore -v assets/images/example.gif || true
git ls-files assets/images/example.gif
```

If the user explicitly requests that asset on the public site, force-stage only that named file with `git add -f`; do not broad-stage unrelated ignored media.

## Deck integration contract

For a new Card 4 or later section, update all of these together:

- top-level `.home-top > .surface` section with a stable `id`
- mobile dot with matching `aria-controls` and `data-section`
- localized dot-label assignment in `renderStaticCopy()`
- desktop grid sizing/media constraints

Keep media bounded (`width`, `aspect-ratio`, and a sensible max size) so intrinsic image dimensions do not create an accidental giant desktop row.

## Deployment proof

After Pages succeeds, check the binary separately from the HTML:

```text
https://acadie.sol.site/assets/images/example.gif?v=<short-sha>
```

Require HTTP 200 and the expected MIME type. In a browser, verify `img.complete`, `naturalWidth`, and `naturalHeight`; HTML containing the `<img>` tag is not proof that the binary was deployed. Use the cache-busting query when an HTML deployment is newer than a cached asset response.
