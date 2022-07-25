from os import cpu_count
from os.path import join

import pytest

import numpy as np

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from pyleecan.Classes.Skew import Skew

from Tests import save_plot_path as save_path


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
def test_SPMSM015_plot_contour_B_FEMM():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    simu = Simu1(name="test_plot_contour_SPMSM_015", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / np.sqrt(2)
    Phi0 = 140 * np.pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * np.exp(1j * Phi0)).real
    Iq_ref = (I0_rms * np.exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        OP=OPdq(Id_ref=Id_ref, Iq_ref=Iq_ref, N0=1000), Na_tot=252 * 9, Nt_tot=4 * 9,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=True,
        nb_worker=int(0.5 * cpu_count()),
        is_get_meshsolution=True,
        Kmesh_fineness=0.5,
    )

    out = simu.run()

    out.mag.meshsolution.plot_contour(
        is_show_fig=False, save_path=join(save_path, "plot_mesh.png")
    )
    out.mag.meshsolution.plot_contour(
        group_names="stator core",
        is_show_fig=False,
        save_path=join(save_path, "plot_mesh_stator.png"),
    )
    # out.mag.meshsolution.plot_contour(
    #     is_animated=True,
    #     group_names="stator core",
    #     is_show_fig=False,
    #     save_path=join(save_path, "plot_mesh_stator.gif"),
    # )

    pass


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
def test_Benchmark_plot_contour_B_FEMM():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    simu = Simu1(name="test_plot_contour_Benchmark", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(Id_ref=0, Iq_ref=0, N0=2504), Na_tot=2048, Nt_tot=50,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=False,
        is_periodicity_t=True,
        is_get_meshsolution=True,
        nb_worker=int(0.5 * cpu_count()),
    )

    out = simu.run()

    out.plot_B_mesh(save_path=join(save_path, "plot_B_mesh.png"))

    # out.plot_B_mesh(
    #     group_names="stator core",
    #     is_animated=True,
    #     is_show_fig=False,
    #     save_path=join(save_path, "plot_B_mesh.gif"),
    # )

    out.mag.meshsolution.plot_contour(
        group_names=["rotor magnets", "rotor core"],
        is_show_fig=False,
        save_path=join(save_path, "plot_mesh_stator.png"),
    )

    pass


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
def test_Benchmark_skew_plot_contour_B_FEMM():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    simu = Simu1(name="test_plot_contour_Benchmark", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(Id_ref=0, Iq_ref=0, N0=2504), Na_tot=2048, Nt_tot=50,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=False,
        is_periodicity_t=True,
        is_get_meshsolution=True,
        nb_worker=int(0.5 * cpu_count()),
    )

    simu.machine.rotor.skew = Skew(type_skew="linear", is_step=True, Nstep=2,)

    out = simu.run()

    out.plot_B_mesh(
        "time[2]", "indice", "z[1]", save_path=join(save_path, "plot_B_mesh.png")
    )

    # out.plot_B_mesh(
    #     group_names="stator core",
    #     is_animated=True,
    #     is_show_fig=False,
    #     save_path=join(save_path, "plot_B_mesh.gif"),
    # )

    out.mag.meshsolution.plot_contour(
        group_names=["rotor magnets", "rotor core"],
        is_show_fig=False,
        save_path=join(save_path, "plot_mesh_stator.png"),
    )

    pass


if __name__ == "__main__":
    test_SPMSM015_plot_contour_B_FEMM()
    test_Benchmark_plot_contour_B_FEMM()
    test_Benchmark_skew_plot_contour_B_FEMM()
    print("Done")
