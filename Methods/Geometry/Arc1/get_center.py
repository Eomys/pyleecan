# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc1.get_center
Compute the coordinate of the center of an Arc1 method
@date Created on Fri Dec 05 13:37:19 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from numpy import abs as np_abs, angle as np_angle, arcsin, exp, pi


def get_center(self):
    """Return the center of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    Zc: complex
        Complex coordinates of the center of the Arc1
    """

    self.check()

    # The center is on the bisection of [begin, end]
    z1 = self.begin
    z2 = self.end
    R = self.radius

    # Centre at the middle of begin and end (distance(Z1, Z2) = diameter )
    if abs(abs(z2 - z1) - abs(2 * R)) < 1e-6:
        Zc = (z2 + z1) / 2.0
    else:
        # Alpha is the opening angle (Begin-Center-End)
        alpha = 2 * arcsin(abs(z2 - z1) / (2 * R))
        if R > 0:
            Zc = z2 + R * exp(1j * (np_angle(z2 - z1) % (2 * pi))) * exp(
                1j * (pi / 2 + np_abs(alpha) / 2)
            )
        else:
            Zc = z1 - R * exp(1j * (np_angle(z1 - z2) % (2 * pi))) * exp(
                1j * (pi / 2 + np_abs(alpha) / 2)
            )

    # Return (0,0) if the point is too close from 0
    if np_abs(Zc) < 1e-6:
        Zc = 0

    return Zc
