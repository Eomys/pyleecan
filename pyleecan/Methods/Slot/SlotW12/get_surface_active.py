# -*- coding: utf-8 -*-

from numpy import arcsin, exp

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """
    # get the name of the lamination
    st = self.get_name_lam()

    if self.is_outwards():
        Zmid = self.get_Rbo() + self.H0 + 2 * self.R1 + self.H1
    else:
        Zmid = self.get_Rbo() - self.H0 - 2 * self.R1 - self.H1

    if self.R1 > 0:
        line_list = self.build_geometry()[2:-2]
    else:
        line_list = self.build_geometry()[1:-1]
    line_list.append(
        Segment(begin=line_list[-1].get_end(), end=line_list[0].get_begin())
    )

    surface = SurfLine(
        line_list=line_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Zmid
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
