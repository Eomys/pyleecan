# -*- coding: utf-8 -*-

from numpy import arcsin, exp

from ....Classes.Arc3 import Arc3
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    curve_list: list
        A list of 4 Segment and 3 Arc3

    """

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = 2*R2
    alpha = float(arcsin(self.R2 / Rbo))

    # comp point coordinate (in complex)
    Z0 = Rbo * exp(1j * 0)
    Z1 = Z0 * exp(-1j * alpha)

    if self.is_outwards():
        Z2 = Z1 + self.H0
        Z3 = Z2 + self.R1 * 2
        Z4 = Z3 + self.H1
        rot_sign = True
    else:  # inward slot
        Z2 = Z1 - self.H0
        Z3 = Z2 - self.R1 * 2
        Z4 = Z3 - self.H1
        rot_sign = False

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Z7 = Z2.conjugate()
    Z8 = Z1.conjugate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.R1 > 0:  # R1=0 => Z2==Z3
        curve_list.append(Arc3(Z2, Z3, rot_sign))
    if self.H1 > 0:  # H1=0 => Z3==Z4
        curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc3(Z4, Z5, rot_sign))
    if self.H1 > 0:  # H1=0 => Z5==Z6
        curve_list.append(Segment(Z5, Z6))
    if self.R1 > 0:  # R1=0 => Z6==Z7
        curve_list.append(Arc3(Z6, Z7, rot_sign))
    curve_list.append(Segment(Z7, Z8))

    return curve_list
