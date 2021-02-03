# -*- coding: utf-8 -*-

from numpy import arcsin, exp


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    point_dict = self._comp_point_coordinate()
    Z4 = point_dict["Z4"]
    Rbo = self.get_Rbo()

    if self.is_outwards():
        return abs(Z4) - Rbo
    else:  # inward slot
        return Rbo - abs(Z4)
