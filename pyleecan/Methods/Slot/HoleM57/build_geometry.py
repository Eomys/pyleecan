# -*- coding: utf-8 -*-

from numpy import arcsin, cos, exp, angle, pi, sin, tan, array

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.Geometry.inter_line_line import inter_line_line
import matplotlib.pyplot as plt
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB


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

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    vent_label = lam_label + "_" + surf_type + "_R" + str(R_id) + "-"
    mag_label = lam_label + "_" + HOLEM_LAB + "_R" + str(R_id) + "-"

    # Get all the points
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    Z1s = point_dict["Z1s"]
    Z2s = point_dict["Z2s"]
    Z3s = point_dict["Z3s"]
    Z4s = point_dict["Z4s"]
    Z5s = point_dict["Z5s"]
    Z6s = point_dict["Z6s"]
    Z7s = point_dict["Z7s"]
    Z8s = point_dict["Z8s"]

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
    # curve_list = set_name_line(curve_list, "hole_1_line")
    point_ref = (Z1 + Z2 + Z7 + Z8) / 4
    S1 = SurfLine(line_list=curve_list, label=vent_label + "T0-S0", point_ref=point_ref)

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
    # curve_list = set_name_line(curve_list, "magnet_1_line")
    point_ref = (Z2 + Z3 + Z6 + Z7) / 4
    S2 = SurfLine(
        line_list=curve_list,
        label=mag_label + "T0-S0",
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
    # curve_list = set_name_line(curve_list, "hole_2_line")
    point_ref = (Z6 + Z5 + Z4) / 3

    S3 = SurfLine(line_list=curve_list, label=vent_label + "T1-S0", point_ref=point_ref)

    # Symmetry Air surface (W3) with magnet_1
    curve_list = list()
    curve_list.append(Segment(Z2s, Z1s))
    curve_list.append(Segment(Z1s, Z8s))
    if self.W2 > 0:
        curve_list.append(Segment(Z8s, Z7s))
    curve_list.append(Segment(Z7s, Z2s))
    point_ref = (Z1s + Z2s + Z8s + Z7s) / 4
    # initiating the label of the line on the air surface
    # curve_list = set_name_line(curve_list, "hole_3_line")
    S4 = SurfLine(line_list=curve_list, label=vent_label + "T2-S0", point_ref=point_ref)

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
    # curve_list = set_name_line(curve_list, "magnet_2_line")
    S5 = SurfLine(
        line_list=curve_list,
        label=mag_label + "T1-S0",
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
    # curve_list = set_name_line(curve_list, "hole_4_line")
    S6 = SurfLine(line_list=curve_list, label=vent_label + "T1-S0", point_ref=point_ref)

    # Air surface between magnet_0 and magnet_1 with W1 == 0
    curve_list = list()
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z3s))
    curve_list.append(Segment(Z3s, Z6s))
    curve_list.append(Segment(Z6s, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z3))

    # initiating the label of the line on the air surface
    # curve_list = set_name_line(curve_list, "hole_2_line")
    point_ref = (Z5 + Z4) / 2

    S7 = SurfLine(line_list=curve_list, label=vent_label + "T2-S0", point_ref=point_ref)

    # Air surface without magnet_0 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z1, Z8))
    curve_list.append(Segment(Z8, Z5))
    curve_list.append(Segment(Z5, Z4))
    curve_list.append(Segment(Z4, Z1))

    # initiating the label of the line on the air surface
    # curve_list = set_name_line(curve_list, "hole_1_line")
    point_ref = (Z5 + Z1) / 2

    S8 = SurfLine(line_list=curve_list, label=vent_label + "T1-S0", point_ref=point_ref)

    # Air surface without magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z1s, Z8s))
    curve_list.append(Segment(Z8s, Z5s))
    curve_list.append(Segment(Z5s, Z4s))
    curve_list.append(Segment(Z4s, Z1s))

    # initiating the label of the line on the air surface
    # curve_list = set_name_line(curve_list, "hole_2_line")
    point_ref = (Z5s + Z1s) / 2

    S9 = SurfLine(line_list=curve_list, label=vent_label + "T0-S0", point_ref=point_ref)

    # Air surface No magnet and W1 == 0
    curve_list = list()
    curve_list.append(Segment(Z4, Z1))
    curve_list.append(Segment(Z1, Z8))
    curve_list.append(Segment(Z8, Z5))
    curve_list.append(Segment(Z5, Z8s))
    curve_list.append(Segment(Z8s, Z1s))
    curve_list.append(Segment(Z1s, Z4))

    # initiating the label of the line on the air surface
    # curve_list = set_name_line(curve_list, "hole_1_line")
    point_ref = (Z4 + Z5) / 2

    S12 = SurfLine(
        line_list=curve_list, label=vent_label + "T0-S0", point_ref=point_ref
    )

    # TODO correct vent_label TX id
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
    elif not self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        surf_list = [S8, S9]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        surf_list = [S12]
    else:
        raise Exception("Not implemented Yet")

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
