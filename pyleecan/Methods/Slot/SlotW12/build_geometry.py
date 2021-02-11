# -*- coding: utf-8 -*-

from numpy import arcsin, exp

from ....Classes.Arc3 import Arc3
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve
    in the list

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    curve_list: list
        A list of 4 Segment and 3 Arc3

    """

    if self.is_outwards():
        rot_sign = True
    else:  # inward slot
        rot_sign = False

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.R1 > 0:  # R1=0 => Z2==Z3
        curve_list.append(Arc3(Z2, Z3, rot_sign))
    if self.H1 > 0:  # H1=0 => Z3==Z4
        curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc3(Z4, Z5, rot_sign))
    if self.H1 > 0:  # H1=0 => Z5==Z6
        curve_list.append(Segment(Z5, Z6))
    if self.R1 > 0:  # R1=0 => Z6==Z7
        curve_list.append(Arc3(Z6, Z7, rot_sign))
    curve_list.append(Segment(Z7, Z8))

    return curve_list
