# Elmer and ParaView Validation Workflow

## Update on April 18, 2026

The "Validation Snapshot" section later in this file describes the first end-to-end wiring checkpoint only. Its near-zero torque numbers are now obsolete and must not be used as the current Elmer accuracy baseline.

Current local status as of April 19, 2026:

- ParaView GUI launch and batch screenshot rendering both work on the local Windows installation.
- All new default magnetic simulations now request `8` workers by default (`MagFEMM`, `MagElmer`, validation runners, and LUT default simulations).
- FEMM follows that default worker count.
- The local Windows `Elmer 26.1-Release` build still logs `Running with just one thread per task` even when `OMP_NUM_THREADS=8` is injected, so true Elmer multithreading is not yet confirmed on this machine.
- Nissan LEAF 2012 Elmer validation is now in a usable range against direct FEMM replay:
  - 3000 rpm: `+1.23%`
  - 7000 rpm: `-3.56%`
  - 9000 rpm: `-0.90%`
- Toyota Prius 2004 now has one revalidated explicit-circuit reference point against direct FEMM replay:
  - point: `static_1200_full_load` at `1200 rpm`
  - direct FEMM replay: `474.7511976029111 Nm`
  - corrected Elmer explicit circuit: `472.69344949105835 Nm`
  - torque delta: `-0.43%`
  - the exact Prius checklist is documented in [Prius_Elmer_Explicit_Circuit_CN.md](./Prius_Elmer_Explicit_Circuit_CN.md)

For the current Leaf-focused Elmer optimization notes, use [Elmer_Simulation_Optimization_CN.md](./Elmer_Simulation_Optimization_CN.md) as the authoritative summary. For the Prius explicit-circuit configuration that currently matches FEMM, use [Prius_Elmer_Explicit_Circuit_CN.md](./Prius_Elmer_Explicit_Circuit_CN.md).

This repository now includes a complete local Elmer magnetic-solver path plus ParaView post-processing helpers for Windows installations where Elmer or ParaView are not on `PATH`.

## Binary Resolution

`pyleecan/Functions/get_path_binary.py` now resolves executables in this order:

1. Explicit file or directory path.
2. Environment overrides such as `PYLEECAN_ELMERSOLVER`, `PYLEECAN_ELMERGRID`, `PYLEECAN_PARAVIEW`, `PYLEECAN_PVPYTHON`, and `PYLEECAN_PVBATCH`.
3. Normal `PATH` lookup.
4. Standard Windows install folders such as `C:\Program Files\Elmer*\bin`, `C:\Program Files\ParaView*\bin`, `D:\Software\Elmer*\bin`, and `D:\Software\ParaView*\bin`.

This is required for the current local setup where Elmer and ParaView may be installed under `D:\Software\...` instead of `PATH` or `Program Files`.

## ParaView Helpers

The new helpers live under `pyleecan/Functions/ParaView/`:

- `resolve_result_file`: resolve a VTU/VTK file or the latest timestep inside a result directory.
- `render_vtu_screenshot`: run `pvpython` or `pvbatch` and save a screenshot from an Elmer result.
- `launch_paraview`: open the ParaView GUI on the resolved result file.
- `build_paraview_render_script`: generate the batch script used by `pvpython` / `pvbatch`.

If `array_name` is omitted or set to `None`, the renderer now auto-selects a usable array and prefers magnetic-flux-density-like fields when they exist.

## Elmer Mesh Reuse

`MagElmer.import_file` is now wired all the way into `ElmerGrid`:

- `comp_flux_airgap.py` skips Gmsh redraw when `import_file` is provided.
- `gen_elmer_mesh.py` now consumes the imported `.msh` file or a directory containing it.
- `gen_elmer_mesh.py` also runs `ElmerGrid` from the real save directory instead of the not-yet-created output folder.
- `VarSimu.set_reused_data` now reuses a reference Elmer `.msh` in the same way it already reused FEMM reference files.

This means the first Elmer run can generate the mesh and later operating points can reuse it without redrawing or remeshing the machine.

## Validation Runners

Tracked runners are available under `Tests/Validation/Loss/`:

- `run_prius_efficiency_map.py`
- `run_elmer_validation_prius.py`
- `run_elmer_validation_leaf.py`

The Prius efficiency-map runner generates the local LUT cache used to seed full-load replay points under `.local/verification/prius2004_full_validation/`. The Elmer runners:

