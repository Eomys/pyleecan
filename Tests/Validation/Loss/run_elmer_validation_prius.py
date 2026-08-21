from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Tests.Validation.Loss.elmer_validation_common import (
    ElmerPointRequest,
    build_point_rows,
    format_metric,
    format_percent,
    markdown_table,
    relative_to_repo,
    run_elmer_validation_case,
)
from Tests.Validation.Loss.prius_validation_preflight import (
    PriusValidationPreflightError,
    known_elmer_executable_paths,
    require_existing_files,
    require_executables,
    require_python_modules,
)


CASE_NAME = "prius2004"
MACHINE_PATH = (
    REPO_ROOT / "SimulationModels" / "Toyota_Prius_2004" / "IPMSM_Toyota_Prius_2004.json"
)
BASELINE_SUMMARY_PATH = (
    REPO_ROOT / ".local" / "verification" / "prius2004_full_validation" / "summary.json"
)
BASELINE_NPZ_PATH = (
    REPO_ROOT
    / ".local"
    / "verification"
    / "prius2004_full_validation"
    / "results"
    / "efficiency_map"
    / "prius2004_loss_efficiency_map.npz"
)
OUTPUT_ROOT = REPO_ROOT / ".local" / "verification" / "elmer_prius2004"
REPORT_PATH = OUTPUT_ROOT / "report.md"
DEFAULT_NT_TOT = 48
DEFAULT_NA_TOT = 720
DEFAULT_KMESH_FINENESS = 1.0

POINT_REQUEST_LIST = [
    ElmerPointRequest("static_1200_full_load", 1200.0, screenshot=True),
    ElmerPointRequest("fw_2000_full_load", 2000.0),
    ElmerPointRequest("mtpv_4500_full_load", 4500.0),
]


def require_prius_baseline_inputs(baseline_summary_path, baseline_npz_path):
    """Check the local Prius FEMM/LUT baseline files before launching solvers."""

    require_existing_files(
        required_files={
            "Prius FEMM baseline summary": baseline_summary_path,
            "Prius efficiency-map NPZ": baseline_npz_path,
        },
        purpose="Toyota Prius 2004 Elmer validation",
        repo_root=REPO_ROOT,
        recovery_steps=[
            "Generate a Prius efficiency-map cache with Tests\\Validation\\Loss\\run_prius_efficiency_map.py, or restore the previous .local\\verification\\prius2004_full_validation artifacts.",
            "Pass --baseline-summary-path and --baseline-npz-path if the cache is stored outside the default .local location.",
            "Use --check-inputs to verify local artifacts before starting FEMM/Elmer.",
        ],
    )


def require_prius_elmer_runtime(check_solvers=True):
    """Check Python and external solver dependencies for Prius Elmer replay."""

    require_python_modules(
        module_names=["gmsh", "femm"],
        purpose="Toyota Prius 2004 Elmer validation",
        recovery_steps=[
            "Run python -m pip install -e \".[test]\" or use the prepared .local\\envs\\Exenv interpreter.",
        ],
    )
    if not check_solvers:
        return

    require_executables(
        requirements=[
            (
                "FEMM executable",
                ["femm"],
                [
                    Path("C:/femm42/bin/femm.exe"),
                    Path("C:/Program Files/femm42/bin/femm.exe"),
                    Path("C:/Program Files (x86)/femm42/bin/femm.exe"),
                ],
            ),
            (
                "ElmerGrid executable",
                ["ElmerGrid"],
                known_elmer_executable_paths("ElmerGrid.exe"),
            ),
            (
                "ElmerSolver executable",
                ["ElmerSolver"],
                known_elmer_executable_paths("ElmerSolver.exe"),
            ),
        ],
        purpose="Toyota Prius 2004 Elmer validation",
        recovery_steps=[
            "Install Elmer and FEMM, or add their bin directories to PATH before running the replay.",
            "On Windows, FEMM is commonly installed at C:\\femm42\\bin and Elmer under C:\\Program Files\\Elmer*\\bin.",
        ],
    )


