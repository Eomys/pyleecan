# -*- coding: utf-8 -*-

from numpy import angle, arcsin, arctan, array, cos, exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """
    Rext = self.get_Rext()

    Rmax = Rext - self.H1

    # magnet pole pitch angle, must be <2*pi/2*p
    alpham = 2 * arcsin(self.W0 / (2 * (Rext - self.H1)))

    Harc = (Rext - self.H1) * (1 - cos(alpham / 2))
    gammam = arctan((self.H0 - self.H1 - Harc) / (self.W0 / 2.0 - self.W1 / 2.0))

    x78 = (self.H3 - self.H2) / cos(gammam)  # distance from 7 to 8
    Z9 = Rext - Harc - self.H1 - 1j * self.W0 / 2.0
    Z8 = Rext - self.H0 - 1j * self.W1 / 2.0
    Z7 = Rext - self.H0 - x78 - 1j * self.W1 / 2.0

    # Magnet coordinate with Z8 as center and x as the top edge of the magnet
    Z8b = self.W2
    Z8c = Z8b + self.W4
    Z5 = Z8b - 1j * self.H3
    Z4 = Z8c - 1j * self.H3
    Z6 = Z5 + 1j * self.H2
    Z3 = Z4 + 1j * self.H2

    Zmag = array([Z8b, Z6, Z5, Z4, Z3, Z8c])
    Zmag = Zmag * exp(1j * angle(Z9 - Z8))
    Zmag = Zmag + Z8

    # final complex numbers Zmag=[Z8b Z6 Z5 Z4 Z3 Z8c]
    (Z8b, Z6, Z5, Z4, Z3, Z8c) = Zmag

    Rmin = min(abs(Z5), abs(Z7))

    return (Rmin, Rmax)
