# -*- coding: utf-8 -*-

from numpy import sin


def comp_W0m(self):
    """Compute (or return) W0 in [m]

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    W0m: float
        W0 in [m]

    """

    if self.W0_is_rad:  # Convert W0 to m
        Rbo = self.get_Rbo()
        return 2 * Rbo * sin((self.W0 / 2))
    else:
        return self.W0
