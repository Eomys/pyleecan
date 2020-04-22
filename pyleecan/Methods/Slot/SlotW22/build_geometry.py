# -*- coding: utf-8 -*-

from numpy import exp

from ....Classes.Arc2 import Arc2
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Segment) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    curve_list: llist
        A list of 5 Segment and 3 Arc2

    """
    Rbo = self.get_Rbo()

    # comp point coordinate (in complex)
    Z1 = Rbo * exp(-1j * self.W0 / 2)
    if self.is_outwards():
        R1 = Rbo + self.H0
        R2 = Rbo + self.H0 + self.H2
    else:  # inward slot
        R1 = Rbo - self.H0
        R2 = Rbo - self.H0 - self.H2
    Z2 = R1 * exp(-1j * self.W0 / 2.0)
    Z3 = R1 * exp(-1j * self.W2 / 2.0)
    Z4 = R2 * exp(-1j * self.W2 / 2.0)

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()
    Zc = 0

    # Creation of curve
    curve_list = list()
    if self.H0 > 0:
        curve_list.append(Segment(Z1, Z2))
    if self.W2 != self.W0:
        curve_list.append(Arc2(Z2, Zc, -(self.W2 - self.W0) / 2))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc2(Z4, Zc, self.W2))
    curve_list.append(Segment(Z5, Z6))
    if self.W2 != self.W0:
        curve_list.append(Arc2(Z6, Zc, -(self.W2 - self.W0) / 2))
    if self.H0 > 0:
        curve_list.append(Segment(Z7, Z8))

    return curve_list
