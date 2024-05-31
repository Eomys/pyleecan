# -*- coding: utf-8 -*-

from numpy import abs as np_abs
from numpy import sqrt


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    point_dict = self._comp_point_coordinate()
    Zmid = point_dict["Zmid"]
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    Rbo = self.get_Rbo()

    if self.is_outwards():
        return np_abs(sqrt(Z2.real**2 + Z2.imag**2)) - np_abs(Rbo)

    else:
        return self.H0
