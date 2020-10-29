# -*- coding: utf-8 -*-

from numpy import angle
from scipy.optimize import fsolve

from ....Classes.Arc1 import Arc1
from ....Classes.Arc3 import Arc3
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_wind(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object
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

    # Create curve list
    curve_list = self.build_geometry()[1:-1]
    curve_list.append(
        Segment(begin=curve_list[-1].get_end(), end=curve_list[0].get_begin())
    )

    # Create surface
    if self.is_outwards():
        Zmid = self.get_Rbo() + self.H0 + self.R1 + self.H3 / 2
    else:
        Zmid = self.get_Rbo() - self.H0 - self.R1 - self.H3 / 2
    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Zmid
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
