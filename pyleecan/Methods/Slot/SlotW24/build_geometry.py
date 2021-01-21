# -*- coding: utf-8 -*-

from ....Classes.Arc2 import Arc2
from ....Classes.Segment import Segment


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
    (_, alpha_2) = self.comp_alphas()

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Zc = 0

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc2(Z2, Zc, alpha_2))
    curve_list.append(Segment(Z3, Z4))

    return curve_list
