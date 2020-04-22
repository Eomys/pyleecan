# -*- coding: utf-8 -*-

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """
    Rbo = self.get_Rbo()

    return float(2 * arcsin(self.W0 / (2 * Rbo)))
