# -*- coding: utf-8 -*-

from numpy import exp, arcsin, tan, cos, sqrt, sin


def comp_volume_magnets(self):
    """Compute the volume of the magnet (if any)

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object

    Returns
    -------
    Vmag: float
        Volume of the magnet [m**3]

    """
    Rbo = self.get_Rbo()
    # Z1
    delta1 = arcsin((self.R1 + self.W2) / (self.R1 + self.R3))
    alpha1 = self.W1 - delta1
    Z1 = self.R3 * exp(-1j * alpha1)
    x1 = Z1.real
    y1 = Z1.imag

    # Zc1
    Zc1 = (self.R3 + self.R1) * exp(-1j * alpha1)
    xc1 = (self.R3 + self.R1) * cos(alpha1)
    yc1 = -(self.R3 + self.R1) * sin(alpha1)

    # Z2
    x2 = (-1 / tan(self.W1) * xc1 + yc1 - self.W2 / cos(self.W1)) / -(
        tan(self.W1) + 1 / tan(self.W1)
    )
    y2 = -tan(self.W1) * x2 + self.W2 / cos(self.W1)
    Z2 = x2 + 1j * y2

    # Z3
    a3 = 1 + tan(self.W1) ** 2
    b3 = -2 * tan(self.W1) * self.W2 / cos(self.W1)
    c3 = (self.W2 / cos(self.W1)) ** 2 - self.R2 ** 2

    x3 = (-b3 + sqrt(b3 ** 2 - 4 * a3 * c3)) / (2 * a3)
    y3 = -tan(self.W1) * x3 + self.W2 / cos(self.W1)
    Z3 = x3 + 1j * y3
    # Z5
    x5 = Rbo - self.H1
    y5 = -self.W0 / 2
    Z5 = x5 + 1j * y5
    # Zc2
    xc2 = Rbo - self.H1 - self.R1
    yc2 = -self.W0 / 2
    Zc2 = xc2 + 1j * yc2
    # Z4
    a4 = (xc2 - x3) ** 2 - self.R1 ** 2
    b4 = 2 * (xc2 - x3) * (y3 - yc2)
    c4 = (y3 - yc2) ** 2 - self.R1 ** 2
    alpha2 = (-b4 - sqrt(b4 ** 2 - 4 * a4 * c4)) / (2 * a4)
    x4 = (xc2 / alpha2 + yc2 + alpha2 * x3 - y3) / (alpha2 + 1 / alpha2)
    y4 = alpha2 * (x4 - x3) + y3
    Z4 = x4 + 1j * y4
    # symmetry
    Z6 = Z5.conjugate()
    x6 = Z6.real
    y6 = Z6.imag
    Z7 = Z4.conjugate()
    x7 = Z7.real
    y7 = Z7.imag
    Z8 = Z3.conjugate()
    x8 = Z8.real
    y8 = Z8.imag
    Z9 = Z2.conjugate()
    x9 = Z9.real
    y9 = Z9.imag
    Z10 = Z1.conjugate()
    x10 = Z10.real
    y10 = Z10.imag

    S_magnet_1 = (
        x1 * y2
        + x2 * y3
        + x3 * y4
        + x4 * y5
        + x5 * y6
        + x6 * y7
        + x7 * y8
        + x8 * y9
        + x9 * y10
        + x10 * y1
    )
    S_magnet_2 = (
        x1 * y10
        + x2 * y1
        + x3 * y2
        + x4 * y3
        + x5 * y4
        + x6 * y5
        + x7 * y6
        + x8 * y7
        + x9 * y8
        + x10 * y9
    )

    S_magnet = 0.5 * abs(S_magnet_1 - S_magnet_2)

    if self.magnet_0:
        return S_magnet * self.magnet_0.Lmag
    else:
        return 0
