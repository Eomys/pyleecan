# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Sep 19 10:12:24 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import arcsin
from pyleecan.Methods import ParentMissingError


def comp_angle_opening(self):
    """Compute the opening angle of the magnet at the lamination bore radius

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    alpha_mag: float
        Magnet opening angle [rad]

    """

    if self.IS_FLAT_BOT:
        if self.parent is not None:
            (Z1, Z2) = self.parent.get_point_bottom()
            return 2 * arcsin(self.Wmag / (2 * abs(Z1)))
        else:
            raise ParentMissingError(
                "Error: The magnet object is not inside a " + "slot object"
            )
    else:
        return self.Wmag
