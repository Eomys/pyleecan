# -*- coding: utf-8 -*-
from numpy import pi, exp, arcsin


def _comp_point_coordinate(self):
    """Compute the point coordinate needed to plot the Slot.

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    point_dict: dict
        A dict of the slot point coordinates

    """

    Rbo = self.get_Rbo()
    hsp = pi / self.Zs
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # Zxt => In the tooth ref (Ox as the sym axis of the tooth)
    Z1t = Rbo * exp(1j * alpha)
    Z2t = Z1t.real - self.H0 + 1j * self.W1 / 2
    Z3t = Z2t - self.H1
    Z4t = Z3t - 1j * (self.W1 - self.W2) / 2
    Z5t = Z4t - self.H2

    # Go to the slot ref
    Z1 = Z1t * exp(-1j * hsp)
    Z2 = Z2t * exp(-1j * hsp)
    Z3 = Z3t * exp(-1j * hsp)
    Z4 = Z4t * exp(-1j * hsp)
    Z5 = Z5t * exp(-1j * hsp)
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()

    # Compute the point in the tooth ref
    Z4t = Z4 * exp(1j * hsp)
    Z5t = Z5 * exp(1j * hsp)
    Zw1t = Z4t - self.H3
    Zw2t = Z5t + self.H4
    Zw3t = Zw2t + 1j * ((self.W1 - self.W2) / 2 - self.W3)
    Zw4t = Zw1t + 1j * ((self.W1 - self.W2) / 2 - self.W3)

    # Go back to slot ref
    Zw1 = Zw1t * exp(1j * -hsp)
    Zw2 = Zw2t * exp(1j * -hsp)
    Zw3 = Zw3t * exp(1j * -hsp)
    Zw4 = Zw4t * exp(1j * -hsp)
    Zw1s = Zw1.conjugate()
    Zw2s = Zw2.conjugate()
    Zw3s = Zw3.conjugate()
    Zw4s = Zw4.conjugate()

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
    point_dict["Z9"] = Z9
    point_dict["Z10"] = Z10
    point_dict["Zw5"] = (Z3t - self.H2) * exp(-1j * hsp)
    point_dict["Zw5s"] = point_dict["Zw5"].conjugate()
    point_dict["Zw1"] = Zw1
    point_dict["Zw2"] = Zw2
    point_dict["Zw3"] = Zw3
    point_dict["Zw4"] = Zw4
    point_dict["Zw1s"] = Zw1s
    point_dict["Zw2s"] = Zw2s
    point_dict["Zw3s"] = Zw3s
    point_dict["Zw4s"] = Zw4s

    return point_dict
