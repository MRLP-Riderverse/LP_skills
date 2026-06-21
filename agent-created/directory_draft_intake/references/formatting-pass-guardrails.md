# Formatting pass guardrails for inbox cleanup

Use this during broad A–Z normalization passes over `acadie_sol_directory/inbox/`.

## Goal
Make drafts conform to the inbox template without accidentally rewriting meaning or inventing structured facts.

## Safe order of operations
1. Normalize section order to:
   - `Description`
   - `Notes`
   - `Public data to carry forward`
   - `Related places`
   - `Public source`
   - `Admin notes`
2. Preserve existing `Category`, `Area`, and `Tags` unless clearly wrong.
3. Move obvious alias sections into the canonical section names:
   - `Public notes` → `Notes`
   - `Contact` / `Details` → `Public data to carry forward`
4. Keep empty optional sections if needed during a formatting pass.
5. Export only after the whole requested slice is normalized.

## Do not over-infer structured fields
Bad pattern:
- sentence contains an address
- formatter guesses it must be an `Address:` line or `Hours:` line
- result becomes wrong but looks structured

Examples of risky prose:
- `Joey's Pub & Eatery at 2050 St. Peter Avenue, Bathurst.`
- `Restaurant and lounge at Bathurst Marina.`
- `Public listing places it at 1300 St Peter Ave, inside Place Bathurst Mall.`

These may belong in `Description` or `Notes` unless the raw address can be separated cleanly.

## Promotion rule
Only promote prose into `Address` / `Hours` / `Phone` / `Email` when:
- the value is explicit
- the label is already present, or
- the field can be separated with near-zero ambiguity

If not, leave it in prose.

## Verification check
Before export, verify every draft has the canonical heading set in the canonical order.
That catches most formatting drift without forcing deeper semantic edits.
