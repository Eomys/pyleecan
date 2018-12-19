# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW28.comp_surface
SlotW28 Computation of surface method
@date Created on Wed Jul 13 12:22:18 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    S1 = self.H0 * self.W0
    Swind = self.comp_surface_wind()

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 + Swind - Sarc
    else:
        return S1 + Swind + Sarc
