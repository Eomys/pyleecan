from os.path import join
from time import time

import pytest
from numpy import array, pi
from numpy.testing import assert_allclose

from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from Tests import save_validation_path as save_path


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.parallel
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_parallelization_mag():
    """test parallelization of FEMM to get B, Tem, PhiWind"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_FEMM_parallelization_mag", machine=Toyota_Prius)

    # Definition of a sinusoidal current
    simu.input = InputCurrent()
    simu.input.OP = OPdq(Id_ref=-100, Iq_ref=200, N0=2000)
    simu.input.Nt_tot = 16  # Number of time step
    simu.input.Na_tot = 1024  # Spatial discretization

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
        is_periodicity_t=True,
    )
    simu2 = simu.copy()
    simu2.mag.nb_worker = 2

    # simlation with Nt_tot < nb_worker
    simu3 = simu.copy()
    simu3.mag.nb_worker = 8
    simu3.input.Nt_tot = 4

    start = time()
    out = simu.run()
    time1 = time() - start

    start = time()
    out2 = simu2.run()
    time2 = time() - start
    print(
        "Execution with one worker: {:.1f}s ||| {:d} workers {:.1f}".format(
            time1, simu2.mag.nb_worker, time2
        )
    )
    simu3.run()

    # Plot the result by comparing the first two simulation
    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Serial", "Parallelization"],
        save_path=join(save_path, simu.name + "_B_t0.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Serial", "Parallelization"],
        save_path=join(save_path, simu.name + "_B_t1.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Tem.plot_2D_Data(
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Phi_wind_stator.plot_2D_Data(
        "time",
        "phase[]",
        data_list=[out2.mag.Phi_wind_stator],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Phi_wind_stator.png"),
        is_show_fig=False,
        **dict_2D
    )

    assert_allclose(
        out.mag.B.components["tangential"].values,
        out2.mag.B.components["tangential"].values,
        rtol=1e-5,
        atol=1e-6,
    )

    assert_allclose(
        out.mag.B.components["radial"].values,
        out2.mag.B.components["radial"].values,
        rtol=1e-5,
        atol=1e-5,
    )

    assert_allclose(out.mag.Tem.values, out2.mag.Tem.values, rtol=1e-5, atol=1e-5)

    return out, out2


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.parallel
@pytest.mark.MeshSol
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_parallelization_meshsolution():
    """test parallelization of FEMM to get meshsolution"""

    SPMSM_003 = load(join(DATA_DIR, "Machine", "SPMSM_003.json"))
    simu = Simu1(name="test_FEMM_parallelization_meshsolution", machine=SPMSM_003)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(
        value=array(
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    time = ImportGenVectLin(start=0, stop=0.015, num=4, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        time=time,
        angle=angle,
        angle_rotor_initial=0.5216 + pi,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_get_meshsolution=True,
        nb_worker=1,
    )
    simu.force = None
    simu.struct = None
    simu2 = simu.copy()
    simu2.mag.nb_worker = 3
    simu2.name += "_parallel"

    out = simu.run()
    out2 = simu2.run()

    # %%
    # Plots solution computed without parallelization
    out.mag.meshsolution.plot_mesh(
        save_path=join(save_path, simu.name + "_mesh_not_parallel.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group("stator core").plot_mesh(
        save_path=join(save_path, simu.name + "_mesh_stator_not_parallel.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.get_group(
        ["stator core", "/", "airgap", "stator winding"]
    ).plot_mesh(
        save_path=join(
            save_path,
            simu.name + "_mesh_stator_interface_not_parallel.png",
        ),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_path, simu.name + "_mu_not_parallel.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_path, simu.name + "_B_not_parallel.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_path, simu.name + "_H_not_parallel.png"),
        is_show_fig=False,
    )

    # %%
    # Plots solution computed with parallelization
    out2.mag.meshsolution.plot_mesh(
        save_path=join(save_path, simu.name + "_mesh_parallel.png"), is_show_fig=False
    )

    out2.mag.meshsolution.get_group("stator core").plot_mesh(
        save_path=join(save_path, simu.name + "_mesh_stator_parallel.png"),
        is_show_fig=False,
    )

    out2.mag.meshsolution.get_group(
        ["stator core", "/", "airgap", "stator winding"]
    ).plot_mesh(
        save_path=join(
            save_path,
            simu.name + "_mesh_stator_interface_parallel.png",
        ),
        is_show_fig=False,
    )

    out2.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_path, simu.name + "_mu_parallel.png"),
        is_show_fig=False,
    )
    out2.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_path, simu.name + "_B_parallel.png"),
        is_show_fig=False,
    )
    out2.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_path, simu.name + "_H_parallel.png"),
        is_show_fig=False,
    )

    return out, out2


if __name__ == "__main__":
    out, out2 = test_FEMM_parallelization_mag()
    # out3, out4 = test_FEMM_parallelization_meshsolution()
