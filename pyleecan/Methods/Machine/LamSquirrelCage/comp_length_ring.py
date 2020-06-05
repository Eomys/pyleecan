# -*- coding: utf-8 -*-

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
