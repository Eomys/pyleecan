# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Dec 06 11:16:39 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import exp, pi, cos, sin, tan

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.Geometry.inter_line_circle import inter_line_circle


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Line) needed to plot the Hole.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object
    alpha : float
        Angle to rotate the hole (Default value = 0) [rad]
    delta : complex
        Complex to translate the hole (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM51

    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"
    Rbo = self.get_Rbo()

    # comp point coordinate (in complex)
    alpha = self.comp_alpha()

    Wslot = 2 * sin(self.W1 / 2) * (Rbo - self.H1)
    L = 0.5 * (Wslot - self.W0) / cos(alpha)  # ||P2,P5||

    # Center of the hole
    Z0 = Rbo - self.H0
    Z2 = Z0 + 1j * self.W0 / 2
    Z25 = Z0 - 1j * self.W0 / 2
    Z15 = Z25 - self.H2
    Z1 = Z2 - 1j * self.W2
    Z26 = Z1 - 1j * self.W3
    Z12 = Z2 - self.H2
    Z13 = Z12 - 1j * self.W2
    Z14 = Z13 - 1j * self.W3
    Z11 = Z12 + 1j * tan(alpha / 2) * self.H2
    Z16 = Z15 - 1j * tan(alpha / 2) * self.H2

    # Draw the left side with center P2, and X axis =(P2,P5), Y axis=(P2,P10)
    Z3 = self.W4 * exp(1j * (pi / 2 - alpha)) + Z2
    Z4 = (self.W4 + self.W5) * exp(1j * (pi / 2 - alpha)) + Z2
    Z5 = (Rbo - self.H1) * exp(1j * self.W1 / 2)
    Z10 = (1j * self.H2) * exp(1j * (pi / 2 - alpha)) + Z2
    Z9 = (1j * self.H2 + self.W4) * exp(1j * (pi / 2 - alpha)) + Z2
    Z8 = (1j * self.H2 + self.W4 + self.W5) * exp(1j * (pi / 2 - alpha)) + Z2
    Z7 = (1j * self.H2 + L) * exp(1j * (pi / 2 - alpha)) + Z2

    # Draw the right side with center P25, X axis (P25,P23), Y axis(P25,P17)
    Z24 = self.W6 * exp(-1j * (pi / 2 - alpha)) + Z25
    Z23 = (self.W6 + self.W7) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z22 = (Rbo - self.H1) * exp(-1j * self.W1 / 2)
    Z17 = (1j * self.H2) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z18 = (-1j * self.H2 + self.W6) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z19 = (-1j * self.H2 + self.W6 + self.W7) * exp(-1j * (pi / 2 - alpha)) + Z25
    Z20 = (-1j * self.H2 + L) * exp(-1j * (pi / 2 - alpha)) + Z25

    # Z6 is the intersection of the line [Z7,Z10] and Circle centre
    # (0,0) radius Rbo - H1
    Zint = inter_line_circle(Z7, Z10, Rbo - self.H1)

    # Select the point with Re(Z) > 0
    if Zint[0].real > 0:
        Z6 = Zint[0]
    else:
        Z6 = Zint[1]
    Z21 = Z6.conjugate()

    surf_list = list()
    # Create all the surfaces for all the cases
    # Air surface bore around magnet_0
    curve_list = list()
    curve_list.append(Arc1(Z21, Z22, Rbo - self.H1))
    curve_list.append(Segment(Z22, Z23))
    curve_list.append(Segment(Z23, Z19))
    curve_list.append(Segment(Z19, Z21))
    point_ref = (Z21 + Z22 + Z23 + Z19) / 4
    S1 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Surface for magnet_0
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z24, Z18))
        curve_list.append(Segment(Z19, Z23))
    else:
        curve_list.append(Segment(Z24, Z18))
        curve_list.append(Segment(Z18, Z19))
        curve_list.append(Segment(Z19, Z23))
        curve_list.append(Segment(Z23, Z24))
    point_ref = (Z24 + Z18 + Z19 + Z23) / 4
    S2 = SurfLine(
        line_list=curve_list, label="Magnet" + st + "_N_R0_T0_S0", point_ref=point_ref
    )

    # Air surface between magnet_0 and magnet_1
    curve_list = list()
    curve_list.append(Segment(Z24, Z25))
    curve_list.append(Segment(Z25, Z26))
    curve_list.append(Segment(Z26, Z14))
    curve_list.append(Segment(Z14, Z16))
    curve_list.append(Segment(Z16, Z18))
    curve_list.append(Segment(Z18, Z24))
    point_ref = (Z25 + Z16) / 2
    S3 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Surface for magnet_1
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z1, Z13))
        curve_list.append(Segment(Z14, Z26))
    else:
        curve_list.append(Segment(Z26, Z1))
        curve_list.append(Segment(Z1, Z13))
        curve_list.append(Segment(Z13, Z14))
        curve_list.append(Segment(Z14, Z26))
    point_ref = (Z26 + Z1 + Z13 + Z14) / 4
    S4 = SurfLine(
        line_list=curve_list, label="Magnet" + st + "_N_R0_T1_S0", point_ref=point_ref
    )

    # Air surface between magnet_1 and magnet_2
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z9))
    curve_list.append(Segment(Z9, Z11))
    curve_list.append(Segment(Z11, Z13))
    curve_list.append(Segment(Z13, Z1))
    point_ref = (Z11 + Z2) / 2
    S5 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Surface for magnet_2
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z4, Z8))
        curve_list.append(Segment(Z9, Z3))
    else:
        curve_list.append(Segment(Z4, Z8))
        curve_list.append(Segment(Z8, Z9))
        curve_list.append(Segment(Z9, Z3))
        curve_list.append(Segment(Z3, Z4))
    point_ref = (Z4 + Z8 + Z9 + Z3) / 4
    S6 = SurfLine(
        line_list=curve_list, label="Magnet" + st + "_N_R0_T2_S0", point_ref=point_ref
    )

    # Air surface bore around magnet_2
    curve_list = list()
    curve_list.append(Arc1(Z5, Z6, Rbo - self.H1))
    curve_list.append(Segment(Z6, Z8))
    curve_list.append(Segment(Z8, Z4))
    curve_list.append(Segment(Z4, Z5))
    point_ref = (Z4 + Z5 + Z6 + Z8) / 4
    S7 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_2 (no magnet_2 and magnet_1)
    curve_list = list()
    curve_list.append(Arc1(Z5, Z6, Rbo - self.H1))
    curve_list.append(Segment(Z6, Z11))
    curve_list.append(Segment(Z11, Z13))
    curve_list.append(Segment(Z13, Z1))
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z5))
    point_ref = (Z2 + Z11) / 2
    S8 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_0 (no magnet_0 and magnet_1)
    curve_list = list()
    curve_list.append(Arc1(Z21, Z22, Rbo - self.H1))
    curve_list.append(Segment(Z22, Z25))
    curve_list.append(Segment(Z25, Z26))
    curve_list.append(Segment(Z26, Z14))
    curve_list.append(Segment(Z14, Z16))
    curve_list.append(Segment(Z16, Z21))
    point_ref = (Z25 + Z16) / 2
    S9 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_1 (no magnet_1 and magnet_0 and magnet_2)
    curve_list = list()
    curve_list.append(Segment(Z24, Z25))
    curve_list.append(Segment(Z25, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z9))
    curve_list.append(Segment(Z9, Z11))
    curve_list.append(Segment(Z11, Z16))
    curve_list.append(Segment(Z16, Z18))
    curve_list.append(Segment(Z18, Z24))
    point_ref = (Z1 + Z13) / 2
    S10 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_1 (no magnet_1 and no magnet_0 and magnet_2)
    curve_list = list()
    curve_list.append(Arc1(Z21, Z22, Rbo - self.H1))
    curve_list.append(Segment(Z22, Z25))
    curve_list.append(Segment(Z25, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z9))
    curve_list.append(Segment(Z9, Z11))
    curve_list.append(Segment(Z11, Z16))
    curve_list.append(Segment(Z16, Z21))
    point_ref = (Z1 + Z13) / 2
    S11 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_1 (no magnet_1 and magnet_0 and no magnet_2)
    curve_list = list()
    curve_list.append(Arc1(Z5, Z6, Rbo - self.H1))
    curve_list.append(Segment(Z6, Z11))
    curve_list.append(Segment(Z11, Z16))
    curve_list.append(Segment(Z16, Z18))
    curve_list.append(Segment(Z18, Z24))
    curve_list.append(Segment(Z24, Z25))
    curve_list.append(Segment(Z25, Z2))
    curve_list.append(Segment(Z2, Z5))
    point_ref = (Z1 + Z13) / 2
    S12 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface No magnet
    curve_list = list()
    curve_list.append(Arc1(Z5, Z6, Rbo - self.H1))
    curve_list.append(Segment(Z6, Z11))
    curve_list.append(Segment(Z11, Z16))
    curve_list.append(Segment(Z16, Z21))
    curve_list.append(Arc1(Z21, Z22, Rbo - self.H1))
    curve_list.append(Segment(Z22, Z25))
    curve_list.append(Segment(Z25, Z2))
    curve_list.append(Segment(Z2, Z5))
    point_ref = (Z1 + Z13) / 2
    S13 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0 and self.magnet_1 and self.magnet_2:
        surf_list = [S1, S2, S3, S4, S5, S6, S7]
    elif not self.magnet_0 and self.magnet_1 and self.magnet_2:
        surf_list = [S9, S4, S5, S6, S7]
    elif self.magnet_0 and not self.magnet_1 and self.magnet_2:
        surf_list = [S1, S2, S10, S6, S7]
    elif not self.magnet_0 and not self.magnet_1 and self.magnet_2:
        surf_list = [S11, S6, S7]
    elif self.magnet_0 and self.magnet_1 and not self.magnet_2:
        surf_list = [S1, S2, S3, S4, S8]
    elif not self.magnet_0 and self.magnet_1 and not self.magnet_2:
        surf_list = [S9, S4, S8]
    elif self.magnet_0 and not self.magnet_1 and not self.magnet_2:
        surf_list = [S1, S2, S12]
    elif not self.magnet_0 and not self.magnet_1 and not self.magnet_2:
        surf_list = [S13]

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
