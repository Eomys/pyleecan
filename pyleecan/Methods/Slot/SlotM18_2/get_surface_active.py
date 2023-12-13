# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full active surface

    Parameters
    ----------
    self : SlotM18_2
        A SlotM18_2 object
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
    Rbo = self.get_Rbo()

    point_dict = self._comp_point_coordinate()
    ZM1 = point_dict["ZM1"]
    ZM2 = point_dict["ZM3"]
    ZM3 = point_dict["ZM4"]
    ZM4 = point_dict["ZM6"]

    curve_list = list()
    curve_list.append(Segment(ZM1, ZM2))

    if self.is_outwards():
        curve_list.append(
            Arc1(
                ZM2,
                ZM3,
                (Rbo - self.H0_bore - self.H0_gap),
                is_trigo_direction=True,
            )
        )
    else:
        curve_list.append(
            Arc1(
                ZM2,
                ZM3,
                (Rbo + self.H0_bore + self.H0_gap),
                is_trigo_direction=True,
            )
        )

    curve_list.append(Segment(ZM3, ZM4))

    if self.is_outwards():
        curve_list.append(Arc1(ZM4, ZM1, -Rbo, is_trigo_direction=False))
    else:
        curve_list.append(Arc1(ZM4, ZM1, -Rbo, is_trigo_direction=False))

    Zmid = (abs(ZM1) + abs(ZM3)) / 2

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Zmid
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    # init prop_dict
    for line in surface.line_list:
        line.prop_dict = dict()

    return surface
