# -*- coding: utf-8 -*-

from numpy import linspace, zeros
from numpy import abs as np_abs
from numpy import sqrt

from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full active surface

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_act: Surface
        Surface corresponding to the Active Area
    """
    Rbo = self.get_Rbo()
    # get the name of the lamination
    st = self.get_name_lam()

    point_dict = self._comp_point_coordinate()
    Zmid = point_dict["Zmid"]
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))

    if self.is_outwards():
        curve_list.append(Arc1(Z4, Z1, -Rbo, is_trigo_direction=False))
    else:
        curve_list.append(Arc1(Z4, Z1, -Rbo, is_trigo_direction=False))

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=(Z1 + Z3) / 2
    )

    # Apply transformation
    if alpha != 0:
        surface.rotate(alpha)
    if delta != 0:
        surface.translate(delta)

    return surface
