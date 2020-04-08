# -*- coding: utf-8 -*-

from numpy import angle, exp

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.Geometry.comp_flower_arc import comp_flower_arc
from pyleecan.Methods import ParentMissingError


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment, Arc1) needed to plot the Magnet.
    The list represents a closed surface.
    The ending point of a curve is always the starting point of the next
    curve in the list

    Parameters
    ----------
    self : MagnetType14
        A MagnetType14 object
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_simplified: bool
        True to avoid line superposition

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """

    # defining label for type_magnetization
    if self.type_magnetization == 0:
        t_p = "Radial"
    else:
        t_p = "Parallel"

    if self.parent is not None:
        (Z1, Z2) = self.parent.get_point_bottom()
        H0 = self.parent.H0
        W0 = self.parent.W0
    else:
        raise ParentMissingError(
            "Error: The magnet object is not inside a " + "slot object"
        )

    # comp point coordinate (in complex)
    if W0 > self.Wmag:  # The magnet is smaller than the slot => center the mag
        Z1 = Z1 * exp(1j * (W0 - self.Wmag) / 2)
        Z2 = Z2 * exp(-1j * (W0 - self.Wmag) / 2)

    if self.is_outwards():
        (alpha_lim, Z4, Z3) = comp_flower_arc(
            abs(angle(Z1) - angle(Z2)), self.Rtop, abs(Z1) - self.Hmag
        )
        Zs3 = (abs(Z1) - H0) * exp(1j * angle(Z1))
        Zs4 = (abs(Z2) - H0) * exp(1j * angle(Z2))
        Zref = abs(Z1) - self.Hmag / 2
    else:
        (alpha_lim, Z4, Z3) = comp_flower_arc(
            abs(angle(Z1) - angle(Z2)), self.Rtop, abs(Z1) + self.Hmag
        )
        Zs3 = (abs(Z1) + H0) * exp(1j * angle(Z1))
        Zs4 = (abs(Z2) + H0) * exp(1j * angle(Z2))
        Zref = abs(Z1) + self.Hmag / 2

    # Creation of curve
    curve_list = list()
    if is_simplified and W0 > self.Wmag:
        curve_list.append(Segment(Z1, Z3))
    elif is_simplified and H0 < self.Hmag:
        curve_list.append(Segment(Zs3, Z3))
    elif not is_simplified:
        curve_list.append(Segment(Z1, Z3))

    curve_list.append(Arc1(Z3, Z4, self.Rtop))

    if is_simplified and W0 > self.Wmag:
        curve_list.append(Segment(Z4, Z2))
    elif is_simplified and H0 < self.Hmag:
        curve_list.append(Segment(Z4, Zs4))
    elif not is_simplified:
        curve_list.append(Segment(Z4, Z2))

    if not is_simplified:
        curve_list.append(Arc1(Z2, Z1, -abs(Z2), is_trigo_direction=False))

    surf_list = list()
    surf_list.append(
        SurfLine(
            line_list=curve_list,
            label="MagnetRotor" + t_p + "_N_R0_T0_S0",
            point_ref=Zref,
        )
    )

    # Apply transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
