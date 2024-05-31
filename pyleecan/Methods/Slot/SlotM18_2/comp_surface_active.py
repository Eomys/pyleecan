# -*- coding: utf-8 -*-
from numpy import pi


def comp_surface_active(self):
    """Compute the Slot inner active surface (by analytical computation)

    Parameters
    ----------
    self : SlotM18_2
        A SlotM18_2 object

    Returns
    -------
    Swind: float
        Slot inner active surface [m**2]

    """

    point_dict = self._comp_point_coordinate()
    ZM1 = point_dict["ZM1"]
    ZM3 = point_dict["ZM3"]

    R1 = abs(ZM1)
    R2 = abs(ZM3)

    S1 = pi * R1**2 / self.Zs
    S2 = pi * R2**2 / self.Zs

    return abs(S1 - S2)
