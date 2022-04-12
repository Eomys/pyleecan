from os.path import join

import numpy as np
from numpy.testing import assert_almost_equal

import pytest

from SciDataTool.Functions.Plot.plot_2D import plot_2D

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostLUT import PostLUT
from pyleecan.Classes.LUTdq import LUTdq

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.Functions.Electrical.dqh_transformation import n2dqh_DataTime
from pyleecan.Functions.Electrical.comp_MTPA import comp_MTPA

from pyleecan.definitions import DATA_DIR

from Tests import save_validation_path as save_path

is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.fixture(scope="module")
def test_ELUT():
    """Fixture to calculate ELUT and use it in all tests"""

    ELUT = test_EEC_ELUT_PMSM_calc()

    return ELUT


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.skip(reason="called by fixture and for direct call to test")
def test_EEC_ELUT_PMSM_calc(n_Id=5, n_Iq=5):
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Build OP_matrix with a meshgrid of Id/Iq
    Id_min, Id_max = -200, 200
    Iq_min, Iq_max = -200, 200
    Id, Iq = np.meshgrid(
        np.linspace(Id_min, Id_max, n_Id), np.linspace(Iq_min, Iq_max, n_Iq)
    )
    OP_matrix = np.zeros((n_Id * n_Iq, 3))
    OP_matrix[:, 0] = 1000
    OP_matrix[:, 1] = Id.ravel()
    OP_matrix[:, 2] = Iq.ravel()

    # Init and run ELUT computation
    ELUT = LUTdq()
    ELUT._set_None()
    ELUT.set_default_simulation(
        machine=Toyota_Prius,
        OP_matrix=OP_matrix,
        type_OP_matrix=1,
        name="test_EEC_ELUT_PMSM",
    )
    ELUT.simu.run()

    # Check flux linkage dqh values
    Phi_dqh_mean = ELUT.get_Phi_dqh_mean()
    OP_list = OP_matrix[:, 1:3].tolist()
    ii = OP_list.index([0, 0])
    stator_label = ELUT.simu.machine.stator.get_label()
    Phi_dqh0 = n2dqh_DataTime(
        ELUT.output_list[ii].mag.Phi_wind[stator_label],
        is_dqh_rms=True,
        phase_dir=ELUT.get_phase_dir(),
    )
    Phi_dqh0_mean = Phi_dqh0.get_along("time=mean", "phase")[Phi_dqh0.symbol]
    assert_almost_equal(Phi_dqh0_mean, Phi_dqh_mean[ii, :], decimal=15)
    assert_almost_equal(Phi_dqh0_mean[0], 0.141, decimal=3)

    if is_show_fig:
        # Plot 3-phase current function of time
        ELUT.Phi_wind[ii].plot_2D_Data("time", "phase[]", **dict_2D)
        Phi_dqh0.plot_2D_Data("time", "phase[]", **dict_2D)

    return ELUT


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
def test_EEC_ELUT_PMSM_MTPA(test_ELUT):
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine for MTPA calculation"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Maximum current [Arms]
    I_max = 250 / np.sqrt(2)
    # Maximum voltage [Vrms]
    U_max = 400
    # Speed vector
    Nspeed = 50
    N0_min = 50
    N0_max = 8000
    # Number of loads
    Ntorque = 5

    OP_matrix_MTPA, U_MTPA, I_MTPA = comp_MTPA(
        machine=Toyota_Prius,
        LUT=test_ELUT,
        Nspeed=Nspeed,
        N0_min=N0_min,
        N0_max=N0_max,
        Ntorque=Ntorque,
        I_max=I_max,
        U_max=U_max,
        n_Id=501,
        n_Iq=501,
    )

    # Check torque values
    assert_almost_equal(OP_matrix_MTPA[:, -1, 3].max(), 342, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, -1, 3].min(), 164, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, 0, 3].max(), 0, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, 0, 3].min(), 0, decimal=0)

    if is_show_fig:
        # Build legend list for each load level
        legend_list = list()
        for i_load in range(Ntorque):
            if Ntorque > 1:
                legend_list.append(
                    "Load level = "
                    + str(int(round(100 * (i_load) / (Ntorque - 1))))
                    + " %"
                )
            else:
                legend_list.append("Load level =  100%")

        # Plot torque speed curve for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 3] for i_load in range(Ntorque)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Average torque [N.m]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Id for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 1] for i_load in range(Ntorque)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Id Current [Arms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Iq for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 2] for i_load in range(Ntorque)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Iq Current [Arms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Ud for each load level
        y_list = [U_MTPA[:, i_load, 0] for i_load in range(Ntorque)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Ud Voltage [Vrms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Uq for each load level
        y_list = [U_MTPA[:, i_load, 1] for i_load in range(Ntorque)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Uq Voltage [Vrms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Id/Iq and Imax on a same graph at a specific load level
        i_load = -1
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            [I_MTPA[:, i_load, 0], I_MTPA[:, i_load, 1], I_MTPA[:, i_load, 2]],
            xlabel="Speed [rpm]",
            ylabel="Current [Arms]",
            legend_list=["Id", "Iq", "Imax"],
            is_show_fig=is_show_fig,
        )

        # Plot Ud/Uq and Umax on a same graph at a specific load level
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            [U_MTPA[:, i_load, 0], U_MTPA[:, i_load, 1], U_MTPA[:, i_load, 2]],
            xlabel="Speed [rpm]",
            ylabel="Voltage [Vrms]",
            legend_list=["Ud", "Uq", "Umax"],
            is_show_fig=is_show_fig,
        )


# To run it without pytest
if __name__ == "__main__":
    ELUT = test_EEC_ELUT_PMSM_calc(n_Id=3, n_Iq=3)
    ELUT.save("ELUT_PMSM.h5")
    # ELUT = load("ELUT_PMSM.h5")
    # test_EEC_ELUT_PMSM_MTPA(ELUT)
