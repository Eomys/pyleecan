# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW23.build_geometry
SlotW23 build_geometry method
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo add constant tooth support
@todo unittest it
"""

from numpy import arcsin, exp, angle

from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.Arc1 import Arc1


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    curve_list: list
        A list of 6 Segment and 1 Arc

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()
    Zc = 0
    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc1(Z4, Z5, abs(Z5)))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))

    return curve_list
