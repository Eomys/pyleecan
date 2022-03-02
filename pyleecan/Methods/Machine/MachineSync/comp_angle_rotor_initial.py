def comp_angle_rotor_initial(self):
    """Compute rotor initial angle between rotor and stator d-axes
    Parameters
    ----------
    self : MachineSync
        A: MachineSync object
    Returns
    -------
    angle_rotor_initial: float
        rotor initial angle given by the difference of rotor and stator d-axes [rad]
    """

    return self.stator.comp_angle_d_axis() - self.rotor.comp_angle_d_axis()
