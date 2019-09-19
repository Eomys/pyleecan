# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW26.build_geometry
SlotW26 build_geometry method
@date Created on Mon Feb 22 11:24:38 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin, exp, sqrt

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Segment) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    curve_list: list
        A list of 4 Segment and 3 Arc1

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        ZC1 = Z2.real + sqrt(self.R1 ** 2 - (self.W0 / 2.0) ** 2)
        Z3 = ZC1 + self.R1 * 1j
        Z4 = Z3 + self.H1
        rot_sign = 1  # Rotation direction for Arc1
    else:  # inward slot
        Z2 = Z1 - self.H0
        ZC1 = Z2.real - sqrt(self.R1 ** 2 - (self.W0 / 2.0) ** 2)
        Z3 = ZC1 + self.R1 * 1j
        Z4 = Z3 - self.H1
        rot_sign = -1  # Rotation direction for Arc1

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.H1 > 0:
        curve_list.append(Arc1(Z2, Z3, rot_sign * self.R1, self.is_outwards()))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Arc3(Z4, Z5, self.is_outwards()))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Arc1(Z6, Z7, rot_sign * self.R1, self.is_outwards()))
    elif self.H1 == 0:
        curve_list.append(Arc1(Z2, Z3, rot_sign * self.R1, self.is_outwards()))
        curve_list.append(Arc3(Z3, Z6, self.is_outwards()))
        curve_list.append(Arc1(Z6, Z7, rot_sign * self.R1, self.is_outwards()))
    else:  # Should never be called
        raise (Slot26_H1, "H1 can't be <0")

    curve_list.append(Segment(Z7, Z8))

    return curve_list


class Slot26_H1(Exception):
    """ """

    pass
