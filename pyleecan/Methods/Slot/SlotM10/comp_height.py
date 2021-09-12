# -*- coding: utf-8 -*-

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    Rbo = self.get_Rbo()

    if self.is_outwards():
        return abs(Z2) - Rbo
    else:
        return Rbo - abs((Z2 + Z3) / 2)
