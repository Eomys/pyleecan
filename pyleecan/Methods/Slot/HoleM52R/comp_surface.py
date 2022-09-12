# -*- coding: utf-8 -*-

from numpy import exp, pi, tan


def comp_surface(self):
    """Compute the surface of the Hole

    Parameters
    ----------
    self : HoleM52R
        A HoleM52R object

    Returns
    -------
    S: float
        Surface of the Hole. [m**2]

    """

    Smag = self.comp_surface_magnets()
    # one side rectangular air area
    Srect = self.W1 * (self.H1 - self.H2) - (4 - pi) * self.R0 ** 2 / 4

    return Smag + 2 * Srect
