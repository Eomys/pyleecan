# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc3.comp_length
Computation of Arc3 length method
@date Created on Tue Mar 01 10:13:25 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import pi


def comp_length(self):
    """Compute the length of the arc

    Parameters
    ----------
    self : Arc3
        An Arc3 object

    Returns
    -------
    length: float
        length of the arc
    """

    self.check()

    R = self.comp_radius()

    # Half circle
    return float(pi * R)
