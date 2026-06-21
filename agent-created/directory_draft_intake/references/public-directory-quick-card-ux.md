# Public Directory Main-Page UX Lessons

Use these lessons when changing the Acadie.sol directory quick-search page or the exporter payload that feeds it.

## Main directory principle

The main directory is for quick public scanning:

- findable
- skimmable
- low cognitive load
- standardized across entries

Full contact/place pages are for richer material:

- photos
- accreditations
- related place clusters
- public source trails
- reviews/context
- unique local story

Do not flood the quick-search card with future full-page material.

## Published vs draft display

Separate published/proper entries from draft previews in the UI.

- Proper entries should display first.
- Draft previews should live in their own section/container.
- This improves scroll comprehension and makes data maturity visible to public users.

## Collapsed card

Collapsed cards should show only quick-scan metadata:

- title
- preview/draft badge when applicable
- category
- a small number of useful tags

Avoid showing the public-area/city pill in the collapsed card if the expanded contact block already carries the official address. This reduces visual noise and duplication.

## Expanded quick card

Expanded cards should show:

- one strong public-facing line
- short bullets for focus points when the source notes are bullet-like
- structured contact/action fields such as address, hours, phone, email, website

Avoid:

- rendering a second “more tags” row after expansion
- duplicating related places if the same location context is already in notes/contact
- rendering relation clusters by default on the quick card
- adding photos/accreditations to the main browse page

## Exporter payload support

When official-entry public notes are written as markdown bullets, have the exporter emit a `note_points` array while preserving `notes` for compatibility. The renderer can then use semantic bullet lists instead of flattening everything into one paragraph.

## Big D calibration example

For Big D Drive-In, the better card-level split was:

- Description: `Home of the Big D Burger.`
- Notes bullets:
  - Traditional drive-in with car-park-and-dine service.
  - Takeout is available.
  - Nearby picnic tables make it easy to stay and eat outside.
  - Long-running Bathurst stop with a 1950s and 1960s diner feel.

The address/phone/hours stay in the contact block. Related places remain available in source data for later full-page/detail features, but are not rendered on the quick card.
