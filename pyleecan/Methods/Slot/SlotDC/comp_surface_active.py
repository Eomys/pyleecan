# -*- coding: utf-8 -*-

from numpy import pi, sin, arcsin, abs as np_abs


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotDC
        A SlotDC object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    [
        Z1,
        Z2,
        Z3,
        Z4,
        Z5,
        Z6,
        Z7,
        Z8,
        Z9,
        Z10,
        Z11,
        Z12,
        _,
        _,
        _,
    ] = self._comp_point_coordinate()

    # Half circle R3
    S1 = self.R3**2 * pi / 2
    # Tapeze H3
    S2 = self.H3 * (self.R3 * 2 + self.D2) / 2
    # Half circle D2
    S3 = (self.D2 / 2) ** 2 * pi / 2
    # Remove arc from Half Circle D2
    alpha1 = float(2 * arcsin(self.W2 / (2 * self.D2 / 2)))
    Sarc1 = ((self.D2 / 2) ** 2.0) / 2.0 * (alpha1 - sin(alpha1))
    # Rectangle Z10,Z9,Z4,Z3
    S4 = self.W2 * np_abs(Z10.real - Z9.real)
    # Circle D1
    S5 = (self.D1 / 2) ** 2 * pi
    # Remove arc from Circle D1 from rectangle Z10,Z9,Z4,Z3
    alpha2 = float(2 * arcsin(self.W2 / (2 * self.D1 / 2)))
    Sarc2 = ((self.D1 / 2) ** 2.0) / 2.0 * (alpha2 - sin(alpha2))
    # Remove arc from Circle D1 from W1 rectangle
    alpha3 = float(2 * arcsin(self.W1 / (2 * self.D1 / 2)))
    Sarc3 = ((self.D1 / 2) ** 2.0) / 2.0 * (alpha3 - sin(alpha3))

    return S1 + S2 + S3 - Sarc1 + S4 + S5 - Sarc2 - Sarc3
