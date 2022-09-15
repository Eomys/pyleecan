import numpy as np

from SciDataTool.Functions.Plot.plot_3D import plot_3D

from ...Classes.Electrical import Electrical
from ...Classes.EEC_PMSM import EEC_PMSM
from ...Classes.Simu1 import Simu1
from ...Classes.OPdq import OPdq
from ...Classes.InputCurrent import InputCurrent


def comp_MTPA(
    machine,
    LUT,
    N0_min,
    N0_max,
    Nspeed,
    Ntorque,
    I_max,
    U_max,
    Rs=None,
    Tsta=20,
    n_Id=100,
    n_Iq=100,
    is_plot=False,
):
    """Return the Air Gap Surface Force

    Parameters
    ----------
    machine : machine
        A machine object
    LUT: LUTdq
        A look up table object
    Tem_vect: ndarray
        Array of requested torque level
    N0_vect: ndarray
        Array of requested speeds
    I_max: float
        Maximum current [Arms]
    U_max: float
        Maximum voltage [Vrms]
    Rs: float
        Stator phase resistance to enforce [Ohm]
    Tsta: float
        Stator widning temperature to enforce [deg]
    n_Id: int
        Desciretization number to interpolate along d-axis
    n_Iq: int
        Desciretization number to interpolate along q-axis

    Returns
    -------
    OP_matrix_MTPA: ndarray
        OP_matrix resulting from MTPA strategy
    U_MTPA: ndarray
        Output voltage [Vrms]
    I_MTPA: ndarray
        Output current [Arms]

    """

    # Speed vector
    N0_vect = np.linspace(N0_min, N0_max, Nspeed)

    # Maximum load vector
    if Ntorque == 1:
        Tem_vect = np.array([])
    else:
        Tem_vect = np.linspace(0, 1, Ntorque)

    # Pole pair number
    p = machine.get_pole_pair_number()
    # Stator winding number of phases
    qs = machine.stator.winding.qs

    OP_matrix = LUT.get_OP_array("N0", "Id", "Iq")

    # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
    Id_min = OP_matrix[:, 1].min()
    Id_max = OP_matrix[:, 1].max()
    Iq_min = OP_matrix[:, 2].min()
    Iq_max = OP_matrix[:, 2].max()

    Id, Iq = np.meshgrid(
        np.linspace(Id_min, Id_max, n_Id), np.linspace(Iq_min, Iq_max, n_Iq)
    )
    Id, Iq = Id.ravel(), Iq.ravel()
    Imax_interp = np.sqrt(Id ** 2 + Iq ** 2)

    simu_MTPA = Simu1(name=machine.name + "_comp_MTPA", machine=machine)

    # Definition of the input
    OP_ref = OPdq(N0=OP_matrix[0, 0], Id_ref=OP_matrix[0, 1], Iq_ref=OP_matrix[0, 2])
    simu_MTPA.input = InputCurrent(OP=OP_ref)

    # Stator winding resistance [Ohm]
    ecc = EEC_PMSM(R1=Rs)  # If Rs None => Compute
    simu_MTPA.elec = Electrical(LUT_enforced=LUT, eec=ecc, Tsta=Tsta)

    # Interpolate stator winding flux in dqh frame for all Id/Iq
    eec_param = simu_MTPA.elec.eec.comp_parameters(
        machine=machine, OP=OP_ref, Tsta=simu_MTPA.elec.Tsta, Id_array=Id, Iq_array=Iq
    )

    # Compute torque
    Tem_sync, Tem_rel = simu_MTPA.elec.eec.comp_torque_sync_rel(eec_param, qs, p)
    Tem_interp = Tem_sync + Tem_rel

    # Init OP_matrix
    OP_matrix_MTPA = np.zeros((Nspeed, Ntorque, 4))
    U_MTPA = np.zeros((Nspeed, Ntorque, 3))
    I_MTPA = np.zeros((Nspeed, Ntorque, 3))

    for ii, N0 in enumerate(N0_vect):

        print("Speed " + str(ii + 1) + "/" + str(Nspeed))

        # Update operating point
        OP_ref.N0 = N0
        OP_ref.felec = None

        eec_param = simu_MTPA.elec.eec.comp_parameters(
            machine,
            OP=OP_ref,
            Tsta=simu_MTPA.elec.Tsta,
            Trot=simu_MTPA.elec.Trot,
            Id_array=Id,
            Iq_array=Iq,
        )

        # Calculate voltage
        out_dict = simu_MTPA.elec.eec.solve(eec_param)
        U_max_interp = np.sqrt(out_dict["Ud"] ** 2 + out_dict["Uq"] ** 2)

        # Finding indices of operating points satisfying Vmax and I_max voltage and torque limitations
        j0 = np.logical_and(U_max_interp <= U_max, Imax_interp <= np.abs(I_max))
        # Finding index of operating point giving maximum positive torque among feasible operating points
        jmax = np.argmax(Tem_interp[j0])

        # Maximum torque achieved for N0
        Tem_max = Tem_interp[j0][jmax]

        # Store values in MTPA
        OP_matrix_MTPA[ii, -1, 0] = N0
        OP_matrix_MTPA[ii, -1, 1] = Id[j0][jmax]
        OP_matrix_MTPA[ii, -1, 2] = Iq[j0][jmax]
        OP_matrix_MTPA[ii, -1, 3] = Tem_max
        U_MTPA[ii, -1, 0] = out_dict["Ud"][j0][jmax]
        U_MTPA[ii, -1, 1] = out_dict["Uq"][j0][jmax]
        U_MTPA[ii, -1, 2] = U_max_interp[j0][jmax]
        I_MTPA[ii, -1, 0] = OP_matrix_MTPA[ii, -1, 1]
        I_MTPA[ii, -1, 1] = OP_matrix_MTPA[ii, -1, 2]
        I_MTPA[ii, -1, 2] = Imax_interp[j0][jmax]

        for kk, Tem_rate in enumerate(Tem_vect[:-1]):

            if Tem_rate == 0:
                Tem_k = 0.01 * Tem_max
                # Finding indices of operating points satisfying Vmax voltage for no torque production
                j0 = np.logical_and(U_max_interp <= U_max, np.abs(Tem_interp) < Tem_k)

                # Finding index of operating point for lowest current
                jmax = np.argmin(np.abs(Imax_interp[j0]))

            else:

                # Finding indices of operating points satisfying maximum voltage and torque level
                j0 = np.logical_and(
                    U_max_interp <= U_max, Tem_interp >= Tem_rate * Tem_max
                )
                # Finding index of operating points with lowest current among feasible operating points
                jmax = np.argmin(Imax_interp[j0])

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

    if is_plot:
        # Init plot map
        dict_map = {
            "Xdata": Id.reshape((n_Iq, n_Id))[0, :],
            "Ydata": Iq.reshape((n_Iq, n_Id))[:, 0],
            "xlabel": "d-axis current [Arms]",
            "ylabel": "q-axis current [Arms]",
            "type_plot": "pcolor",
            "is_contour": True,
        }

        # Plot torque maps
        plot_3D(
            Zdata=Tem_interp.reshape((n_Iq, n_Id)).T,
            zlabel="Average Torque [N.m]",
            title="Torque map in dq plane",
            **dict_map,
        )
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
        plot_3D(
            Zdata=Tem_sync.reshape((n_Iq, n_Id)).T,
            zlabel="Synchrnous Torque [N.m]",
            title="Torque map in dq plane",
            **dict_map,
        )
        plot_3D(
            Zdata=Tem_rel.reshape((n_Iq, n_Id)).T,
            zlabel="Reluctant Torque [N.m]",
            title="Torque map in dq plane",
            **dict_map,
        )

        # Plot Phi_d map
        plot_3D(
            Zdata=eec_param["Phid"].reshape((n_Iq, n_Id)).T,
            zlabel="$\Phi_d$ [Wb]",
            title="Flux linkage map in dq plane (d-axis)",
            **dict_map,
        )

        # Plot Phi_q map
        plot_3D(
            Zdata=eec_param["Phiq"].reshape((n_Iq, n_Id)).T,
            zlabel="$\Phi_q$ [Wb]",
            title="Flux linkage map in dq plane (q-axis)",
            **dict_map,
        )

    return OP_matrix_MTPA, U_MTPA, I_MTPA
