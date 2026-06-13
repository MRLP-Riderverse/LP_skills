#!/usr/bin/env python3
"""Render or write an Acadie.sol directory inbox draft.

Notes-first by default:
- only the title is mandatory
- everything else can stay in Notes
- duplicate checks can block twin writes with the exact fallback wording

The script stays backwards-compatible with older structured flags so later
normalization or scraper-fed workflows can still collapse fields into Notes.
The emitted draft matches the canonical inbox template shape used by
`inbox/_template.md`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DUPLICATE_MESSAGE = "I believe you already have an entry for this: {path}"


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug or "draft"


def normalize_blocks(values):
    blocks = []
    for value in values or []:
        text = str(value).strip()
        if text:
            blocks.append(text)
    return blocks


def parse_kv(items):
    parsed = []
    for item in items or []:
        text = str(item).strip()
        if not text:
            continue
        if "=" not in text:
            parsed.append(text)
            continue
        key, value = text.split("=", 1)
        key = key.strip()
        value = value.strip()
        if key and value:
            parsed.append(f"{key}: {value}")
        elif key:
            parsed.append(key)
    return parsed


def first_heading_title(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8") as handle:
            first_line = handle.readline().strip()
    except OSError:
        return ""
    prefix = "# Draft:"
    if first_line.startswith(prefix):
        return first_line[len(prefix):].strip()
    return ""


def titles_match(candidate: str, existing: str) -> bool:
    a = normalize_text(candidate)
    b = normalize_text(existing)
    if not a or not b:
        return False
    if a == b:
        return True
    shorter, longer = sorted((a, b), key=len)
    return len(shorter) >= 6 and shorter in longer


def find_duplicate(inbox_dir: Path, title: str, aliases=None) -> Path | None:
    aliases = normalize_blocks(aliases)
    candidates = [title, *aliases]
    for path in sorted(inbox_dir.glob("*.md")):
        existing_title = first_heading_title(path)
        if not existing_title:
            continue
        if any(titles_match(candidate, existing_title) for candidate in candidates):
            return path.resolve()
    return None


def build_notes(args) -> str:
    note_blocks = normalize_blocks(args.note)
    if note_blocks:
        return "\n\n".join(note_blocks)

    derived = []
    if args.address:
        derived.append(f"Address: {args.address.strip()}")
    if args.phone:
        derived.append(f"Phone: {args.phone.strip()}")
    if args.hours:
        derived.append(f"Hours: {args.hours.strip()}")
    if args.email:
        derived.append(f"Email: {args.email.strip()}")
    if args.source_label:
        derived.append(f"Source context: {args.source_label.strip()}")
    for source in normalize_blocks(args.source):
        derived.append(f"Source: {source}")
    for fact in normalize_blocks(args.public_fact):
        derived.append(fact)
    derived.extend(normalize_blocks(args.public_note))
    derived.extend(parse_kv(args.field))
    return "\n\n".join(derived)


def build_draft(args) -> str:
    lines = [f"# Draft: {args.title.strip()}", "", "## Notes"]
    notes = build_notes(args)
    if notes:
        lines.append(notes)
    lines.extend(["", "## Admin notes", f"- Submitted by : {args.submitted_by}"])
    for note in normalize_blocks(args.admin_note):
        rendered = f"- {note}"
        if rendered != f"- Submitted by : {args.submitted_by}":
            lines.append(rendered)
    if args.confidence:
        lines.append(f"- Confidence: {args.confidence.strip()}")
    lines.append("")
    return "\n".join(lines)


def output_path_for(args) -> Path | None:
    if args.output:
        return Path(args.output).expanduser()
    if args.write_to_inbox:
        inbox_dir = Path(args.write_to_inbox).expanduser()
        return inbox_dir / f"{slugify(args.title)}.md"
    return None


def main(argv=None):
    parser = argparse.ArgumentParser(description="Render a directory inbox draft")
    parser.add_argument("--title", required=True)
    parser.add_argument("--note", action="append", default=[], help="Notes blocks; repeatable")
    parser.add_argument("--submitted-by", default="Acadie.sol")
    parser.add_argument("--admin-note", action="append", default=[], help="Admin-only notes; repeatable")
    parser.add_argument("--confidence", default="")
    parser.add_argument("--source-label", default="")
    parser.add_argument("--source", action="append", default=[], help="Source lines; repeatable")
    parser.add_argument("--address")
    parser.add_argument("--phone")
    parser.add_argument("--hours")
    parser.add_argument("--email")
    parser.add_argument("--public-fact", action="append", default=[], help="Extra public-facing facts; repeatable")
    parser.add_argument("--public-note", action="append", default=[], help="Public notes; repeatable")
    parser.add_argument("--field", action="append", default=[], help="Extra key=value fields; repeatable")
    parser.add_argument("--alias", action="append", default=[], help="Alternate names for duplicate detection; repeatable")
    parser.add_argument("--check-duplicate-in", default="", help="Inbox directory to scan before writing")
    parser.add_argument("--output", default="", help="Write draft to an explicit file path")
    parser.add_argument("--write-to-inbox", default="", help="Write draft into this inbox directory using a slugified filename")
    args = parser.parse_args(argv)

    if args.check_duplicate_in:
        inbox_dir = Path(args.check_duplicate_in).expanduser()
        duplicate = find_duplicate(inbox_dir, args.title, args.alias)
        if duplicate is not None:
            sys.stdout.write(DUPLICATE_MESSAGE.format(path=duplicate))
            return 2

    draft = build_draft(args)
    out_path = output_path_for(args)
    if out_path is not None:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(draft, encoding="utf-8")
    sys.stdout.write(draft)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
