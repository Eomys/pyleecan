# -*- coding: utf-8 -*-

from numpy import sin


def comp_width(self):
    """Compute the width of the Hole (cf schematics)

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    Whole: float
        Width of the Hole (cf schematics) [m]

    """

    Rbo = self.get_Rbo()
    return 2 * sin(self.W1 / 2) * (Rbo - self.H1)
