# -*- coding: utf-8 -*-

from glob import glob
from os import environ, name as os_name
from os.path import abspath, isdir, isfile, join, split
from shutil import which


_WINDOWS_INSTALL_PATTERNS = {
    "elmersolver": ["Elmer*\\bin"],
    "elmergrid": ["Elmer*\\bin"],
    "paraview": ["ParaView*\\bin"],
    "pvpython": ["ParaView*\\bin"],
    "pvbatch": ["ParaView*\\bin"],
}

_ENV_VAR_MAP = {
    "elmersolver": ["PYLEECAN_ELMERSOLVER", "ELMERSOLVER_BIN", "ELMER_HOME"],
    "elmergrid": ["PYLEECAN_ELMERGRID", "ELMERGRID_BIN", "ELMER_HOME"],
    "paraview": ["PYLEECAN_PARAVIEW", "PARAVIEW_BIN", "PARAVIEW_HOME"],
    "pvpython": ["PYLEECAN_PVPYTHON", "PVPYTHON_BIN", "PARAVIEW_HOME"],
    "pvbatch": ["PYLEECAN_PVBATCH", "PVBATCH_BIN", "PARAVIEW_HOME"],
}


def _unique(items):
    """Return a list with duplicates removed while preserving order."""

    seen = set()
    output = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        output.append(item)
    return output


def _normalized_binary_name(binary_name):
    """Return a lowercase executable name without the Windows extension."""

    name = str(binary_name).strip().lower()
    if name.endswith(".exe"):
        return name[:-4]
    return name


def _candidate_names(binary_name):
    """Return candidate executable names for the current platform."""

    candidate_list = [str(binary_name).strip()]
    if os_name == "nt":
        normalized = _normalized_binary_name(binary_name)
        candidate_list.extend([normalized, normalized + ".exe"])

    return _unique([name for name in candidate_list if name])


def _resolve_path_candidate(path_value, candidate_names):
    """Resolve a file or directory hint into an executable path."""

    if not path_value:
        return None

    raw_path = str(path_value).strip().strip('"')
    if not raw_path:
        return None

    if isfile(raw_path):
        return abspath(raw_path)

    candidate_dirs = [raw_path]
    if isdir(join(raw_path, "bin")):
        candidate_dirs.append(join(raw_path, "bin"))

    for directory in candidate_dirs:
        for candidate_name in candidate_names:
            candidate_path = join(directory, candidate_name)
            if isfile(candidate_path):
                return abspath(candidate_path)

    return None


def _iter_env_paths(binary_name, candidate_names):
    """Yield executable candidates from environment-variable overrides."""

    normalized = _normalized_binary_name(binary_name)
    for env_name in _ENV_VAR_MAP.get(normalized, []):
        value = environ.get(env_name)
        resolved = _resolve_path_candidate(value, candidate_names)
        if resolved is not None:
            yield resolved


def _iter_windows_install_paths(binary_name, candidate_names):
    """Yield executable candidates from standard Windows install locations."""

    if os_name != "nt":
        return

    normalized = _normalized_binary_name(binary_name)
    install_patterns = _WINDOWS_INSTALL_PATTERNS.get(normalized, [])
    if not install_patterns:
        return

    root_list = _unique(
        [
            environ.get("ProgramW6432"),
            environ.get("ProgramFiles"),
            environ.get("ProgramFiles(x86)"),
            "D:/Software",
        ]
    )

    for root_dir in [root for root in root_list if root]:
        for pattern in install_patterns:
            for install_dir in sorted(glob(join(root_dir, pattern)), reverse=True):
                resolved = _resolve_path_candidate(install_dir, candidate_names)
                if resolved is not None:
                    yield resolved


def get_path_binary(binary_name, is_include_file=True):
    """Return the path to an executable or installation directory.

    Resolution order is:
    1. explicit file/directory path passed in ``binary_name``
    2. environment-variable overrides for known tools
    3. PATH lookup
    4. standard Windows installation folders for Elmer and ParaView
    """

    candidate_names = _candidate_names(binary_name)

    path_file = _resolve_path_candidate(binary_name, candidate_names)

    if path_file is None:
        env_candidates = list(_iter_env_paths(binary_name, candidate_names))
        if env_candidates:
            path_file = env_candidates[0]

    if path_file is None:
        for candidate_name in candidate_names:
            path_file = which(candidate_name)
            if path_file:
                path_file = abspath(path_file)
                break

    if path_file is None:
        install_candidates = list(_iter_windows_install_paths(binary_name, candidate_names))
        if install_candidates:
            path_file = install_candidates[0]

    if not is_include_file and path_file:
        path_file, _ = split(path_file)

    return path_file


if __name__ == "__main__":
    print(get_path_binary("python"))
    print(get_path_binary("python", is_include_file=False))
