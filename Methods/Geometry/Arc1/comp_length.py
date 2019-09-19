# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc1.comp_length
Computation of Arc1 length method
@date Created on Fri Dec 05 14:25:08 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from numpy import pi, arcsin


def comp_length(self):
    """Compute the length of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    length: float
        length of the arc
    """

    self.check()

    R = self.radius

    # alpha is the opening angle
    alpha = self.get_angle()

    # 2*pi*R is the length of the total circle
    # The arc is an alpha / 2pi portion of the cercle
    return float(2 * pi * R * (alpha / (2 * pi)))
