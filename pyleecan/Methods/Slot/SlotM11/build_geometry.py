# -*- coding: utf-8 -*-
from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

    Returns
    -------
    curve_list: list
        A list of 3 Segments

    """
    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, _, _, _, _] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    if self.H0 > 0:
        curve_list.append(Segment(Z1, Z2))
    if self.is_outwards():
        curve_list.append(Arc1(Z2, Z3, Rbo + self.H0, is_trigo_direction=True))
    else:
        curve_list.append(Arc1(Z2, Z3, Rbo - self.H0, is_trigo_direction=True))
    if self.H0 > 0:
        curve_list.append(Segment(Z3, Z4))

    return curve_list
