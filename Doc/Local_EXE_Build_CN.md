# 本地 EXE 打包说明

## 目标

该流程用于在当前仓库本地搭建一个与官方发布流程同构的 Windows 打包环境，并生成可运行的本地发布目录。

当前仓库已经提供两个入口：

- `Exe_gen/generate_pyleecan_exe.py`
  官方发布脚本，支持从第 4 步开始在现有仓库上构建打包环境。
- `Exe_gen/build_local_exe.py`
  本地快捷入口，固定在当前仓库执行第 4-5 步：
  - 创建 `.local/envs/Exenv`
  - 安装打包依赖
  - 调用 PyInstaller 生成 GUI exe

## 与旧流程的兼容修正

历史脚本固定使用 `pyinstaller==5.1` 和 `gmsh-sdk`。这在 `Python 3.12` 环境下已经不合适：

- `PyInstaller 5.1` 不适合当前 Python 版本。
- `gmsh-sdk` 已经被主依赖里的 `gmsh` 替代。

因此本仓库当前采用以下策略：

- Python 3.12 及以上：`pyinstaller>=6.11,<7`
- Python 3.11：`pyinstaller>=5.13,<7`
- 更老版本：保持 `pyinstaller==5.1`

## 生成内容

成功执行后，主要产物为：

- `.local/envs/Exenv/`
  本地专用打包虚拟环境
- `.local/packaging/dist/Pyleecan/`
  PyInstaller 原始输出目录，可运行
- `.local/packaging/Output/Pyleecan_Portable/`
  本地便携发布目录，建议优先从这里启动
- `.local/packaging/build/`
  PyInstaller 中间目录，不可直接运行
- `.local/packaging/spec/`
  PyInstaller/安装器生成过程中使用的本地副本 spec/iss 文件

这些目录已经加入 `.gitignore`。

## 运行方式

在仓库根目录执行：

```powershell
python Exe_gen\build_local_exe.py
```

说明：

- 如果 `.local/envs/Exenv` 已存在，脚本会自动跳过环境安装，直接重建第 5 步。
- 构建完成后建议运行：

```powershell
.\.local\packaging\Output\Pyleecan_Portable\Pyleecan.exe
```

或：

```powershell
.\.local\packaging\Output\Pyleecan_Portable\Run_Pyleecan.bat
```

或直接调用官方脚本的第 4-5 步：

```python
from Exe_gen.generate_pyleecan_exe import generate_executable
generate_executable(start=4, stop=5, project_path=r"D:\Project\pyleecan")
```

## 说明

- 第 6 步安装器生成仍依赖 Inno Setup 6。
- 当前机器如果未安装 `C:\Program Files (x86)\Inno Setup 6\iscc.exe`，则只能先生成 exe，不能生成官方安装器。
- GUI exe 打包完成后，涉及 FEMM、Gmsh 等外部求解器的功能是否可运行，还取决于目标机器是否安装对应软件或二进制依赖。
- `.local\packaging\build\pyleecan\Pyleecan.exe` 是 PyInstaller 的中间文件，不要从该路径启动；若直接运行，常见现象就是 `failed to load python DLL`。
- 当前本地打包脚本已经显式携带 `PySide6`/`shiboken6` 运行库与 Qt 插件目录，包含 `shiboken6.abi3.dll`、`concrt140.dll`、`opengl32sw.dll` 和 `PySide6\plugins\platforms\qwindows.dll`。
- 如果使用的是旧版本地产物，可能会在启动时遇到 `ImportError: DLL load failed while importing QtWidgets`；删除旧的 `.local/packaging/dist/`、`.local/packaging/Output/Pyleecan_Portable/` 后按本文流程重新构建即可。
- Windows 本地构建环境当前固定使用 `PySide6==6.7.2`。`PySide6 6.11.0` 在当前 Python 3.12 + Windows 构建链上会导致 `from PySide6 import QtCore` 直接失败，因此已经在依赖文件里回退并钉死版本。
- 打包程序启动时会在 exe 同目录生成 `pyleecan_launch.log`。如需自动验证 `.local\packaging\dist\Pyleecan\Pyleecan.exe` 的 Qt 启动链，可以设置环境变量 `PYLEECAN_SMOKE_TEST=1` 后启动，程序会在完成 Qt/GUI 基础导入后自动退出。
