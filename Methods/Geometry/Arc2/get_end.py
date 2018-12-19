# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc2.get_end
Compute the coordinate of the end of an Arc2 method
@date Created on Mon Dec 08 13:22:57 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from numpy import abs as np_abs, exp


def get_end(self):
    """Return the end of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    end: complex
        Complex coordinates of the end of the Arc2
    """

    self.check()

    # the center is on the bisection of [begin, end]
    z1 = self.begin
    zc = self.center
    angle = self.angle

    # Geometric transformation : center is the origine (-zc)
    # Then rotation of begin of the correct angle (*exp(i*pi*angle))
    # Then return to the main axis (+zc)
    z2 = (z1 - zc) * exp(1j * angle) + zc

    # Return (0,0) if the point is too close from 0
    if np_abs(z2) < 1e-6:
        z2 = 0
    return z2
