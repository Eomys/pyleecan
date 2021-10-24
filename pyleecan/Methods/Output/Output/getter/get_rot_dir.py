def get_rot_dir(self):
    """Return the rotation direction of rotor and magnetic field fundamental

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    rot_dir: int
        Rotation direction of rotor and magnetic field fundamental

    """

    # Already available => Return
    if self.geo.rot_dir is not None:
        return self.geo.rot_dir
    # check for imposed rot_dir in Simulation
    elif (
        self.simu is not None
        and self.simu.input is not None
        and hasattr(self.simu.input, "rot_dir")
        and self.simu.input.rot_dir is not None
    ):
        rot_dir = self.simu.input.rot_dir
    else:  # Compute from stator winding
        rot_dir = self.simu.machine.stator.comp_rot_dir(
            N0=self.elec.OP.get_N0(), felec=self.elec.OP.get_felec()
        )

    self.geo.rot_dir = rot_dir
    return rot_dir
