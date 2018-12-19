# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc2.get_middle
Compute the coordinate of the middle of an Arc2 method
@date Created on Wed May 04 10:56:53 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from numpy import abs as np_abs, angle as np_angle, exp


def get_middle(self):
    """Return the point at the middle of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    Zmid: complex
        Complex coordinates of the middle of the Arc2
    """

    self.check()

    # We use the complex representation of the point
    z1 = self.begin
    zc = self.center

    # Geometric transformation : center is the origine, angle(begin) = 0
    Zstart = (z1 - zc) * exp(-1j * np_angle(z1 - zc))

    # Generation of the point by rotation
    Zmid = Zstart * exp(1j * self.angle / 2.0)

    # Geometric transformation : return to the main axis
    Zmid = Zmid * exp(1j * np_angle(z1 - zc)) + zc

    # Return (0,0) if the point is too close from 0
    if np_abs(Zmid) < 1e-6:
        Zmid = 0

    return Zmid
