# -*- coding: utf-8 -*-

from numpy import arcsin, arctan, cos


def comp_alpha(self):
    """Compute the alpha angle of the slot (cf schematics)

    Parameters
    ----------
    self : HoleM50
        a HoleM50 object

    Returns
    -------
    alpha: float
        Cf schematics [rad]
    """
    Rbo = self.get_Rbo()

    alpham = 2 * arcsin(self.W0 / (2 * (Rbo - self.H1)))

    Harc = (Rbo - self.H1) * (1 - cos(alpham / 2))
    return arctan((self.H0 - self.H1 - Harc) / (self.W0 / 2 - self.W1 / 2))
