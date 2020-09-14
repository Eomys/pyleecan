# -*- coding: utf-8 -*-
from numpy import arcsin, exp


def get_point_bottom(self):
    """Used to get the bottoms points of a single SlotMFlat

    Parameters
    ----------
    self : SlotMFlat
        SlotMFlat object


    Returns
    -------
    (Z1, Z2) : tuple
        points at the bottom of the SlotMFlat

    """

    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening_magnet()

    if self.is_outwards():
        Z1 = Rbo * exp(-1j * alpha / 2) + self.H0
        Z2 = Rbo * exp(1j * alpha / 2) + self.H0
    else:
        Z1 = Rbo * exp(-1j * alpha / 2) - self.H0
        Z2 = Rbo * exp(1j * alpha / 2) - self.H0

    return (Z1, Z2)
