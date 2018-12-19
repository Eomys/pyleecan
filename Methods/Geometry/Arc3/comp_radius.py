# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc3.comp_radius
Computation of Arc3 radius method
@date Created on Tue Mar 01 10:11:01 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import abs as np_abs


def comp_radius(self):
    """Compute the radius of the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    radius: float
        radius of the arc

    """

    self.check()

    z1 = self.begin
    z2 = self.end

    return np_abs(z1 - z2) / 2.0  # Radius of the arc
