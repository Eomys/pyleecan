# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMFlat.comp_surface
SlotMFlat Computation of surface method
@date Created on Mon Dec 22 13:25:11 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    W0m = self.comp_W0m()
    S1 = self.H0 * W0m

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 - Sarc
    else:
        return S1 + Sarc
