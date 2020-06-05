# -*- coding: utf-8 -*-
from numpy import exp

from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine
from ....Methods import NotImplementedYetError


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        List of surface delimiting the winding zone
    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"

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

    surf_list = list()
    if Nrad == 1 and Ntan == 1:
        curve_list = list()
        if self.is_outwards():
            curve_list.append(
                Arc1(begin=Z1, end=Z2, radius=-R0, is_trigo_direction=True)
            )
        else:
            curve_list.append(
                Arc1(begin=Z1, end=Z2, radius=R0, is_trigo_direction=False)
            )
        curve_list.append(Arc1(begin=Z2, end=Z1, radius=-Rbo, is_trigo_direction=False))
        surf_list.append(
            SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=(Ztan1 + Ztan2) / 2,
            )
        )
    elif Nrad == 1 and Ntan == 2:
        # First part
        curve_list = list()
        if self.is_outwards():
            curve_list.append(
                Arc1(begin=Z1, end=Ztan2, radius=R0, is_trigo_direction=True)
            )
        else:
            curve_list.append(
                Arc1(begin=Z1, end=Ztan2, radius=-R0, is_trigo_direction=False)
            )
        curve_list.append(Segment(begin=Ztan2, end=Ztan1))
        curve_list.append(
            Arc1(begin=Ztan1, end=Z1, radius=-Rbo, is_trigo_direction=False)
        )
        surf_list.append(
            SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=(Ztan1 + Ztan2) / 2 - 1j * R0 / 2,
            )
        )
        # Second part
        curve_list = list()
        if not is_simplified:
            curve_list.append(Segment(begin=Ztan1, end=Ztan2))
        if self.is_outwards():
            curve_list.append(
                Arc1(begin=Ztan2, end=Z2, radius=R0, is_trigo_direction=True)
            )
        else:
            curve_list.append(
                Arc1(begin=Ztan2, end=Z2, radius=-R0, is_trigo_direction=False)
            )
        curve_list.append(
            Arc1(begin=Z2, end=Ztan1, radius=-Rbo, is_trigo_direction=False)
        )
        surf_list.append(
            SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=(Ztan1 + Ztan2) / 2 + 1j * R0 / 2,
            )
        )
    else:
        raise NotImplementedYetError(
            "SlotCirc is compatible only for winding (Nrad=1,Ntan=1) or (Nrad=1,Ntan=2)"
        )

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
