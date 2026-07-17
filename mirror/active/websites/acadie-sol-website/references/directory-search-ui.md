# Acadie.sol directory search UI notes

Session-derived conventions for the directory surface:
- Use one primary search field with live search on input and Enter.
- Prefer a small inline clear `×` inside the input over a separate Clear button.
- Rename “Options” to “Filters” for the filter affordance and popover title.
- Keep action buttons compact and pill-shaped; avoid stacked/tall button blocks.
- Remove public-facing footer copy like “small public mirror” when it reads as infrastructure text.
- When catalog entries appear missing, verify the source repo/data first; if the data exists and the page is stale, treat it as deployment/cache lag before rewriting content.

Verification pattern used successfully:
- Run a JS syntax check on the extracted inline script.
- Use headless Chrome `--dump-dom` to confirm the rendered DOM contains the new controls/text and excludes removed copy.
- Capture a screenshot only if visual layout still needs judgment.
