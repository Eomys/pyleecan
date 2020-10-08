# -*- coding: utf-8 -*-


def get_rot_dir(self):
    """Return the rotation direction

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    rot_dir: int
        Rotation direction

    """

    # Already available => Return
    if self.geo.rot_dir is not None:
        return self.geo.rot_dir
    else:  # Compute
        rot_dir = self.simu.machine.stator.comp_rot_dir()
        self.geo.rot_dir = rot_dir
        return rot_dir
