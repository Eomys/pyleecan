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


CASE_NAME = "leaf2012"
MACHINE_PATH = (
    REPO_ROOT / "SimulationModels" / "Nissan_Leaf_2012" / "Nissan_Leaf_2012_DXF.json"
)
BASELINE_SUMMARY_PATH = (
    REPO_ROOT / ".local" / "verification" / "leaf_full_validation" / "summary.json"
)
BASELINE_NPZ_PATH = (
    REPO_ROOT
    / ".local"
    / "verification"
    / "leaf_full_validation"
    / "results"
    / "efficiency_map"
    / "leaf2012_efficiency_map.npz"
)
OUTPUT_ROOT = REPO_ROOT / ".local" / "verification" / "elmer_leaf2012"
REPORT_PATH = OUTPUT_ROOT / "report.md"
DEFAULT_NT_TOT = 48
DEFAULT_NA_TOT = 720
DEFAULT_KMESH_FINENESS = 1.0

POINT_REQUEST_LIST = [
    ElmerPointRequest("static_3000_full_load", 3000.0, screenshot=True),
    ElmerPointRequest("fw_7000_full_load", 7000.0),
    ElmerPointRequest("mtpv_9000_full_load", 9000.0),
]


def build_report(summary, baseline_summary):
    point_rows = build_point_rows(summary["points"])
    public_reference = baseline_summary["public_reference"]
    static_public = baseline_summary["comparison"]["static_3000rpm_point"]
    first_point = summary["points"][0]
    screenshot_path = first_point["artifacts"].get("screenshot")
    screenshot_error = first_point["artifacts"].get("screenshot_error")

    sections = [
        "# Nissan LEAF 2012 Elmer Validation",
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
        "## 2. Published LEAF Reference",
        "",
        f"- Public envelope values reused from the local LEAF report: peak power {format_metric(public_reference['peak_power_kW'])} kW, peak torque {format_metric(public_reference['peak_torque_Nm'])} N.m, max speed {format_metric(public_reference['max_speed_rpm'], '{:.0f}')} rpm.",
        f"- 3000 rpm public operating point: {format_metric(static_public['reference_power_kW'])} kW / {format_metric(static_public['reference_torque_Nm'])} N.m.",
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
        "- Each validation point first replays the selected full-load `Id/Iq` seed with a direct FEMM static solve; that replay is the torque/power baseline used in the table above.",
        "- The 3000 rpm point is used both as the mesh-generation reference and as the public operating point comparison.",
        "- The 7000 rpm and 9000 rpm points reuse the first point's `.msh`, so the Elmer validation also exercises the repaired mesh-reuse path on FW and MTPV conditions.",
        "- Public benchmark values are taken from the repository's existing LEAF full-validation summary and its ORNL/DOE source list.",
        "",
    ]
    return "\n".join(sections)


def main():
    parser = argparse.ArgumentParser(
        description="Run Nissan LEAF 2012 Elmer validation against local FEMM baselines"
    )
    parser.add_argument("--open-paraview", action="store_true")
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

    summary, baseline_summary = run_elmer_validation_case(
        case_name=CASE_NAME,
        machine_path=MACHINE_PATH,
        baseline_summary_path=BASELINE_SUMMARY_PATH,
        baseline_npz_path=BASELINE_NPZ_PATH,
        output_root=OUTPUT_ROOT,
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
