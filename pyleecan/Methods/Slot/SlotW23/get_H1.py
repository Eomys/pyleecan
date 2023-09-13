# -*- coding: utf-8 -*-

from numpy import tan
from numpy import arcsin, exp, sqrt, pi
from ....Functions.Geometry.inter_line_line import inter_line_line


def get_H1(self):
    """Return H1 in [m]

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    H1: float
        H1 in [m]

    """

    if not (self.H1_is_rad):
        return self.H1

    Rbo = self.get_Rbo()

    # alpha is the angle to rotate Z0 so ||Z1,Z8|| = W0
    alpha = float(arcsin(self.W0 / (2 * Rbo)))

    if self.is_outwards():
        Z2 = (Rbo + self.H0) * exp(-1j * alpha)

    else:  # inward slot
        Z2 = (Rbo - self.H0) * exp(-1j * alpha)

    if self.H1_is_rad:  # H1 in rad
        if self.is_cstt_tooth:
            Z2t = Z2 * exp(1j * pi / self.Zs)
            Zangle = exp(-1j * ((pi / 2) - self.H1)) + Z2t

            Zt1 = 1j * (self.W3 / 2)
            Zt2 = 1 + (1j * self.W3) / 2
            L = inter_line_line(Zt1, Zt2, Z2t, Zangle)
            Z3 = L[0]
            return abs(Z3.real - Z2.real)

        else:
            return (self.W1 - self.W0) * tan(self.H1) / 2.0  # convertion to m
