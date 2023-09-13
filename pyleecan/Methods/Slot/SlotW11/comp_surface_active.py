# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    S3 = 0.5 * (self.W1 + self.W2) * (self.H2 - self.R1)
    S4 = pi * self.R1 ** 2 / 2.0 + self.R1 * (self.W2 - 2 * self.R1)

    return S3 + S4
