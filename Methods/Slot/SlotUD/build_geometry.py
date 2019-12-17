# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW11.build_geometry
SlotW11 build_geometry method
@date Created on Tue Jun 30 14:54:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve
    in the list

    Parameters
    ----------
    self : SlotUD
        A SlotUD object

    Returns
    -------
    curve_list: list
        A list of Segments

    """

    # Apply symmetry if needed
    point_list = self.point_list.copy()
    if self.is_sym:
        for point in self.point_list[::-1]:
            point_list.append(point.conjugate())

    # Creation of curve
    curve_list = list()
    for ii in range(len(point_list) - 1):
        curve_list.append(Segment(point_list[ii], point_list[ii + 1]))

    return curve_list
