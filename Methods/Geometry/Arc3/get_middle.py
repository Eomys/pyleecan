# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc3.get_middle
Compute the coordinate of the middle of an Arc3 method
@date Created on Wed May 04 11:04:12 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import abs as np_abs, angle as np_angle, exp, pi


def get_middle(self):
    """Return the point at the middle of the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    Zmid: complex
        Complex coordinates of the middle of the Arc3
    """

    # We use the complex representation of the point
    z1 = self.begin
    zc = self.get_center()
    R = self.comp_radius()

    # Generation of the point by rotation
    if self.is_trigo_direction:  # Top
        Zmid = R * exp(1j * pi / 2.0)
    else:  # Bottom
        Zmid = R * exp(-1j * pi / 2.0)

    # Geometric transformation : return to the main axis
    Zmid = Zmid * exp(1j * np_angle(z1 - zc)) + zc

    # Return (0,0) if the point is too close from 0
    if np_abs(Zmid) < 1e-6:
        Zmid = 0

    return Zmid
