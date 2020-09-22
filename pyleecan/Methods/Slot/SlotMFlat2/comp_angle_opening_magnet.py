# -*- coding: utf-8 -*-

from numpy import arctan


def comp_angle_opening_magnet(self):
    """Compute the opening angle at the top of the slot

    Parameters
    ----------
    self : SlotMFlat2
        A SlotMFlat2 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    if self.W1 > 0:
        Rbo = self.get_Rbo()
        return float(2 * arctan(self.W1 / (2 * Rbo)))
    else:
        return self.comp_angle_magnet()