def build_report(summary, baseline_summary):
    point_rows = build_point_rows(summary["points"])
    static_public = baseline_summary["comparison"]["static_vs_published"]
    first_point = summary["points"][0]
    screenshot_path = first_point["artifacts"].get("screenshot")
    screenshot_error = first_point["artifacts"].get("screenshot_error")

    sections = [
        "# Toyota Prius 2004 Elmer Validation",
        "",
        f"- Generated at (UTC): `{summary['generated_at_utc']}`",
        f"- Machine file: `{summary['machine_file']}`",
        f"- FEMM baseline summary: `{relative_to_repo(summary['baseline_summary_file'])}`",
        f"- FEMM baseline NPZ: `{relative_to_repo(summary['baseline_npz_file'])}`",
        f"- Result root: `{relative_to_repo(summary['output_root'])}`",
        f"- Elmer settings: `Nt_tot={summary['settings']['nt_tot']}`, `Na_tot={summary['settings']['na_tot']}`, `Kmesh={summary['settings']['kmesh_fineness']}`",
        f"- Reused mesh: `{relative_to_repo(summary['reused_reference_msh'])}`",
        "",
        "## 1. Elmer vs FEMM Points",
        "",
        markdown_table(
            [
                "Point",
                "Speed [rpm]",
                "Region",
                "FEMM T [Nm]",
                "Elmer T [Nm]",
                "Torque Delta",
                "FEMM P [kW]",
                "Elmer P [kW]",
                "Power Delta",
                "FEMM I [A]",
                "Elmer I [A]",
                "FEMM U [V]",
                "Elmer U [V]",
            ],
            point_rows,
        ),
        "",
        "## 2. Published Static Reference",
        "",
        f"- Local public reference copied from the existing FEMM validation: {format_metric(static_public['reference_power_kW'])} kW / {format_metric(static_public['reference_torque_Nm'])} N.m at 1200 rpm.",
        f"- FEMM point used here: {format_metric(first_point['femm_baseline']['P_out_W'] * 1e-3)} kW / {format_metric(first_point['femm_baseline']['Tem_av_Nm'])} N.m.",
        f"- Elmer point measured here: {format_metric(first_point['elmer']['P_out_W'] * 1e-3)} kW / {format_metric(first_point['elmer']['Tem_av_Nm'])} N.m.",
        f"- Elmer vs published delta: power {format_percent((first_point['elmer']['P_out_W'] * 1e-3 - static_public['reference_power_kW']) / static_public['reference_power_kW'] * 100.0)}, torque {format_percent((first_point['elmer']['Tem_av_Nm'] - static_public['reference_torque_Nm']) / static_public['reference_torque_Nm'] * 100.0)}.",
        "",
        "## 3. ParaView Artifact",
        "",
        f"- Screenshot: `{relative_to_repo(screenshot_path)}`" if screenshot_path else "- Screenshot: `n/a`",
        f"- Screenshot error: `{screenshot_error}`" if screenshot_error else "- Screenshot error: none",
        "",
        "## 4. Notes",
        "",
        "- The first operating point builds the Gmsh mesh and runs ElmerGrid normally.",
        "- The later two points reuse the first point's `.msh` through `MagElmer.import_file`, which exercises the repaired Elmer reuse path.",
        "- Public benchmark values are taken from the repository's existing Prius FEMM validation summary and its ORNL-based report.",
        "",
    ]
    return "\n".join(sections)


def main():
    parser = argparse.ArgumentParser(
        description="Run Toyota Prius 2004 Elmer validation against local FEMM baselines"
    )
    parser.add_argument("--open-paraview", action="store_true")
    parser.add_argument(
        "--baseline-summary-path",
        type=Path,
        default=BASELINE_SUMMARY_PATH,
        help="Path to the Prius full-validation summary JSON.",
    )
    parser.add_argument(
        "--baseline-npz-path",
        type=Path,
        default=BASELINE_NPZ_PATH,
        help="Path to the Prius efficiency-map NPZ used to seed replay points.",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=OUTPUT_ROOT,
        help="Directory where Elmer replay outputs are written.",
    )
    parser.add_argument(
        "--check-inputs",
        action="store_true",
        help="Validate local artifacts and solver availability, then exit.",
    )
    parser.add_argument(
        "--skip-solver-check",
        action="store_true",
        help="Skip external executable discovery before launching the replay.",
    )
    parser.add_argument(
        "--nt-tot",
        type=int,
        default=DEFAULT_NT_TOT,
        help="Transient time-step count. Defaults to the 48-step release baseline.",
    )
    parser.add_argument("--na-tot", type=int, default=DEFAULT_NA_TOT)
    parser.add_argument(
        "--kmesh-fineness", type=float, default=DEFAULT_KMESH_FINENESS
    )
    args = parser.parse_args()

    try:
        require_prius_baseline_inputs(args.baseline_summary_path, args.baseline_npz_path)
        require_prius_elmer_runtime(check_solvers=not args.skip_solver_check)
    except PriusValidationPreflightError as error:
        parser.exit(2, str(error) + "\n")

    if args.check_inputs:
        print("Prius Elmer validation inputs are available.")
        return

    summary, baseline_summary = run_elmer_validation_case(
        case_name=CASE_NAME,
        machine_path=MACHINE_PATH,
        baseline_summary_path=args.baseline_summary_path,
        baseline_npz_path=args.baseline_npz_path,
        output_root=args.output_root,
        point_request_list=POINT_REQUEST_LIST,
        nt_tot=args.nt_tot,
        na_tot=args.na_tot,
        kmesh_fineness=args.kmesh_fineness,
        open_paraview_gui=args.open_paraview,
    )

    REPORT_PATH.write_text(build_report(summary, baseline_summary), encoding="utf-8")
    print(f"Wrote summary to {OUTPUT_ROOT / 'summary.json'}")
    print(f"Wrote report to {REPORT_PATH}")


if __name__ == "__main__":
    main()
