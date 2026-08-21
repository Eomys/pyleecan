#!/usr/bin/env python
"""Repository policy checks used by pre-commit and CI."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path, PurePosixPath


PROJECT_ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_TOP_LEVEL_DIRS = {
    ".local",
    ".tox",
    "Exenv",
    "Output",
    "build",
    "dist",
    "pyleecan.egg-info",
}
FORBIDDEN_TOP_LEVEL_PREFIXES = (".venv",)
FORBIDDEN_FILE_NAMES = {
    "optixcache.db",
    "optixcache.db-shm",
    "optixcache.db-wal",
    "pyleecan_launch.log",
}
PYTEST_TEMPORARY_MARKER_PATTERN = re.compile(r"\bpytest\.mark\.(dev|failed)\b")


def normalize_path(raw_path: str) -> tuple[Path, PurePosixPath]:
    """Return the absolute file path and repo-relative POSIX path."""

    path = Path(raw_path)
    if path.is_absolute():
        absolute_path = path.resolve()
    else:
        absolute_path = (PROJECT_ROOT / path).resolve()

    try:
        relative_path = absolute_path.relative_to(PROJECT_ROOT)
    except ValueError:
        relative_path = Path(raw_path)

    return absolute_path, PurePosixPath(relative_path.as_posix())


def check_forbidden_paths(paths: list[str]) -> list[str]:
    """Reject packaging, cache and virtualenv artifacts that should stay untracked."""

    violations: list[str] = []
    for raw_path in paths:
        _absolute_path, relative_path = normalize_path(raw_path)
        if not relative_path.parts:
            continue

        top_level = relative_path.parts[0]
        if top_level in FORBIDDEN_TOP_LEVEL_DIRS or top_level.startswith(
            FORBIDDEN_TOP_LEVEL_PREFIXES
        ):
            violations.append(
                f"{relative_path}: packaging/cache artifact must not be committed"
            )
            continue

        if relative_path.name in FORBIDDEN_FILE_NAMES:
            violations.append(
                f"{relative_path}: generated cache/log artifact must not be committed"
            )

    return violations


def read_text_file(path: Path) -> list[str]:
    """Read a text file defensively and return its lines."""

    try:
        return path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return []


def check_pytest_markers(paths: list[str]) -> list[str]:
    """Reject temporary pytest markers that should not be merged."""

    violations: list[str] = []
    for raw_path in paths:
        absolute_path, relative_path = normalize_path(raw_path)
        if absolute_path.suffix != ".py" or not absolute_path.is_file():
            continue

        for line_number, line in enumerate(read_text_file(absolute_path), start=1):
            match = PYTEST_TEMPORARY_MARKER_PATTERN.search(line)
            if match:
                violations.append(
                    f"{relative_path}:{line_number}: temporary pytest marker "
                    f"'{match.group(0)}' must be removed before commit"
                )

    return violations


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run repository policy checks used by pre-commit and CI."
    )
    parser.add_argument(
        "--check",
        choices=("all", "forbidden-paths", "pytest-markers"),
        default="all",
        help="Select which policy subset to validate.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files to inspect. pre-commit populates this automatically.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not args.paths:
        return 0

    violations: list[str] = []
    if args.check in ("all", "forbidden-paths"):
        violations.extend(check_forbidden_paths(args.paths))
    if args.check in ("all", "pytest-markers"):
        violations.extend(check_pytest_markers(args.paths))

    if not violations:
        return 0

    print("Repository policy check failed:", file=sys.stderr)
    for violation in violations:
        print(f"  - {violation}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
