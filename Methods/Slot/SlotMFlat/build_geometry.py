# -*- coding: utf-8 -*-

from numpy import exp

from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is always the starting point of the next curve
    in the list

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    curve_list: list
        A list of 3 Segment for each slot + W3 arc

    """
    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening()
    alpha_mag = self.comp_angle_opening_magnet()

    # Point coordinate for a slot center on Ox
    Z1 = Rbo * exp(-1j * alpha_mag / 2)
    Z2 = Rbo * exp(1j * alpha_mag / 2)
    if self.is_outwards():
        Z3 = Z1 + self.H0
        Z4 = Z2 + self.H0
    else:
        Z3 = Z1 - self.H0
        Z4 = Z2 - self.H0

    # Curve list of a single slot
    curve_list = list()
    if self.H0 > 0:
        curve_list.append(Segment(Z1, Z3))
    curve_list.append(Segment(Z3, Z4))
    if self.H0 > 0:
        curve_list.append(Segment(Z4, Z2))

    # Complete curve list for all the slots (for one pole)
    slot_list = list()
    for ii in range(len(self.magnet)):
        # Compute angle of the middle of the slot
        beta = -alpha / 2 + alpha_mag / 2 + ii * (self.W3 + alpha_mag)
        # Duplicate and rotate the slot + bore for each slot
        for line in curve_list:
            new_line = type(line)(init_dict=line.as_dict())
            new_line.rotate(beta)
            slot_list.append(new_line)
        if ii != len(self.magnet) - 1:  # Add the W3 except for the last slot
            slot_list.append(Arc2(slot_list[-1].get_end(), 0, self.W3))

    return slot_list
