# -*- coding: utf-8 -*-

from numpy import pi


def comp_length_ring(self):
    """Computation of the squirrel cage end-ring average perimeter (circumferential length)

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    Lring: float
        Length of the ring [m]

    """

    # calculation of the average radius of the center of the end-ring (distance to z-axis of the electrical machine)
    Rmw = self.slot.comp_radius_mid_active()

    return 2 * pi * Rmw
