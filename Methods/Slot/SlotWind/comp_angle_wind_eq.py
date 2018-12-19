# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotWind.comp_angle_eq
SlotW10 Computation of average angle method
@date Created on Tue Dec 09 17:07:09 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi


def comp_angle_wind_eq(self):
    """Compute the equivalent angle of the winding part of the slot
    (Ideal polar shape with the same surface and height)

    Parameters
    ----------
    self : SlotWind
        A SlotWind object

    Returns
    -------
    alpha: float
        Average angle of the slot [rad]

    """

    Swind = self.comp_surface_wind()
    Hwind = self.comp_height_wind()
    Rmw = self.comp_radius_mid_wind()
    Rext = Rmw + Hwind / 2
    Rint = Rmw - Hwind / 2

    return Swind * 2 * pi / (pi * Rext ** 2 - pi * Rint ** 2)
