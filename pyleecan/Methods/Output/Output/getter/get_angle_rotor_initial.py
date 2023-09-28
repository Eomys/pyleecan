def get_angle_rotor_initial(self):
    """Return the difference between the d axis angle of the stator and the rotor

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    angle_rotor_initial: float
        difference between the d axis angle of the stator and the rotor [rad]

    """

    # Already available => Return
    if self.geo.angle_rotor_initial is not None:
        return self.geo.angle_rotor_initial
    else:  # Compute
        self.geo.angle_rotor_initial = self.simu.machine.comp_angle_rotor_initial()
        return self.geo.angle_rotor_initial
