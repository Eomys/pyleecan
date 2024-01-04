# -*- coding: utf-8 -*-
from numpy import pi, exp, arcsin


def _comp_point_coordinate(self):
    """Compute the point coordinate needed to plot the Slot.

    Parameters
    ----------
    self : SlotW62
        A SlotW62 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates

    """

    Rbo = self.get_Rbo()
    hsp = pi / self.Zs  # Half slot pitch

    alpha2 = arcsin(self.W1 / (2 * Rbo))

    # Point used to define geometry of slot
    Z1 = Rbo * exp(-1j * hsp)
    Z1 = Z1 * exp(1j * hsp)
    Z1 = Z1 * exp(1j * alpha2)

    Z2 = Z1 - self.H1
    Z3 = Z2 - ((self.W1 - self.W0) / 2) * 1j
    Z4 = Z3 - self.H0

    # Zw are points used to define geometry of winding
    Zw1 = Z3 + self.W3 * 1j - self.H3
    Zw2 = Zw1 - self.H2
    Zw3 = Zw2 + self.W2 * 1j
    Zw4 = Zw1 + self.W2 * 1j

    # Set points in correct base with a rotation
    Z1 = Z1 * exp(-1j * hsp)
    Z2 = Z2 * exp(-1j * hsp)
    Z3 = Z3 * exp(-1j * hsp)
    Z4 = Z4 * exp(-1j * hsp)
    Zw1 = Zw1 * exp(-1j * hsp)
    Zw2 = Zw2 * exp(-1j * hsp)
    Zw3 = Zw3 * exp(-1j * hsp)
    Zw4 = Zw4 * exp(-1j * hsp)

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()

    Zw1s = Zw1.conjugate()
    Zw2s = Zw2.conjugate()
    Zw3s = Zw3.conjugate()
    Zw4s = Zw4.conjugate()

    point_dict = dict()
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
    point_dict["Zw3"] = Zw3
    point_dict["Zw4"] = Zw4
    point_dict["Zw1s"] = Zw1s
    point_dict["Zw2s"] = Zw2s
    point_dict["Zw3s"] = Zw3s
    point_dict["Zw4s"] = Zw4s

    return point_dict
