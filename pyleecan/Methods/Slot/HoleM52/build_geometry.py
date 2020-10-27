# -*- coding: utf-8 -*-

from numpy import exp

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
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
    Rbo = self.get_Rbo()

    alpha1 = self.comp_alpha()
    Z1 = (Rbo - self.H0) * exp(1j * alpha1 / 2)
    Z9 = (Rbo - self.H0) * exp(-1j * alpha1 / 2)

    Z0 = (Z1 + Z9) / 2
    Z5 = Z0 - self.H1

    Z4 = Z5 + 1j * self.W0 / 2
    Z6 = Z4.conjugate()

    Z3 = Z4 + self.H2
    Z7 = Z3.conjugate()

    W1 = self.comp_W1()
    Z2 = Z3 + 1j * W1
    Z8 = Z2.conjugate()

    Z11 = Z3 + (self.H1 - self.H2)
    Z10 = Z7 + (self.H1 - self.H2)

    # Creation of the air curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z11))
    curve_list.append(Segment(Z11, Z1))
    point_ref = (Z1 + Z2 + Z3 + Z11) / 4
    S1 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Creation of the magnet curve
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z3, Z11))
        curve_list.append(Segment(Z7, Z10))
    else:
        curve_list.append(Segment(Z4, Z11))
        curve_list.append(Segment(Z11, Z10))
        curve_list.append(Segment(Z10, Z6))
        curve_list.append(Segment(Z6, Z4))
    point_ref = (Z11 + Z4 + Z6 + Z10) / 4
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

    # Creation of the second air curve
    curve_list = list()
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Segment(Z9, Z10))
    curve_list.append(Segment(Z10, Z7))
    point_ref = (Z7 + Z8 + Z9 + Z10) / 4
    S3 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Area with no magnet (S1 + S2 + S3)
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    if self.H2 > 0:
        curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z6))
    if self.H2 > 0:
        curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Segment(Z9, Z1))
    point_ref = (Z11 + Z4 + Z6 + Z10) / 4
    S4 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    if self.magnet_0:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S3.label = S3.label + "_R0_T1_S0"  # Hole
        surf_list = [S1, S2, S3]
    else:
        S4.label = S4.label + "_R0_T0_S0"  # Hole
        surf_list = [S4]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
