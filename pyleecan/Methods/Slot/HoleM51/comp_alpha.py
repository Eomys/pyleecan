# -*- coding: utf-8 -*-

from numpy import arctan, cos, sin, pi


def comp_alpha(self):
    """Compute the angle of the Hole (cf schematics)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    alpha: float
        Angle of the Hole (cf schematics) [rad]

    """
    Rbo = self.get_Rbo()

    alpha = -arctan(
        2
        * (self.H0 - self.H1 * cos(0.5 * self.W1) + Rbo * cos(0.5 * self.W1) - Rbo)
        / (2.0 * self.H1 * sin(0.5 * self.W1) - 2 * Rbo * sin(0.5 * self.W1) + self.W0)
    )

    return alpha
