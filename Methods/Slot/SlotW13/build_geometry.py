# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW13.build_geometry
SlotW13 build_geometry method
@date Created on Mon Jul 11 12:39:27 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object

    Returns
    -------
    curve_list: list
        A list of 9 Segment

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    if self.H0 > 0:
        curve_list.append(Segment(Z1, Z2))
    if self.H1 > 0 and self.W1 > self.W0:
        curve_list.append(Segment(Z2, Z3))
    if self.W1 > self.W2:
        curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    if self.W1 > self.W2:
        curve_list.append(Segment(Z7, Z8))
    if self.H1 > 0 and self.W1 > self.W0:
        curve_list.append(Segment(Z8, Z9))
    if self.H0 > 0:
        curve_list.append(Segment(Z9, Z10))

    return curve_list
