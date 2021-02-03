# -*- coding: utf-8 -*-

from numpy import arcsin, exp, pi, sqrt


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    point_dict = self._comp_point_coordinate()
    Z5 = point_dict["Z5"]
    if self.is_outwards():
        Ztan2 = Z5 + Z5.imag * (1 - 1j)
        return Ztan2.real - Rbo
    else:
        Ztan2 = Z5 + Z5.imag * (-1 - 1j)
        return Rbo - Ztan2.real
