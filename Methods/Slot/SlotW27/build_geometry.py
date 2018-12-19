# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW27.build_geometry
SlotW27 build_geometry method
@date Created on Tue Mar 07 10:52:09 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin, exp

from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object

    Returns
    -------
    curve_list: list
        A list of 9 Segment

    """
    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z10|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 + self.H1 + (self.W2 - self.W1) / 2.0 * 1j
        Z5 = Z4 + self.H2 + (self.W3 - self.W2) / 2.0 * 1j
    else:  # inward slot
        Z2 = Z1 - self.H0
        Z3 = Z2 + (self.W1 - self.W0) * 1j / 2.0
        Z4 = Z3 - self.H1 + (self.W2 - self.W1) / 2.0 * 1j
        Z5 = Z4 - self.H2 + (self.W3 - self.W2) / 2.0 * 1j

    # symetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = [
        Z10,
        Z9,
        Z8,
        Z7,
        Z6,
        Z5,
        Z4,
        Z3,
        Z2,
        Z1,
    ]

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Segment(Z9, Z10))

    return curve_list
