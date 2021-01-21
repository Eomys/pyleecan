# -*- coding: utf-8 -*-

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


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
    curve_list.append(Arc1(Z2, Z3, -abs(Z2), is_trigo_direction=False))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Arc1(Z4, Z5, abs(Z5)))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Arc1(Z6, Z7, -abs(Z2), is_trigo_direction=False))
    curve_list.append(Segment(Z7, Z8))
    return curve_list
