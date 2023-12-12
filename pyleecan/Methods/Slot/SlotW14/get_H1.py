# -*- coding: utf-8 -*-
from numpy import arcsin, cos, exp, pi, sin, tan
from pyleecan.Functions.Geometry.inter_line_line import inter_line_line


def get_H1(self):
    """Return H1 in [m]

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    H1: float
        H1 in [m]

    """

    # H1 in rad
    if self.H1_is_rad:
        Rbo = self.get_Rbo()
        hssp = pi / self.Zs

        # alpha is the angle to rotate P0 so ||P1,P9|| = W0
        alpha = arcsin(self.W0 / (2 * Rbo))
        Harc = float(Rbo * (1 - cos(alpha)))

        Z1 = Rbo * exp(-1j * alpha)
        if self.is_outwards():
            R1 = Rbo - Harc + self.H0
            Z2 = Z1 + self.H0
        else:
            R1 = Rbo - Harc - self.H0
            Z2 = Z1 - self.H0

        Z3 = R1 + 1j * (self.W3 / 2 - R1 * sin(hssp)) / cos(hssp)

        # Z3t is Z3 in tooth ref
        Z3t = Z3 * exp(1j * hssp)
        if self.is_outwards():
            Z4t = Z3t + self.H3
        else:
            Z4t = Z3t - self.H3

        Z4 = Z4t * exp(-1j * hssp)
        # ending calcul slot point

        Zop = 0.5 * tan(self.H1)

        if self.is_outwards():
            Zc2 = Z2 - 0.5 * 1j + Zop
        else:
            Zc2 = Z2 - 0.5 * 1j - Zop

        ZiH = inter_line_line(Z3, Z4, Z2, Zc2)
        ZiH = ZiH[0]

        if self.is_outwards():
            H1 = abs(ZiH - Z3)
        else:
            H1 = abs(Z3 - ZiH)
        return H1  # convertion to m

    else:  # H1 in m
        return self.H1
