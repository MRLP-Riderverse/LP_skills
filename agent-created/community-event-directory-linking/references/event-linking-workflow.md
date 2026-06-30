# Event / directory linking notes

Example pattern from the Bathurst summer event workflow:
- Public event announcement references a host venue and a nearby organizer.
- The organizer can be both a business and a venue hub.
- The event should point at the venue/location record.
- The search index needs both the event and the organizer/venue entry.
- A calendar/ICS artifact should be created or refreshed when the site exposes one.

Practical checklist:
1. Confirm the canonical host/venue name and address.
2. Confirm the event title and local start time.
3. Add the organizer/business entry with only public contact data.
4. Add the location record if the address/anchor is missing.
5. Add the event record and link host_entry_ids / location_id.
6. Regenerate search index rows for all touched records.
7. Verify by reading the files back.

Workflow preference learned here:
- Intake can stay deliberately low-friction at the draft stage: only the entry name is mandatory; extra notes belong in a Notes block until later cleanup.
- For public business drafts, stage only public-facing details first.
