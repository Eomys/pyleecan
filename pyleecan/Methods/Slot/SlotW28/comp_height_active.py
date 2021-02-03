# -*- coding: utf-8 -*-

from numpy import arcsin, exp, pi, sqrt


def comp_height_active(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    point_dict = self._comp_point_coordinate()
    Z2 = point_dict["Z2"]
    Z5 = point_dict["Z5"]
    Z7 = point_dict["Z7"]
    if self.is_outwards():
        Ztan2 = Z5 + Z5.imag * (-1 - 1j)
    else:
        Ztan2 = Z5 + Z5.imag * (+1 - 1j)
    Ztan1 = (Z2 + Z7) / 2.0

    return abs(Ztan2 - Ztan1)
