# Acadie.sol search/filter overlay pattern

Source: session where the directory search UI was refined for the Acadie.sol public page.

## User-facing preferences captured
- Top shortcut pills (`View all`, `Filters`) should be visually grouped near the right edge, not spread left.
- The pills should be compact and clearly secondary to the main search input.
- The `Filters` UI should behave like a real modal sheet, not a floating block of text.
- Modal behavior should include a backwall / backdrop blur that dims the rest of the page while the sheet is open.
- The filter sheet should own the content, with the backdrop closing it when clicked.
- Button order should match the mental model: `Reset` left, `Done` right.

## Implementation notes
- Use a fixed overlay container for the popover and a nested sheet/dialog for the actual controls.
- Keep the search input and its clear `×` inside the input field as the primary control.
- Prefer compact pill dimensions for the secondary actions so they read as shortcuts, not primary buttons.
- When the page is a mobile/public surface, optimize for one-handed right-thumb use: align the shortcut cluster toward the right.
