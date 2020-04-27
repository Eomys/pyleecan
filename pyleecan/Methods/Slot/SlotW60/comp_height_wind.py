# -*- coding: utf-8 -*-

from numpy import pi, exp


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11] = self._comp_point_coordinate()

    # Compute the point in the tooth ref
    hsp = pi / self.Zs
    Z4t = Z4 * exp(1j * hsp)
    Zw4t = Z4t - self.H3 + 1j * ((self.W1 - self.W2) / 2 - self.W3)

    return abs(Zw4t) - abs(Z5)
