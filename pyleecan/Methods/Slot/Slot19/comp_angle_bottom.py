# -*- coding: utf-8 -*-

from numpy import arcsin


def comp_angle_bottom(self):
    """Compute the slot bottom angle of the Slot

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    alpha: float
        slot bottom angle [rad]

    """

    Rbo = self.get_Rbo()

    if self.Wx_is_rad:
        return self.W1
    else:
        if self.is_outwards():
            alpha = 2 * float(arcsin(self.W1 / (2 * Rbo + 2 * self.H0)))
        else:  # inward slot
            alpha = 2 * float(arcsin(self.W1 / (2 * Rbo - 2 * self.H0)))

    return alpha
