#!/usr/bin/env python3
"""Fail if a plugin changed without its version being bumped.

CLAUDE.md rule 4 requires bumping `plugin.json` `version` and the matching
`marketplace.json` entry on every change. `validate.py` checks the two agree
with each other, but agreeing on a stale number still passes — a pull request
that rewrote a plugin's whole build route once merged with the version
untouched. This closes that hole.

Usage:
    python3 scripts/check_version_bump.py <base-ref>

<base-ref> is what the branch is being merged into, e.g. `origin/main`. Compares
against the merge base, so unrelated commits landing on main do not count as
changes. Exits non-zero with an explanation when a bump is missing.

Skipped when there is no base ref (a plain push to main), since the check
belongs on the pull request.
"""

import json
import subprocess
import sys
from collections import defaultdict

MANIFEST = ".claude-plugin/plugin.json"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          check=False).stdout.strip()


def semver(text: str):
    try:
        return tuple(int(p) for p in str(text).split("."))
    except ValueError:
        return None


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("no base ref given, skipping version-bump check")
        return 0
    base = sys.argv[1]

    merge_base = git("merge-base", base, "HEAD") or base
    changed = [f for f in git("diff", "--name-only", merge_base, "HEAD").splitlines() if f]
    if not changed:
        print("no changed files")
        return 0

    touched = defaultdict(list)
    for path in changed:
        parts = path.split("/")
        if len(parts) > 2 and parts[0] == "plugins":
            touched[parts[1]].append(path)

    if not touched:
        print("no plugin directories touched")
        return 0

    errors = []
    for name, files in sorted(touched.items()):
        manifest = f"plugins/{name}/{MANIFEST}"
        try:
            with open(manifest, encoding="utf-8") as fh:
                new = json.load(fh).get("version")
        except FileNotFoundError:
            errors.append(f"{name}: {manifest} is missing")
            continue

        raw_old = git("show", f"{merge_base}:{manifest}")
        if not raw_old:
            print(f"  {name}: new plugin at {new}, no bump required")
            continue
        old = json.loads(raw_old).get("version")

        v_new, v_old = semver(new), semver(old)
        if v_new is None or v_old is None:
            errors.append(f"{name}: version not semver (old {old!r}, new {new!r})")
        elif v_new == v_old:
            listed = "\n      ".join(sorted(files)[:8])
            more = "" if len(files) <= 8 else f"\n      ... and {len(files) - 8} more"
            errors.append(
                f"{name}: {len(files)} file(s) changed but version is still {old}.\n"
                f"      Bump plugins/{name}/{MANIFEST} AND the matching entry in\n"
                f"      .claude-plugin/marketplace.json (CLAUDE.md rule 4).\n"
                f"      Changed:\n      {listed}{more}")
        elif v_new < v_old:
            errors.append(f"{name}: version went backwards, {old} -> {new}")
        else:
            print(f"  {name}: {old} -> {new}, {len(files)} file(s) changed")

    if errors:
        print("\nVersion bump check FAILED:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("\nVersion bump check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
