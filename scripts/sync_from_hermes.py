#!/usr/bin/env python3
"""Refresh LP_skills from the active Hermes profile.

The repository has two backup layers:
- agent-created/: curated, human-oriented recovery copies
- mirror/: deterministic filesystem mirror of active and archived skills

Runtime metadata, caches, bytecode, and VCS directories are intentionally excluded.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

HERMES_SKILLS = Path.home() / ".hermes" / "skills"
HERMES_SCRIPTS = Path.home() / ".hermes" / "scripts"
REPO = Path(__file__).resolve().parents[1]
CURATED = REPO / "agent-created"
MIRROR = REPO / "mirror"
MANIFEST_JSON = REPO / "MIRROR_MANIFEST.json"
MANIFEST_MD = REPO / "MIRROR_MANIFEST.md"

EXCLUDED_NAMES = {".git", "__pycache__", ".weather_cache", ".hub", ".curator_backups"}
EXCLUDED_FILES = {
    ".usage.json",
    ".usage.json.runtime",
    ".usage.json.lock",
    ".bundled_manifest",
    ".curator_state",
}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def skill_name(skill_dir: Path) -> str | None:
    path = skill_dir / "SKILL.md"
    if not path.is_file():
        return None
    match = re.search(r"^name:\s*([^\n]+)", path.read_text(errors="replace")[:5000], re.MULTILINE)
    return match.group(1).strip() if match else None


def copy_tree(src: Path, dst: Path) -> int:
    count = 0
    for path in src.rglob("*"):
        rel = path.relative_to(src)
        if any(part in EXCLUDED_NAMES for part in rel.parts):
            continue
        if path.is_file() and (path.name in EXCLUDED_FILES or path.suffix in EXCLUDED_SUFFIXES):
            continue
        target = dst / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_symlink():
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() or target.is_symlink():
                target.unlink()
            target.symlink_to(path.readlink())
            count += 1
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            count += 1
    return count


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def files_for_manifest(root: Path) -> list[dict[str, object]]:
    result = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in EXCLUDED_NAMES for part in path.relative_to(root).parts):
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        result.append({"path": str(path.relative_to(root)), "sha256": digest, "bytes": path.stat().st_size})
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-archive", action="store_true", help="Only mirror active skills")
    args = parser.parse_args()

    if not HERMES_SKILLS.is_dir():
        raise SystemExit(f"Hermes skills directory not found: {HERMES_SKILLS}")

    live_dirs = [
        p for p in HERMES_SKILLS.rglob("SKILL.md")
        if ".archive" not in p.relative_to(HERMES_SKILLS).parts
    ]
    live_skill_dirs = [p.parent for p in live_dirs]
    live_by_name = {name: path for path in live_skill_dirs if (name := skill_name(path))}

    # Refresh the curated copies by frontmatter name, so renamed folders still sync.
    curated_updates = []
    for curated_dir in sorted(CURATED.iterdir()):
        if not curated_dir.is_dir():
            continue
        current_name = skill_name(curated_dir)
        if current_name and current_name in live_by_name:
            reset_dir(curated_dir)
            copy_tree(live_by_name[current_name], curated_dir)
            curated_updates.append(current_name)

    # Repair the old flat gallery artifact into a normal restorable skill directory.
    gallery_note = CURATED / "acadie-sol-gallery.md"
    gallery_source = live_by_name.get("acadie-sol-gallery")
    gallery_dir = CURATED / "acadie-sol-gallery"
    if gallery_source:
        reset_dir(gallery_dir)
        copy_tree(gallery_source, gallery_dir)
        if gallery_note.exists():
            gallery_note.unlink()
        curated_updates.append("acadie-sol-gallery")

    # The weather cron uses a wrapper outside the skill directory; keep a recovery copy.
    weather_wrapper = HERMES_SCRIPTS / "bathurst_weather_telegram.sh"
    weather_backup = CURATED / "weatherAPI-home" / "bathurst_weather_telegram.sh"
    if weather_wrapper.is_file():
        weather_backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(weather_wrapper, weather_backup)
        weather_backup.chmod(0o755)

    active_dst = MIRROR / "active"
    reset_dir(active_dst)
    active_files = copy_tree(HERMES_SKILLS, active_dst)
    # The active mirror must not accidentally include the archive tree.
    archive_in_active = active_dst / ".archive"
    if archive_in_active.exists():
        shutil.rmtree(archive_in_active)

    archive_files = 0
    if not args.no_archive:
        archive_src = HERMES_SKILLS / ".archive"
        archive_dst = MIRROR / "archive"
        if archive_src.is_dir():
            reset_dir(archive_dst)
            archive_files = copy_tree(archive_src, archive_dst)

    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    manifest = {
        "generated_at_utc": generated,
        "source": str(HERMES_SKILLS),
        "active_skill_directories": sorted(str(p.relative_to(HERMES_SKILLS)) for p in live_skill_dirs),
        "active_skill_count": len(live_by_name),
        "active_files": files_for_manifest(active_dst),
        "archive_files": files_for_manifest(MIRROR / "archive") if not args.no_archive else [],
        "curated_refreshed_by_frontmatter": sorted(set(curated_updates)),
        "excluded": sorted(EXCLUDED_NAMES | EXCLUDED_FILES | EXCLUDED_SUFFIXES),
    }
    MANIFEST_JSON.write_text(json.dumps(manifest, indent=2) + "\n")

    lines = [
        "# Hermes Skills Mirror",
        "",
        f"Generated: `{generated}`",
        f"Source: `{HERMES_SKILLS}`",
        "",
        "This repository contains a disaster-recovery mirror of the active Hermes skills.",
        "The curated `agent-created/` layer is kept for human-selected recovery copies;",
        "the `mirror/` layer is the broad deterministic backup.",
        "",
        "## Counts",
        "",
        f"- Active skill directories: {len(live_by_name)}",
        f"- Active mirrored files: {len(manifest['active_files'])}",
        f"- Archived mirrored files: {len(manifest['archive_files'])}",
        f"- Curated skills refreshed: {len(set(curated_updates))}",
        "",
        "## Recovery",
        "",
        "- Active skills: `mirror/active/`",
        "- Archived skills: `mirror/archive/`",
        "- SHA-256 manifest: `MIRROR_MANIFEST.json`",
        "- Re-run: `python3 scripts/sync_from_hermes.py`",
        "",
        "## Excluded",
        "",
        "Runtime metadata, `.git` directories, `__pycache__`, weather caches, and Python bytecode are excluded.",
        "Secrets are not copied from `.env` or other files outside the skills tree.",
        "",
    ]
    MANIFEST_MD.write_text("\n".join(lines))
    print(json.dumps({
        "active_skills": len(live_by_name),
        "active_files": len(manifest["active_files"]),
        "archive_files": len(manifest["archive_files"]),
        "curated_refreshed": sorted(set(curated_updates)),
        "manifest": str(MANIFEST_JSON),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
