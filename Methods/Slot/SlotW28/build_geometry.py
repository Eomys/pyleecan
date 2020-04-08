# -*- coding: utf-8 -*-

from numpy import arcsin, exp, pi, sqrt

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    curve_list: list
        A list of 4 Segment and 3 Arc1

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, rot_sign] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc1(Z2, Z3, rot_sign * self.R1, self.is_outwards()))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc3(Z4, Z5, self.is_outwards()))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Arc1(Z6, Z7, rot_sign * self.R1, self.is_outwards()))
    curve_list.append(Segment(Z7, Z8))

    return curve_list
