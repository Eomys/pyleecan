# -*- coding: utf-8 -*-

def get_rot_dir(self):
    """Return the rotation direction

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    alpha_rotor: numpy.ndarray
        angular position of the rotor as a function of time (vector) [rad]

    """

    # Already available => Return
    if self.geo.rot_dir is not None and self.geo.rot_dir.size > 0:
        return self.geo.rot_dir
    else:  # Compute
        return self.simu.machine.stator.comp_rot_dir()
