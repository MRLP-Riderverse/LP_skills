# Community Mobile UX Pass — Static Directory/Event Sites

Use this reference when a public community site is technically correct but feels like an admin/export interface on mobile.

## First-impression test

1. Open the home, directory, and events pages at phone width before clicking anything.
2. Capture the visible text above the fold and ask: would a local visitor understand what to do without knowing the repo/data model?
3. Flag any public copy that reveals implementation state instead of visitor value.

## Copy cleanup targets

Replace internal labels with visitor-facing intent:

- `published / active` → usually hide; show date/status only if meaningful to visitors.
- `placeholder` → hide or soften to `Preview` only during testing.
- `static event layer fed by the directory repo` → `Shows, meals, gatherings, pop-ups, and community dates`.
- `Directory browse` / `Official entries` → `Places` / `Local places`.
- `Filter` → `More options` when filters are secondary.
- `Event feed` → `Related events`.
- `Related places` must be visually subordinate to the event/card it supports.

## Navigation simplification

If discover/search/explore are not genuinely different workflows, collapse them into one path:

- primary CTA: `Find local places`
- secondary CTA: `What’s happening`
- search field visible early
- optional lenses/categories behind a secondary control
- browse cards below the same experience

Avoid forcing a mode choice before the user sees content.

## Card hierarchy

Primary cards should not share the same treatment as contextual/supporting cards.

- Main event card: date badge, title, time, host, venue/location, short vibe, actions.
- Linked/related place inside event: smaller block, top divider, clear label (`Linked places`).
- Global related/location section: separate divider, different border/background, explanatory note if needed.

## Cultural/local belonging pass

Lead with local purpose and warmth before tooling:

- name/identity
- local region reference
- plain-language promise
- one primary action
- one secondary action
- small live preview

This is a visual-communication problem as much as an implementation problem: public users should feel place and belonging before they see controls.