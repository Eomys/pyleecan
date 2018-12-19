# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW27.comp_surface
SlotW27 Computation of surface method
@date Created on Mon Mar 07 17:34:45 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object

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
