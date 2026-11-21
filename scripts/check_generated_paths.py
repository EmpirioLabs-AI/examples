#!/usr/bin/env python3
"""Refuse staged refresh changes that touch anything build_examples.py does not generate.

    python scripts/check_generated_paths.py      # checks what is staged (git diff --cached)

refresh.yml regenerates the examples in a job that holds no credential and hands the
result, as a patch, to the job that pushes it. That job pushes only when every staged
path is generated output: README.md and the files of a model folder under models/.
Only regular files are accepted (no symlink, submodule or executable). So a compromised
generator still cannot change the scripts, tests or workflows that later runs execute.

Standard library only: it runs in the job that can push.
"""

from __future__ import annotations

import re
import subprocess
import sys

ALLOWED = re.compile(
    r"^(README\.md|models/[a-z0-9][a-z0-9.-]{0,79}/"
    r"(README\.md|request\.sh|submit\.sh|poll\.sh|example\.py|example_openai\.py|realtime\.py))$"
)
REGULAR = {"000000", "100644"}  # absent (an addition's old side or a deletion's new side), or a plain file


def problems(raw: bytes) -> list[str]:
    """Problems in `git diff --cached --raw --no-renames -z` output."""
    out = []
    fields = raw.split(b"\0")
    i = 0
    while i < len(fields) - 1:
        meta, path = fields[i].decode(), fields[i + 1].decode("utf-8", "replace")
        i += 2
        if not meta.startswith(":"):
            out.append(f"unexpected diff line {meta!r}")
            continue
        old_mode, new_mode = meta[1:].split()[:2]
        if not ALLOWED.match(path) or ".." in path.split("/"):
            out.append(f"{path}: the refresh does not generate this path")
        elif old_mode not in REGULAR or new_mode not in REGULAR:
            out.append(f"{path}: mode {old_mode} -> {new_mode}; only regular files may change")
    return out


def main() -> int:
    raw = subprocess.run(["git", "diff", "--cached", "--raw", "--no-renames", "-z"], check=True, capture_output=True).stdout
    found = problems(raw)
    for problem in found:
        print(f"ERROR: {problem}")
    if found:
        print("The refresh patch was refused; nothing was pushed.")
        return 1
    count = raw.count(b"\0") // 2
    print(f"refresh patch OK: {count} generated path(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
