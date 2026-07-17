---
name: workspace-automation
description: "Automate workspace tools and office workflows: docs, email, calendars, databases, presentations, OCR, meeting pipelines, and geospatial lookups."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [workspace, office, automation, documents, presentations, OCR, meetings, maps]
    related_skills: [browser-qa-automation]
---

# Workspace Automation

Class-level skill for automating productivity systems and office workflows.

Use this when working across:
- document and data systems
- office productivity suites
- presentation authoring or extraction
- meeting summaries and pipeline jobs
- geospatial lookups and route/timezone queries

## Core workflow

1. Identify the source system and the target artifact.
2. Prefer native APIs or structured CLIs over manual copying.
3. Extract or transform data once, then reuse the structured output.
4. Verify the produced artifact directly, not just the API call.

## Subsections

### Workspace APIs

Use the native service API or CLI for tasks in Airtable, Google Workspace, Notion, and similar systems.

- CRUD, search, filters, and upserts
- mailbox/calendar/doc automation
- page/database syncing
- structured metadata writes

### Document and presentation work

- Extract text from PDFs, scans, and reports.
- Create or edit slide decks and templates.
- Preserve layout, notes, and source content when round-tripping.
- Prefer structured parsers over OCR when the input is already text-based.

### Meeting and pipeline automation

- Operate meeting-summary pipelines.
- Inspect job status and replay failed runs when needed.
- Verify the output artifact, not just the background job state.

### Geospatial lookups

- Geocode addresses and place names.
- Resolve routes, distances, and timezones.
- Use location APIs for structured lookup tasks instead of ad hoc guessing.

## Verification checklist

- Confirm the target system accepted the change.
- Re-read or re-open the resulting artifact.
- Check for formatting, ordering, and metadata regressions.
- For pipelines, confirm the generated output or downstream state changed as expected.

## Notes

This umbrella absorbs narrow workspace tools that are all variants of the same pattern: structured productivity systems, document pipelines, and office automation.