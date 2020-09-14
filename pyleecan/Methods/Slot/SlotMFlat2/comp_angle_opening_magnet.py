# -*- coding: utf-8 -*-

from numpy import arctan


def comp_angle_opening_slot(self):
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
    return float(2 * arctan(self.W1 / (2 * (Rbo + self.H0))))
