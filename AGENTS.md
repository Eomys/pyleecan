# Repository Guidelines

## Project Structure & Module Organization
`pyleecan/` is the main package. Keep data models and generated objects in `pyleecan/Classes/`, domain logic in `pyleecan/Methods/`, shared utilities in `pyleecan/Functions/`, packaged assets in `pyleecan/Data/`, and the PySide6 desktop interface in `pyleecan/GUI/`. `pyleecan/Generator/` contains code and UML generation helpers. Tests live under `Tests/` and largely mirror the package layout, with extra integration areas such as `Validation/`, `Simulation/`, and `Tutorials/`. User notebooks are stored in `Tutorials/`; repo documentation and architecture notes live in `Doc/`; Windows packaging files live in `Exe_gen/`.

## Build, Test, and Development Commands
Use an editable install for development:

`python -m pip install -e ".[test]"` installs the package with pytest dependencies.

`pytest Tests` runs the full suite.

`pytest -m star Tests` runs the pre-PR smoke subset defined in `pytest.ini`.

`tox run -e 3.12` runs tests in a managed tox environment.

`tox run -e black` formats `pyleecan/` with Black.

`python -m pyleecan` launches the GUI locally.

`python Exe_gen\build_local_exe.py` builds the Windows PyInstaller package used for local EXE delivery.

`.local\packaging\dist\Pyleecan\Pyleecan.exe` is the rebuilt one-folder EXE output used for startup diagnostics, while `.local\packaging\Output\Pyleecan_Portable\Pyleecan.exe` is the staged portable release copy. The local packaging virtual environment now lives at `.local\envs\Exenv\`.

If you touch UML or diagram generation, install Node dependencies with `npm install` to get Mermaid CLI support.

For Windows EXE work, do not run `.local\packaging\build\pyleecan\Pyleecan.exe`; it is only an intermediate PyInstaller artifact and commonly fails with `failed to load python DLL`.

## Coding Style & Naming Conventions
Use 4-space indentation and Black formatting. The repo has a minimal `.pre-commit-config.yaml`, so run `pre-commit run --all-files` or at least `tox run -e black` before submitting. Follow existing naming patterns: `CamelCase` for classes and many files in `pyleecan/Classes/`, `snake_case` for functions, modules, and tests such as `test_gmsh.py`. Put new logic in the matching domain folder and mirror new coverage under `Tests/<Domain>/...`.

## Testing Guidelines
Tests use `pytest` plus markers declared in `pytest.ini` for domains and runtime cost, for example `@pytest.mark.GMSH`, `@pytest.mark.long_5s`, and `@pytest.mark.star`. Name tests `test_*.py` and keep them close to the code they exercise. Many tests depend on optional tools like PySide6, GMSH, FEMM, or `swat-em`; skip or scope runs accordingly when those dependencies are unavailable. No repo-wide coverage threshold is configured, so prioritize targeted regression tests for every behavior change.

For packaged GUI changes on Windows, run at least one startup smoke check. Set `PYLEECAN_SMOKE_TEST=1` before launching `.local\packaging\dist\Pyleecan\Pyleecan.exe`; the application should initialize Qt and exit cleanly. Startup diagnostics are written to `pyleecan_launch.log` next to the launched exe.

The local Windows build chain is currently pinned to `PySide6==6.7.2`. Do not casually upgrade that dependency without rebuilding the EXE and revalidating Qt startup, because `PySide6 6.11.0` has already failed in this repository's Python 3.12 packaging environment.

## Commit & Pull Request Guidelines
Recent history favors short, imperative subjects, sometimes with prefixes such as `[BF]`, `[CC]`, and `[WP]`. Match that style: one focused change per commit, concise summary line, and a body when dependency or compatibility context matters. Pull requests should explain the motivation, list affected modules, note the exact test commands run, and link the relevant issue or discussion. Include screenshots for GUI changes and call out any solver-specific setup needed for reviewers.

Do not commit `.local/` packaging or virtual-environment artifacts unless the task explicitly requires shipping generated binaries. Commit source changes, dependency pins, and packaging scripts instead.
