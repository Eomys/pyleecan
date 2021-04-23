# -*- coding: utf-8 -*-

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM16
        A SlotM16 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    point_dict = self._comp_point_coordinate()
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]

    Rbo = self.get_Rbo()

    if self.is_outwards():
        return abs(Z4) - Rbo
    else:
        return Rbo - abs((Z4 + Z5) / 2)
