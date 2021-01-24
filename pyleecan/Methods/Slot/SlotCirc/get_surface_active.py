# -*- coding: utf-8 -*-
from numpy import exp

from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine
from ....Methods import NotImplementedYetError


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object
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

    # Compute point
    Rbo = self.get_Rbo()
    alpha_op = self.comp_angle_opening()
    R0 = ((self.W0 / 2) ** 2 + self.H0 ** 2) / (2 * self.H0)

    Z1 = Rbo * exp(-1j * alpha_op / 2)
    Z2 = Rbo * exp(1j * alpha_op / 2)
    Ztan1 = Rbo
    if self.is_outwards():
        Ztan2 = (Z1 + Z2) / 2 + self.H0
    else:
        Ztan2 = (Z1 + Z2) / 2 - self.H0

    # Create surface
    curve_list = list()
    if self.is_outwards():
        curve_list.append(Arc1(begin=Z1, end=Z2, radius=-R0, is_trigo_direction=True))
    else:
        curve_list.append(Arc1(begin=Z1, end=Z2, radius=R0, is_trigo_direction=False))
    curve_list.append(Arc1(begin=Z2, end=Z1, radius=-Rbo, is_trigo_direction=False))
    surf = SurfLine(
        line_list=curve_list,
        label="Wind_" + st + "_R0_T0_S0",
        point_ref=(Ztan1 + Ztan2) / 2,
    )

    # Apply transformation
    surf.rotate(alpha)
    surf.translate(delta)

    return surf
