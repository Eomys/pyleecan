# -*- coding: utf-8 -*-

from numpy import angle, exp, sqrt

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.Geometry.comp_flower_arc import comp_flower_arc
from ....Methods import ParentMissingError


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment, Arc1) needed to plot the Magnet.
    The list represents a closed surface.
    The ending point of a curve is always the starting point of the next
    curve in the list

    Parameters
    ----------
    self : MagnetType15
        A MagnetType15 object
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

    # comp magnet bottom and top angle
    R = sqrt(abs(Z1) ** 2 - (self.Wmag / 2) ** 2)
    W_bottom = 2 * angle(R + 1j * self.Wmag / 2)

    # comp point coordinate (in complex) for the bottom line
    if W0 > W_bottom:  # The magnet is smaller than the slot => center the mag
        Z1 = Z1 * exp(1j * (W0 - W_bottom) / 2)
        Z2 = Z2 * exp(-1j * (W0 - W_bottom) / 2)

    # compute coordinates for the top line
    sign = -1 if self.is_outwards() else 1

    Z3 = Z1 + sign * self.Hmag
    Z4 = Z2 + sign * self.Hmag
    Zs3 = Z1 + sign * H0
    Zs4 = Z2 + sign * H0
    Zref = abs(Z1) + sign * self.Hmag / 2

    # Creation of the curves
    curve_list = list()

    # magnet left side
    if is_simplified:
        if W0 > W_bottom:
            curve_list.append(Segment(Z1, Z3))
        elif H0 < self.Hmag:
            curve_list.append(Segment(Zs3, Z3))
    elif not is_simplified:
        curve_list.append(Segment(Z1, Z3))

    # magnet top arc
    curve_list.append(Arc1(Z3, Z4, self.Rtop))

    # magnet right side
    if is_simplified:
        if W0 > W_bottom:
            curve_list.append(Segment(Z4, Z2))
        elif H0 < self.Hmag:
            curve_list.append(Segment(Z4, Zs4))
    elif not is_simplified:
        curve_list.append(Segment(Z4, Z2))

    # magnet bottom line
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
