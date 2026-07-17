#!/usr/bin/env python3
"""Verify LP_skills/MIRROR_MANIFEST.json against the checked-in mirror."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MIRROR_MANIFEST.json"


def check_group(root: Path, entries: list[dict]) -> list[str]:
    errors: list[str] = []
    expected = {entry["path"]: entry for entry in entries}
    actual = {str(path.relative_to(root)): path for path in root.rglob("*") if path.is_file()}
    for rel in sorted(set(expected) - set(actual)):
        errors.append(f"missing: {root.name}/{rel}")
    for rel in sorted(set(actual) - set(expected)):
        errors.append(f"unlisted: {root.name}/{rel}")
    for rel in sorted(set(expected) & set(actual)):
        path = actual[rel]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expected[rel]["sha256"]:
            errors.append(f"hash mismatch: {root.name}/{rel}")
        if path.stat().st_size != expected[rel]["bytes"]:
            errors.append(f"size mismatch: {root.name}/{rel}")
    return errors


def main() -> int:
    if not MANIFEST.is_file():
        print(f"FAIL: missing {MANIFEST}")
        return 1
    data = json.loads(MANIFEST.read_text())
    errors = check_group(ROOT / "mirror" / "active", data.get("active_files", []))
    errors += check_group(ROOT / "mirror" / "archive", data.get("archive_files", []))
    if errors:
        print("FAIL: mirror verification")
        print("\n".join(errors))
        return 1
    print(
        "PASS: mirror verification; "
        f"active_files={len(data.get('active_files', []))}; "
        f"archive_files={len(data.get('archive_files', []))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
