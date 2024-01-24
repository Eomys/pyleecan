from numpy import pi


from ....Classes.MachineSIPMSM import MachineSIPMSM
from ....Classes.SubdomainModel_SPMSM import SubdomainModel_SPMSM


def comp_flux_airgap(self, output, axes_dict, Is_val=None, Ir_val=None):
    """Build and solve Subdomain model (SDM) to calculate and store magnetic quantities

    Parameters
    ----------
    self : MagSDM
        a MagSDM object
    output : Output
        an Output object
    axes_dict: {Data}
        Dict of axes used for magnetic calculation

    Returns
    -------
    out_dict: dict
        Dict containing the following quantities:
            Br : ndarray
                Airgap radial flux density (Nt,Na) [T]
            Bt : ndarray
                Airgap tangential flux density (Nt,Na) [T]
            Tem : ndarray
                Electromagnetic torque over time (Nt,) [Nm]
            Phi_wind_stator : ndarray
                Stator winding flux (qs,Nt) [Wb]
            Phi_wind : dict
                Dict of winding fluxlinkage with respect to Machine.get_lam_list_label (qs,Nt) [Wb]
            meshsolution: MeshSolution
                MeshSolution object containing magnetic quantities B, H, mu for each time step
    """

    logger = self.get_logger()

    # Init output
    out_dict = dict()

    # Get time and angular axes
    Angle = axes_dict["angle"]
    Time = axes_dict["time"]

    # Set the angular symmetry factor according to the machine and check if it is anti-periodic
    per_a, is_antiper_a = Angle.get_periodicity()

    # Import angular vector from Data object
    angle = Angle.get_values(
        is_oneperiod=self.is_periodicity_a,
        is_antiperiod=is_antiper_a and self.is_periodicity_a,
    )

    # Check if the time axis is anti-periodic
    _, is_antiper_t = Time.get_periodicity()

    # Number of time steps
    time = Time.get_values(
        is_oneperiod=self.is_periodicity_t,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )
    Nt = time.size

    # Get rotor angular position
    angle_rotor = output.get_angle_rotor()[0:Nt]

    self.subdomain_model.per_a = per_a
    self.subdomain_model.is_antiper_a = is_antiper_a
    self.subdomain_model.machine_polar_eq = output.simu.machine.get_polar_eq()

    self.subdomain_model.set_subdomains(self.Nharm_coeff, Is_val, self.is_mmfr)

    (
        out_dict["B_{rad}"],
        out_dict["B_{circ}"],
        out_dict["Tem"],
        out_dict["Phi_wind_stator"],
    ) = self.subdomain_model.solve(angle, angle_rotor)

    return out_dict
