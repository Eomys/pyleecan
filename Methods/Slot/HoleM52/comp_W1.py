# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Feb 01 17:47:04 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import exp, pi, tan


def comp_W1(self):
    """Compute W1 (cf schematics)

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    W1: float
        cf schematics [m]

    """

    Rbo = self.get_Rbo()

    alpha = self.comp_alpha()

    # Angle between (P1,P2) and (0,P0) is slot_pitch /2
    # It is also the angle (P1,P2,S)
    hsp = pi / self.Zh  # Half Slot Pitch

    # Distance P1,P9
    D19 = ((Rbo - self.H0) * exp(1j * alpha / 2)).imag * 2

    # S is the intersectioni between (P1,P9) and the parallel to x passing by P2
    D1S = tan(hsp) * (self.H1 - self.H2)

    return D19 / 2.0 - D1S - self.W0 / 2.0
