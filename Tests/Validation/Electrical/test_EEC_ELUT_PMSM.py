from os.path import join

import numpy as np
from numpy.testing import assert_almost_equal

import pytest

from SciDataTool.Functions.Plot.plot_2D import plot_2D
from SciDataTool.Functions.Plot.plot_3D import plot_3D

from pyleecan.Classes.ImportGenPWM import ImportGenPWM
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostLUT import PostLUT
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_ANL import EEC_ANL
from pyleecan.Classes.EEC_PMSM import EEC_PMSM

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.Functions.Electrical.coordinate_transformation import n2dqh_DataTime
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
    Id_min, Id_max = -100, 100
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

    # Check flux linkage dqh values
    Phi_dqh_mean = ELUT.get_Phidqh_mean()
    OP_list = OP_matrix[:, 1:3].tolist()
    ii = OP_list.index([0, 0])
    Phi_dqh0 = n2dqh_DataTime(
        ELUT.Phi_wind[ii],
        is_dqh_rms=True,
    )
    Phi_dqh0_mean = Phi_dqh0.get_along("time=mean", "phase")[Phi_dqh0.symbol]
    assert_almost_equal(Phi_dqh0_mean, Phi_dqh_mean[ii, :], decimal=20)
    assert_almost_equal(Phi_dqh0_mean[0], 0.141, decimal=3)

    # Plot 3-phase current function of time
    ELUT.Phi_wind[ii].plot_2D_Data(
        "time",
        "phase[]",
        save_path=join(save_path, name + "_flux_linkage_abc.png"),
        is_show_fig=is_show_fig,
        **dict_2D,
    )
    Phi_dqh0.plot_2D_Data(
        "time",
        "phase[]",
        save_path=join(save_path, name + "_flux_linkage_dqh.png"),
        is_show_fig=is_show_fig,
        **dict_2D,
    )

    return out, ELUT


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
def test_EEC_ELUT_PMSM_MTPA(test_ELUT, n_Id=51, n_Iq=101):
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine for MTPA calculation"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    qs = Toyota_Prius.stator.winding.qs
    p = Toyota_Prius.get_pole_pair_number()

    name = "test_EEC_ELUT_PMSM_MTPA"
    simu_MTPA = Simu1(name=name, machine=Toyota_Prius)

    # Definition of the input
    OP_ref = OPdq(N0=1000, Id_ref=50, Iq_ref=100)
    simu_MTPA.input = InputCurrent(
        Na_tot=1024,
        Nt_tot=1024,
        OP=OP_ref,
    )

    OP_matrix = test_ELUT.OP_matrix
    # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
    Id_min = np.min(OP_matrix[:, 1])
    Id_max = np.max(OP_matrix[:, 1])
    Iq_min = np.min(OP_matrix[:, 2])
    Iq_max = np.max(OP_matrix[:, 2])

    Id, Iq = np.meshgrid(
        np.linspace(Id_min, Id_max, n_Id), np.linspace(Iq_min, Iq_max, n_Iq)
    )
    Id, Iq = Id.ravel(), Iq.ravel()

    elec_model = Electrical(eec=EEC_PMSM(), ELUT_enforced=test_ELUT)

    # Interpolate stator winding flux in dqh frame for all Id/Iq
    elec_model.eec.parameters = elec_model.ELUT_enforced.get_param_dict(
        Id=Id, Iq=Iq, param_list=["Idqh", "Phidqh"]
    )

    # Compute torque
    Tem_sync, Tem_rel = elec_model.eec.comp_torque_sync_rel(qs, p)
    Tem_interp = Tem_sync + Tem_rel

    # Init plot map
    dict_map = {
        "Xdata": Id.reshape((n_Iq, n_Id))[0, :],
        "Ydata": Iq.reshape((n_Iq, n_Id))[:, 0],
        "xlabel": "d-axis current [Arms]",
        "ylabel": "q-axis current [Arms]",
        "type_plot": "pcolor",
        "is_contour": True,
        "is_show_fig": is_show_fig,
    }

    # Plot torque map
    plot_3D(
        Zdata=Tem_interp.reshape((n_Iq, n_Id)).T,
        zlabel="Average Torque [N.m]",
        title="Torque map in dq plane",
        save_path=join(save_path, name + "_torque_map.png"),
        **dict_map,
    )

    # Plot Phi_d map
    plot_3D(
        Zdata=elec_model.eec.parameters["Phid"].reshape((n_Iq, n_Id)).T,
        zlabel="$\Phi_d$ [Wb]",
        title="Flux linkage map in dq plane (d-axis)",
        save_path=join(save_path, name + "_phid_map.png"),
        **dict_map,
    )

    # Plot Phi_q map
    plot_3D(
        Zdata=elec_model.eec.parameters["Phiq"].reshape((n_Iq, n_Id)).T,
        zlabel="$\Phi_q$ [Wb]",
        title="Flux linkage map in dq plane (q-axis)",
        save_path=join(save_path, name + "_phiq_map.png"),
        **dict_map,
    )

    # MTPA
    # Maximum current [Arms]
    I_max = 250 / np.sqrt(2)
    Imax_interp = np.sqrt(Id ** 2 + Iq ** 2)
    # Maximum voltage [Vrms]
    U_max = 300
    # Speed vector
    Nspeed = 50
    N0_min = 50
    N0_max = 8000
    N0_vect = np.linspace(N0_min, N0_max, Nspeed)
    # Maximum load vector
    Ntorque = 5
    is_braking = False  # True to include negative torque (braking)
    if is_braking:
        Ntorque = (
            2 * Ntorque + 1
        )  # Take twice the number of torques + odd to include zero torque
    if not is_braking and Ntorque == 1:
        I_max_vect = np.array([I_max])
    elif is_braking:
        I_max_vect = np.linspace(-I_max, I_max, Ntorque)
    else:
        I_max_vect = np.linspace(0, I_max, Ntorque)

    # Init OP_matrix
    OP_matrix_MTPA = np.zeros((Nspeed, Ntorque, 4))
    U_MTPA = np.zeros((Nspeed, Ntorque, 3))
    I_MTPA = np.zeros((Nspeed, Ntorque, 3))

    for ii, N0 in enumerate(N0_vect):

        print("Speed " + str(ii + 1) + "/" + str(Nspeed))

        # Update operating point
        OP_ref.N0 = N0
        OP_ref.felec = None

        # Update stator resistance with skin effect
        elec_model.eec.comp_parameters(
            Toyota_Prius,
            OP=OP_ref,
            Tsta=elec_model.Tsta,
            Trot=elec_model.Trot,
        )

        # Calculate voltage
        out_dict = elec_model.eec.solve_EEC()
        U_max_interp = np.sqrt(out_dict["Ud"] ** 2 + out_dict["Uq"] ** 2)

        for kk, I_max0 in enumerate(I_max_vect):

            if I_max0 == 0:
                # Finding indices of operating points satisfying Vmax voltage for Iq=0 (no torque production)
                j0 = np.logical_and(U_max_interp <= U_max, np.abs(Iq) == 0)

                # Finding index of operating point giving lowest current
                jmax = np.argmin(np.abs(Imax_interp[j0]))

                # print(Id_interp[j0][jmax])
                # print(Iq_interp[j0][jmax])

            else:
                # Finding indices of operating points satisfying Vmax and XImax(i) voltage and torque limitations
                j0 = np.logical_and(
                    U_max_interp <= U_max, Imax_interp <= np.abs(I_max0)
                )

                if I_max0 > 0:
                    # Finding index of operating point giving maximum positive torque among feasible operating points
                    jmax = np.argmax(Tem_interp[j0])
                else:
                    # Finding index of operating point giving maximum negative torque among feasible operating points
                    jmax = np.argmin(Tem_interp[j0])

            # Store values in MTPA
            OP_matrix_MTPA[ii, kk, 0] = N0
            OP_matrix_MTPA[ii, kk, 1] = Id[j0][jmax]
            OP_matrix_MTPA[ii, kk, 2] = Iq[j0][jmax]
            OP_matrix_MTPA[ii, kk, 3] = Tem_interp[j0][jmax]
            U_MTPA[ii, kk, 0] = out_dict["Ud"][j0][jmax]
            U_MTPA[ii, kk, 1] = out_dict["Uq"][j0][jmax]
            U_MTPA[ii, kk, 2] = U_max_interp[j0][jmax]
            I_MTPA[ii, kk, 0] = OP_matrix_MTPA[ii, kk, 1]
            I_MTPA[ii, kk, 1] = OP_matrix_MTPA[ii, kk, 2]
            I_MTPA[ii, kk, 2] = Imax_interp[j0][jmax]

    if Ntorque > 1:
        # Plot torque speed curve for each load level
        y_list = list()
        legend_list = list()
        for i_load in range(Ntorque):
            y_list.append(OP_matrix_MTPA[:, i_load, 3])
            legend_list.append(
                "Load level = " + str(int(round(100 * (i_load) / (Ntorque - 1)))) + " %"
            )
        plot_2D(
            [OP_matrix_MTPA[:, i_load, 0]],
            y_list,
            xlabel="Speed [rpm]",
            ylabel="Average torque [N.m]",
            legend_list=legend_list,
            # save_path=join(save_path, name + "_MTPA_torque_speed.png"),
            # is_show_fig=is_show_fig,
        )

    i_load = -1
    plot_2D(
        [OP_matrix_MTPA[:, i_load, 0]],
        [I_MTPA[:, i_load, 0], I_MTPA[:, i_load, 1], I_MTPA[:, i_load, 2]],
        xlabel="Speed [rpm]",
        ylabel="Current [Arms]",
        legend_list=["Id", "Iq", "Imax"],
        # save_path=join(save_path, name + "_current_MTPA_OP" + str(i_load) + ".png"),
        # is_show_fig=is_show_fig,
    )

    plot_2D(
        [OP_matrix_MTPA[:, i_load, 0]],
        [U_MTPA[:, i_load, 0], U_MTPA[:, i_load, 1], U_MTPA[:, i_load, 2]],
        xlabel="Speed [rpm]",
        ylabel="Voltage [Vrms]",
        legend_list=["Ud", "Uq", "Umax"],
        # save_path=join(save_path, name + "_voltage_MTPA_OP" + str(i_load) + ".png"),
        # is_show_fig=is_show_fig,
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
def test_EEC_ELUT_PMSM_PWM(test_ELUT):
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine including PWM"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Simu with EEC using ELUT
    fmax = 20000
    fswi = 7000
    Vdc1 = 800  # Bus voltage
    U0 = 460  # Phase voltage
    simu_EEC = Simu1(name="test_LUT_PMSM", machine=Toyota_Prius)

    # Definition of the input
    simu_EEC.input = InputVoltage(
        Na_tot=1024,
        Nt_tot=1024,
        PWM=ImportGenPWM(fmax=fmax, fswi=fswi, Vdc1=Vdc1, U0=U0),
        OP=OPdq(N0=1000, Id_ref=50, Iq_ref=100, Ud_ref=200, Uq_ref=300),
    )

    simu_EEC.elec = Electrical(eec=EEC_ANL(), ELUT_enforced=test_ELUT)

    out_EEC = simu_EEC.run()

    # Plot 3-phase current function of time
    out_EEC.elec.Is_harm.plot_2D_Data(
        "freqs",
        save_path=join(save_path, "EEC_FEMM_IPMSM_Is_harm.png"),
        is_show_fig=is_show_fig,
        **dict_2D,
    )

    return out_EEC


# To run it without pytest
if __name__ == "__main__":
    # out0, ELUT = test_EEC_ELUT_PMSM_calc()
    # ELUT.save("ELUT_PMSM.h5")
    ELUT = load("ELUT_PMSM.h5")
    test_EEC_ELUT_PMSM_MTPA(ELUT)
    # test_EEC_ELUT_PMSM_PWM(ELUT)
