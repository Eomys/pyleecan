from os.path import join

import numpy as np
from numpy.testing import assert_almost_equal

import pytest

from SciDataTool.Functions.Plot.plot_2D import plot_2D
from SciDataTool.Functions.Plot.plot_3D import plot_3D

from pyleecan.Classes.ElecLUTdq import ElecLUTdq

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostLUT import PostLUT

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.skip(reason="Work in progress")
def test_ElecLUTdq_solve_MTPA():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine for MTPA calculation"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # LUT_enforced = None

    LUT_enforced = load("C:/pyleecan/pyleecan_B/pyleecan/pyleecan/Results/LUT.h5")

    # Speed vector
    Nspeed = 50
    # Number of loads
    Nload = 5

    # First simulation creating femm file
    simu = Simu1(name="test_ElecLUTdq_solve_MTPA", machine=Toyota_Prius)

    # Initialization of the simulation starting point
    simu.input = InputCurrent(
        OP=OPdq(),
        Nt_tot=4 * 8,
        Na_tot=200 * 8,
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    OP_matrix = np.zeros((Nspeed, 3))
    OP_matrix[:, 0] = np.linspace(50, 8000, Nspeed)
    simu.var_simu = VarLoadCurrent(is_keep_all_output=True)
    simu.var_simu.set_OP_matrix(
        OP_matrix, "N0", "Id", "Iq", input_index=0, is_update_input=True
    )

    simu.elec = ElecLUTdq(
        Urms_max=400,
        Jrms_max=30e6,
        n_interp=100,
        n_Id=5,
        n_Iq=5,
        Id_max=0,
        Iq_min=0,
        LUT_enforced=LUT_enforced,
        is_grid_dq=True,
        LUT_simu=Simu1(
            input=InputCurrent(
                OP=OPdq(),
                Nt_tot=4 * 8,
                Na_tot=200 * 8,
                is_periodicity_a=True,
                is_periodicity_t=True,
            ),
            var_simu=VarLoadCurrent(
                postproc_list=[PostLUT(is_save_LUT=False)], is_keep_all_output=True,
            ),
            mag=MagFEMM(
                is_periodicity_a=True,
                is_periodicity_t=True,
                nb_worker=4,
                is_get_meshsolution=True,
            ),
        ),
    )

    load_vect = np.linspace(0, 1, Nload)
    OP_matrix_MTPA = np.zeros((Nspeed, Nload, 4))
    U_MTPA = np.zeros((Nspeed, Nload, 3))
    I_MTPA = np.zeros((Nspeed, Nload, 3))
    Phidq_MTPA = np.zeros((Nspeed, Nload, 2))
    out_load = list()
    for ii, load_rate in enumerate(load_vect):
        if ii > 0 and LUT_enforced is None:
            simu.elec.LUT_enforced = out.output_list[0].simu.elec.LUT_enforced

        simu.elec.load_rate = load_rate

        out = simu.run()

        # Store values in MTPA
        OP_matrix_MTPA[:, ii, 0] = out["N0"].result
        OP_matrix_MTPA[:, ii, 1] = out["Id"].result
        OP_matrix_MTPA[:, ii, 2] = out["Iq"].result
        OP_matrix_MTPA[:, ii, 3] = [out_ii.elec.Tem_av for out_ii in out.output_list]
        U_MTPA[:, ii, 0] = [out_ii.elec.OP.Ud_ref for out_ii in out.output_list]
        U_MTPA[:, ii, 1] = [out_ii.elec.OP.Uq_ref for out_ii in out.output_list]
        U_MTPA[:, ii, 2] = [
            out_ii.elec.OP.get_U0_UPhi0()["U0"] for out_ii in out.output_list
        ]
        I_MTPA[:, ii, 0] = OP_matrix_MTPA[:, ii, 1]
        I_MTPA[:, ii, 1] = OP_matrix_MTPA[:, ii, 2]
        I_MTPA[:, ii, 2] = [
            out_ii.elec.OP.get_I0_Phi0()["I0"] for out_ii in out.output_list
        ]
        Phidq_MTPA[:, ii, 0] = [out_ii.elec.eec.Phid for out_ii in out.output_list]
        Phidq_MTPA[:, ii, 1] = [out_ii.elec.eec.Phiq for out_ii in out.output_list]

        out_load.append(out)

    # Check torque values
    assert_almost_equal(OP_matrix_MTPA[:, -1, 3].max(), 342, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, -1, 3].min(), 164, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, 0, 3].max(), 0, decimal=0)
    assert_almost_equal(OP_matrix_MTPA[:, 0, 3].min(), 0, decimal=0)

    if is_show_fig:
        # Build legend list for each load level
        legend_list = list()
        for i_load in range(Nload):
            if Nload > 1:
                legend_list.append(
                    "Load level = "
                    + str(int(round(100 * (i_load) / (Nload - 1))))
                    + " %"
                )
            else:
                legend_list.append("Load level =  100%")

        # Plot torque speed curve for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 3] for i_load in range(Nload)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Average torque [N.m]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Id for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 1] for i_load in range(Nload)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Id Current [Arms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Iq for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 2] for i_load in range(Nload)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Iq Current [Arms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Ud for each load level
        y_list = [U_MTPA[:, i_load, 0] for i_load in range(Nload)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Ud Voltage [Vrms]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )

        # Plot Uq for each load level
        y_list = [U_MTPA[:, i_load, 1] for i_load in range(Nload)]
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

        # Init plot map
        dict_map = {
            "Xdata": I_MTPA[:, :, 0],  # Id
            "Ydata": I_MTPA[:, :, 1],  # Iq
            "xlabel": "d-axis current [Arms]",
            "ylabel": "q-axis current [Arms]",
            "type_plot": "pcolor",
            "is_contour": True,
        }

        # Plot torque maps
        # plot_3D(
        #     Zdata=OP_matrix_MTPA[:, :, -1],
        #     zlabel="Average Torque [N.m]",
        #     title="Torque map in dq plane",
        #     **dict_map,
        # )

        # # Plot Phi_d map
        # plot_3D(
        #     Zdata=eec_param["Phid"].reshape((n_Iq, n_Id)).T,
        #     zlabel="$\Phi_d$ [Wb]",
        #     title="Flux linkage map in dq plane (d-axis)",
        #     **dict_map,
        # )

        # # Plot Phi_q map
        # plot_3D(
        #     Zdata=eec_param["Phiq"].reshape((n_Iq, n_Id)).T,
        #     zlabel="$\Phi_q$ [Wb]",
        #     title="Flux linkage map in dq plane (q-axis)",
        #     **dict_map,
        # )

        # plot_3D(
        #     Zdata=Id.reshape((n_Iq, n_Id)).T,
        #     zlabel="Average Torque [N.m]",
        #     title="Torque map in dq plane",
        #     # save_path=join(save_path, name + "_torque_map.png"),
        #     **dict_map,
        # )
        # plot_3D(
        #     Zdata=Iq.reshape((n_Iq, n_Id)).T,
        #     zlabel="Average Torque [N.m]",
        #     title="Torque map in dq plane",
        #     # save_path=join(save_path, name + "_torque_map.png"),
        #     **dict_map,
        # )
        # plt.contour(
        #     dict_map["Xdata"],
        #     dict_map["Ydata"],
        #     U_max_interp.reshape((n_Iq, n_Id)),
        #     colors="blue",
        #     linewidths=0.8,
        # )
        # plot_3D(
        #     Zdata=Tem_sync.reshape((n_Iq, n_Id)).T,
        #     zlabel="Synchrnous Torque [N.m]",
        #     title="Torque map in dq plane",
        #     **dict_map,
        # )
        # plot_3D(
        #     Zdata=Tem_rel.reshape((n_Iq, n_Id)).T,
        #     zlabel="Reluctant Torque [N.m]",
        #     title="Torque map in dq plane",
        #     **dict_map,
        # )

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_ElecLUTdq_solve_MTPA()

    # ELUT = test_EEC_ELUT_PMSM_calc(n_Id=3, n_Iq=3)
    # ELUT.save("ELUT_PMSM.h5")
    # ELUT = load("ELUT_PMSM.h5")
    # test_EEC_ELUT_PMSM_MTPA(ELUT)
