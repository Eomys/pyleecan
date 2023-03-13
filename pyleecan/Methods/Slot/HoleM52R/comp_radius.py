# -*- coding: utf-8 -*-

from numpy import exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the hole

    Parameters
    ----------
    self : HoleM52
        A HoleM52R object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the hole [m]

    """

    Rext = self.get_Rext()

    Rmax = Rext - self.H0

    alpha = self.comp_alpha()
    Z1 = (Rext - self.H0) * exp(1j * alpha / 2)
    Z5 = Z1.real - self.H1
    Rmin = abs(Z5)

    return (Rmin, Rmax)
