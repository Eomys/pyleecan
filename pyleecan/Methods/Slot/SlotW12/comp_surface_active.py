# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    S3 = 2 * self.R2 * self.H1
    S4 = pi * self.R2**2 / 2.0

    return S3 + S4
