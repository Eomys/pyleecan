# -*- coding: utf-8 -*-

from numpy import abs as np_abs
from numpy import sqrt 


def comp_height_active(self):
    """Compute the height of the active area

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object

    Returns
    -------
    Hwind: float
        Height of the active area [m]

    """
    Rbo = self.get_Rbo()
    point_dict = self._comp_point_coordinate()

    Zmid =point_dict["Zmid"]
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    if self.is_outwards():
    
        R1 = np_abs(Rbo)
        R2 = np_abs(sqrt(Z1.real**2 + Z1.imag**2))

    else:
        R1 = np_abs(Zmid)
        R2 = np_abs(Rbo)
    return R2 - R1
