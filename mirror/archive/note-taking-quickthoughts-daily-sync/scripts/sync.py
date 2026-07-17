#!/usr/bin/env python3
"""QuickThoughts Daily Sync.

Exports dated slices from QuickThoughts into ~/brain/sources and imports them into
GBrain with idempotent, atomic file writes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from tempfile import NamedTemporaryFile

QUICKTHOUGHTS_FILE = Path("/home/midnight/Documents/Notes/notecore/inbox/QuickThoughts.txt")
BRAIN_SOURCES_DIR = Path("/home/midnight/brain/sources")
STATE_FILE = Path("/home/midnight/.hermes/state/quickthoughts-sync-state.json")
GBRAIN_CMD = "/home/midnight/.bun/bin/gbrain"
SEPARATOR_RE = re.compile(r"^\s*########\s*$")
CANONICAL_HEADER_RE = re.compile(r"^⁜\s*(\d{2}:\d{2}:\d{2})\s*\|\s*(\d{2})\.(\d{2})\.(\d{2})\s*>\s*(.*)$")
LEGACY_HEADER_RE = re.compile(r"^\[(\d{4}-\d{2}-\d{2})\]\s*(.*)$")


def get_date_atlantic() -> str:
    result = subprocess.run(
        ["date", "+%Y-%m-%d"],
        capture_output=True,
        text=True,
        env={**os.environ, "TZ": "America/Halifax"},
        check=True,
    )
    return result.stdout.strip()


def get_timestamp_atlantic() -> str:
    result = subprocess.run(
        ["date", "+%Y-%m-%dT%H:%M:%S%z"],
        capture_output=True,
        text=True,
        env={**os.environ, "TZ": "America/Halifax"},
        check=True,
    )
    ts = result.stdout.strip()
    if len(ts) > 19 and ts[-4:].isdigit():
        ts = ts[:-2] + ":" + ts[-2:]
    return ts


def read_state() -> dict:
    if not STATE_FILE.exists():
        return {"last_sync_date": None, "synced_dates": {}}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"last_sync_date": None, "synced_dates": {}}


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", delete=False, dir=path.parent, encoding="utf-8") as fh:
        fh.write(content)
        fh.flush()
        os.fsync(fh.fileno())
        tmp_path = Path(fh.name)
    os.replace(tmp_path, path)


def write_state(state: dict) -> None:
    atomic_write_text(STATE_FILE, json.dumps(state, indent=2, sort_keys=True) + "\n")


def _consume_canonical_block(lines: list[str], start: int) -> tuple[list[str], int]:
    block: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if i != start and CANONICAL_HEADER_RE.match(line):
            break
        block.append(line)
        i += 1
        if i <= len(lines) and SEPARATOR_RE.match(line):
            break
    if not any(SEPARATOR_RE.match(line) for line in block):
        block.append("  ########")
    return block, i


def _consume_legacy_block(lines: list[str], start: int) -> tuple[list[str], int]:
    block = [lines[start].rstrip("\n")]
    i = start + 1
    while i < len(lines):
        line = lines[i].rstrip("\n")
        if CANONICAL_HEADER_RE.match(line) or LEGACY_HEADER_RE.match(line):
            break
        if not line.strip():
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or CANONICAL_HEADER_RE.match(lines[j]) or LEGACY_HEADER_RE.match(lines[j]):
                i = j
                break
        block.append(line)
        i += 1
    return block, i


def parse_entries(filepath: Path) -> list[dict]:
    if not filepath.exists():
        return []

    lines = filepath.read_text(encoding="utf-8", errors="ignore").splitlines()
    entries: list[dict] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        canonical = CANONICAL_HEADER_RE.match(line)
        if canonical:
            hhmmss, dd, mm, yy, _rest = canonical.groups()
            date_str = f"20{yy}-{mm}-{dd}"
            block, i = _consume_canonical_block(lines, i)
            entries.append(
                {
                    "date": date_str,
                    "sort_key": f"{date_str}T{hhmmss}",
                    "raw": "\n".join(block).strip(),
                    "kind": "canonical",
                }
            )
            continue

        legacy = LEGACY_HEADER_RE.match(line)
        if legacy:
            date_str, _rest = legacy.groups()
            block, i = _consume_legacy_block(lines, i)
            entries.append(
                {
                    "date": date_str,
                    "sort_key": f"{date_str}T00:00:00",
                    "raw": "\n".join(block).strip(),
                    "kind": "legacy",
                }
            )
            continue

        i += 1

    entries.sort(key=lambda item: item["sort_key"])
    return entries


def extract_entries_by_date(filepath: Path, target_date: str) -> list[str]:
    return [entry["raw"] for entry in parse_entries(filepath) if entry["date"] == target_date]


def render_markdown(date_str: str, entries: list[str]) -> str:
    lines = [f"# QuickThoughts {date_str}", "", f"## Raw entries from {date_str}", ""]
    for entry in entries:
        lines.append(entry)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def run_import() -> tuple[bool, str]:
    result = subprocess.run(
        [GBRAIN_CMD, "import", "--no-embed", str(BRAIN_SOURCES_DIR)],
        capture_output=True,
        text=True,
        timeout=180,
    )
    return result.returncode == 0, (result.stdout + result.stderr).strip()


def send_telegram(msg: str) -> bool:
    try:
        result = subprocess.run(
            ["telegram-notify", msg],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0
    except Exception:
        return False


def compute_dates_to_sync(last_date: str | None, review_date: str) -> list[str]:
    if not last_date:
        return [review_date]
    try:
        last_dt = datetime.strptime(last_date, "%Y-%m-%d")
        review_dt = datetime.strptime(review_date, "%Y-%m-%d")
    except ValueError:
        return [review_date]

    dates: list[str] = []
    check_dt = last_dt + timedelta(days=1)
    while check_dt <= review_dt:
        dates.append(check_dt.strftime("%Y-%m-%d"))
        check_dt += timedelta(days=1)
    return dates or [review_date]


def file_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="Review date YYYY-MM-DD instead of yesterday in Atlantic time")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    state = read_state()
    last_date = state.get("last_sync_date")
    current_date = get_date_atlantic()
    review_date = args.date or (datetime.strptime(current_date, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")

    if args.status:
        print(f"Last sync: {last_date or 'Never'}")
        print(f"Current: {current_date}")
        print(f"Reviewing: {review_date}")
        print(f"Tracked dates: {len(state.get('synced_dates', {}))}")
        return 0

    if last_date == review_date and not args.force and not args.dry_run:
        print(f"Already synced through reviewed day ({review_date})")
        return 0

    dates_to_sync = [review_date] if (args.date and (args.force or args.dry_run)) else compute_dates_to_sync(last_date, review_date)
    if args.date and not dates_to_sync:
        dates_to_sync = [review_date]

    rendered_by_date: dict[str, str] = {}
    total_entries = 0
    for date_str in dates_to_sync:
        entries = extract_entries_by_date(QUICKTHOUGHTS_FILE, date_str)
        if not entries:
            continue
        rendered_by_date[date_str] = render_markdown(date_str, entries)
        total_entries += len(entries)

    if not rendered_by_date:
        print("No new entries")
        if not args.dry_run:
            send_telegram(
                f"🧠 QuickThoughts Sync - {review_date}\n\nℹ️ No new entries since last sync ({last_date or 'Never'})\n\nNext review: Tomorrow, 2:00 AM AST"
            )
        return 0

    if args.dry_run:
        for date_str in sorted(rendered_by_date):
            print(f"--- {date_str} ({rendered_by_date[date_str].count('⁜ ') + rendered_by_date[date_str].count('[')} entries) ---")
            print(rendered_by_date[date_str])
        return 0

    BRAIN_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    for date_str, content in rendered_by_date.items():
        md_path = BRAIN_SOURCES_DIR / f"quickthoughts-{date_str}.md"
        atomic_write_text(md_path, content)
        print(f"Wrote {md_path} with {content.count('⁜ ') + content.count('[')} entries")

    success, output = run_import()
    if not success:
        print(f"Import failed: {output}")
        send_telegram(f"🧠 QuickThoughts Sync - FAILED ❌\n\nError: {output[:200]}\n\nLast sync: {last_date or 'Never'}")
        return 1

    synced_dates = state.setdefault("synced_dates", {})
    for date_str, content in rendered_by_date.items():
        synced_dates[date_str] = {
            "entry_count": sum(1 for entry in parse_entries(QUICKTHOUGHTS_FILE) if entry["date"] == date_str),
            "sha256": file_sha256(content),
            "synced_at": get_timestamp_atlantic(),
        }

    state["last_sync_date"] = review_date
    state["last_sync_timestamp"] = get_timestamp_atlantic()
    state["total_entries_synced"] = state.get("total_entries_synced", 0) + total_entries
    write_state(state)

    report = (
        f"🧠 QuickThoughts Sync - {review_date}\n\n"
        f"✅ {total_entries} entries imported to GBrain\n\n"
        f"Themes:\n• Auto-synced from QuickThoughts.txt\n• Entries preserved with full context\n\n"
        f"Sync: {get_timestamp_atlantic().split('T')[1][:5]} AST ✅"
    )
    send_telegram(report)
    print(f"Sync complete: {total_entries} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
