# Search filter overlay regression note

## Symptom
The filter popover appeared as a weird block under the search bar and did not overlay the results cleanly.

## Root cause
The filter UI was nested inside the search panel that still had clipping/stacking behavior. The overlay inherited the panel's layout instead of behaving like a full-screen modal.

## Fix pattern
- Keep the search field inside the control panel.
- Move the filter overlay out as a sibling of the control panel, not a child.
- Make the overlay `position: fixed` with a full-screen backdrop.
- Put the actual dialog in a centered sheet above the backdrop.
- Use one launcher button as a true toggle:
  - click once opens
  - click again closes
  - `Escape` closes
  - backdrop click closes

## Verification
- Confirm the overlay's bounding box spans the viewport when open.
- Confirm the dialog sheet sits above search/results, not inside the search stack.
- Confirm a second click on the launcher closes the overlay.
