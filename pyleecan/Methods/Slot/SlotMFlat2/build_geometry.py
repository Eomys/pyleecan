# -*- coding: utf-8 -*-

from numpy import exp, sin

from ....Classes.Arc2 import Arc2
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is always the starting point of the next curve
    in the list

    Parameters
    ----------
    self : SlotMFlat2
        A SlotMFlat2 object

    Returns
    -------
    curve_list: list
        A list of 7 Segments for each slot + W3 arc

    """
    Rbo = self.get_Rbo()
    alpha = self.comp_angle_opening()
    alpha_slot = self.comp_angle_opening_slot()
    alpha_mag = self.comp_angle_opening_magnet()

    # Point coordinate for a slot center on Ox
    Z1 = Rbo * exp(-1j * alpha_slot / 2)
    Z8 = Rbo * exp(1j * alpha_slot / 2)

    R1 = self.comp_W0m() / (2 * sin(alpha_mag / 2))
    Z3 = R1 * exp(-1j * alpha_mag / 2)
    Z6 = R1 * exp(1j * alpha_mag / 2)

    if self.is_outwards():
        Z2 = Z1 + self.H1
        Z7 = Z8 + self.H1
        Z4 = Z3 + self.H0
        Z5 = Z6 + self.H0
    else:
        Z2 = Z1 - self.H1
        Z7 = Z8 - self.H1
        Z4 = Z3 - self.H0
        Z5 = Z6 - self.H0

    # Curve list of a single slot
    curve_list = list()
    if self.H1 > 0:
        curve_list.append(Segment(Z1, Z2))

    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))

    if self.H1 > 0:
        curve_list.append(Segment(Z7, Z8))

    # Copied from SlotMFlat. Probably not working for more than one Magnet
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
