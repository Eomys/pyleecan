# -*- coding: utf-8 -*-

from numpy import sin, pi


def comp_surface(self):
    """Compute the Hole total surface (by analytical computation).

    Parameters
    ----------
    self : HoleM60
        A HoleM60 object

    Returns
    -------
    S: float
        Hole total surface [m**2]

    """
    # Two discus of radius H0 / 2
    S1 = 2 * (pi * (self.H0 / 2) ** 2)
    # Two rectangles of dimensions (W2 - H0) x H0
    S2 = 2 * ((self.W2 - self.H0) * self.H0)

    return S1 + S2
