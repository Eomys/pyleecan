from os.path import join
from time import time

import pytest
from numpy.testing import assert_allclose

from Tests import save_validation_path as save_path
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR


is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.parallel
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_set_previous():
    """test to validate set previous .ans result file in current .fem to use it as initialization
    and speed up calculation time"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_FEMM_set_previous", machine=Toyota_Prius)

    # Definition of a sinusoidal current
    simu.input = InputCurrent(
        OP=OPdq(Id_ref=-100, Iq_ref=200, N0=2000), Nt_tot=32 * 4, Na_tot=1024
    )

    # Definition of the magnetic simulation with previous ans file
    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        is_set_previous=True,
        nb_worker=4,
    )

    # Definition of the magnetic simulation without previous ans file
    simu2 = simu.copy()
    simu2.mag.is_set_previous = False

    start = time()
    out = simu.run()
    time1 = time() - start

    start = time()
    out2 = simu2.run()
    time2 = time() - start
    print(
        "Execution with set previous: {:.1f}s ||| without set previous {:.1f}".format(
            time1, time2
        )
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

    if is_show_fig:
        legend_list = ["With previous", "Without previous"]
        # Plot the result by comparing the first two simulation
        out.mag.B.plot_2D_Data(
            "angle{°}",
            "time[0]",
            data_list=[out2.mag.B],
            legend_list=legend_list,
            save_path=join(save_path, simu.name + "_B_t0.png"),
            is_show_fig=is_show_fig,
            **dict_2D
        )

        out.mag.B.plot_2D_Data(
            "angle{°}",
            "time[0]",
            data_list=[out2.mag.B],
            legend_list=legend_list,
            save_path=join(save_path, simu.name + "_B_t1.png"),
            is_show_fig=is_show_fig,
            **dict_2D
        )

        out.mag.Tem.plot_2D_Data(
            "time",
            data_list=[out2.mag.Tem],
            legend_list=legend_list,
            save_path=join(save_path, simu.name + "_Tem.png"),
            is_show_fig=is_show_fig,
            **dict_2D
        )

        out.mag.Phi_wind_stator.plot_2D_Data(
            "time",
            "phase",
            data_list=[out2.mag.Phi_wind_stator],
            legend_list=legend_list,
            save_path=join(save_path, simu.name + "_Phi_wind_stator.png"),
            is_show_fig=is_show_fig,
            **dict_2D
        )

    return out, out2


if __name__ == "__main__":
    out, out2 = test_FEMM_set_previous()
