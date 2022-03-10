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

    # Maximum current density
    J_max = output.simu.input.J_max
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

    # Calculate maximum current function of current density
    Swire = machine.stator.winding.conductor.comp_surface_active()

    Nwire = (
        machine.stator.winding.conductor.Nwppc_rad
        * machine.stator.winding.conductor.Nwppc_tan
    )
    Npcp = machine.stator.winding.Npcp
    Imax = J_max * Swire * Npcp * Nwire

    # Run look up table calculation
    self.Id_min = -Imax
    self.Iq_max = Imax
    LUT = self.comp_LUTdq()

    # Refine Id/Iq mesh
    Id, Iq = np.meshgrid(
        np.linspace(self.Id_min, self.Id_max, self.n_interp * self.n_Id),
        np.linspace(self.Iq_min, self.Iq_max, self.n_interp * self.n_Iq),
    )
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
        (Umax_interp <= U_max, Imax_interp <= Imax, Pem_interp >= Pem_av_ref)
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
