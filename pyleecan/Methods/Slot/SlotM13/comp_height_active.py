# -*- coding: utf-8 -*-

from numpy import abs as np_abs


def comp_height_active(self):
    """Compute the height of the active area

    Parameters
    ----------
    self : SlotM13
        A SlotM13 object

    Returns
    -------
    Hwind: float
        Height of the active area [m]

    """

    [_, _, _, _, ZM1, ZM2, ZM3, ZM4, ZM0] = self._comp_point_coordinate()

    if self.is_outwards():
        R1 = np_abs(ZM0)
        R2 = np_abs(ZM1)
    else:
        R1 = np_abs((ZM1 + ZM4) / 2)
        R2 = np_abs(ZM0)
    return R2 - R1
