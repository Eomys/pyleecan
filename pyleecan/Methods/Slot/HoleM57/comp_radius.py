# -*- coding: utf-8 -*-

from numpy import pi, cos, sin, tan, arcsin, exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]
    """
    Rbo = self.get_Rbo()

    Rmax = Rbo - self.H1

    # "Tooth" angle (P1',0,P1)
    alpha_T = 2 * arcsin(self.W3 / (2 * (Rbo - self.H1)))
    # magnet pole pitch angle (Z1,0,Z1')
    alpha_S = 2 * pi / self.Zh - alpha_T
    # Angle (P1,P1',P4') and (P5',P4', )
    alpha = (pi - self.W0) / 2

    Z1 = (Rbo - self.H1) * exp(-1j * alpha_S / 2)
    x11 = 2 * sin(alpha_S / 2) * (Rbo - self.H1)  # Distance from P1 to P1'
    # In rect triangle P4, P1, perp (P1,P1') with P4
    H = tan(alpha) * (x11 / 2 - self.W1 / 2)
    Z4 = Z1.real - H - 1 * self.W1 / 2
    x45 = self.H2 / cos(alpha)  # distance from P4 to P5
    Z5 = Z4 - x45

    Rmin = abs(Z5)

    return (Rmin, Rmax)
