# -*- coding: utf-8 -*-

from numpy import arcsin, exp, sqrt

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Segment) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    curve_list: list
        A list of 4 Segment and 3 Arc1

    """
    Rbo = self.get_Rbo()

    # getting all point coordinate
    [
        Z1,
        Z2,
        Z3,
        Z4,
        Z5,
        Z6,
        Z7,
        Z8,
        Ztan1,
        Ztan2,
        Zmid,
        Zrad1,
        Zrad2,
        rot_sign,
    ] = self._comp_point_coordinate()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1]

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.H1 > 0:
        curve_list.append(
            Arc1(Z2, Z3, rot_sign * self.R1, is_trigo_direction=self.is_outwards())
        )
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Arc3(Z4, Z5, self.is_outwards()))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(
            Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=self.is_outwards())
        )
    elif self.H1 == 0:
        curve_list.append(
            Arc1(Z2, Z3, rot_sign * self.R1, is_trigo_direction=self.is_outwards())
        )
        curve_list.append(Arc3(Z3, Z6, self.is_outwards()))
        curve_list.append(
            Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=self.is_outwards())
        )
    else:  # Should never be called
        raise (Slot26_H1, "H1 can't be <0")

    curve_list.append(Segment(Z7, Z8))

    return curve_list


class Slot26_H1(Exception):
    """ """

    pass
