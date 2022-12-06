# -*- coding: utf-8 -*-

from numpy import arcsin, pi


def comp_alpha(self):
    """The opening angle incl. W1 width and a Rext - H0 radius

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    alpha: float
        Angle between P1 and P9 (cf schematics) [rad]

    """
    Rext = self.get_Rext()

    alpha = 2 * arcsin((2 * self.W1 + self.W0) / (2 * (Rext - self.H0)))

    return alpha
