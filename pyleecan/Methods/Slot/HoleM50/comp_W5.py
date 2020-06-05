# -*- coding: utf-8 -*-

from numpy import cos


def comp_W5(self):
    """Compute the W5 width of the slot (cf schematics)

    Parameters
    ----------
    self : HoleM50
        a HoleM50 object

    Returns
    -------
    W5: float
        Cf schematics [m]

    """

    alpha = self.comp_alpha()

    # Distance fromZ8 to Z9
    L89 = (self.W0 / 2 - self.W1 / 2) / cos(alpha)

    return L89 - self.W4 - self.W2
