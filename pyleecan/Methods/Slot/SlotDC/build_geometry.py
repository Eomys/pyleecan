# -*- coding: utf-8 -*-

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotDC
        A SlotDC object

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
        _,
        _,
        _,
    ] = self._comp_point_coordinate()

    # Adapt the lines according to the lamination
    if self.is_outwards():
        sign = 1
        direc = True
    else:
        sign = -1
        direc = False

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc1(Z2, Z3, sign * self.D1 / 2, is_trigo_direction=direc))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc1(Z4, Z5, sign * self.D2 / 2, is_trigo_direction=direc))
    curve_list.append(Segment(Z5, Z6))

    curve_list.append(Arc1(Z6, Z7, sign * self.R3, is_trigo_direction=direc))

    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Arc1(Z8, Z9, sign * self.D2 / 2, is_trigo_direction=direc))
    curve_list.append(Segment(Z9, Z10))
    curve_list.append(Arc1(Z10, Z11, sign * self.D1 / 2, is_trigo_direction=direc))
    curve_list.append(Segment(Z11, Z12))

    return curve_list
