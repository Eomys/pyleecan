# -*- coding: utf-8 -*-

from numpy import cos, exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the hole

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the hole [m]

    """

    Rext = self.get_Rext()

    Rmax = Rext - self.H1
    Z7 = Rext - self.H0 - 1j * self.W1 / 2
    Z6 = Z7 - 1j * (self.H2 - self.H3) * cos(self.W4)
    Z4 = (self.W2 - 1j * self.H3) * exp(-1j * self.W4) + Z6

    Rmin = min(abs(Z7), abs(Z4))
    return (Rmin, Rmax)
