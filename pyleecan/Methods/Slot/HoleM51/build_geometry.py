# -*- coding: utf-8 -*-

from numpy import exp, pi, cos, sin, tan

from ....Classes.Segment import Segment
from ....Classes.Arc1 import Arc1
from ....Classes.SurfLine import SurfLine


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
        st = "_Stator"
    else:
        st = "_Rotor"
    Rext = self.get_Rext()

    # Get all the points
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z8 = point_dict["Z8"]
    Z9 = point_dict["Z9"]
    Z11 = point_dict["Z11"]
    Z13 = point_dict["Z13"]
    Z14 = point_dict["Z14"]
    Z16 = point_dict["Z16"]
    Z18 = point_dict["Z18"]
    Z19 = point_dict["Z19"]
    Z21 = point_dict["Z21"]
    Z22 = point_dict["Z22"]
    Z23 = point_dict["Z23"]
    Z24 = point_dict["Z24"]
    Z25 = point_dict["Z25"]
    Z26 = point_dict["Z26"]

    surf_list = list()
    # Create all the surfaces for all the cases
    # Air surface bore around magnet_0
    curve_list = list()
    curve_list.append(Arc1(Z21, Z22, Rext - self.H1))
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
    # Defining type of magnetization of the magnet
    if self.magnet_0:
        if self.magnet_0.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"
    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T0_S0"
    S2 = SurfLine(line_list=curve_list, label=magnet_label, point_ref=point_ref)

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
    # Defining type of magnetization of the magnet
    if self.magnet_1:
        if self.magnet_1.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"
    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T1_S0"
    S4 = SurfLine(line_list=curve_list, label=magnet_label, point_ref=point_ref)

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
    # Defining type of magnetization of the magnet
    if self.magnet_2:
        if self.magnet_2.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"
    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T2_S0"
    S6 = SurfLine(line_list=curve_list, label=magnet_label, point_ref=point_ref)

    # Air surface bore around magnet_2
    curve_list = list()
    curve_list.append(Arc1(Z5, Z6, Rext - self.H1))
    curve_list.append(Segment(Z6, Z8))
    curve_list.append(Segment(Z8, Z4))
    curve_list.append(Segment(Z4, Z5))
    point_ref = (Z4 + Z5 + Z6 + Z8) / 4
    S7 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_2 (no magnet_2 and magnet_1)
    curve_list = list()
    curve_list.append(Arc1(Z5, Z6, Rext - self.H1))
    curve_list.append(Segment(Z6, Z11))
    curve_list.append(Segment(Z11, Z13))
    curve_list.append(Segment(Z13, Z1))
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z5))
    point_ref = (Z2 + Z11) / 2
    S8 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface bore around magnet_0 (no magnet_0 and magnet_1)
    curve_list = list()
    curve_list.append(Arc1(Z21, Z22, Rext - self.H1))
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
    curve_list.append(Arc1(Z21, Z22, Rext - self.H1))
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
    curve_list.append(Arc1(Z5, Z6, Rext - self.H1))
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
    curve_list.append(Arc1(Z5, Z6, Rext - self.H1))
    curve_list.append(Segment(Z6, Z11))
    curve_list.append(Segment(Z11, Z16))
    curve_list.append(Segment(Z16, Z21))
    curve_list.append(Arc1(Z21, Z22, Rext - self.H1))
    curve_list.append(Segment(Z22, Z25))
    curve_list.append(Segment(Z25, Z2))
    curve_list.append(Segment(Z2, Z5))
    point_ref = (Z1 + Z13) / 2
    S13 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0 and self.magnet_1 and self.magnet_2:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S3.label = S3.label + "_R0_T1_S0"  # Hole
        S5.label = S5.label + "_R0_T2_S0"  # Hole
        S7.label = S7.label + "_R0_T3_S0"  # Hole
        surf_list = [S1, S2, S3, S4, S5, S6, S7]
    elif not self.magnet_0 and self.magnet_1 and self.magnet_2:
        S9.label = S9.label + "_R0_T0_S0"  # Hole
        S5.label = S5.label + "_R0_T1_S0"  # Hole
        S7.label = S7.label + "_R0_T2_S0"  # Hole
        surf_list = [S9, S4, S5, S6, S7]
    elif self.magnet_0 and not self.magnet_1 and self.magnet_2:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S10.label = S10.label + "_R0_T1_S0"  # Hole
        S7.label = S7.label + "_R0_T2_S0"  # Hole
        surf_list = [S1, S2, S10, S6, S7]
    elif not self.magnet_0 and not self.magnet_1 and self.magnet_2:
        S11.label = S11.label + "_R0_T0_S0"  # Hole
        S7.label = S7.label + "_R0_T1_S0"  # Hole
        surf_list = [S11, S6, S7]
    elif self.magnet_0 and self.magnet_1 and not self.magnet_2:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S3.label = S3.label + "_R0_T1_S0"  # Hole
        S8.label = S8.label + "_R0_T2_S0"  # Hole
        surf_list = [S1, S2, S3, S4, S8]
    elif not self.magnet_0 and self.magnet_1 and not self.magnet_2:
        S9.label = S9.label + "_R0_T0_S0"  # Hole
        S8.label = S8.label + "_R0_T1_S0"  # Hole
        surf_list = [S9, S4, S8]
    elif self.magnet_0 and not self.magnet_1 and not self.magnet_2:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S12.label = S12.label + "_R0_T1_S0"  # Hole
        surf_list = [S1, S2, S12]
    elif not self.magnet_0 and not self.magnet_1 and not self.magnet_2:
        S13.label = S13.label + "_R0_T0_S0"  # Hole
        surf_list = [S13]

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
