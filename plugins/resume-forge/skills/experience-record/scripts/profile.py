#!/usr/bin/env python3
"""experience-record — master profile file manager.

Standard library only. No third-party dependencies, no network access.

Subcommands
-----------
  init      create the folder structure and an empty, valid profile
  validate  check a profile file against the bundled schema
  save      validate -> back up -> write atomically (refuses silent data loss)

Usage
-----
  python3 scripts/profile.py init --dir <folder> --name "<their name>"
  python3 scripts/profile.py validate --file <folder>/master_profile.json
  python3 scripts/profile.py save --dir <folder> --from <new_profile.json>

Exit codes: 0 on success, 1 when a save or validation is refused, 2 when a file
could not be read, written, or backed up at all.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROFILE_NAME = "master_profile.json"
BACKUP_DIR = ".backups"
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "assets" / "master-profile.schema.json"

# Counts that must never silently shrink.
COUNTED_SECTIONS = ("experiences", "skills", "projects", "education", "target_roles",
                    "development_areas")
# Sections whose entries carry an id. These are tracked one by one, so dropping
# one entry and adding another in the same save cannot cancel out.
ID_SECTIONS = ("experiences", "skills", "projects", "education")


# --------------------------------------------------------------------------- #
# Minimal JSON-Schema validator (draft-07 subset: exactly what our schema uses)
# --------------------------------------------------------------------------- #

_TYPE_MAP = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
    "number": (int, float),
    "integer": int,
}


def _validate_node(value: Any, schema: dict, path: str, errors: list[str]) -> None:
    expected = schema.get("type")
    if expected:
        py = _TYPE_MAP.get(expected)
        # bool is a subclass of int in Python; keep them apart.
        ok = isinstance(value, py) and not (expected in ("number", "integer")
                                            and isinstance(value, bool))
        if not ok:
            errors.append(f"{path or 'root'}: expected {expected}, got "
                          f"{type(value).__name__}")
            return

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not one of {schema['enum']}")

    if "pattern" in schema and isinstance(value, str):
        if not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} must match {schema['pattern']}")

    if isinstance(value, dict):
        props = schema.get("properties", {})
        for req in schema.get("required", []):
            if req not in value:
                errors.append(f"{path or 'root'}: missing required field '{req}'")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path or 'root'}: unexpected field '{key}'")
        for key, sub in props.items():
            if key in value:
                _validate_node(value[key], sub, f"{path}.{key}" if path else key, errors)

    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            _validate_node(item, schema["items"], f"{path}[{i}]", errors)


def load_schema() -> dict:
    with open(SCHEMA_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def validate_profile(profile: Any) -> list[str]:
    errors: list[str] = []
    _validate_node(profile, load_schema(), "", errors)
    return errors


# --------------------------------------------------------------------------- #
# File operations
# --------------------------------------------------------------------------- #

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_json(path: Path) -> Any:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _atomic_write(path: Path, payload: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(payload)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def _backup_target(folder: Path, target: Path) -> Path:
    backup_dir = folder / BACKUP_DIR
    backup_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    backup = backup_dir / f"master_profile_{stamp}.json"
    n = 2
    while backup.exists():  # two saves in the same second must not collide
        backup = backup_dir / f"master_profile_{stamp}-{n}.json"
        n += 1
    shutil.copy2(target, backup)
    return backup


# The old file may have been edited by hand, so these tolerate malformed parts.
def _len(items: Any) -> int:
    return len(items) if isinstance(items, list) else 0


def _dicts(items: Any) -> list[dict]:
    return [i for i in items if isinstance(i, dict)] if isinstance(items, list) else []


def _counts(profile: dict) -> dict[str, int]:
    counts = {k: _len(profile.get(k)) for k in COUNTED_SECTIONS}
    experiences = _dicts(profile.get("experiences"))
    counts["stories"] = sum(_len(e.get("stories")) for e in experiences)
    counts["accomplishments"] = sum(_len(e.get("accomplishments")) for e in experiences)
    return counts


def _ids(profile: dict) -> set[tuple[str, str]]:
    ids = {(section, str(item["id"]))
           for section in ID_SECTIONS
           for item in _dicts(profile.get(section)) if item.get("id")}
    for exp in _dicts(profile.get("experiences")):
        ids |= {("stories", str(s["id"])) for s in _dicts(exp.get("stories")) if s.get("id")}
    return ids


def _accomplishments_per_role(profile: dict) -> dict[str, int]:
    # Accomplishments have no id, so count them per role: a loss in one role
    # must not be hidden by a gain in another.
    return {str(e.get("id")): _len(e.get("accomplishments"))
            for e in _dicts(profile.get("experiences"))}


def _losses(old: dict, new: dict) -> list[str]:
    """Everything `old` holds that `new` does not, one line each."""
    losses = []
    old_c, new_c = _counts(old), _counts(new)
    losses += [f"{k}: {old_c[k]} -> {new_c[k]}" for k in old_c if new_c[k] < old_c[k]]
    losses += [f"{section}: {ident} is missing"
               for section, ident in sorted(_ids(old) - _ids(new))]
    old_r, new_r = _accomplishments_per_role(old), _accomplishments_per_role(new)
    losses += [f"accomplishments under {role}: {was} -> {new_r.get(role, 0)}"
               for role, was in old_r.items() if new_r.get(role, 0) < was]
    return losses


# --------------------------------------------------------------------------- #
# Subcommands
# --------------------------------------------------------------------------- #

def cmd_init(args) -> int:
    folder = Path(args.dir).expanduser().resolve()
    target = folder / PROFILE_NAME
    if target.exists() and not args.force:
        print(f"REFUSED: {target} already exists. This folder already holds a profile.")
        print("         This is a returning session: read the profile and continue it.")
        return 1

    profile = {
        "meta": {
            "owner_label": args.name,
            "created": _now_iso(),
            "last_updated": _now_iso(),
            "interrogation_stage": "intake",
            "self_portrait": {"in_their_words": "", "through_line": "", "known_for": "",
                              "headed_toward": "", "moving_away_from": "", "constraints": "",
                              "source": "user", "confirmed": False},
            "next_focus": "Stage 1 — intake and self-portrait.",
            "open_questions": [],
            "session_log": [],
        },
        "education": [],
        "experiences": [],
        "skills": [],
        "projects": [],
        "target_roles": [],
        "development_areas": [],
    }
    errors = validate_profile(profile)
    if errors:
        print("INTERNAL ERROR: starter profile failed validation:")
        for e in errors:
            print("  -", e)
        return 2
    try:
        for sub in ("sources", "exports", BACKUP_DIR):
            (folder / sub).mkdir(parents=True, exist_ok=True)
        # --force replaces a whole record, so it gets the same backup as a save.
        if target.exists():
            backup = _backup_target(folder, target)
            print(f"NOTE: the existing profile was copied to {backup} before being replaced.")
        _atomic_write(target, json.dumps(profile, indent=2, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(f"ERROR: could not create the profile in {folder} — {exc}")
        print("       Any existing profile is untouched.")
        return 2
    print(f"OK: created {target}")
    print(f"    folders: sources/  exports/  {BACKUP_DIR}/")
    return 0


def cmd_validate(args) -> int:
    path = Path(args.file).expanduser().resolve()
    try:
        profile = _read_json(path)
    except ValueError as exc:  # bad JSON, or bytes that are not UTF-8
        print(f"INVALID: {path} is not readable JSON — {exc}")
        return 1
    except OSError as exc:
        print(f"ERROR: could not read {path} — {exc}")
        return 2
    errors = validate_profile(profile)
    if errors:
        print(f"INVALID: {len(errors)} problem(s) in {path}")
        for e in errors[:40]:
            print("  -", e)
        if len(errors) > 40:
            print(f"  ... and {len(errors) - 40} more")
        return 1
    print(f"VALID: {path}")
    return 0


def cmd_save(args) -> int:
    folder = Path(args.dir).expanduser().resolve()
    target = folder / PROFILE_NAME
    source = Path(getattr(args, "from")).expanduser().resolve()

    if source == target:
        print("REFUSED: --from is the profile itself. Write the new version to a separate")
        print("         temp file and save from that, so the current one can be checked")
        print("         and backed up. Nothing was written.")
        return 1
    if not target.exists():
        print(f"REFUSED: there is no profile at {target}.")
        print("         Check --dir. A new record is created with init, not save.")
        print("         Nothing was written.")
        return 1

    try:
        new = _read_json(source)
    except ValueError as exc:  # bad JSON, or bytes that are not UTF-8
        print(f"REFUSED: the new profile is not readable JSON — {exc}")
        print("         Nothing was written. The existing profile is untouched.")
        return 1
    except OSError as exc:
        print(f"ERROR: could not read {source} — {exc}")
        print("       Nothing was written. The existing profile is untouched.")
        return 2

    errors = validate_profile(new)
    if errors:
        print(f"REFUSED: the new profile has {len(errors)} schema problem(s):")
        for e in errors[:40]:
            print("  -", e)
        print("         Nothing was written. The existing profile is untouched.")
        return 1

    try:
        old = _read_json(target)
    except (ValueError, OSError):
        old = None
    if not isinstance(old, dict):
        old = None  # unparseable, or not a profile at all

    losses: list[str] = []
    changes: list[str] = []
    if old is not None:
        losses = _losses(old, new)
        if losses and not args.allow_shrink:
            print("REFUSED: this save would remove existing content:")
            for line in losses:
                print(f"  - {line}")
            print("         Nothing was written. The existing profile is untouched.")
            print("         Re-read the current profile, merge properly, and try again.")
            print("         Only pass --allow-shrink if the person asked for this removal,")
            print("         or asked for an item to move from one role to another.")
            return 1
        old_c, new_c = _counts(old), _counts(new)
        changes = [f"{k} {old_c[k]}->{new_c[k]}" for k in new_c if new_c[k] != old_c[k]]

    # Back up whatever is on disk before overwriting it — an unparseable file is
    # the case where the copy matters most, so it must not depend on parsing.
    try:
        backup = _backup_target(folder, target)
    except OSError as exc:
        print(f"ERROR: could not back up the existing profile — {exc}")
        print("       Nothing was written. The existing profile is untouched.")
        return 2
    if old is None:
        print("WARNING: the existing profile could not be parsed, so its contents "
              "could not be checked for data loss.")
        print(f"         The unreadable file was copied to {backup} before writing.")
        print("         Recover from there if this save was not what you intended.")

    new.setdefault("meta", {})["last_updated"] = _now_iso()

    try:
        for sub in ("sources", "exports"):
            (folder / sub).mkdir(parents=True, exist_ok=True)
        _atomic_write(target, json.dumps(new, indent=2, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(f"ERROR: the profile could not be written — {exc}")
        print("       The existing profile is untouched.")
        return 2

    print(f"SAVED: {target}")
    if losses:
        print("       removed, as allowed: " + "; ".join(losses))
    if changes:
        print("       changed: " + ", ".join(changes))
    elif old is not None:
        print("       counts unchanged (content within existing entries may have been edited)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="profile.py",
                                     description="experience-record profile manager")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="create folders and an empty profile")
    p.add_argument("--dir", required=True)
    p.add_argument("--name", required=True, help="the person's name")
    p.add_argument("--force", action="store_true",
                   help="replace an existing profile with an empty one (it is backed up first)")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("validate", help="check a profile against the schema")
    p.add_argument("--file", required=True)
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("save", help="validate, back up, and write the profile")
    p.add_argument("--dir", required=True)
    p.add_argument("--from", required=True, dest="from", help="path to the new profile JSON")
    p.add_argument("--allow-shrink", action="store_true",
                   help="permit a save that removes existing entries")
    p.set_defaults(func=cmd_save)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:  # output piped into head/less and closed early
        os._exit(0)
