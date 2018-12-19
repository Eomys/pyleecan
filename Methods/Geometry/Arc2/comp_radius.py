# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc2.comp_radius
Computation of Arc2 radius method
@date Created on Fri Feb 12 09:52:45 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import abs as np_abs


def comp_radius(self):
    """Compute the radius of the arc

    Parameters
    ----------
    self : Arc2
        An Arc2 object

    Returns
    -------
    radius: float
        radius of the arc
    """

    self.check()

    z1 = self.begin
    zc = self.center
    return np_abs(z1 - zc)  # Radius of the arc
