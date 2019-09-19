# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW25.build_geometry
SlotW25 build_geometry method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    curve_list: list
        A list of 4 Segment and 3 Arc

    """
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()
    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z8, Z7))
    curve_list.append(Arc1(Z7, Z6, -abs(Z2), is_trigo_direction=False))
    curve_list.append(Segment(Z6, Z5))
    curve_list.append(Arc1(Z5, Z4, abs(Z5)))
    curve_list.append(Segment(Z4, Z3))
    curve_list.append(Arc1(Z3, Z2, -abs(Z2), is_trigo_direction=False))
    curve_list.append(Segment(Z2, Z1))
    return curve_list
