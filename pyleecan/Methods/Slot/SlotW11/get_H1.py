# -*- coding: utf-8 -*-

from numpy import tan


def get_H1(self):
    """Return H1 in [m]

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    H1: float
        H1 in [m]

    """

    if self.H1_is_rad:  # H1 in rad
        H1 = (self.W1 - self.W0) / 2.0 * tan(self.H1)  # convertion to m
    else:  # H1 in m
        H1 = self.H1
