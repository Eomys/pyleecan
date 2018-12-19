# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Sep 19 10:16:45 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import pi


def comp_ratio_opening(self, p):
    """Compute the magnet pole arc width to pole width ratio

    Parameters
    ----------
    self : Magnet
        A Magnet object
    p : int
        Pole pair number

    Returns
    -------
    taum: float
        Ratio magnet pole arc width to pole width []

    """

    return self.comp_angle_opening() / (2 * pi / (2 * p))
