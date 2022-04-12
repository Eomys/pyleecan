import numpy as np

from ....Classes.OutLoss import OutLoss

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
    machine = output.simu.machine
    OP = output.elec.OP

    # Maximum voltage
    U_max = output.simu.input.U_max
    # Input useful power to reach
    Pem_av_ref = OP.Pem_av_ref
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

    # Maximum phase current
    I_max = output.simu.input.I_max

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
                self.Id_min = -I_max
        if self.Id_max is None:
            if self.n_Id == 1 and self.Id_min is not None:
                self.Id_max = self.Id_min
            else:
                self.Id_max = I_max
        if self.Iq_min is None:
            if self.n_Iq == 1 and self.Iq_max is not None:
                self.Iq_min = self.Iq_max
            else:
                self.Iq_min = -I_max
        if self.Iq_max is None:
            if self.n_Iq == 1 and self.Iq_min is not None:
                self.Iq_max = self.Iq_min
            else:
                self.Iq_max = I_max

        # Run method to calculate LUT
        LUT = self.comp_LUTdq()

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
    Nd = self.n_Id if self.n_Id == 1 else self.n_interp
    Nq = self.n_Iq if self.n_Iq == 1 else self.n_interp
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
            # Interpolate losses from LUT
            Ploss_dqh = LUT.interp_Ploss_dqh(Id, Iq, N0=OP.N0)
            Ploss_ovl = np.sum(Ploss_dqh, axis=1)
        else:
            # Only consider stator Joule losses
            Ploss_ovl = qs * Rs * (Id ** 2 + Iq ** 2)

        # Calculate electromagnetic power
        Pem_av_interp = qs * (Ud * Id + Uq * Iq)

        # Calculate useful power by substracting losses
        Puse_interp = Pem_av_interp - Ploss_ovl

        # Finding indices of operating points satisfying maximum voltage/current and input power
        i0 = np.logical_and.reduce(
            (Umax_interp <= U_max, Imax_interp <= I_max, Puse_interp >= Pem_av_ref)
        )
        if np.any(i0):
            # Finding index of operating point with lowest losses among feasible operating points
            imin = np.argmin(Ploss_ovl[i0])

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

            delta_Pem = Puse_interp[i0][imin] - Pem_av_ref
            niter_Pem = niter_Pem + 1

        else:
            # Finding indices of operating points only satisfying maximum voltage/current
            i0 = np.logical_and.reduce((Umax_interp <= U_max, Imax_interp <= I_max))
            # Finding index of operating points that maximize the power
            imin = np.argmax(Puse_interp[i0])
            # Stop loop
            delta_Pem = delta_Pem_max
            self.get_logger().info(
                "Input power cannot be reached within current and voltage constraints, taking maximum feasible power"
            )

    # Store electrical quantities
    output.elec.Pem_av = Pem_av_interp[i0][imin]
    output.elec.P_useful = Puse_interp[i0][imin]
    output.elec.Tem_av = Puse_interp[i0][imin] / (2 * np.pi * OP.N0 / 60)
    if is_loss_model:
        output.elec.Pj_losses = Ploss_dqh[i0, 0][imin]
    else:
        output.elec.Pj_losses = Ploss_ovl[i0][imin]
    output.elec.OP.Id_ref = Id[i0][imin]
    output.elec.OP.Iq_ref = Iq[i0][imin]
    output.elec.OP.Ud_ref = Ud[i0][imin]
    output.elec.OP.Uq_ref = Uq[i0][imin]

    if is_loss_model:
        # Store losses
        output.loss = OutLoss(
            Pjoule=Ploss_dqh[i0, 0][imin],
            Pstator=Ploss_dqh[i0, 1][imin],
            Pmagnet=Ploss_dqh[i0, 2][imin],
            Protor=Ploss_dqh[i0, 3][imin],
            Pprox=Ploss_dqh[i0, 4][imin],
        )
