# -*- coding: utf-8 -*-
from numpy import arcsin, pi


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    alpha = float(arcsin(self.W3 / (2 * self.get_Rbo())))
    return 2 * pi / self.Zs - 2 * alpha
