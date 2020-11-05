# -*- coding: utf-8 -*-


def get_rot_dir(self):
    """Return the rotation direction of the magnetic field fundamental
    WARNING: rot_dir = -1 to have positive rotor rotating direction, i.e. rotor position moves towards positive angle

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    rot_dir: int
        Rotation direction of magnetic field fundamental

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
        rot_dir = self.simu.machine.stator.comp_rot_dir()
        
    self.geo.rot_dir = rot_dir
    return rot_dir
