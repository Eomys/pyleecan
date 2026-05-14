"""Run a lightweight LUTdq efficiency-map demonstration without external solvers."""

import argparse
import json
import sys
from pathlib import Path

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pyleecan.Classes.ElecLUTdq import ElecLUTdq
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LUT import LUT
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Functions.load import load
from pyleecan.Functions.Simulation.LUTdq import run_efficiency_map_lut
from pyleecan.definitions import DATA_DIR


class AnalyticEfficiencyLUT(LUT):
    """Small analytical dq LUT for repeatable demos and smoke tests."""

    Id_axis = np.linspace(-150.0, 25.0, 8)
    Iq_axis = np.linspace(0.0, 170.0, 9)
    Phi_mag = 0.075
    Ld = 0.00032
    Lq = 0.00056

    def __init__(self, **kwargs):
        kwargs.setdefault("simu", Simu1(loss=None))
        super().__init__(**kwargs)

    def get_OP_array(self, *_args):
        Id_grid, Iq_grid = np.meshgrid(self.Id_axis, self.Iq_axis)
        return np.column_stack(
            [
                np.full(Id_grid.size, 1000.0),
                Id_grid.ravel(),
                Iq_grid.ravel(),
            ]
        )

    def interp_Phi_dqh(self, Id, Iq):
        Id = np.asarray(Id, dtype=float)
        Iq = np.asarray(Iq, dtype=float)
        return (
            self.Phi_mag + self.Ld * Id,
            self.Lq * Iq,
            np.zeros_like(Id),
        )

    def get_Phi_dqh_mag_mean(self):
        return np.array([self.Phi_mag, 0.0, 0.0])

    def interp_Tem_rip_dqh(self, Id, Iq):
        return None


def positive_int(value):
    value = int(value)
    if value < 2:
        raise argparse.ArgumentTypeError("value must be at least 2")
    return value


def finite_or_none(value):
    value = float(value)
    return value if np.isfinite(value) else None


def build_demo_simulation():
    machine = load(str(Path(DATA_DIR) / "Machine" / "Toyota_Prius.json"))
    return Simu1(
        name="demo_lutdq_efficiency_map",
        machine=machine,
        input=InputCurrent(
            OP=OPdq(N0=1000.0, Id_ref=0.0, Iq_ref=0.0),
            Nt_tot=16,
            Nrev=1,
        ),
        elec=ElecLUTdq(
            LUT_enforced=AnalyticEfficiencyLUT(),
            Urms_max=230.0,
            Irms_max=170.0,
            n_Id=8,
            n_Iq=9,
            n_interp=72,
            type_skin_effect=0,
        ),
        var_simu=VarLoadCurrent(is_keep_all_output=True),
    )


def run_demo(args):
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = PROJECT_ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    simu = build_demo_simulation()
    speed = np.linspace(500.0, 6000.0, args.speed_count)
    load_vect = np.linspace(0.25, 1.0, args.load_count)

    result = run_efficiency_map_lut(
        simu,
        speed_vect=speed,
        load_vect=load_vect,
        cache_path=str(output_dir / args.file_prefix),
        plot_dir=None if args.no_plot else str(output_dir),
        file_prefix=args.file_prefix,
        is_show_fig=args.show_fig,
    )

    summary_path = output_dir / "summary.json"
    summary = {
        "speed_count": int(speed.size),
        "load_count": int(load_vect.size),
        "max_torque_Nm": finite_or_none(np.nanmax(result["Tem_max"])),
        "max_efficiency": finite_or_none(np.nanmax(result["efficiency"])),
        "base_speed_rpm": finite_or_none(result["base_speed_rpm"]),
        "cache_paths": result["cache_paths"],
        "plot_paths": result.get("plot_paths", {}),
    }
    with open(summary_path, "w", encoding="utf-8") as summary_file:
        json.dump(summary, summary_file, indent=2, sort_keys=True)

    print("LUTdq efficiency-map demo complete")
    print(f"Output directory: {output_dir}")
    print(f"Cache NPZ: {result['cache_paths']['npz_path']}")
    print(f"Summary JSON: {summary_path}")
    print(f"Max efficiency: {summary['max_efficiency']:.4f}")
    if summary["base_speed_rpm"] is not None:
        print(f"Base speed: {summary['base_speed_rpm']:.1f} rpm")

    return summary


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate a lightweight LUTdq efficiency-map demo."
    )
    parser.add_argument(
        "--output-dir",
        default=".local/lutdq_demo",
        help="Directory for generated cache, plots and summary.",
    )
    parser.add_argument("--speed-count", type=positive_int, default=8)
    parser.add_argument("--load-count", type=positive_int, default=5)
    parser.add_argument("--file-prefix", default="lutdq_demo")
    parser.add_argument("--no-plot", action="store_true")
    parser.add_argument("--show-fig", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    run_demo(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
