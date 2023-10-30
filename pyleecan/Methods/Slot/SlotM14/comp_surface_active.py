# -*- coding: utf-8 -*-
from numpy import pi, sin, arcsin, angle


def comp_surface_active(self):
    """Compute the Slot inner active surface (by analytical computation)

    Parameters
    ----------
    self : SlotM14
        A SlotM14 object

    Returns
    -------
    Swind: float
        Slot inner active surface [m**2]

    """

    point_dict = self._comp_point_coordinate()
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]

    R1 = abs(ZM1)
    R2 = abs(ZM2)

    S1 = pi * R1 ** 2 * (self.W1 / (2 * pi))
    S2 = pi * R2 ** 2 * (self.W1 / (2 * pi))

    # Arc (Zm1,0,Zm2)
    alpha = -2 * angle(ZM2)
    Sarc1 = (R2 ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Arc (ZM1, Zc, ZM2)
    alpha = 2 * float(arcsin(-ZM2.imag / self.Rtopm))
    Sarc2 = (self.Rtopm ** 2.0) / 2.0 * (alpha - sin(alpha))

    return abs(S1 - S2) - Sarc1 + Sarc2
