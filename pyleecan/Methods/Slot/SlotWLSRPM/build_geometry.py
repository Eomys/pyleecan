# -*- coding: utf-8 -*-

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    curve_list: llist
        A list of 5 Segments and 2 Arcs

    """

    Rbo = self.get_Rbo()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc1(Z2, Z3, self.R1, is_trigo_direction=True))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Arc1(Z6, Z7, self.R1, is_trigo_direction=True))
    curve_list.append(Segment(Z7, Z8))

    return curve_list
