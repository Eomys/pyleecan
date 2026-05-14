from __future__ import annotations

from importlib.util import find_spec
from pathlib import Path

from pyleecan.Functions.get_path_binary import get_path_binary


class PriusValidationPreflightError(RuntimeError):
    """Raised when a Prius validation workflow cannot start safely."""


def relative_to_repo(path, repo_root):
    """Return a compact path for user-facing validation messages."""

    try:
        return str(Path(path).resolve().relative_to(Path(repo_root).resolve()))
    except Exception:
        return str(path)


def missing_required_files(required_files):
    """Return the subset of required files that are missing."""

    return {
        label: Path(path)
        for label, path in required_files.items()
        if not Path(path).is_file()
    }


def build_missing_files_message(
    *,
    purpose,
    missing_files,
    repo_root,
    recovery_steps,
):
    """Build an actionable missing-artifact error message."""

    lines = [purpose + " cannot start because required local artifacts are missing:"]
    for label, path in missing_files.items():
        lines.append("- " + label + ": " + relative_to_repo(path, repo_root))

    if recovery_steps:
        lines.append("")
        lines.append("Recovery steps:")
        for step in recovery_steps:
            lines.append("- " + step)

    return "\n".join(lines)


def require_existing_files(*, required_files, purpose, repo_root, recovery_steps):
    """Raise a preflight error if any required local artifact is absent."""

    missing_files = missing_required_files(required_files)
    if missing_files:
        raise PriusValidationPreflightError(
            build_missing_files_message(
                purpose=purpose,
                missing_files=missing_files,
                repo_root=repo_root,
                recovery_steps=recovery_steps,
            )
        )


def missing_python_modules(module_names):
    """Return import names that are unavailable in the active interpreter."""

    return [name for name in module_names if find_spec(name) is None]


def require_python_modules(*, module_names, purpose, recovery_steps):
    """Raise a preflight error if required Python modules are unavailable."""

    missing_modules = missing_python_modules(module_names)
    if not missing_modules:
        return

    lines = [purpose + " cannot start because Python modules are missing:"]
    for module_name in missing_modules:
        lines.append("- " + module_name)

    if recovery_steps:
        lines.append("")
        lines.append("Recovery steps:")
        for step in recovery_steps:
            lines.append("- " + step)

    raise PriusValidationPreflightError("\n".join(lines))


def find_first_available_executable(command_names, extra_paths=()):
    """Return the first executable found by Pyleecan or explicit candidates."""

    for command_name in command_names:
        command_path = get_path_binary(command_name)
        if command_path:
            return Path(command_path)

    for path in extra_paths:
        path = Path(path)
        if path.is_file():
            return path

    return None


def require_executables(*, requirements, purpose, recovery_steps):
    """Raise a preflight error if required external executables are unavailable."""

    missing = []
    for label, command_names, extra_paths in requirements:
        if find_first_available_executable(command_names, extra_paths) is None:
            missing.append(label)

    if not missing:
        return

    lines = [purpose + " cannot start because external executables are missing:"]
    for label in missing:
        lines.append("- " + label)

    if recovery_steps:
        lines.append("")
        lines.append("Recovery steps:")
        for step in recovery_steps:
            lines.append("- " + step)

    raise PriusValidationPreflightError("\n".join(lines))


def known_elmer_executable_paths(executable_name):
    """Return common Windows Elmer installation candidates."""

    candidates = []
    for root in [
        Path("C:/Program Files"),
        Path("C:/Program Files (x86)"),
        Path("D:/Software"),
    ]:
        if root.exists():
            candidates.extend(root.glob("Elmer*/bin/" + executable_name))
    return candidates