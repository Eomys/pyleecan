# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Circle.comp_surface
Compute the circle surface method
@date Created on Thu Jul 27 13:51:43 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from numpy import pi


def comp_surface(self):
    """Compute the circle surface

    Parameters
    ----------
    self : Circle
        A Circle object

    Returns
    -------
    surf: float
        The circle surface [m**2]

    """

    return pi * self.radius ** 2
