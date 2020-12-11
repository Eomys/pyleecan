# -*- coding: utf-8 -*-

from numpy import abs as np_abs


def comp_height_active(self):
    """Compute the height of the active area

    Parameters
    ----------
    self : SlotM12
        A SlotM12 object

    Returns
    -------
    Hwind: float
        Height of the active area [m]

    """

    point_dict = self._comp_point_coordinate()
    ZM0 = point_dict["ZM0"]
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]
    ZM3 = point_dict["ZM3"]
    ZM4 = point_dict["ZM4"]

    if self.is_outwards():
        R1 = np_abs(ZM0)
        R2 = np_abs(ZM1)
    else:
        R1 = np_abs((ZM1 + ZM4) / 2)
        R2 = np_abs(ZM0)
    return R2 - R1
