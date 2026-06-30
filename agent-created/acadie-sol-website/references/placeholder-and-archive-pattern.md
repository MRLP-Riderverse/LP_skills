# Placeholder + Archive Pattern — June 2026

How Acadie.sol handles events that exist in the data but should not feel like a real public listing to visitors.

## Why

Visitors shouldn't read a listing and think "I missed something." Anything that's a system/seed/fixture/test event renders as a *preview* through the same renderer chain public visitors see; admin pulls the data live from source truth on GitHub.

## Two-axis Way to Classify Events

| Axis | Public listing | Preview only |
|---|---|---|
| Timeline | Real / scheduled | Real, but represents a placeholder event |
| Presence in feed | Renders full summary | Renders the localized preview copy |
| `status` field | `published` | `published` *or* `archived` (cosmetic — keeps data integrity) |
| Visible to admins | Yes (source of truth on GitHub) | Yes (same — nothing is actually deleted) |
| Excluded from home/directory aggregations | Only via status/active filter | Only via status/active filter |

## Renderer Side (`events.html`)

- `publicTitle(event)` → strips "Placeholder" and re-renders as "Preview" so the title itself flags the listing.
- `publicSummary(event)` → if `summary` matches `/placeholder|non-public/i`, returns the localized preview copy (`previewSummary` in `EVENTS_COPY.en` / `.fr`) instead of the raw text.

So all you have to do on the data side to flag an event as preview-only is include `placeholder` (or `non-public`) anywhere in its `summary` text. The renderer does the rest. Verified on the socialite reading event.

## "Delete" Pattern (no actual delete)

Since the project commits the source-of-truth JSON to GitHub, we never delete to remove from the public surface. To hide:

1. Set `status: "archived"` and `computed_status: "archived"` on the event in `assets/events-data.json`.
2. Update the top-line counts (`event_count`, `active_count`, `archived_count`).
3. The events page already filters by `eventMatches(event)` — it hides archived when `filter === 'upcoming'`. Archive filter exposes them in `Archive`.

Used for: `louga-event-placeholder`, `big-d-community-placeholder`. Both replaced with archived status; full record kept on GitHub.

## Future: Archive JSON System

User noted (June 2026): "later on when scale.. we'll have to think of a way to query the archive for preservation reasons.."

Until that exists, the working answer is: GitHub history is the archive. Anyone with admin can `git log -p assets/events-data.json` to recover any state. When archive search becomes needed, the natural seam is *its own* generated asset (e.g. `assets/events-archive.json`) built by the export script, plus a minimal `/admin/archive.html` page that lists archived entries with bidirectional links to source commits. Don't pull this off tonight's scope — the placeholder pattern above is sufficient for current scale.

## Verification

```bash
node -e 'const d=JSON.parse(require("fs").readFileSync("assets/events-data.json","utf8")); console.log("OK", d.event_count, "active", d.active_count, "archived", d.archived_count); d.items.forEach(i=>console.log(" ", i.id, "->", i.status))'
```

Inspect:
- Counts match: `active_count + archived_count === event_count`
- `status` strings are exactly `"published"` or `"archived"` (no drift)
- Archived items still have valid `id` + readable `summary` (preview copy) so admin lookup stays useful
