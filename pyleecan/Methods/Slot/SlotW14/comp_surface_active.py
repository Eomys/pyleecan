# -*- coding: utf-8 -*-

from numpy import arcsin, cos, exp, pi, sin, sqrt, tan


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9] = self._comp_point_coordinate()

    # Compute area of triangle Z5,Z6
    S1 = abs(Z6.imag) * abs(Z5.real - Z4.real) / 2
    S2 = (abs(Z6.imag) + abs(Z7.imag)) * abs(Z7.real - Z6.real) / 2

    if self.is_outwards():
        return (S1 + S2) * 2
    else:
        return (S2 - S1) * 2
