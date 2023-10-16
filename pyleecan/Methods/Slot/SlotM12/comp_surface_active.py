# -*- coding: utf-8 -*-
from numpy import arcsin, pi, sin


def comp_surface_active(self):
    """Compute the Slot active inner surface (by analytical computation)

    Parameters
    ----------
    self : SlotM12
        A SlotM12 object

    Returns
    -------
    Swind: float
        Slot active inner surface [m**2]

    """

    point_dict = self._comp_point_coordinate()
    ZM0 = point_dict["ZM0"]
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]
    alpha = 2 * float(arcsin(self.W1 / (2 * abs(ZM0))))
    Sarc = (abs(ZM0) ** 2.0) / 2.0 * (alpha - sin(alpha))

    S1 = abs(ZM1 - ZM2) * self.W1
    if self.is_outwards():
        return S1 - Sarc
    else:
        return S1 + Sarc
