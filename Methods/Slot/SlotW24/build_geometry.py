# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW24.build_geometry
SlotW24 build_geometry method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    curve_list: list
        A list of 2 Segment and 1 Arc

    """
    (alpha_0, alpha_2) = self.comp_alphas()
    [Z1, Z2, Z3, Z4] = self._comp_point_coordinate()
    Zc = 0
    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc2(Z2, Zc, alpha_2))
    curve_list.append(Segment(Z3, Z4))

    return curve_list
