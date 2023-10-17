# -*- coding: utf-8 -*-
from numpy import arcsin, sin


def comp_surface_active(self):
    """Compute the Slot active inner surface (by analytical computation)

    Parameters
    ----------
    self : SlotM13
        A SlotM13 object

    Returns
    -------
    Swind: float
        Slot active inner surface [m**2]

    """

    point_dict = self._comp_point_coordinate()
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]
    alpha = 2 * float(arcsin(self.W1 / (2 * self.Rtopm)))
    Sarc = (self.Rtopm ** 2.0) / 2.0 * (alpha - sin(alpha))

    S1 = abs(ZM1 - ZM2) * self.W1
    return S1 + Sarc
