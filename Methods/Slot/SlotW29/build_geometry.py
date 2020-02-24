# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW29.build_geometry
SlotW29 build_geometry method
@date Created on Thu Feb 23 10:36:36 2017
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    curve_list: list
        A list of 11 Segment

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    if self.H0 > 0:
        curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    if self.H1 > 0:
        curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    if self.H1 > 0:
        curve_list.append(Segment(Z9, Z10))
    curve_list.append(Segment(Z10, Z11))
    if self.H0 > 0:
        curve_list.append(Segment(Z11, Z12))

    return curve_list
