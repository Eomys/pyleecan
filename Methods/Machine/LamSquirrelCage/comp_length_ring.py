# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSquirrelCage.comp_length_ring
LamSquirrelCage Computation of ring length method
@date Created on Tue Jan 27 16:26:47 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import pi


def comp_length_ring(self):
    """Computation of the ring length

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    Lring: float
        Length of the ring [m]

    """

    Rmw = self.slot.comp_radius_mid_wind()

    return 2 * pi * Rmw
