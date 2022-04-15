import numpy as np

from ....Classes.EEC_PMSM import EEC_PMSM
from ....Classes.OutLoss import OutLoss
from ....Classes.InputPower import InputPower

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the ElecLUTdq module"""
    if self.parent is None:
        raise InputError("The Electrical object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    self.get_logger().info("Starting Electric module")

    # Get output, machine and OP
    output = self.parent.parent

    if not isinstance(output.simu.input, InputPower):
        raise Exception("Cannot run ElecLUTdq if Input is not InputPower")

    machine = output.simu.machine
    OP = output.elec.OP

    # Maximum voltage
    Urms_max = output.simu.input.Urms_max
    # Electrical frequency
    felec = OP.get_felec()
    # Electrical pulsation
    ws = 2 * np.pi * felec
    # Stator winding number of phases
    qs = machine.stator.winding.qs
    # Get winding resistance
    Rs = machine.stator.comp_resistance_wind(T=self.Tsta)

    if self.type_skin_effect > 0:
        # Account for skin effect
        kr_skin = machine.stator.winding.conductor.comp_skin_effect_resistance(
            T_op=self.Tsta, freq=OP.get_felec()
        )
        Rs *= kr_skin
    else:
        kr_skin = 1

    # Maximum phase current
    Irms_max = output.simu.input.Irms_max

    if self.LUT_enforced is not None:
        # Take enforced LUT
        LUT = self.LUT_enforced

        # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
        OP_matrix = LUT.get_OP_matrix()
        self.Id_min = OP_matrix[:, 1].min()
        self.Id_max = OP_matrix[:, 1].max()
        self.Iq_min = OP_matrix[:, 2].min()
        self.Iq_max = OP_matrix[:, 2].max()

    else:
        # Run look up table calculation
        # Check dq current boundaries
        if self.Id_min is None:
            if self.n_Id == 1 and self.Id_max is not None:
                self.Id_min = self.Id_max
            else:
                self.Id_min = -Irms_max
        if self.Id_max is None:
            if self.n_Id == 1 and self.Id_min is not None:
                self.Id_max = self.Id_min
            else:
                self.Id_max = Irms_max
        if self.Iq_min is None:
            if self.n_Iq == 1 and self.Iq_max is not None:
                self.Iq_min = self.Iq_max
            else:
                self.Iq_min = -Irms_max
        if self.Iq_max is None:
            if self.n_Iq == 1 and self.Iq_min is not None:
                self.Iq_max = self.Iq_min
            else:
                self.Iq_max = Irms_max

        # Run method to calculate LUT
        LUT = self.comp_LUTdq()

        # Store LUT
        output.simu.elec.LUT_enforced = LUT

    # Check if there is a loss model
    is_loss_model = LUT.simu.loss is not None

    # iteration until convergence is reached, and max number of iterations on EEC
    delta_Pem = 1e10
    delta_Pem_max = 0.1
    Nmax = 20
    niter_Pem = 1
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
    while abs(delta_Pem) > delta_Pem_max and niter_Pem < Nmax:

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

        if is_loss_model:
            # Interpolate losses from LUT:
            # - 1st column : Joule losses
            # - 2nd column : stator core losses
            # - 3rd column : magnet losses
            # - 4th column : rotor core losses
            # - 5th column : proximity losses
            Ploss_dqh = LUT.interp_Ploss_dqh(Id, Iq, N0=OP.N0)
            Ploss_ovl = np.sum(Ploss_dqh, axis=1)
        else:
            # Only consider stator Joule losses
            Ploss_ovl = qs * Rs * (Id ** 2 + Iq ** 2)

        if is_loss_model:
            # The input power must cover electrical power + additional losses
            P_in = qs * (Ud * Id + Uq * Iq) + np.sum(Ploss_dqh[:, 1:], axis=1)
        else:
            # The input power must cover electrical power + Joule losses
            P_in = qs * (Ud * Id + Uq * Iq)

        # The output power is the input power minus all losses
        P_out = P_in - Ploss_ovl

        # Set input/ouput power condition
        if OP.Pem_av_in is None:
            P_cond = P_out >= OP.Pem_av_ref
        else:
            P_cond = P_in >= OP.Pem_av_in

        # Set maximum voltage condition
        U_cond = Umax_interp <= Urms_max

        # Set maximum current condition
        I_cond = Imax_interp <= Irms_max

        # Finding indices of operating points satisfying voltage, current and power conditions
        i0 = np.logical_and.reduce((U_cond, I_cond, P_cond))

        if np.any(i0):
            # Finding index of operating point with lowest losses among feasible operating points
            imin = np.argmin(Ploss_ovl[i0])

            # Get error between calculated and requested powers
            if OP.Pem_av_in is None:
                delta_Pem = P_out[i0][imin] - OP.Pem_av_ref
            else:
                delta_Pem = P_in[i0][imin] - OP.Pem_av_in

            if abs(delta_Pem) > delta_Pem_max:
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

            niter_Pem = niter_Pem + 1

        else:
            # Find strategy to get closest to requested power although violating voltage / current constraints
            i1 = np.logical_and(P_cond, U_cond)
            i2 = np.logical_and(P_cond, I_cond)

            if np.any(i1):
                # Only consider requested power and voltage constraint
                i0 = i1
            elif np.any(i2):
                # Only consider requested power and current constraint
                i0 = i2
            else:
                # Only consider requested power
                i0 = P_cond

            if np.any(i0):
                # Find indices of operating points that reaches power
                if OP.Pem_av_in is None:
                    P_min = np.min(P_out[i0])
                    P_cond = P_out == P_min
                else:
                    P_min = np.min(P_in[i0])
                    P_cond = P_out == P_min

                if np.where(P_cond)[0].size == 1:
                    # Take the only point that reaches requested power
                    imin = 0
                else:
                    # Take the operating point that minimizes voltage
                    imin = np.argmin(Umax_interp[i0])

                # Get error between calculated and requested powers
                if OP.Pem_av_in is None:
                    delta_Pem = P_out[i0][imin] - OP.Pem_av_ref
                else:
                    delta_Pem = P_in[i0][imin] - OP.Pem_av_in

                if abs(delta_Pem) > delta_Pem_max:
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

                niter_Pem = niter_Pem + 1

            else:
                # Find operating point that get closest to requested power
                if OP.Pem_av_in is None:
                    P_max = np.max(P_out)
                    i0 = P_out == P_max
                else:
                    P_max = np.max(P_in)
                    i0 = P_out == P_max

                if np.where(i0)[0].size == 1:
                    # Take the closest point to requested power
                    imin = 0
                else:
                    # Take the operating point that minimizes voltage
                    imin = np.argmin(Umax_interp[i0])

                # Stop loop
                delta_Pem = delta_Pem_max

    # Launch warnings
    if OP.Pem_av_in is None and P_out[i0][imin] < OP.Pem_av_ref:
        self.get_logger().warning(
            "Output power cannot be reached within current and voltage constraints, taking maximum feasible power"
        )

    elif OP.Pem_av_in is not None and P_in[i0][imin] < OP.Pem_av_in:
        self.get_logger().warning(
            "Input power cannot be reached within current and voltage constraints, taking maximum feasible power"
        )

    if Umax_interp[i0][imin] > Urms_max:
        self.get_logger().warning("Voltage constraint cannot be reached")

    if Imax_interp[i0][imin] > Irms_max:
        self.get_logger().warning("Current constraint cannot be reached")

    # Store electrical quantities
    output.elec.P_out = P_out[i0][imin]
    output.elec.P_in = P_in[i0][imin]
    output.elec.OP.efficiency = output.elec.P_out / output.elec.P_in
    if output.simu.input.is_generator:
        # Calculate torque from input power
        output.elec.Tem_av = output.elec.P_in / (2 * np.pi * OP.N0 / 60)
    else:
        # Calculate torque from output power
        output.elec.Tem_av = output.elec.P_out / (2 * np.pi * OP.N0 / 60)

    if is_loss_model:
        output.elec.Pj_losses = Ploss_dqh[i0, 0][imin]
    else:
        output.elec.Pj_losses = Ploss_ovl[i0][imin]

    # Store voltage and currents
    output.elec.OP.Id_ref = Id[i0][imin]
    output.elec.OP.Iq_ref = Iq[i0][imin]
    output.elec.OP.Ud_ref = Ud[i0][imin]
    output.elec.OP.Uq_ref = Uq[i0][imin]

    # Store EEC parameters
    output.elec.eec = EEC_PMSM(
        Phid=Phid[i0][imin],
        Phiq=Phiq[i0][imin],
        R1=Rs,
        Tsta=self.Tsta,
        Trot=self.Trot,
        type_skin_effect=self.type_skin_effect,
        Xkr_skinS=kr_skin,
    )

    if is_loss_model:
        # Store losses
        output.loss = OutLoss(
            Pjoule=Ploss_dqh[i0, 0][imin],
            Pstator=Ploss_dqh[i0, 1][imin],
            Pmagnet=Ploss_dqh[i0, 2][imin],
            Protor=Ploss_dqh[i0, 3][imin],
            Pprox=Ploss_dqh[i0, 4][imin],
        )

    # Calculate slot current density
    output.elec.get_Jrms()

    # Calculate linear current density along airgap
    Irms = np.sqrt(output.elec.OP.Id_ref ** 2 + output.elec.OP.Iq_ref ** 2)
    Irms_slot = Irms * machine.stator.winding.Ntcoil / machine.stator.winding.Npcp
    slot_pitch = 2 * np.pi / machine.stator.get_Zs() * machine.stator.Rint
    output.elec.Arms = Irms_slot / slot_pitch

    # Calculate back-emf rms value
    Phid_mag = LUT.get_Phi_dqh_mag_mean()[0]
    output.elec.Erms = ws * Phid_mag

    # Calculate inductances
    if Id[i0][imin] != 0:
        output.elec.eec.Ld = (Phid[i0][imin] - Phid_mag) / Id[i0][imin]
    if Iq[i0][imin] != 0:
        output.elec.eec.Lq = Phiq[i0][imin] / Iq[i0][imin]

    # Calculate torque ripple
    Tem_rip_pp = LUT.interp_Tem_rip_dqh(Id[i0][imin], Iq[i0][imin])
    output.mag.Tem_rip_pp = float(Tem_rip_pp)
    output.mag.Tem_rip_norm = np.abs(Tem_rip_pp / output.elec.Tem_av)
