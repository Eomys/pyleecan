# -*- coding: utf-8 -*-

from numpy import tan


def get_H1(self):
    """Return H1 in [m]

    Parameters
    ----------
    self : SlotW21
        A SlotW21 object

    Returns
    -------
    H1: float
        H1 in [m]

    """
    if self.is_cstt_tooth:
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()

    if self.H1_is_rad:  # H1 in rad
        return ((self.W1 - self.W0)* tan(self.H1) / 2.0)   # convertion to m
    else:  # H1 in m
        return self.H1
