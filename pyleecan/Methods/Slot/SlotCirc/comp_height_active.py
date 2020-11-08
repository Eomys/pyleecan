# -*- coding: utf-8 -*-

from numpy import exp


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]
    """

    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening()

    Z1 = Rbo * exp(-1j * alpha / 2)
    Z2 = Rbo * exp(1j * alpha / 2)
    if self.is_outwards():
        Zbot = (Z1 + Z2) / 2 + self.H0
    else:
        Zbot = (Z1 + Z2) / 2 - self.H0
    return abs(Rbo - abs(Zbot))
