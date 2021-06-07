# -*- coding: utf-8 -*-

from numpy import exp, arcsin, tan, cos, sqrt, sin

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object
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

    # Z1
    delta1 = arcsin((self.R1 + self.W2) / (self.R1 + self.R3))
    alpha1 = self.W1 - delta1
    Z1 = self.R3 * exp(-1j * alpha1)

    # Zc1
    Zc1 = (self.R3 + self.R1) * exp(-1j * alpha1)
    xc1 = (self.R3 + self.R1) * cos(alpha1)
    yc1 = -(self.R3 + self.R1) * sin(alpha1)

    # Z2
    x2 = (-1 / tan(self.W1) * xc1 + yc1 - self.W2 / cos(self.W1)) / -(
        tan(self.W1) + 1 / tan(self.W1)
    )
    y2 = -tan(self.W1) * x2 + self.W2 / cos(self.W1)
    Z2 = x2 + 1j * y2

    # Z3
    a3 = 1 + tan(self.W1) ** 2
    b3 = -2 * tan(self.W1) * self.W2 / cos(self.W1)
    c3 = (self.W2 / cos(self.W1)) ** 2 - self.R2 ** 2

    x3 = (-b3 + sqrt(b3 ** 2 - 4 * a3 * c3)) / (2 * a3)
    y3 = -tan(self.W1) * x3 + self.W2 / cos(self.W1)
    Z3 = x3 + 1j * y3
    # Z5
    x5 = Rbo - self.H1
    y5 = -self.W0 / 2
    Z5 = x5 + 1j * y5
    # Zc2
    xc2 = Rbo - self.H1 - self.R1
    yc2 = -self.W0 / 2
    Zc2 = xc2 + 1j * yc2
    # Z4
    a4 = (xc2 - x3) ** 2 - self.R1 ** 2
    b4 = 2 * (xc2 - x3) * (y3 - yc2)
    c4 = (y3 - yc2) ** 2 - self.R1 ** 2
    alpha2 = (-b4 - sqrt(b4 ** 2 - 4 * a4 * c4)) / (2 * a4)
    x4 = (xc2 / alpha2 + yc2 + alpha2 * x3 - y3) / (alpha2 + 1 / alpha2)
    y4 = alpha2 * (x4 - x3) + y3
    Z4 = x4 + 1j * y4
    # symmetry
    Z6 = Z5.conjugate()
    Z7 = Z4.conjugate()
    Z8 = Z3.conjugate()
    Z9 = Z2.conjugate()
    Z10 = Z1.conjugate()

    # Creation of the magnet curve
    curve_list_mag = list()
    curve_list_mag.append(Segment(Z3, Z4))
    curve_list_mag.append(Segment(Z4, Z7))
    curve_list_mag.append(Segment(Z7, Z8))
    curve_list_mag.append(Segment(Z8, Z3))

    point_ref = (Z3 + Z4 + Z7 + Z8) / 4

    # curve_list_mag = list()
    # curve_list_mag.append(
    #     Arc1(begin=Z1, end=Z2, radius=self.R1, is_trigo_direction=True)
    # )
    # curve_list_mag.append(Segment(Z2, Z3))
    # curve_list_mag.append(Segment(Z3, Z4))
    # curve_list_mag.append(
    #     Arc1(begin=Z4, end=Z5, radius=self.R1, is_trigo_direction=True)
    # )
    # curve_list_mag.append(Segment(Z5, Z6))
    # curve_list_mag.append(
    #     Arc1(begin=Z6, end=Z7, radius=self.R1, is_trigo_direction=True)
    # )
    # curve_list_mag.append(Segment(Z7, Z8))
    # curve_list_mag.append(Segment(Z8, Z9))
    # curve_list_mag.append(
    #     Arc1(begin=Z9, end=Z10, radius=self.R1, is_trigo_direction=True)
    # )
    # curve_list_mag.append(
    #     Arc1(begin=Z10, end=Z1, radius=-self.R3, is_trigo_direction=False)
    # )
    # point_ref = (Z1 + Z2 + Z3 + Z4 + Z5 + Z6 + Z7 + Z8 + Z9 + Z10) / 10
    # Defining type of magnetization of the magnet
    if self.magnet_0:
        if self.magnet_0.type_magnetization == 0:
            type_mag = "_Radial"
        else:
            type_mag = "_Parallel"
    else:
        type_mag = "None"

    magnet_label = "HoleMagnet" + st + type_mag + "_N_R0_T0_S0"

    # if self.magnet_0:
    #     S1 = SurfLine(line_list=curve_list_mag, label=magnet_label, point_ref=point_ref)

    # else:
    #     S1 = SurfLine(line_list=curve_list_mag, label="Hole", point_ref=point_ref)

    # surf_list = [S1]

    S1 = SurfLine(line_list=curve_list_mag, label=magnet_label, point_ref=point_ref)

    # Creation of the air curve (bottom)

    curve_list_air = list()
    curve_list_air.append(
        Arc1(begin=Z1, end=Z2, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(Segment(Z2, Z3))
    curve_list_air.append(Segment(Z3, Z8))
    curve_list_air.append(Segment(Z8, Z9))
    curve_list_air.append(
        Arc1(begin=Z9, end=Z10, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(
        Arc1(begin=Z10, end=Z1, radius=-self.R3, is_trigo_direction=False)
    )
    point_ref = (Z1 + Z2 + Z3 + Z8 + Z9 + Z10) / 6

    S2 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # Creation of the second air curve (top)
    curve_list_air = list()
    curve_list_air.append(
        Arc1(begin=Z4, end=Z5, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(Segment(Z5, Z6))

    curve_list_air.append(
        Arc1(begin=Z6, end=Z7, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(Segment(Z7, Z4))

    point_ref = (Z4 + Z5 + Z6 + Z7) / 4

    S3 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    # Air without magnet (S4=S1+S2+S3)
    curve_list_air = list()
    curve_list_air.append(
        Arc1(begin=Z1, end=Z2, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(Segment(Z2, Z3))
    curve_list_air.append(Segment(Z3, Z4))
    curve_list_air.append(
        Arc1(begin=Z4, end=Z5, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(Segment(Z5, Z6))
    curve_list_air.append(
        Arc1(begin=Z6, end=Z7, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(Segment(Z7, Z8))
    curve_list_air.append(Segment(Z8, Z9))
    curve_list_air.append(
        Arc1(begin=Z9, end=Z10, radius=self.R1, is_trigo_direction=True)
    )
    curve_list_air.append(
        Arc1(begin=Z10, end=Z1, radius=-self.R3, is_trigo_direction=False)
    )
    point_ref = (Z1 + Z2 + Z3 + Z4 + Z5 + Z6 + Z7 + Z8 + Z9 + Z10) / 10

    S4 = SurfLine(line_list=curve_list_air, label="Hole" + st, point_ref=point_ref)

    if self.magnet_0:
        S2.label = S2.label + "_R0_T0_S0"  # Hole
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
