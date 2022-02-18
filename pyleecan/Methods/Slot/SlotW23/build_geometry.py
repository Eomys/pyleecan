# -*- coding: utf-8 -*-

from numpy import arcsin, exp, angle

from ....Classes.Segment import Segment

from ....Classes.Arc1 import Arc1


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    curve_list: list
        A list of 6 Segment and 1 Arc

    """

    line_dict = self._comp_line_dict()

    curve_list = [
        line_dict["1-2"],
        line_dict["2-3"],
        line_dict["3-4"],
        line_dict["4-5"],
        line_dict["5-6"],
        line_dict["6-7"],
        line_dict["7-8"],
    ]
    return [line for line in curve_list if line is not None]
