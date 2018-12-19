# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW12.comp_surface
SlotW12 Computation of surface method
@date Created on Tue Mar 07 14:54:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    Rbo = self.get_Rbo()

    S1 = self.H0 * 2 * self.R2
    S2 = 4 * self.R1 * self.R2
    S3 = pi * self.R1 ** 2
    Swind = self.comp_surface_wind()

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S1 + S2 + S3 + Swind - Sarc
    else:
        return S1 + S2 + S3 + Swind + Sarc
