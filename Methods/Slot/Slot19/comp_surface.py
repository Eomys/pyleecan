# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot19.comp_surface
Slot19 Computation of surface method
@date Created on Mon Jun 29 15:28:55 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
@todo: unittest
"""

from numpy import sin, pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : Slot19
        A Slot19 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    Rbo = self.get_Rbo()

    # Wint is the with at the top of the opening
    alpha0 = self.comp_angle_opening()
    alpha1 = self.comp_angle_bottom()

    if self.is_outwards():
        R1 = Rbo + self.H0
    else:
        R1 = Rbo - self.H0

    W0 = 2 * Rbo * sin(alpha0 / 2)
    W1 = 2 * R1 * sin(alpha1 / 2)

    Str = 1 / 2 * (W0 + W1) * self.H0
    S0 = Rbo ** 2 / 2 * (alpha0 - sin(alpha0))
    S1 = R1 ** 2 / 2 * (alpha1 - sin(alpha1))

    return Str + S1 - S0
