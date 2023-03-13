from os.path import join, split, exists

import numpy as np
import pytest

import SciDataTool

print(SciDataTool.__version__)

from SciDataTool.Functions.Plot.plot_2D import plot_2D
from SciDataTool.Functions.Plot.plot_3D import plot_3D

from pyleecan.Classes.ElecLUTdq import ElecLUTdq

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostLUT import PostLUT
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelJoule import LossModelJoule
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.DataKeeper import DataKeeper

from pyleecan.Functions.load import load
from pyleecan.Functions.Load.load_json import LoadMissingFileError

from pyleecan.definitions import DATA_DIR
from pyleecan.definitions import RESULT_DIR

is_show_fig = True


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.skip(reason="Work in progress")
def test_efficiency_map():
    """Validation of the efficiency map of the Toyota Prius motor, based on the one presented in
    "Electromagnetic Analysis and Design Methodology for Permanent Magnet Motors Using MotorAnalysis-PM Software",
    available at https://www.mdpi.com/2075-1702/7/4/75."""

    Toyota_Prius = load(join(DATA_DIR, "Machine", f"Toyota_Prius.json"))
    LUT_file_name = f"LUT_eff_Toyota_Prius.h5"
    path_to_LUT = join(RESULT_DIR, LUT_file_name)

    if not exists(split(path_to_LUT)[0]):
        raise Exception("The path to LUT is not valid.")

    # Speed vector
    Nspeed = 50
    # Number of loads
    Nload = 7

    # First simulation creating femm file
    simu = Simu1(name="test_ElecLUTdq_efficiency_map", machine=Toyota_Prius)

    # Initialization of the simulation starting point
    simu.input = InputCurrent(
        OP=OPdq(),
        Nt_tot=4 * 20,  # *8,
        Na_tot=200 * 8,
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    datakeeper_list = [
        DataKeeper(
            name="Torque",
            unit="N.m",
            symbol="T",
            keeper=lambda output: output.elec.Tem_av,
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="Efficiency",
            unit="",
            symbol="eff",
            keeper=lambda output: output.elec.OP.efficiency,
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="current density",
            unit="A/mm^2",
            symbol="J",
            keeper=lambda output: output.elec.get_Jrms() * 1e-6,
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="Ud",
            unit="V",
            symbol="Ud",
            keeper=lambda output: output.elec.OP.Ud_ref,
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="Uq",
            unit="V",
            symbol="Uq",
            keeper=lambda output: output.elec.OP.Uq_ref,
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="U0",
            unit="V",
            symbol="U0",
            keeper=lambda output: output.elec.OP.get_U0_UPhi0()["U0"],
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="I0",
            unit="A",
            symbol="I0",
            keeper=lambda output: output.elec.OP.get_I0_Phi0()["I0"],
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="Phid",
            unit="Wb",
            symbol="Phid",
            keeper=lambda output: output.elec.eec.Phid,
            error_keeper=lambda simu: np.nan,
        ),
        DataKeeper(
            name="Phiq",
            unit="Wb",
            symbol="Phiq",
            keeper=lambda output: output.elec.eec.Phiq,
            error_keeper=lambda simu: np.nan,
        ),
    ]

    OP_matrix = np.zeros((Nspeed, 3))
    OP_matrix[:, 0] = np.linspace(500, 6000, Nspeed)
    simu.var_simu = VarLoadCurrent(datakeeper_list=datakeeper_list)
    simu.var_simu.set_OP_array(OP_matrix, "N0", "Id", "Iq")

    simu.elec = ElecLUTdq(
        Urms_max=153,
        Jrms_max=27e6,
        n_interp=100,
        n_Id=5,
        n_Iq=5,
        Id_max=0,
        Iq_min=0,
        LUT_enforced=None,
        is_grid_dq=True,
        Tsta=120,
        type_skin_effect=1,
        LUT_simu=Simu1(
            input=InputCurrent(
                OP=OPdq(),
                Nt_tot=4 * 10,  # *8,
                Na_tot=200 * 8,
                is_periodicity_a=True,
                is_periodicity_t=True,
            ),
            var_simu=VarLoadCurrent(
                postproc_list=[PostLUT(is_save_LUT=True, file_name=LUT_file_name)],
                is_keep_all_output=True,
            ),
            mag=MagFEMM(
                is_periodicity_a=True,
                is_periodicity_t=True,
                nb_worker=4,
                is_get_meshsolution=True,
            ),
            loss=Loss(
                is_get_meshsolution=False,
                Tsta=100,
                model_dict={
                    "stator core": LossModelSteinmetz(group="stator core"),
                    "rotor core": LossModelSteinmetz(group="rotor core"),
                    "joule": LossModelJoule(group="stator winding"),
                    "proximity": LossModelProximity(group="stator winding"),
                    "magnets": LossModelMagnet(group="rotor magnets"),
                },
            ),
        ),
    )
    try:
        LUT_enforced = load(path_to_LUT)
        simu.elec.LUT_enforced = LUT_enforced
    except (FileNotFoundError, LoadMissingFileError):
        print("The LUT could not be loaded, so it will be computed.")
        LUT_enforced = None

    load_vect = np.linspace(0, 1, Nload)
    OP_matrix_MTPA = np.zeros((Nspeed, Nload, 6))
    U_MTPA = np.zeros((Nspeed, Nload, 3))
    I_MTPA = np.zeros((Nspeed, Nload, 3))
    Phidq_MTPA = np.zeros((Nspeed, Nload, 2))
    out_load = list()
    for ii, load_rate in enumerate(load_vect):

        if ii > 0 and LUT_enforced is None:
            simu.elec.LUT_enforced = load(path_to_LUT)

        simu.elec.load_rate = load_rate

        out = simu.run()

        # Store values in MTPA
        OP_matrix_MTPA[:, ii, 0] = out["N0"].result
        OP_matrix_MTPA[:, ii, 1] = out["Id"].result
        OP_matrix_MTPA[:, ii, 2] = out["Iq"].result
        OP_matrix_MTPA[:, ii, 3] = out["T"].result
        OP_matrix_MTPA[:, ii, 4] = out["eff"].result
        OP_matrix_MTPA[:, ii, 5] = out["J"].result
        U_MTPA[:, ii, 0] = out["Ud"].result
        U_MTPA[:, ii, 1] = out["Uq"].result
        U_MTPA[:, ii, 2] = out["U0"].result
        I_MTPA[:, ii, 0] = out["Id"].result
        I_MTPA[:, ii, 1] = out["Iq"].result
        I_MTPA[:, ii, 2] = out["I0"].result
        Phidq_MTPA[:, ii, 0] = out["Phid"].result
        Phidq_MTPA[:, ii, 1] = out["Phiq"].result

        out_load.append(out)

    # Check torque values
    # assert_almost_equal(OP_matrix_MTPA[:, -1, 3].max(), 342, decimal=0)
    # assert_almost_equal(OP_matrix_MTPA[:, -1, 3].min(), 164, decimal=0)
    # assert_almost_equal(OP_matrix_MTPA[:, 0, 3].max(), 0, decimal=0)
    # assert_almost_equal(OP_matrix_MTPA[:, 0, 3].min(), 0, decimal=0)

    # if not is_LUT_exists:
    #     simu.elec.LUT_enforced.save(save_path=path_to_LUT)

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
        # Plot max torque with respect to speed
        y_list = [OP_matrix_MTPA[:, -1, 3]]
        plot_2D(
            [OP_matrix_MTPA[:, -1, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Average torque [N.m]",
            legend_list=legend_list,
            is_show_fig=is_show_fig,
        )
        # Plot power with respect to speed
        y_list = [
            OP_matrix_MTPA[:, -1, 3]
            * OP_matrix_MTPA[:, -1, 0]
            * 2
            * np.pi
            / 60
            * 1e-3
            * OP_matrix_MTPA[:, -1, 4]
        ]
        plot_2D(
            [OP_matrix_MTPA[:, -1, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Power [kW]",
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
        # Plot J for each load level
        y_list = [OP_matrix_MTPA[:, i_load, 5] for i_load in range(Nload)]
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Current density [A/mm^2]",
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
        # =============================================#
        # Plot efficiency map
        plot_3D(
            Xdata=OP_matrix_MTPA[:, :, 0],  # Rotational speed
            Ydata=OP_matrix_MTPA[:, :, 3],  # Torque
            Zdata=OP_matrix_MTPA[:, :, 4],  # Efficiency
            xlabel="Rotational speed",
            ylabel="Torque",
            zlabel="Efficiency",
            title="Efficiency map in torque, speed plane",
            type_plot="pcolormesh",
            is_contour=True,
            levels=[0.7, 0.85, 0.9, 0.92, 0.93, 0.94, 0.95],
            gamma=5,
        )
        # =============================================#

        # ==============Plot losses in the d-q plane=======#
        LUT_grid = out.simu.elec.LUT_enforced

        # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
        OP_matrix = LUT_grid.get_OP_array("N0", "Id", "Iq")
        Id_min = OP_matrix[:, 1].min()
        Id_max = OP_matrix[:, 1].max()
        Iq_min = OP_matrix[:, 2].min()
        Iq_max = OP_matrix[:, 2].max()

        nd, nq = 100, 100
        Id_vect = np.linspace(Id_min, Id_max, nd)
        Iq_vect = np.linspace(Iq_min, Iq_max, nq)
        Id, Iq = np.meshgrid(Id_vect, Iq_vect)
        Id, Iq = Id.ravel(), Iq.ravel()

        # Interpolate Phid/Phiq on the refined mesh

        Ploss_dqh = LUT_grid.interp_Ploss_dqh(Id, Iq, N0=1200)
        dict_map = {
            "Xdata": Id.reshape((nd, nq))[0, :],
            "Ydata": Iq.reshape((nd, nq))[:, 0],
            "xlabel": "d-axis current [Arms]",
            "ylabel": "q-axis current [Arms]",
            "type_plot": "pcolormesh",
            "is_contour": True,
        }
        loss_list = ["stator core", "rotor core", "joule", "proximity", "magnets"]
        for i, loss in enumerate(loss_list):
            plot_3D(
                Zdata=Ploss_dqh[:, i].reshape((nd, nq)),
                zlabel=f"{loss} [W]",
                **dict_map,
            )
        # ==================================================#
        Tem_rip = LUT_grid.interp_Tem_rip_dqh(Id, Iq)

        # Plot T_em_rip map
        plot_3D(
            Zdata=Tem_rip.reshape((nd, nq)),
            zlabel="T_emrip$ ",
            title="Torque ripple map in dq plane",
            **dict_map,
        )

        Phi_dqh_grid = LUT_grid.interp_Phi_dqh(Id, Iq)

        # Plot Phi_d map
        plot_3D(
            Zdata=Phi_dqh_grid[0, :].reshape((nd, nq)).T,
            zlabel="$\Phi_d$ [Wb]",
            title="Flux linkage map in dq plane (d-axis)",
            **dict_map,
        )

        # Plot Phi_q map
        plot_3D(
            Zdata=Phi_dqh_grid[1, :].reshape((nd, nq)).T,
            zlabel="$\Phi_q$ [Wb]",
            title="Flux linkage map in dq plane (q-axis)",
            **dict_map,
        )
    # ======================================================#
    # # Init plot map
    # dict_map = {
    #     "Xdata": I_MTPA[:, :, 0],  # Id
    #     "Ydata": I_MTPA[:, :, 1],  # Iq
    #     "xlabel": "d-axis current [Arms]",
    #     "ylabel": "q-axis current [Arms]",
    #     "type_plot": "pcolormesh",
    #     "is_contour": True,
    # }

    # # Plot torque maps
    # plot_3D(
    #     Zdata=OP_matrix_MTPA[:, :, 3],
    #     zlabel="Average Torque [N.m]",
    #     title="Torque map in dq plane",
    #     **dict_map,
    # )

    # plot_3D(
    #     Zdata=Id.reshape((nd, nq)).T,
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

    out = test_efficiency_map()
