# -*- coding: utf-8 -*-

from numpy import arcsin, cos, exp, angle, pi, sin, tan, array

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.Geometry.inter_line_line import inter_line_line
import matplotlib.pyplot as plt


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM57

    """

    if self.get_is_stator():  # check if the slot is on the stator
        st = "_Stator"
    else:
        st = "_Rotor"
    Rbo = self.get_Rbo()

    # "Tooth" angle (P1',0,P1)
    alpha_T = 2 * arcsin(self.W3 / (2 * (Rbo - self.H1)))
    # magnet pole pitch angle (Z1,0,Z1')
    alpha_S = (2 * pi / self.Zh) - alpha_T
    # Angle (P1,P1',P4') and (P5',P4', )
    alpha = (pi - self.W0) / 2
    # Half slot pitch
    hssp = pi / self.Zh

    Z1 = (Rbo - self.H1) * exp(-1j * alpha_S / 2)
    x11 = 2 * sin(alpha_S / 2) * (Rbo - self.H1)  # Distance from P1 to P1'
    # In rect triangle P4, P1, perp (P1,P1') with P4
    H = tan(alpha) * (x11 / 2 - self.W1 / 2)
    Z4 = Z1.real - H - 1j * self.W1 / 2

    x45 = self.H2 / cos(alpha)  # distance from P4 to P5
    Z5 = Z4 - x45

    # Get coordinates of "random" points on (P5,P8) and (P1,P8)
    # In ref P4 center and P1 on X+ axis
    Z58 = (self.W4 - 1j * self.H2) * exp(1j * angle(Z1 - Z4)) + Z4
    # In the tooth ref
    Z18 = (Rbo - self.H1 - self.H2 + 1j * self.W3 / 2) * exp(-1j * hssp)
    Z8 = inter_line_line(Z5, Z58, Z1, Z18)[0]

    # In ref "b" P4 center and P1 on X+ axis
    Z8b = (Z8 - Z4) * exp(-1j * angle(Z1 - Z4))
    Z2 = (Z8b + 1j * self.H2 - self.W2) * exp(1j * angle(Z1 - Z4)) + Z4
    Z3 = (Z8b + 1j * self.H2 - self.W2 - self.W4) * exp(1j * angle(Z1 - Z4)) + Z4
    Z7 = (Z8b - self.W2) * exp(1j * angle(Z1 - Z4)) + Z4
    Z6 = (Z8b - self.W2 - self.W4) * exp(1j * angle(Z1 - Z4)) + Z4

    # Symmetry
    Z1s = Z1.conjugate()
    Z2s = Z2.conjugate()
    Z3s = Z3.conjugate()
    Z4s = Z4.conjugate()
    Z5s = Z5.conjugate()
    Z6s = Z6.conjugate()
    Z7s = Z7.conjugate()
    Z8s = Z8.conjugate()

    surf_list = list()
    # Z_list = array([Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8])
    # plt.plot(Z_list.real, Z_list.imag, "x r")
    # for ii in range(8):
    #     plt.text(Z_list[ii].real, Z_list[ii].imag, "Z" + str(ii + 1))
    # plt.show()
    # Check schematics:
    assert abs(abs(Z7 - Z8) - self.W2) < 1e-6
    assert abs(abs(Z6 - Z7) - self.W4) < 1e-6
    assert abs(abs(Z2 - Z3) - self.W4) < 1e-6
    assert abs(abs(Z2 - Z7) - self.H2) < 1e-6
    assert abs(abs(Z4 - Z4s) - self.W1) < 1e-6
    assert abs(abs(Z5 - Z5s) - self.W1) < 1e-6
    # TODO: Create all the surfaces for all the cases
    # (with/without magnet W1>0 or W1=0)
    # Air surface (W3) with magnet_0
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z7))
    if self.W2 > 0:
        curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z1))

    # initiating the label of the line on the air surface
    curve_list = set_name_line(curve_list, "hole_1_line")
    point_ref = (Z1 + Z2 + Z7 + Z8) / 4
    S1 = SurfLine(line_list=curve_list, label="Air", point_ref=point_ref)

    # Magnet_0 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z7, Z2))
        curve_list.append(Segment(Z3, Z6))
    else:
        curve_list.append(Segment(Z2, Z3))
        curve_list.append(Segment(Z3, Z6))
        curve_list.append(Segment(Z6, Z7))
        curve_list.append(Segment(Z7, Z2))

    # initiating the label of the line of the magnet surface
    curve_list = set_name_line(curve_list, "magnet_1_line")
    point_ref = (Z2 + Z3 + Z6 + Z7) / 4
    S2 = SurfLine(
        line_list=curve_list,
        label="Magnet" + st + "_N_R0_T0_S0",
        point_ref=point_ref,
    )

    # Air surface with magnet_0 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z3))
    if abs(Z4 - Z3) > 1e-6:
        curve_list.append(Segment(Z3, Z4))

    # initiating the label of the line on the air surface
    curve_list = set_name_line(curve_list, "hole_2_line")
    point_ref = (Z6 + Z5 + Z4) / 3

    S3 = SurfLine(line_list=curve_list, label="Air", point_ref=point_ref)

    # Symmetry Air surface (W3) with magnet_1
    curve_list = list()
    curve_list.append(Segment(Z2s, Z1s))
    curve_list.append(Segment(Z1s, Z8s))
    if self.W2 > 0:
        curve_list.append(Segment(Z8s, Z7s))
    curve_list.append(Segment(Z7s, Z2s))
    point_ref = (Z1s + Z2s + Z8s + Z7s) / 4
    # initiating the label of the line on the air surface
    curve_list = set_name_line(curve_list, "hole_3_line")
    S4 = SurfLine(line_list=curve_list, label="Air", point_ref=point_ref)

    # magnet_1 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z2s, Z7s))
        curve_list.append(Segment(Z6s, Z3s))
    else:
        curve_list.append(Segment(Z3s, Z2s))
        curve_list.append(Segment(Z2s, Z7s))
        curve_list.append(Segment(Z7s, Z6s))
        curve_list.append(Segment(Z6s, Z3s))
    point_ref = (Z3s + Z2s + Z7s + Z6s) / 4

    # initiating the label of the line on the magnet surface
    curve_list = set_name_line(curve_list, "magnet_2_line")
    S5 = SurfLine(
        line_list=curve_list,
        label="Magnet" + st + "_N_R0_T1_S0",
        point_ref=point_ref,
    )

    # Air surface with magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z3s, Z6s))
    curve_list.append(Segment(Z6s, Z5s))
    curve_list.append(Segment(Z5s, Z4s))
    if abs(Z4 - Z3) > 1e-6:
        curve_list.append(Segment(Z4s, Z3s))

    point_ref = (Z3s + Z6s + Z5s) / 3

    # initiating the label of the line on the air surface
    curve_list = set_name_line(curve_list, "hole_4_line")
    S6 = SurfLine(line_list=curve_list, label="Air", point_ref=point_ref)

    # Air surface between magnet_0 and magnet_1 with W1 == 0
    curve_list = list()
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z3s))
    curve_list.append(Segment(Z3s, Z6s))
    curve_list.append(Segment(Z6s, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z3))

    # initiating the label of the line on the air surface
    curve_list = set_name_line(curve_list, "hole_2_line")
    point_ref = (Z5 + Z4) / 2

    S7 = SurfLine(line_list=curve_list, label="Air", point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0 and self.magnet_1 and self.W1 > 0:
        surf_list = [S1, S2, S3, S6, S5, S4]
    elif self.magnet_0 and self.magnet_1 and self.W1 == 0:
        surf_list = [S1, S2, S7, S5, S4]
    # elif self.magnet_0 and not self.magnet_1 and self.W1 > 0:
    #     surf_list = [S1, S2, S3, S9]
    # elif self.magnet_0 and not self.magnet_1 and self.W1 == 0:
    #     surf_list = [S1, S2, S10]
    # elif not self.magnet_0 and self.magnet_1 and self.W1 > 0:
    #     surf_list = [S8, S6, S5, S4]
    # elif not self.magnet_0 and self.magnet_1 and self.W1 == 0:
    #     surf_list = [S11, S5, S4]
    # elif not self.magnet_0 and not self.magnet_1 and self.W1 > 0:
    #     surf_list = [S8, S9]
    # elif not self.magnet_0 and not self.magnet_1 and self.W1 == 0:
    #     surf_list = [S12]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list


def set_name_line(hole_lines, name):
    """Define the  label of each line of the hole

    Parameters
    ----------
    hole_lines: list
        a list of line object of the slot
    name: str
        the name to give to the line
    Returns
    -------
    hole_lines: list
        List of line object with label
    """

    for ii in range(len(hole_lines)):
        hole_lines[ii].label = name + "_" + str(ii)
    return hole_lines