1. Load the tracked Prius or Leaf machine model from `SimulationModels/`.
2. Read the existing local FEMM baseline summaries and NPZ maps from `.local/verification/...`.
3. Pick representative full-load operating points.
4. Run Elmer on those points.
5. Reuse the first point's `.msh` for later points.
6. Save a ParaView screenshot from the reference Elmer run.
7. Write `.local/verification/elmer_<case>/summary.json`, `point_comparison.csv`, and `report.md`.

Example commands:

```powershell
python Tests\Validation\Loss\run_prius_efficiency_map.py --check-inputs
python Tests\Validation\Loss\run_prius_efficiency_map.py
python Tests\Validation\Loss\run_elmer_validation_prius.py
python Tests\Validation\Loss\run_elmer_validation_leaf.py
```

Optional tuning:

```powershell
python Tests\Validation\Loss\run_elmer_validation_prius.py --nt-tot 12 --na-tot 720 --kmesh-fineness 1.0
python Tests\Validation\Loss\run_elmer_validation_leaf.py --open-paraview
```

The current validation scripts assume the existing local FEMM baselines remain available under `.local/verification/`. Those artifacts are intentionally not tracked in git. If a baseline has been deleted or moved, run the Prius efficiency-map runner first or pass explicit `--baseline-summary-path` and `--baseline-npz-path` values to `run_elmer_validation_prius.py`.

`run_elmer_validation_prius.py --check-inputs` also checks the optional Python modules and external FEMM/Elmer executables before launching long solver work. Use `--skip-solver-check` only when a non-standard solver launcher is configured and the automatic discovery is known to be too strict.

For non-standard Elmer installs, set `ELMER_HOME` to the installation root before running the validation, for example:

```powershell
$env:ELMER_HOME = "D:\Software\Elmer 26.1-Release"
```

## Initial Integration Snapshot (Obsolete)

The workflow above was exercised locally on April 16, 2026 with:

- ParaView `6.1.0` from `C:\Program Files\ParaView 6.1.0`
- Elmer `26.1-Release` from `C:\Program Files\Elmer 26.1-Release`
- `Nt_tot=16`, `Na_tot=720`, `Kmesh=1.0`

Generated reports:

- Prius: `.local\verification\elmer_prius2004\report.md`
- LEAF: `.local\verification\elmer_leaf2012\report.md`

Summary of the measured Elmer vs existing FEMM baselines:

| Case | Reference point | FEMM torque [Nm] | Elmer torque [Nm] | Torque delta | FEMM power [kW] | Elmer power [kW] | Power delta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Prius 2004 | 1200 rpm full load | 432.414 | 24.512 | -94.33% | 59.941 | 3.080 | -94.86% |
| LEAF 2012 | 3000 rpm full load | 374.571 | 0.997 | -99.73% | 125.150 | 0.313 | -99.75% |

The later Prius and LEAF operating points also completed successfully while reusing the first point's `.msh`, which confirms the repaired `MagElmer.import_file` and `VarSimu.set_reused_data` path works in practice.

ParaView screenshot generation also completed successfully for the first point of each case through `pvpython`. ParaView emitted a settings-directory warning under `%APPDATA%\ParaView`, but the batch render still returned exit code `0` and produced the requested screenshots.

## Current Limitations

The local validation proves that:

- binary discovery works for Elmer and ParaView even when they are only installed under `Program Files`,
- ElmerGrid conversion and ElmerSolver execution are wired into Pyleecan,
- Elmer result recovery, ParaView screenshot generation, and `.msh` reuse across operating points all work end to end.

It also shows that:

- the original April 16 wiring snapshot below is obsolete and must not be used as a current accuracy baseline,
- LEAF now has a usable direct-FEMM comparison workflow,
- Prius now has one revalidated explicit-circuit reference point at `1200 rpm`; that point should follow the dedicated checklist in `Doc/Prius_Elmer_Explicit_Circuit_CN.md`,
- generalized Prius multi-point reruns are still separate work and should not be inferred from the single revalidated point above.

The dominant remaining gaps are:

- Elmer `scalars.dat` currently exposes torque and losses, but not the winding flux-linkage or winding-voltage columns needed for a voltage comparison.
- Elmer `U_rms` recovery is still incomplete because `scalars.dat / VTU` winding-voltage reconstruction is not yet consistently available.
- Prius has only been revalidated at the documented `1200 rpm` explicit-circuit point; the rest of the Prius operating range should be treated as unverified until rerun under the corrected configuration.
