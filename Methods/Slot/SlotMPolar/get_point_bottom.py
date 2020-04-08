# -*- coding: utf-8 -*-
from numpy import arcsin, exp


def get_point_bottom(self):
    """Used to get the bottoms points of a single SlotMPolar

    Parameters
    ----------
    self : SlotMPolar
        A SlotMPolar object


    Returns
    -------
    (Z1, Z2) : tuple
        points at the bottom of the SlotMPolar

    """

    Rbo = self.get_Rbo()

    if self.is_outwards():
        Z1 = (Rbo + self.H0) * exp(-1j * self.W0 / 2)
        Z2 = (Rbo + self.H0) * exp(1j * self.W0 / 2)
    else:
        Z1 = (Rbo - self.H0) * exp(-1j * self.W0 / 2)
        Z2 = (Rbo - self.H0) * exp(1j * self.W0 / 2)

    return (Z1, Z2)
