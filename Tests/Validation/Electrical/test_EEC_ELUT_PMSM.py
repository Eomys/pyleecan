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

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.Functions.Electrical.dqh_transformation import (
    get_phase_dir_DataTime,
    n2dqh_DataTime,
)
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

    _, ELUT = test_EEC_ELUT_PMSM_calc()

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

    # Generate ELUT
    name = "test_EEC_ELUT_PMSM"
    simu = Simu1(name=name, machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputCurrent(
        Nt_tot=8 * 12,
        Na_tot=8 * 200,
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
    )

    # Build OP_matrix with a meshgrid of Id/Iq
    Id_min, Id_max = -200, 200
    Iq_min, Iq_max = -200, 200
    Id, Iq = np.meshgrid(
        np.linspace(Id_min, Id_max, n_Id), np.linspace(Iq_min, Iq_max, n_Iq)
    )
    OP_matrix = np.zeros((n_Id * n_Iq, 3))
    OP_matrix[:, 0] = simu.input.OP.N0
    OP_matrix[:, 1] = Id.ravel()
    OP_matrix[:, 2] = Iq.ravel()

    # Set varspeed simulation
    simu.var_simu = VarLoadCurrent(
        type_OP_matrix=1,
        OP_matrix=OP_matrix,
        is_keep_all_output=True,
        stop_if_error=True,
    )

    # Define second simu for FEMM comparison
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)

    # Postprocessing
    simu.var_simu.postproc_list = [PostLUT(is_save_LUT=True)]

    out = simu.run()

    ELUT = out.simu.var_simu.postproc_list[0].LUT

    # Check phase_dir calculation
    assert ELUT.get_phase_dir() == get_phase_dir_DataTime(ELUT.Phi_wind[0])

    # Check flux linkage dqh values
    Phi_dqh_mean = ELUT.get_Phidqh_mean()
    OP_list = OP_matrix[:, 1:3].tolist()
    ii = OP_list.index([0, 0])
    Phi_dqh0 = n2dqh_DataTime(
        ELUT.Phi_wind[ii],
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

    return out, ELUT


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
def test_EEC_ELUT_PMSM_MTPA(test_ELUT, n_Id=51, n_Iq=101):
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
        n_Id=n_Id,
        n_Iq=n_Iq,
    )

    # Check torque values
    assert_almost_equal(OP_matrix_MTPA[:, -1, 3].max(), 342, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, -1, 3].min(), 160, decimal=0)
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
        i_load = 0
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
    # out0, ELUT = test_EEC_ELUT_PMSM_calc()
    # ELUT.save("ELUT_PMSM.h5")
    ELUT = load("ELUT_PMSM.h5")
    test_EEC_ELUT_PMSM_MTPA(ELUT)
