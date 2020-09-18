# -*- coding: utf-8 -*-

from numpy import arctan


def comp_angle_opening_magnet(self):
    """Compute the angle at the top of the magnet in the slot (underneath the slot opening)

    Parameters
    ----------
    self : SlotMFlat2
        A SlotMFlat2 object

    Returns
    -------
    alpha: float
        Angle at the top of the magnet in the slot [rad]

    """
    Rbo = self.get_Rbo()
    W0 = self.comp_W0m()
    if self.is_outwards():
        return float(2 * arctan(W0 / (2 * (Rbo + self.H1))))
    else:
        return float(2 * arctan(W0 / (2 * (Rbo - self.H1))))

    # if self.W0_is_rad:
    #     return self.W0
    # else:  # Convert W0 from m to rad
    #     Rbo = self.get_Rbo()
    #     return float(2 * arcsin(self.W0 / (2 * Rbo)))
