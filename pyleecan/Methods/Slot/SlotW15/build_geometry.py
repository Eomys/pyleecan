# -*- coding: utf-8 -*-

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


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

    line_dict = self._comp_line_dict()

    curve_list = [
        line_dict["1-2"],
        line_dict["2-3"],
        line_dict["3-4"],
        line_dict["4-5"],
        line_dict["5-6"],
        line_dict["6-8"],
        line_dict["8-9"],
        line_dict["9-10"],
        line_dict["10-11"],
        line_dict["11-12"],
        line_dict["12-13"],
    ]
    return [line for line in curve_list if line is not None]
