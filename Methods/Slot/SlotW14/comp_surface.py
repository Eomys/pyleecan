# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Mar 31 12:30:37 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import arcsin, cos, pi, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9] = self._comp_point_coordinate()
    W1 = abs(Z7.imag) * 2

    S1 = (W1 + self.W0) * self.H1 / 2
    S0 = self.W0 * self.H0

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    Swind = self.comp_surface_wind()

    if self.is_outwards():
        return S1 + S0 + Swind - Sarc
    else:
        return S1 + S0 + Swind + Sarc
