# -*- coding: utf-8 -*-
from numpy import pi, exp, arcsin, sin
from ....Functions.Geometry.inter_line_line import inter_line_line


def _comp_point_coordinate(self):
    """Compute the point coordinate needed to plot the Slot.

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates

    """

    Rbo = self.get_Rbo()
    hsp = pi / self.Zs  # Half slot pitch

    alpha = arcsin(self.W1 / (2 * Rbo))

    # Point used to define geometry of slot
    Z1 = Rbo * exp(1j * alpha)
    Z2 = Z1 - self.H2
    Z3 = Z2 - ((self.W1 - self.W0) / 2) * sin(self.H1) - 1j * ((self.W1 - self.W0) / 2)
    Z4 = Z3 - self.H0

    # Set points in correct base with a rotation
    Z1 = Z1 * exp(-1j * hsp)
    Z2 = Z2 * exp(-1j * hsp)
    Z3 = Z3 * exp(-1j * hsp)
    Z4 = Z4 * exp(-1j * hsp)

    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()

    Zmid = (Z2 + Z7) / 2

    # Zw are points used to define geometry of winding
    Zw1 = Zmid - 1j * self.W2 / 2
    Zc = Zw1 - 1
    Zw2 = inter_line_line(Z5, Z4, Zw1, Zc)
    Zw2 = Zw2[0]

    Zw1s = Zw1.conjugate()
    Zw2s = Zw2.conjugate()

    point_dict = dict()
    # symetry
    point_dict["Z1"] = Z1
    point_dict["Z2"] = Z2
    point_dict["Z3"] = Z3
    point_dict["Z4"] = Z4
    point_dict["Z5"] = Z5
    point_dict["Z6"] = Z6
    point_dict["Z7"] = Z7
    point_dict["Z8"] = Z8

    point_dict["Zw1"] = Zw1
    point_dict["Zw2"] = Zw2
    point_dict["Zw1s"] = Zw1s
    point_dict["Zw2s"] = Zw2s

    return point_dict
