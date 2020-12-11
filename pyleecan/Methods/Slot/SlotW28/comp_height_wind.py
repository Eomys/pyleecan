# -*- coding: utf-8 -*-

from numpy import arcsin, exp, pi, sqrt


def comp_height_wind(self):
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

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, rot_sign] = self._comp_point_coordinate()
    if self.is_outwards():
        Ztan2 = Z5 + Z5.imag * (-1 - 1j)
    else:
        Ztan2 = Z5 + Z5.imag * (+1 - 1j)
    Ztan1 = (Z2 + Z7) / 2.0

    return abs(Ztan2 - Ztan1)
