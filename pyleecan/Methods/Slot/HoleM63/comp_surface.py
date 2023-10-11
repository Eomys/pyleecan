# -*- coding: utf-8 -*-

from numpy import sqrt, arctan, sin, arcsin


def comp_surface(self):
    """Compute the surface of the Hole

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object

    Returns
    -------
    S: float
        Surface of the Hole. [m**2]

    """
    if self.top_flat:
        return self.H0 * self.W0

    else:
        Rbo = self.get_Rbo()
        alpha = 2 * arcsin((self.W0 / 2) / (Rbo - self.H1))

        return self.H0 * self.W0 + (((Rbo - self.H1) ** 2) * (alpha - sin(alpha)) / 2)
