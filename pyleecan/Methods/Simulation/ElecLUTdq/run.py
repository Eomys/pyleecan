import numpy as np

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
            self.Id_min = -I_max
        if self.Id_max is None:
            self.Id_max = I_max
        if self.Iq_min is None:
            self.Iq_min = -I_max
        if self.Iq_max is None:
            self.Iq_max = I_max

        # Run method to calculate LUT
        LUT = self.comp_LUTdq()

    # iteration until convergence is reached, and max number of iterations on EEC
    delta_Pem = 1e10
    delta_Pem_max = 0.1
    Nmax = 20
    niter_Pem = 1
    Id_min = self.Id_min
    Id_max = self.Id_max
    Iq_min = self.Iq_min
    Iq_max = self.Iq_max
    Ndq = self.n_interp
    while abs(delta_Pem) > delta_Pem_max and niter_Pem < Nmax:

        # Refine Id/Iq mesh
        Id_vect = np.linspace(Id_min, Id_max, Ndq)
        Iq_vect = np.linspace(Iq_min, Iq_max, Ndq)
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

        # TODO: interpolate iron losses from LUT
        Piron = 0

        # Calculate Joule losses
        Plosses = Rs * (Id ** 2 + Iq ** 2) + Piron

        # Calculate useful power by substracting losses
        Pem_interp = qs * (Ud * Id + Uq * Iq) - Plosses

        # Calculate electromagnetic torque
        Tem_interp = Pem_interp / (2 * np.pi * OP.N0 / 60)

        # Finding indices of operating points satisfying maximum voltage/current and input power
        i0 = np.logical_and.reduce(
            (Umax_interp <= U_max, Imax_interp <= I_max, Pem_interp >= Pem_av_ref)
        )

        # Finding index of operating points with lowest losses among feasible operating points
        imin = np.argmin(Plosses[i0])

        # Store electrical quantities contained in out_dict in OutElec
        output.elec.Pem_av_ref = Pem_interp[i0][imin]
        output.elec.Tem_av_ref = Tem_interp[i0][imin]
        output.elec.OP.Id_ref = Id[i0][imin]
        output.elec.OP.Iq_ref = Iq[i0][imin]
        output.elec.OP.Ud_ref = Ud[i0][imin]
        output.elec.OP.Uq_ref = Uq[i0][imin]

        jd = np.where(Id_vect == Id[i0][imin])[0][0]
        jq = np.where(Iq_vect == Iq[i0][imin])[0][0]

        jd_min = max([jd - 1, 0])
        jd_max = min([jd + 1, Ndq - 1])
        jq_min = max([jq - 1, 0])
        jq_max = min([jq + 1, Ndq - 1])

        Id_min = Id_vect[jd_min]
        Id_max = Id_vect[jd_max]
        Iq_min = Iq_vect[jq_min]
        Iq_max = Iq_vect[jq_max]

        delta_Pem = Pem_interp[i0][imin] - Pem_av_ref
        niter_Pem = niter_Pem + 1
