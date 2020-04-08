# -*- coding: utf-8 -*-

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    curve_list: list
        A list of 6 Segment and 5 Arc

    """

    [
        Z1,
        Z2,
        Z3,
        Z4,
        Z5,
        Z6,
        Z7,
        Z8,
        Z9,
        Z10,
        Z11,
        Z12,
        Z13,
    ] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Arc1(Z3, Z4, self.R1))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Arc1(Z5, Z6, self.R2))
    curve_list.append(Arc1(Z6, Z8, abs(Z7)))
    curve_list.append(Arc1(Z8, Z9, self.R2))
    curve_list.append(Segment(Z9, Z10))
    curve_list.append(Arc1(Z10, Z11, self.R1))
    curve_list.append(Segment(Z11, Z12))
    curve_list.append(Segment(Z12, Z13))

    return curve_list
