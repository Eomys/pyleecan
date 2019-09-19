# -*- coding: utf-8 -*-
"""@package Methods.Machine.MagnetType13.build_geometry
MagnetType13 build_geometry method
@date Created on Wed Dec 17 15:54:58 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import exp, angle, array, arcsin, cos

from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Methods import ParentMissingError


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment, Arc1) needed to plot the Magnet.
    The list represents a closed surface.
    The ending point of a curve is always the starting point of the next curve
    in the list

    Parameters
    ----------
    self : MagnetType13
        A MagnetType13 object
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_simplified: bool
        True to avoid line superposition

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the magnet

    """
    # defining label for type_magnetization
    if self.type_magnetization == 0:
        t_p = "Radial"
    else:
        t_p = "Parallel"

    if self.parent is not None:
        (Z1, Z2) = self.parent.get_point_bottom()
        H0 = self.parent.H0
        W0 = self.parent.comp_W0m()
    else:
        raise ParentMissingError(
            "Error: The magnet object is not inside a " + "slot object"
        )

    alpha_lim = 2 * arcsin(self.Wmag * 0.5 / self.Rtop)  # Angle of the top arc
    H_top_arc = self.Rtop * (1 - cos(alpha_lim / 2))  # Heiht of the top arc

    # comp point coordinate (in complex)
    if W0 > self.Wmag:  # The magnet is smaller than the slot => center the mag
        Z1 = Z1 + 1j * (W0 - self.Wmag) / 2
        Z2 = Z2 - 1j * (W0 - self.Wmag) / 2

    if self.is_outwards():
        Z3 = Z1 - (self.Hmag - H_top_arc)
        Zs3 = Z1 - H0
        Z4 = Z2 - (self.Hmag - H_top_arc)
        Zs4 = Z2 - H0
    else:
        Z3 = Z1 + (self.Hmag - H_top_arc)
        Zs3 = Z1 + H0
        Z4 = Z2 + (self.Hmag - H_top_arc)
        Zs4 = Z2 + H0

    # Creation of curve
    curve_list = list()
    if is_simplified and W0 > self.Wmag:
        curve_list.append(Segment(Z1, Z3))
    elif is_simplified and H0 < (self.Hmag - H_top_arc):
        curve_list.append(Segment(Zs3, Z3))
    elif not is_simplified:
        curve_list.append(Segment(Z1, Z3))

    if self.is_outwards():
        curve_list.append(Arc1(Z3, Z4, -self.Rtop, is_trigo_direction=False))
    else:
        curve_list.append(Arc1(Z3, Z4, self.Rtop))

    if is_simplified and W0 > self.Wmag:
        curve_list.append(Segment(Z4, Z2))
    elif is_simplified and H0 < (self.Hmag - H_top_arc):
        curve_list.append(Segment(Z4, Zs4))
    elif not is_simplified:
        curve_list.append(Segment(Z4, Z2))

    if not is_simplified:
        curve_list.append(Segment(Z2, Z1))

    surf_list = list()
    surf_list.append(
        SurfLine(
            line_list=curve_list,
            label="MagnetRotor" + t_p + "_N_R0_T0_S0",
            point_ref=(Z1 + Z2 + Z3 + Z4) / 4,
        )
    )

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
