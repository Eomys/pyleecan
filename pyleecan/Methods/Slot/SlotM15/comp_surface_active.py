# -*- coding: utf-8 -*-
from numpy import arcsin, sin


def comp_surface_active(self):
    """Compute the Slot active inner surface (by analytical computation)

    Parameters
    ----------
    self : SlotM15
        A SlotM15 object

    Returns
    -------
    Swind: float
        Slot active inner surface [m**2]

    """

    # "Main rectangle"
    point_dict = self._comp_point_coordinate()
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]
    S1 = abs(ZM1 - ZM2) * self.W1

    # Top Arc
    alpha = 2 * float(arcsin(self.W1 / (2 * self.Rtopm)))
    Sarc = (self.Rtopm**2.0) / 2.0 * (alpha - sin(alpha))

    # Bottom polar to remove
    alpha = 2 * float(arcsin(self.W1 / (2 * abs(ZM1))))
    Sarc2 = (abs(ZM1) ** 2.0) / 2.0 * (alpha - sin(alpha))

    return S1 + Sarc - Sarc2
