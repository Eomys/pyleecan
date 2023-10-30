# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full active surface

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_act: Surface
        Surface corresponding to the Active Area
    """

    # get the name of the lamination
    st = self.get_name_lam()

    point_dict = self._comp_point_coordinate()
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM2"]
    ZM3 = point_dict["ZM3"]
    ZM4 = point_dict["ZM4"]
    Z1 = point_dict["Z1"]
    Z4 = point_dict["Z4"]

    curve_list = list()
    curve_list.append(Segment(ZM1, ZM2))
    # Case Z2-Z1 overlapping with ZM1-ZM2
    if self.H0 != 0 and self.H0 < self.H1 and self.W0 == self.W1:
        curve_list.append(Segment(ZM1, Z1))
        curve_list.append(Segment(Z1, ZM2))
    else:
        curve_list.append(Segment(ZM1, ZM2))
    curve_list.append(Segment(ZM2, ZM3))

    # Case Z3-Z4 overlapping with ZM3-ZM4
    if self.H0 != 0 and self.H0 < self.H1 and self.W0 == self.W1:
        curve_list.append(Segment(ZM3, Z4))
        curve_list.append(Segment(Z4, ZM4))
    else:
        curve_list.append(Segment(ZM3, ZM4))
    curve_list.append(Segment(ZM4, ZM1))

    Zmid = (ZM1 + ZM3) / 2

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Zmid
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
