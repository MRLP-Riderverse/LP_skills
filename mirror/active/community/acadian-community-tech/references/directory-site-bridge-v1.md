# Directory site bridge V1

This note captures the connected mockup pattern used for the Acadie.sol site + directory.

## Goal
Let the public site show the directory while the inbox is still being updated.

## V1 pattern
- The site repo renders a dedicated `directory.html` page.
- The page loads generated JSON, not the raw markdown inbox directly.
- The JSON is generated from `acadie_sol_directory/inbox/*.md`.
- Any draft card with a `# Draft:` title gets a visible `DRAFT` badge in the UI.
- The top-level site nav should point to `directory.html`, not an in-page anchor, when the goal is a distinct browsable directory view.

## Data shape
Minimal fields are enough for V1:
- title
- draft boolean / badge
- category if present
- area if present
- short summary from notes
- source URLs

## Practical lessons
- Keep the page ugly-but-clear before chasing polish.
- Use the inbox as the source of truth for now.
- Put the generation step in a rerunnable script under `scripts/` so the preview can be refreshed consistently.
- Draft badges make the preview honest and usable at the same time.

## Implementation notes
- The generator script can live at `scripts/build-directory-data.py`.
- The rendered JSON can live at `assets/directory-data.json`.
- The public page can be a simple static HTML file until the data flow is proven.
