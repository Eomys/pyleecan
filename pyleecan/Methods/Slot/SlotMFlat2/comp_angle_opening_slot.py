# -*- coding: utf-8 -*-

from numpy import arcsin


def comp_angle_opening_slot(self):
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
        return float(2 * arcsin(self.W1 / (2 * Rbo)))
    else: 
        return self.comp_angle_opening()
