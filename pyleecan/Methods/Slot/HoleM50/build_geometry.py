# -*- coding: utf-8 -*-

from numpy import arcsin, arctan, cos, exp, array, angle, pi
from numpy import imag as np_imag
from scipy.optimize import fsolve

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM50

    """

    if self.get_is_stator():  # check if the slot is on the stator
        st = "_Stator"
    else:
        st = "_Rotor"
    Rext = self.get_Rext()

    # magnet pole pitch angle, must be <2*pi/2*p
    alpham = 2 * arcsin(self.W0 / (2 * (Rext - self.H1)))  # angle (Z9,0,Z9')

    Harc = (Rext - self.H1) * (1 - cos(alpham / 2))
    # alpha on schematics
    gammam = arctan((self.H0 - self.H1 - Harc) / (self.W0 / 2.0 - self.W1 / 2.0))
    #  betam = pi/2-alpham/2-gammam;#40.5
    hssp = pi / self.Zh

    x78 = (self.H3 - self.H2) / cos(gammam)  # distance from 7 to 8
    Z9 = Rext - Harc - self.H1 - 1j * self.W0 / 2
    Z8 = Rext - self.H0 - 1j * self.W1 / 2
    Z7 = Rext - self.H0 - x78 - 1j * self.W1 / 2
    Z1 = (Rext - self.H1) * exp(1j * (-hssp + arcsin(self.W3 / (2 * (Rext - self.H1)))))
    Z11 = (Z1 * exp(1j * hssp) + self.H4) * exp(-1j * hssp)
    Z10 = (Z9 * exp(1j * hssp) + self.H4) * exp(-1j * hssp)

    # Magnet coordinate with Z8 as center and x as the top edge of the magnet
    Z8b = self.W2
    Z8c = Z8b + self.W4
    Z5 = Z8b - 1j * self.H3
    Z4 = Z8c - 1j * self.H3
    Z6 = Z5 + 1j * self.H2
    Z3 = Z4 + 1j * self.H2

    Zmag = array([Z8b, Z6, Z5, Z4, Z3, Z8c])
    Zmag = Zmag * exp(1j * angle(Z9 - Z8))
    Zmag = Zmag + Z8

    # final complex numbers Zmag=[Z8b Z6 Z5 Z4 Z3 Z8c]
    (Z8b, Z6, Z5, Z4, Z3, Z8c) = Zmag

    # Rotation so [Z1,Z2] is parallel to the x axis
    Z3r, Z1r, Z6r = Z3 * exp(1j * hssp), Z1 * exp(1j * hssp), Z6 * exp(1j * hssp)
    # numerical resolution to find the last point Z2
    x = fsolve(lambda x: np_imag((Z3r - (Z1r - x)) / (Z6r - Z3r)), self.H3 - self.H2)
    Z2 = (Z1r - x[0]) * exp(-1j * hssp)

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
    Z8cs = Z8c.conjugate()
    Z8bs = Z8b.conjugate()

    surf_list = list()

    # Create all the surfaces for all the cases
    # Air surface (W3) with magnet_0
    curve_list = list()
    curve_list.append(Segment(Z1, Z2, label=""))
    curve_list.append(Segment(Z2, Z3, label=""))
    curve_list.append(Segment(Z3, Z8c, label="Hole_0_Right"))
    curve_list.append(Segment(Z8c, Z9, label="Hole_0_Top"))
    if self.H4 > 0:
        curve_list.append(Segment(Z9, Z10, label=""))
    curve_list.append(
        Arc1(
            Z10,
            Z11,
            -Rext + self.H1,
            is_trigo_direction=False,
            label="Tangential_Bridge",
        )
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11, Z1, label=""))
    point_ref = (Z1 + Z2 + Z3 + Z8c + Z9 + Z10 + Z11) / 7
    S1 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Magnet_0 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z8c, Z3, label=""))
        curve_list.append(Segment(Z6, Z8b, label=""))
    else:
        if Z3 != Z4:  # Z3 == Z4 if H2 = 0
            curve_list.append(Segment(Z3, Z4, label="Magnet_0_Right"))
        curve_list.append(Segment(Z4, Z5, label="Magnet_0_Bottom"))
        if Z5 != Z6:  # Z5 == Z6 if H2 = 0
            curve_list.append(Segment(Z5, Z6, label="Magnet_0_Left"))
        curve_list.append(Segment(Z6, Z8b, label="Magnet_0_Left"))
        curve_list.append(Segment(Z8b, Z8c, label="Magnet_0_Top"))
        curve_list.append(Segment(Z8c, Z3, label="Magnet_0_Right"))
    point_ref = (Z3 + Z4 + Z5 + Z6 + Z8b + Z8c) / 6

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

    # Air surface with magnet_0 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z6, Z7, label=""))
    curve_list.append(Segment(Z7, Z8, label="Radial_Bridge"))
    if self.W2 > 0:  # if W2=0 Z8 = Z8b
        curve_list.append(Segment(Z8, Z8b, label=""))
    curve_list.append(Segment(Z8b, Z6, label="Hole_0_Left"))
    point_ref = (Z6 + Z7 + Z8 + Z8b) / 4

    S3 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Symmetry Air surface (W3) with magnet_1
    curve_list = list()
    curve_list.append(Segment(Z1s, Z2s, label=""))
    curve_list.append(Segment(Z2s, Z3s, label=""))
    curve_list.append(Segment(Z3s, Z8cs, label="Hole_1_Left"))
    curve_list.append(Segment(Z8cs, Z9s, label="Hole_1_Top"))
    if self.H4 > 0:
        curve_list.append(Segment(Z9s, Z10s, label=""))
    curve_list.append(
        Arc1(
            Z10s,
            Z11s,
            Rext - self.H1,
            is_trigo_direction=True,
            label="Tangential_Bridge",
        )
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11s, Z1s, label=""))
    point_ref = (Z1s + Z2s + Z3s + Z8cs + Z9s + Z10s + Z11s) / 7

    S4 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # magnet_1 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z8cs, Z3s, label=""))
        curve_list.append(Segment(Z6s, Z8bs, label=""))
    else:
        if Z3s != Z4s:  # Z3 == Z3 if H2 = 0
            curve_list.append(Segment(Z3s, Z4s, label="Magnet_1_Left"))
        curve_list.append(Segment(Z4s, Z5s, label="Magnet_1_Bottom"))
        if Z5s != Z6s:  # Z5 == Z6 if H2 = 0
            curve_list.append(Segment(Z5s, Z6s, label="Magnet_1_Right"))
        curve_list.append(Segment(Z6s, Z8bs, label="Magnet_1_Right"))
        curve_list.append(Segment(Z8bs, Z8cs, label="Magnet_1_Top"))
        curve_list.append(Segment(Z8cs, Z3s, label="Magnet_1_Left"))
    point_ref = (Z3s + Z4s + Z5s + Z6s + Z8bs + Z8cs) / 6
    # Defining type of magnetization of the magnet
    if self.magnet_1:
        if self.magnet_1.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"
    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T1_S0"
    S5 = SurfLine(line_list=curve_list, label=magnet_label, point_ref=point_ref)

    # Air surface with magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z6s, Z7s, label=""))
    curve_list.append(Segment(Z7s, Z8s, label="Radial_Bridge"))  # rad. bridge
    if self.W2 > 0:  # if W2=0: Z8s = Z8bs
        curve_list.append(Segment(Z8s, Z8bs, label="Hole_1_Top"))
    curve_list.append(Segment(Z8bs, Z6s, label="Hole_1_Right"))
    point_ref = (Z6s + Z7s + Z8s + Z8bs) / 4

    S6 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface both magnets and W1 = 0 (S6 + S3)
    curve_list = list()
    curve_list.append(Segment(Z6, Z7, label=""))
    curve_list.append(Segment(Z7, Z6s, label=""))
    curve_list.append(Segment(Z6s, Z8bs, label="Hole_1_Right"))
    if self.W2 > 0:  # If W2 = 0: Z8b = Z8 = Z8bs
        curve_list.append(Segment(Z8bs, Z8s, label="Hole_1_Top"))
        curve_list.append(Segment(Z8s, Z8b, label="Hole_0_Top"))
    curve_list.append(Segment(Z8b, Z6, label="Hole_0_Left"))  # == Magnet_0_Left
    point_ref = (Z6 + Z7 + Z6s + Z8s + Z8bs + Z8b) / 6
    S7 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface without magnet_0 and W1 > 0 (S1 + S2 + S3)
    curve_list = list()
    curve_list.append(Segment(Z1, Z2, label=""))
    curve_list.append(Segment(Z2, Z3, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z3, Z4, label=""))
    curve_list.append(Segment(Z4, Z5, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z5, Z6, label=""))
    curve_list.append(Segment(Z6, Z7, label=""))
    curve_list.append(Segment(Z7, Z8, label=""))
    curve_list.append(Segment(Z8, Z9, label=""))
    if self.H4 > 0:
        curve_list.append(Segment(Z9, Z10))
    curve_list.append(
        Arc1(Z10, Z11, -Rext + self.H1, is_trigo_direction=False, label="")
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11, Z1))
    point_ref = (Z1 + Z2 + Z3 + Z8c + Z9 + Z10 + Z11) / 7
    S8 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface without magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z1s, Z2s, label=""))
    curve_list.append(Segment(Z2s, Z3s, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z3s, Z4s, label=""))
    curve_list.append(Segment(Z4s, Z5s, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z5s, Z6s, label=""))
    curve_list.append(Segment(Z6s, Z7s, label=""))
    curve_list.append(Segment(Z7s, Z8s, label=""))
    curve_list.append(Segment(Z8s, Z9s, label=""))
    if self.H4 > 0:
        curve_list.append(Segment(Z9s, Z10s, label=""))
    curve_list.append(
        Arc1(Z10s, Z11s, Rext - self.H1, is_trigo_direction=True, label="")
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11s, Z1, label=""))
    point_ref = (Z1s + Z2s + Z3s + Z8cs + Z9s + Z10s + Z11s) / 7
    S9 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface with magnet_0 without magnet_1 and W1 = 0
    # (S4 + S5 + S7)
    curve_list = list()
    curve_list.append(Segment(Z1s, Z2s, label=""))
    curve_list.append(Segment(Z2s, Z3s, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z3s, Z4s, label=""))
    curve_list.append(Segment(Z4s, Z5s, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z5s, Z6s, label=""))
    curve_list.append(Segment(Z6s, Z7s, label=""))
    curve_list.append(Segment(Z7s, Z6, label=""))
    curve_list.append(Segment(Z6, Z8b, label=""))
    if Z8b != Z8s:
        curve_list.append(Segment(Z8b, Z8s, label=""))
    curve_list.append(Segment(Z8s, Z9s, label=""))
    if self.H4 > 0:
        curve_list.append(Segment(Z9s, Z10s, label=""))
    curve_list.append(
        Arc1(Z10s, Z11s, Rext - self.H1, is_trigo_direction=True, label="")
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11s, Z1s, label=""))
    point_ref = (Z1s + Z2s + Z3s + Z8cs + Z9s + Z10s + Z11s) / 7
    S10 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface with magnet_1 without magnet_0 and W1 = 0
    # (S1 + S2 + S7)
    curve_list = list()
    curve_list.append(Segment(Z1, Z2, label=""))
    curve_list.append(Segment(Z2, Z3, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z3, Z4, label=""))
    curve_list.append(Segment(Z4, Z5, label=""))
    if self.H2 > 0:
        curve_list.append(Segment(Z5, Z6, label=""))
    curve_list.append(Segment(Z6, Z7, label=""))
    curve_list.append(Segment(Z7, Z6s, label=""))
    curve_list.append(Segment(Z6s, Z8bs, label=""))
    if Z8bs != Z8:
        curve_list.append(Segment(Z8bs, Z8, label=""))
    curve_list.append(Segment(Z8, Z9, label=""))
    if self.H4 > 0:
        curve_list.append(Segment(Z9, Z10, label=""))
    curve_list.append(
        Arc1(Z10, Z11, -Rext + self.H1, is_trigo_direction=False, label="")
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11, Z1, label=""))
    point_ref = (Z1 + Z2 + Z3 + Z8c + Z9 + Z10 + Z11) / 7
    S11 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Air surface without magnets and W1 = 0
    # (S4 + S5 + S7 + S2 + S1)
    curve_list = list()
    curve_list.append(Segment(Z1, Z2, label=""))
    curve_list.append(Segment(Z2, Z3, label=""))
    if Z3 != Z4:  # if H2 = 0
        curve_list.append(Segment(Z3, Z4, label=""))
    curve_list.append(Segment(Z4, Z5, label=""))
    if Z5 != Z6:  # if H2 = 0
        curve_list.append(Segment(Z5, Z6, label=""))
    curve_list.append(Segment(Z6, Z7, label=""))
    curve_list.append(Segment(Z7, Z6s, label=""))
    if Z5s != Z6s:
        curve_list.append(Segment(Z6s, Z5s, label=""))
    curve_list.append(Segment(Z5s, Z4s, label=""))
    if Z3s != Z4s:
        curve_list.append(Segment(Z4s, Z3s, label=""))
    curve_list.append(Segment(Z3s, Z2s, label=""))
    curve_list.append(Segment(Z2s, Z1s, label=""))
    if self.H4 > 0:
        curve_list.append(Segment(Z1s, Z11s, label=""))
    curve_list.append(Arc1(Z11s, Z10s, -Rext + self.H1, is_trigo_direction=False))
    if self.H4 > 0:
        curve_list.append(Segment(Z10s, Z9s, label=""))
    curve_list.append(Segment(Z9s, Z8s, label=""))
    curve_list.append(Segment(Z8s, Z9, label=""))
    if self.H4 > 0:
        curve_list.append(Segment(Z9, Z10, label=""))
    curve_list.append(
        Arc1(Z10, Z11, -Rext + self.H1, is_trigo_direction=False, label="")
    )
    if self.H4 > 0:
        curve_list.append(Segment(Z11, Z1, label=""))

    point_ref = (Z6 + Z8b + Z7 + Z8 + Z6s + Z8bs) / 6
    S12 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

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
        S4.label = S4.label + "_R0_T1_S0"  # Hole
        surf_list = [S11, S5, S4]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S8.label = S8.label + "_R0_T0_S0"  # Hole
        S9.label = S9.label + "_R0_T1_S0"  # Hole
        surf_list = [S8, S9]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S12.label = S12.label + "_R0_T0_S0"  # Hole
        surf_list = [S12]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
