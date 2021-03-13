# -*- coding: utf-8 -*-
from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotM17
        A SlotM17 object

    Returns
    -------
    curve_list: list
        Empty list (no lamination, only active surface)

    """

    return list()
