# -*- coding: utf-8 -*-

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the object.
    The ending point of a curve is the starting point of the next curve
    in the list

    Parameters
    ----------
    self : SlotUD
        A SlotUD object

    Returns
    -------
    curve_list: list
        A list of Segments

    """

    return self.line_list.copy()
