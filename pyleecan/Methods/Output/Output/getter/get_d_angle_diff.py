# -*- coding: utf-8 -*-


def get_d_angle_diff(self):
    """Return the initial d axis angle

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    d_angle_diff: float
        difference between the d axis angle of the stator and the rotor [rad]

    """

    # Already available => Return
    if self.geo.d_angle_diff is not None and self.geo.d_angle_diff.size > 0:
        return self.geo.d_angle_diff
    else:  # Compute
        d_angle_diff = self.simu.machine.stator.comp_angle_d_axis() - self.simu.machine.rotor.comp_angle_d_axis()
        self.geo.d_angle_diff = d_angle_diff
        return d_angle_diff
