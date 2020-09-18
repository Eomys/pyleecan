# -*- coding: utf-8 -*-
from numpy import sin, exp


def get_point_bottom(self):
    """Used to get the bottoms points of a single SlotMFlat2

    Parameters
    ----------
    self : SlotMFlat
        SlotMFlat object


    Returns
    -------
    (Z1, Z2) : tuple
        points at the bottom of the SlotMFlat

    """

    alpha = self.comp_angle_opening_magnet()
    R1 = self.comp_W0m() / (2 * sin(alpha / 2))

    if self.is_outwards():
        Z1 = R1 * exp(-1j * alpha / 2) + self.H0
        Z2 = R1 * exp(1j * alpha / 2) + self.H0
    else:
        Z1 = R1 * exp(-1j * alpha / 2) - self.H0
        Z2 = R1 * exp(1j * alpha / 2) - self.H0

    return (Z1, Z2)
