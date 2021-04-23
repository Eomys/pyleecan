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
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]
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
