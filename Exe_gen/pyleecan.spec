# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_dynamic_libs

sys.setrecursionlimit(3000)
block_cipher = None

PROJECT_ROOT = os.environ.get("PYLEECAN_PROJECT_ROOT", SPECPATH)
PACKAGING_ENV = os.environ.get(
    "PYLEECAN_PACKAGING_ENV",
    os.path.join(PROJECT_ROOT, ".local", "envs", "Exenv"),
)
site_packages = os.path.join(PACKAGING_ENV, "Lib", "site-packages")
data_candidates = [
    (os.path.join(site_packages, "pyvista"), ".\\pyvista"),
    (os.path.join(site_packages, "scipy"), ".\\scipy"),
    (os.path.join(site_packages, "scipy.libs"), ".\\scipy.libs"),
    (os.path.join(site_packages, "matplotlib"), ".\\matplotlib"),
    (os.path.join(site_packages, "vtkmodules"), ".\\vtkmodules"),
    (os.path.join(site_packages, "pyzmq.libs"), ".\\pyzmq.libs"),
    (os.path.join(site_packages, "PySide6", "plugins"), ".\\PySide6\\plugins"),
    (
        os.path.join(site_packages, "PySide6", "translations"),
        ".\\PySide6\\translations",
    ),
    (os.path.join(site_packages, "PySide6", "resources"), ".\\PySide6\\resources"),
    (os.path.join(PROJECT_ROOT, "pyleecan", "Data"), ".\\pyleecan\\Data"),
    (
        os.path.join(PROJECT_ROOT, "pyleecan", "Classes", "Class_Dict.json"),
        ".\\Pyleecan\\Classes",
    ),
]
datas = [(src, dest) for src, dest in data_candidates if os.path.exists(src)]
binaries = []
binary_candidates = []
binary_candidates.extend(collect_dynamic_libs("PySide6", destdir="PySide6"))
binary_candidates.extend(collect_dynamic_libs("shiboken6", destdir="PySide6"))

seen_binaries = set()
for src, dest in binary_candidates:
    if not os.path.exists(src):
        continue
    key = (os.path.normcase(os.path.basename(src)), os.path.normcase(dest))
    if key in seen_binaries:
        continue
    binaries.append((src, dest))
    seen_binaries.add(key)

a = Analysis(
    [os.path.join(PROJECT_ROOT, "pyleecan", "run_GUI.py")],
    pathex=[PROJECT_ROOT],
    binaries=binaries,
    datas=datas,
    hiddenimports=[  # Leave first line empty for Import of pyd
        "pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup",
        "pyleecan.GUI.Dialog.DMatLib.DMatLib",
        "pyleecan.GUI.Tools.SidebarWindow",
        "pyleecan.GUI.Tools.MachinePlotWidget",
        "pyleecan.Functions.GMSH.draw_GMSH",
        "pyleecan.GUI.Tools.WTreeEdit.WTreeEdit",
        "pyleecan.GUI.Tools.GuiOption.WGuiOption",
    ],
    hookspath=[],
    runtime_hooks=[os.path.join(PROJECT_ROOT, "Exe_gen", "runtime_pyside6.py")],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Pyleecan",
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=os.path.join(PROJECT_ROOT, "Exe_gen", "pyleecan_64.ico"),
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Pyleecan",
)
