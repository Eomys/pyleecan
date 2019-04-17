# -*- coding: utf-8 -*-
"""@package Methods.Slot.HoleM50.comp_alpha
Compute the magnets angle of slot type 53
@date Created on Mo Apr 15 09:00:00 2019
@author sebastian_g
@todo unittest it
"""
from numpy import pi


def comp_alpha(self):
    """Compute the magnets angle of the slot type 53

    Parameters
    ----------
    self : HoleM53
        a HoleM53 object

    Returns
    -------
    alpha: float
        magnet angle [rad]
    """
    return pi / 2 - self.W4
