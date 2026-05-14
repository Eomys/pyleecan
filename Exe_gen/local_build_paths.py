# -*- coding: utf-8 -*-
"""Shared local path layout for Windows packaging artifacts."""

from dataclasses import dataclass
import os
from os import listdir, makedirs, remove, rmdir
from os.path import dirname, isdir, isfile, join, normpath
from shutil import move


@dataclass(frozen=True)
class LocalBuildPaths:
    """Repository-local paths for environments and packaging artifacts."""

    repo_root: str
    local_root: str
    env_root: str
    env_path: str
    packaging_root: str
    build_root: str
    build_path: str
    dist_root: str
    dist_path: str
    output_root: str
    portable_path: str
    spec_root: str
    spec_path: str
    installer_root: str
    installer_script_path: str
    installer_output_path: str


def get_local_build_paths(repo_root):
    """Return the standardized local workspace layout for the repository."""

    repo_root = normpath(repo_root)
    local_root = join(repo_root, ".local")
    env_root = join(local_root, "envs")
    packaging_root = join(local_root, "packaging")
    build_root = join(packaging_root, "build")
    dist_root = join(packaging_root, "dist")
    output_root = join(packaging_root, "Output")
    spec_root = join(packaging_root, "spec")
    installer_root = join(packaging_root, "installer")

    return LocalBuildPaths(
        repo_root=repo_root,
        local_root=local_root,
        env_root=env_root,
        env_path=join(env_root, "Exenv"),
        packaging_root=packaging_root,
        build_root=build_root,
        build_path=join(build_root, "pyleecan"),
        dist_root=dist_root,
        dist_path=join(dist_root, "Pyleecan"),
        output_root=output_root,
        portable_path=join(output_root, "Pyleecan_Portable"),
        spec_root=spec_root,
        spec_path=join(spec_root, "pyleecan.spec"),
        installer_root=installer_root,
        installer_script_path=join(installer_root, "pyleecan.iss"),
        installer_output_path=join(output_root, "Pyleecan Setup.exe"),
    )


def ensure_local_build_dirs(paths):
    """Create the parent directories used by the local packaging layout."""

    for path in [
        paths.local_root,
        paths.env_root,
        paths.packaging_root,
        paths.build_root,
        paths.dist_root,
        paths.output_root,
        paths.spec_root,
        paths.installer_root,
    ]:
        makedirs(path, exist_ok=True)


def migrate_legacy_local_artifacts(paths, logger=print):
    """Move old root-level local artifacts into the standardized `.local` layout."""

    legacy_map = [
        (join(paths.repo_root, "Exenv"), paths.env_path),
        (join(paths.repo_root, "build"), paths.build_root),
        (join(paths.repo_root, "dist"), paths.dist_root),
        (join(paths.repo_root, "Output"), paths.output_root),
        (join(paths.repo_root, "pyleecan.spec"), paths.spec_path),
        (join(paths.repo_root, "pyleecan.iss"), paths.installer_script_path),
    ]

    ensure_local_build_dirs(paths)
    for legacy_path, target_path in legacy_map:
        if isdir(legacy_path) or isfile(legacy_path):
            logger("Relocating local artifact " + legacy_path + " -> " + target_path)
            _move_path(legacy_path, target_path)


def _move_path(src_path, dst_path):
    """Move a file or directory into place, merging directories when needed."""

    parent_path = dirname(dst_path)
    if parent_path:
        makedirs(parent_path, exist_ok=True)

    if isfile(src_path):
        if isfile(dst_path):
            remove(dst_path)
        elif isdir(dst_path):
            _merge_directory(src_path, dst_path)
            return
        move(src_path, dst_path)
        return

    if not isdir(src_path):
        return

    if not isdir(dst_path):
        move(src_path, dst_path)
        return

    _merge_directory(src_path, dst_path)
    if isdir(src_path) and not listdir(src_path):
        rmdir(src_path)


def _merge_directory(src_dir, dst_dir):
    """Move directory contents recursively into an existing target directory."""

    if isfile(src_dir):
        _move_path(src_dir, join(dst_dir, os.path.basename(src_dir)))
        return

    makedirs(dst_dir, exist_ok=True)
    for entry_name in listdir(src_dir):
        _move_path(join(src_dir, entry_name), join(dst_dir, entry_name))
    if isdir(src_dir) and not listdir(src_dir):
        rmdir(src_dir)
