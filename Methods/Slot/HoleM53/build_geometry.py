# -*- coding: utf-8 -*-
"""@package Methods.Machine.HoleM53.build_geometry
HoleM53 build_geometry method
@date Created on Fri Mar 16 11:03:07 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import cos, exp, sin

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.Geometry.inter_line_circle import inter_line_circle
from pyleecan.Methods.Slot.HoleM53 import Slot53InterError


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Hole.
    The ending point of a curve is the starting point of the next curve in the
    list

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of Magnet Surface and Air Surface on the slot

    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "_Stator"
    else:
        st = "_Rotor"
    Rbo = self.get_Rbo()

    Z7 = Rbo - self.H0 - 1j * self.W1 / 2
    Z6 = Z7 - 1j * (self.H2 - self.H3) * cos(self.W4)
    Z8 = Z7 + (self.H2 - self.H3) * sin(self.W4)

    # Compute the coordinate in the ref of Z6 with rotation -W4
    Z5 = self.W2 * exp(-1j * self.W4) + Z6
    Z4 = (self.W2 - 1j * self.H3) * exp(-1j * self.W4) + Z6
    Z3 = (self.W2 + self.W3 - 1j * self.H3) * exp(-1j * self.W4) + Z6
    Z2 = (self.W2 + self.W3) * exp(-1j * self.W4) + Z6
    Z9 = (self.W2 + 1j * (self.H2 - self.H3)) * exp(-1j * self.W4) + Z6
    Z10 = (self.W2 + self.W3 + 1j * (self.H2 - self.H3)) * exp(-1j * self.W4) + Z6

    # Z1 and Z11 are defined as intersection between line and circle
    Zlist = inter_line_circle(Z8, Z10, Rbo - self.H1)
    if len(Zlist) == 2 and Zlist[0].imag < 0 and Zlist[0].real > 0:
        Z11 = Zlist[0]
    elif len(Zlist) == 2 and Zlist[1].imag < 0 and Zlist[1].real > 0:
        Z11 = Zlist[1]
    else:
        raise Slot53InterError("ERROR: Slot 53, Can't find Z11 coordinates")

    Zlist = inter_line_circle(Z2, Z6, Rbo - self.H1)
    if len(Zlist) == 2 and Zlist[0].imag < 0 and Zlist[0].real > 0:
        Z1 = Zlist[0]
    elif len(Zlist) == 2 and Zlist[1].imag < 0 and Zlist[1].real > 0:
        Z1 = Zlist[1]
    else:
        raise Slot53InterError("ERROR: Slot 53, Can't find Z1 coordinates")

    # Symmetry
    Z1s = Z1.conjugate()
    Z2s = Z2.conjugate()
    Z3s = Z3.conjugate()
    Z4s = Z4.conjugate()
    Z5s = Z5.conjugate()
    Z6s = Z6.conjugate()
    Z7s = Z7.conjugate()
    Z8s = Z8.conjugate()
    Z9s = Z9.conjugate()
    Z10s = Z10.conjugate()
    Z11s = Z11.conjugate()

    # Air surface with magnet_0
    curve_list_air = list()
    curve_list_air.append(Segment(Z1, Z2))
    curve_list_air.append(Segment(Z2, Z10))
    curve_list_air.append(Segment(Z10, Z11))
    curve_list_air.append(Arc1(Z11, Z1, -Rbo + self.H1))
    point_ref = (Z1 + Z2 + Z10 + Z11) / 4
    S1 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # magnet_0 surface
    curve_list_mag = list()
    if is_simplified:
        curve_list_air.append(Segment(Z5, Z9))
        curve_list_air.append(Segment(Z2, Z10))
    else:
        curve_list_mag.append(Segment(Z3, Z4))
        curve_list_mag.append(Segment(Z4, Z9))
        curve_list_mag.append(Segment(Z9, Z10))
        curve_list_mag.append(Segment(Z10, Z3))
    point_ref = (Z3 + Z4 + Z9 + Z10) / 4
    # Defining type of magnetization of the magnet
    if self.magnet_0:
        if self.magnet_0.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"
    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T0_S0"
    S2 = SurfLine(line_list=curve_list_mag, label=magnet_label, point_ref=point_ref)

    # Air suface with magnet_0 and W1 > 0
    curve_list_air = list()
    if self.W2 > 0:
        curve_list_air.append(Segment(Z5, Z6))
    curve_list_air.append(Segment(Z6, Z7))
    curve_list_air.append(Segment(Z7, Z8))
    if self.W2 > 0:
        curve_list_air.append(Segment(Z8, Z9))
        curve_list_air.append(Segment(Z9, Z5))
        point_ref = (Z5 + Z6 + Z7 + Z8 + Z9) / 5
    else:
        curve_list_air.append(Segment(Z8, Z6))
        point_ref = (Z6 + Z7 + Z8) / 3
    S3 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # Air surface with magnet_1
    curve_list_air = list()
    curve_list_air.append(Segment(Z1s, Z2s))
    curve_list_air.append(Segment(Z2s, Z10s))
    curve_list_air.append(Segment(Z10s, Z11s))
    curve_list_air.append(Arc1(Z11s, Z1s, Rbo - self.H1))
    point_ref = (Z1s + Z2s + Z10s + Z11s) / 4
    S4 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # magnet_1 surface
    curve_list_mag = list()
    if is_simplified:
        curve_list_air.append(Segment(Z5s, Z9s))
        curve_list_air.append(Segment(Z2s, Z10s))
    else:
        curve_list_mag.append(Segment(Z3s, Z4s))
        curve_list_mag.append(Segment(Z4s, Z9s))
        curve_list_mag.append(Segment(Z9s, Z10s))
        curve_list_mag.append(Segment(Z10s, Z3s))
    point_ref = (Z3s + Z4s + Z9s + Z10s) / 4
    # Defining type of magnetization of the magnet
    if self.magnet_1:
        if self.magnet_1.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"
    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T1_S0"
    S5 = SurfLine(line_list=curve_list_mag, label=magnet_label, point_ref=point_ref)

    # Air suface with magnet_1 and W1 > 0
    curve_list_air = list()
    if self.W2 > 0:
        curve_list_air.append(Segment(Z5s, Z6s))
    curve_list_air.append(Segment(Z6s, Z7s))
    curve_list_air.append(Segment(Z7s, Z8s))
    if self.W2 > 0:
        curve_list_air.append(Segment(Z8s, Z9s))
        curve_list_air.append(Segment(Z9s, Z5s))
        point_ref = (Z5s + Z6s + Z7s + Z8s + Z9s) / 5
    else:
        curve_list_air.append(Segment(Z8s, Z6s))
        point_ref = (Z6s + Z7s + Z8s) / 3
    S6 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # Air with both magnet and W1 = 0
    curve_list_air = list()
    if self.W2 > 0:
        curve_list_air.append(Segment(Z5, Z6))
    curve_list_air.append(Segment(Z6, Z6s))
    if self.W2 > 0:
        curve_list_air.append(Segment(Z6s, Z5s))
    curve_list_air.append(Segment(Z5s, Z9s))
    if self.W2 > 0:
        curve_list_air.append(Segment(Z9s, Z8s))
        curve_list_air.append(Segment(Z8s, Z9))
    curve_list_air.append(Segment(Z9, Z5))
    point_ref = (Z6 + Z6s + Z8) / 3
    S7 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # first hole without magnet_0 and W1 > 0
    curve_list_mag = list()
    curve_list_mag.append(Segment(Z1, Z2))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z2, Z3))
    curve_list_mag.append(Segment(Z3, Z4))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z4, Z5))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z5, Z6))
    curve_list_mag.append(Segment(Z6, Z7))
    curve_list_mag.append(Segment(Z7, Z8))
    curve_list_mag.append(Segment(Z8, Z11))
    curve_list_air.append(Arc1(Z11, Z1, -Rbo + self.H1))
    point_ref = (Z3 + Z4 + Z9 + Z10) / 4
    S8 = SurfLine(line_list=curve_list_mag, label="Hole" + st, point_ref=point_ref)

    # second hole without magnet_1 and W1 > 0
    curve_list_mag = list()
    curve_list_mag.append(Segment(Z1s, Z2s))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z2s, Z3s))
    curve_list_mag.append(Segment(Z3s, Z4s))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z4s, Z5s))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z5s, Z6s))
    curve_list_mag.append(Segment(Z6s, Z7s))
    curve_list_mag.append(Segment(Z7s, Z8s))
    curve_list_mag.append(Segment(Z8s, Z11s))
    curve_list_air.append(Arc1(Z11s, Z1s, -Rbo + self.H1))
    point_ref = (Z3s + Z4s + Z9s + Z10s) / 4
    S9 = SurfLine(line_list=curve_list_mag, label="Hole" + st, point_ref=point_ref)

    # No magnet_1 and W1 = 0
    curve_list_mag = list()
    curve_list_mag.append(Segment(Z1s, Z2s))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z2s, Z3s))
    curve_list_mag.append(Segment(Z3s, Z4s))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z4s, Z5s))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z5s, Z6s))
    curve_list_mag.append(Segment(Z6s, Z6))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z6, Z5))
    curve_list_mag.append(Segment(Z5, Z9))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z9, Z8))
    curve_list_mag.append(Segment(Z8s, Z11s))
    curve_list_air.append(Arc1(Z11s, Z1s, -Rbo + self.H1))
    point_ref = (Z3s + Z4s + Z9s + Z10s) / 4
    S10 = SurfLine(line_list=curve_list_mag, label="Hole" + st, point_ref=point_ref)

    # No magnet_0 and W1 = 0
    curve_list_mag = list()
    curve_list_mag.append(Segment(Z1, Z2))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z2, Z3))
    curve_list_mag.append(Segment(Z3, Z4))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z4, Z5))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z5, Z6))
    curve_list_mag.append(Segment(Z6, Z6s))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z6s, Z5s))
    curve_list_mag.append(Segment(Z5s, Z9s))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z9s, Z8s))
    curve_list_mag.append(Segment(Z8, Z11))
    curve_list_air.append(Arc1(Z11, Z1, -Rbo + self.H1))
    point_ref = (Z3 + Z4 + Z9 + Z10) / 4
    S11 = SurfLine(line_list=curve_list_mag, label="Hole" + st, point_ref=point_ref)

    # No magnet and W1 = 0
    curve_list_mag = list()
    curve_list_air.append(Arc1(Z1, Z11, Rbo - self.H1))
    curve_list_mag.append(Segment(Z11, Z8))
    curve_list_mag.append(Segment(Z8, Z11s))
    curve_list_air.append(Arc1(Z11s, Z1s, Rbo - self.H1))
    curve_list_mag.append(Segment(Z1s, Z2s))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z2s, Z3s))
    curve_list_mag.append(Segment(Z3s, Z4s))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z4s, Z5s))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z5s, Z6s))
    curve_list_mag.append(Segment(Z6s, Z6))
    if self.W2 > 0:
        curve_list_mag.append(Segment(Z6, Z5))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z5, Z4))
    curve_list_mag.append(Segment(Z4, Z3))
    if self.H3 > 0:
        curve_list_mag.append(Segment(Z3, Z2))
    curve_list_mag.append(Segment(Z2, Z1))

    point_ref = (Z6 + Z8 + Z6s) / 3
    S12 = SurfLine(line_list=curve_list_mag, label="Hole" + st, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0 and self.magnet_1 and self.W1 > 0:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S3.label = S3.label + "_R0_T1_S0"  # Hole
        S6.label = S6.label + "_R0_T2_S0"  # Hole
        S4.label = S4.label + "_R0_T3_S0"  # Hole
        surf_list = [S1, S2, S3, S6, S5, S4]
    elif self.magnet_0 and self.magnet_1 and self.W1 == 0:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S7.label = S7.label + "_R0_T1_S0"  # Hole
        S4.label = S4.label + "_R0_T2_S0"  # Hole
        surf_list = [S1, S2, S7, S5, S4]
    elif self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S3.label = S3.label + "_R0_T1_S0"  # Hole
        S9.label = S9.label + "_R0_T2_S0"  # Hole
        surf_list = [S1, S2, S3, S9]
    elif self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S10.label = S10.label + "_R0_T1_S0"  # Hole
        surf_list = [S1, S2, S10]
    elif not self.magnet_0 and self.magnet_1 and self.W1 > 0:
        S8.label = S8.label + "_R0_T0_S0"  # Hole
        S6.label = S6.label + "_R0_T1_S0"  # Hole
        S4.label = S4.label + "_R0_T2_S0"  # Hole
        surf_list = [S8, S6, S5, S4]
    elif not self.magnet_0 and self.magnet_1 and self.W1 == 0:
        S11.label = S11.label + "_R0_T0_S0"  # Hole
        S4.label = S4.label + "_R0_T2_S0"  # Hole
        surf_list = [S11, S5, S4]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S8.label = S8.label + "_R0_T0_S0"  # Hole
        S9.label = S9.label + "_R0_T1_S0"  # Hole
        surf_list = [S8, S9]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S12.label = S12.label + "_R0_T0_S0"  # Hole
        surf_list = [S12]

    # Apply the transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
