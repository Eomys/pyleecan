"""PyInstaller runtime hook for packaged PySide6 applications."""

import ctypes
import os
import sys
import tempfile
import traceback
from datetime import datetime


def _resolve_log_path():
    """Return a writable log file path for launch diagnostics."""

    candidates = []
    env_path = os.getenv("PYLEECAN_BOOTSTRAP_LOG")
    if env_path:
        candidates.append(env_path)

    exe_dir = os.path.dirname(getattr(sys, "executable", ""))
    if exe_dir:
        candidates.append(os.path.join(exe_dir, "pyleecan_launch.log"))

    candidates.append(os.path.join(tempfile.gettempdir(), "pyleecan_launch.log"))

    for path in candidates:
        try:
            folder = os.path.dirname(path)
            if folder:
                os.makedirs(folder, exist_ok=True)
            with open(path, "a", encoding="utf-8"):
                pass
            return path
        except OSError:
            continue

    return candidates[-1]


def _append_log(message):
    """Append a line to the launch diagnostics log."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(_resolve_log_path(), "a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] runtime_pyside6: {message}\n")
    except OSError:
        pass


def _add_dll_directory(path):
    """Best-effort DLL search path registration on Windows."""

    if not os.path.isdir(path):
        _append_log(f"skip AddDllDirectory, missing path: {path}")
        return

    try:
        os.add_dll_directory(path)
        _append_log(f"registered DLL directory: {path}")
    except (AttributeError, FileNotFoundError, OSError) as err:
        _append_log(f"failed AddDllDirectory({path}): {err}")


def _preload_dll(path):
    """Load a critical DLL explicitly so import errors are logged deterministically."""

    if not os.path.isfile(path):
        _append_log(f"skip preload, missing DLL: {path}")
        return

    try:
        ctypes.WinDLL(path)
        _append_log(f"preloaded DLL: {path}")
    except OSError as err:
        _append_log(f"failed to preload {path}: {err}")
    except Exception:
        _append_log(
            f"unexpected preload failure for {path}:\n{traceback.format_exc()}"
        )


base_dir = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
pyside_dir = os.path.join(base_dir, "PySide6")
shiboken_dir = os.path.join(base_dir, "shiboken6")
plugins_dir = os.path.join(pyside_dir, "plugins")
platforms_dir = os.path.join(plugins_dir, "platforms")

_append_log(
    "initializing hook with "
    + f"sys.executable={getattr(sys, 'executable', '')}, "
    + f"sys._MEIPASS={getattr(sys, '_MEIPASS', '')}, "
    + f"base_dir={base_dir}"
)

for candidate in (base_dir, pyside_dir, shiboken_dir, plugins_dir, platforms_dir):
    _add_dll_directory(candidate)

path_prefix = [
    candidate
    for candidate in (pyside_dir, shiboken_dir, base_dir)
    if os.path.isdir(candidate)
]
if path_prefix:
    os.environ["PATH"] = os.pathsep.join(path_prefix + [os.environ.get("PATH", "")])
    _append_log("updated PATH with packaged DLL directories")

if os.path.isdir(plugins_dir):
    os.environ["QT_PLUGIN_PATH"] = plugins_dir
    _append_log(f"QT_PLUGIN_PATH={plugins_dir}")

if os.path.isdir(platforms_dir):
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = platforms_dir
    _append_log(f"QT_QPA_PLATFORM_PLUGIN_PATH={platforms_dir}")

for dll_name in (
    "python3.dll",
    "python312.dll",
    os.path.join("PySide6", "MSVCP140.dll"),
    os.path.join("PySide6", "VCRUNTIME140.dll"),
    os.path.join("PySide6", "VCRUNTIME140_1.dll"),
    os.path.join("PySide6", "Qt6Core.dll"),
    os.path.join("PySide6", "Qt6Gui.dll"),
    os.path.join("PySide6", "Qt6Widgets.dll"),
    os.path.join("PySide6", "pyside6.abi3.dll"),
    os.path.join("PySide6", "shiboken6.abi3.dll"),
):
    _preload_dll(os.path.join(base_dir, dll_name))
