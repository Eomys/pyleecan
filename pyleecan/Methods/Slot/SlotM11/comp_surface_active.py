# -*- coding: utf-8 -*-
from numpy import pi


def comp_surface_active(self):
    """Compute the Slot inner active surface (by analytical computation)

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

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

    S1 = pi * R1**2 * (self.W1 / (2 * pi))
    S2 = pi * R2**2 * (self.W1 / (2 * pi))

    return abs(S1 - S2)
