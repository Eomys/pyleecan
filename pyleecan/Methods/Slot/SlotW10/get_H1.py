# -*- coding: utf-8 -*-

from numpy import tan


def get_H1(self):
    """Return H1 in [m]

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    H1: float
        H1 in [m]

    """

    if self.H1_is_rad:  # H1 in rad
        return ((self.W1 - self.W0) / 2.0) * tan(self.H1)  # convertion to m
    else:  # H1 in m
        return self.H1
