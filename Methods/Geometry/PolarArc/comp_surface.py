# -*- coding: utf-8 -*-
"""@package Methods.Geometry.PolarArc.comp_surface
Compute the PolarArc surface method
@date Created on Thu Jul 27 13:51:43 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from numpy import pi


def comp_surface(self):
    """Compute the PolarArc surface

    Parameters
    ----------
    self : PolarArc
        A PolarArc object

    Returns
    -------
    surf: float
        The PolarArc surface [m**2]

    """

    Rint = abs(self.point_ref) - self.height / 2
    Rext = Rint + self.height

    return (pi * Rext ** 2 - pi * Rint ** 2) * (self.angle / (2 * pi))
