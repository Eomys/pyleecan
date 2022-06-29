import numpy as np


def solve_MTPA(self, LUT, Rs):
    """Solve EEC using Maximum Torque Per Ampere strategy with respect to voltage and current constraints

    Parameters
    ----------
    self : ElecLUTdq
        a ElecLUTdq object
    LUT : LUTdq
        Calculated look-up table
    Rs: float
        Stator phase resistance [Ohm]

    Returns
    ----------
    out_dict: dict
        Dict containing all output quantities

    """

    # Get output, machine and OP
    output = self.parent.parent

    machine = output.simu.machine
    OP = output.elec.OP

    # Maximum voltage
    Urms_max = self.Urms_max
    # Maximum current
    Irms_max = self.Irms_max
    # Electrical frequency
    felec = OP.get_felec()
    # Electrical pulsation
    ws = 2 * np.pi * felec
    # Stator winding number of phases
    qs = machine.stator.winding.qs
    # Number of pole pair
    p = machine.get_pole_pair_number()

    # iteration until convergence is reached, and max number of iterations on EEC
    delta_Tem = 1e10
    delta_Tem_max = 0.1
    Nmax = 20
    niter_Tem = 1
    Tem_max_old = 0
    Id_old = 0
    Id_min = self.Id_min
    Id_max = self.Id_max
    Iq_min = self.Iq_min
    Iq_max = self.Iq_max
    Nd = (
        self.n_Id
        if self.n_Id == 1
        else int(self.n_Id * self.n_interp / (self.n_Id + self.n_Iq))
    )
    Nq = (
        self.n_Iq
        if self.n_Iq == 1
        else int(self.n_Iq * self.n_interp / (self.n_Id + self.n_Iq))
    )

    # Check if there is a loss model
    is_loss_model = LUT.simu.loss is not None

    while abs(delta_Tem) > delta_Tem_max and niter_Tem < Nmax:

        # Refine Id/Iq mesh
        Id_vect = np.linspace(Id_min, Id_max, Nd)
        Iq_vect = np.linspace(Iq_min, Iq_max, Nq)
        Id, Iq = np.meshgrid(Id_vect, Iq_vect)
        Id, Iq = Id.ravel(), Iq.ravel()

        # Calculate maximum current
        Imax_interp = np.sqrt(Id ** 2 + Iq ** 2)

        # Interpolate Phid/Phiq on the refined mesh
        (Phid, Phiq, Phih) = LUT.interp_Phi_dqh(Id, Iq)

        # Calculate voltage (Ud/Uq) for the refined mesh
        Ud = Rs * Id - Phiq * ws
        Uq = Rs * Iq + Phid * ws
        Umax_interp = np.sqrt(Ud ** 2 + Uq ** 2)

        # Calculate electromagnetic torque
        Tem_interp = qs * p * (Phid * Iq - Phiq * Id)

        # Set maximum voltage condition
        U_cond = Umax_interp <= Urms_max

        if is_loss_model:
            # Interpolate losses from LUT
            Ploss_dqh = LUT.interp_Ploss_dqh(Id, Iq, N0=OP.N0)
            Ploss_ovl = np.sum(Ploss_dqh, axis=1)
            Ploss_dqh_wo_Joule = LUT.interp_Ploss_dqh(
                Id, Iq, N0=OP.N0, exclude_models=["LossModelWinding"]
            )
            # The input power must cover electrical power + additional losses
            P_in = qs * (Ud * Id + Uq * Iq) + np.sum(Ploss_dqh_wo_Joule, axis=1)
        else:
            # Only consider stator Joule losses
            Ploss_ovl = qs * Rs * (Id ** 2 + Iq ** 2)
            # The input power must cover electrical power + Joule losses
            P_in = qs * (Ud * Id + Uq * Iq)

        # The output power is the input power minus all losses
        P_out = P_in - Ploss_ovl

        if self.load_rate == 0:
            # Finding indices of operating points satisfying voltage constraint for no torque production
            i0 = np.logical_and(U_cond, Iq == 0)

            # Finding index of operating point for lowest current
            imin = np.argmin(np.abs(Imax_interp[i0]))

            # Transform target from reaching torque to reach minimum Id
            delta_Tem = Id[i0][imin] - Id_old

        else:
            # Set maximum current condition
            I_cond = Imax_interp <= Irms_max

            # Finding indices of operating points satisfying voltage and current constraints
            i0 = np.logical_and(U_cond, I_cond)

            # Finding index of operating point giving maximum positive torque among feasible operating points
            imin = np.argmax(Tem_interp[i0])

            # Maximum torque achieved for N0
            Tem_max = Tem_interp[i0][imin]

            if self.load_rate < 1:
                # Finding indices of operating points satisfying maximum voltage and torque level
                i0 = np.logical_and(U_cond, Tem_interp >= self.load_rate * Tem_max)

                # Finding index of operating points with lowest current among feasible operating points
                imin = np.argmin(Imax_interp[i0])

                # Check torque difference
                delta_Tem = np.abs(self.load_rate * Tem_max - Tem_interp[i0][imin])

            else:
                # Check if maximum torque changes depending on Id/Iq discretization
                delta_Tem = Tem_max - Tem_max_old
                Tem_max_old = Tem_max

        if abs(delta_Tem) > delta_Tem_max:
            # Zoom in Id / Iq grid to achieve better accuracy on output values
            jd = np.where(Id_vect == Id[i0][imin])[0][0]
            jq = np.where(Iq_vect == Iq[i0][imin])[0][0]

            jd_min = max([jd - 1, 0])
            jd_max = min([jd + 1, Nd - 1])
            jq_min = max([jq - 1, 0])
            jq_max = min([jq + 1, Nq - 1])

            Id_min = Id_vect[jd_min]
            Id_max = Id_vect[jd_max]
            Iq_min = Iq_vect[jq_min]
            Iq_max = Iq_vect[jq_max]

        niter_Tem = niter_Tem + 1

    # Launch warnings
    if Umax_interp[i0][imin] > Urms_max:
        self.get_logger().warning("Voltage constraint cannot be reached")

    if Imax_interp[i0][imin] > Irms_max:
        self.get_logger().warning("Current constraint cannot be reached")

    out_dict = dict()

    # Calculate efficiency
    out_dict["P_in"] = P_in[i0][imin]
    out_dict["P_out"] = P_out[i0][imin]
    eff = out_dict["P_out"] / out_dict["P_in"]
    out_dict["efficiency"] = eff if eff > 0 else 0
    # out_dict["efficiency"] = out_dict["P_out"] / out_dict["P_in"]

    # Calculate torque from output power
    out_dict["Tem_av"] = Tem_interp[i0][imin]

    # Store voltage and currents
    out_dict["Id"] = Id[i0][imin]
    out_dict["Iq"] = Iq[i0][imin]
    out_dict["Ud"] = Ud[i0][imin]
    out_dict["Uq"] = Uq[i0][imin]

    # Store dq fluxes
    out_dict["Phid"] = Phid[i0][imin]
    out_dict["Phiq"] = Phiq[i0][imin]

    # Calculate flux linkage and back-emf
    Phidqh_mag = LUT.get_Phi_dqh_mag_mean()
    out_dict["Phid_mag"] = Phidqh_mag[0]
    out_dict["Phiq_mag"] = Phidqh_mag[1]
    out_dict["Erms"] = ws * Phidqh_mag[0]

    # Calculate inductances
    if Id[i0][imin] != 0:
        out_dict["Ld"] = (Phid[i0][imin] - out_dict["Phid_mag"]) / Id[i0][imin]
    if Iq[i0][imin] != 0:
        out_dict["Lq"] = Phiq[i0][imin] / Iq[i0][imin]

    # Calculate torque ripple
    Tem_rip_pp = LUT.interp_Tem_rip_dqh(Id[i0][imin], Iq[i0][imin])
    if Tem_rip_pp is not None:
        out_dict["Tem_rip_pp"] = float(Tem_rip_pp)
        if out_dict["Tem_av"] == 0:
            out_dict["Tem_rip_norm"] = 0
        else:
            out_dict["Tem_rip_norm"] = np.abs(Tem_rip_pp / out_dict["Tem_av"])

    return out_dict
