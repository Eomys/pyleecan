# -*- coding: utf-8 -*-

from numpy import exp, pi, sqrt

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM58
        A HoleM58 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM58

    """

    if self.get_is_stator():  # check if the slot is on the stator
        st = "_Stator"
    else:
        st = "_Rotor"
    Rext = self.get_Rext()

    Z0 = Rext - self.H0
    Z2 = Z0 + 1j * (self.W0 / 2)
    Z1 = Z2 - 1j * self.W2
    Z12 = Z1 - 1j * self.W1
    Z11 = Z2 - 1j * self.W0
    Z5 = Z2 - self.H2
    Z6 = Z5 - 1j * self.W2
    Z7 = Z6 - 1j * self.W1
    Z8 = Z5 - 1j * self.W0

    Zc1 = (Rext - self.H1 - self.R0) * exp(1j * self.W3 / 2)

    # Z3 is the tangent point of the circle for (Z3,Z2)
    # (X3 - X2) * (X3 - Xc) + (Y3 - Y2) * (Y3 - Yc)
    # Z3 is on the circle
    # (X3 - Xc) ** 2 + (Y3 - Yc) ** 2 - R0 ** 2
    R0 = self.R0
    X2 = Z2.real
    Y2 = Z2.imag
    Xc = Zc1.real
    Yc = Zc1.imag
    # Solved with Sympy
    X3 = (
        R0 ** 2 * X2
        - R0 ** 2 * Xc
        - R0
        * Y2
        * sqrt(
            -(R0 ** 2)
            + X2 ** 2
            - 2 * X2 * Xc
            + Xc ** 2
            + Y2 ** 2
            - 2 * Y2 * Yc
            + Yc ** 2
        )
        + R0
        * Yc
        * sqrt(
            -(R0 ** 2)
            + X2 ** 2
            - 2 * X2 * Xc
            + Xc ** 2
            + Y2 ** 2
            - 2 * Y2 * Yc
            + Yc ** 2
        )
        + X2 ** 2 * Xc
        - 2 * X2 * Xc ** 2
        + Xc ** 3
        + Xc * Y2 ** 2
        - 2 * Xc * Y2 * Yc
        + Xc * Yc ** 2
    ) / (X2 ** 2 - 2 * X2 * Xc + Xc ** 2 + Y2 ** 2 - 2 * Y2 * Yc + Yc ** 2)
    Y3 = (
        R0 ** 2 * Y2
        - R0 ** 2 * Yc
        + R0
        * (X2 - Xc)
        * sqrt(
            -(R0 ** 2)
            + X2 ** 2
            - 2 * X2 * Xc
            + Xc ** 2
            + Y2 ** 2
            - 2 * Y2 * Yc
            + Yc ** 2
        )
        + X2 ** 2 * Yc
        - 2 * X2 * Xc * Yc
        + Xc ** 2 * Yc
        + Y2 ** 2 * Yc
        - 2 * Y2 * Yc ** 2
        + Yc ** 3
    ) / (X2 ** 2 - 2 * X2 * Xc + Xc ** 2 + Y2 ** 2 - 2 * Y2 * Yc + Yc ** 2)
    Z3 = X3 + 1j * Y3

    # Same for Z4
    X5 = Z5.real
    Y5 = Z5.imag
    X4 = (
        R0 ** 2 * X5
        - R0 ** 2 * Xc
        + R0
        * Y5
        * sqrt(
            -(R0 ** 2)
            + X5 ** 2
            - 2 * X5 * Xc
            + Xc ** 2
            + Y5 ** 2
            - 2 * Y5 * Yc
            + Yc ** 2
        )
        - R0
        * Yc
        * sqrt(
            -(R0 ** 2)
            + X5 ** 2
            - 2 * X5 * Xc
            + Xc ** 2
            + Y5 ** 2
            - 2 * Y5 * Yc
            + Yc ** 2
        )
        + X5 ** 2 * Xc
        - 2 * X5 * Xc ** 2
        + Xc ** 3
        + Xc * Y5 ** 2
        - 2 * Xc * Y5 * Yc
        + Xc * Yc ** 2
    ) / (X5 ** 2 - 2 * X5 * Xc + Xc ** 2 + Y5 ** 2 - 2 * Y5 * Yc + Yc ** 2)
    Y4 = (
        R0 ** 2 * Y5
        - R0 ** 2 * Yc
        - R0
        * (X5 - Xc)
        * sqrt(
            -(R0 ** 2)
            + X5 ** 2
            - 2 * X5 * Xc
            + Xc ** 2
            + Y5 ** 2
            - 2 * Y5 * Yc
            + Yc ** 2
        )
        + X5 ** 2 * Yc
        - 2 * X5 * Xc * Yc
        + Xc ** 2 * Yc
        + Y5 ** 2 * Yc
        - 2 * Y5 * Yc ** 2
        + Yc ** 3
    ) / (X5 ** 2 - 2 * X5 * Xc + Xc ** 2 + Y5 ** 2 - 2 * Y5 * Yc + Yc ** 2)
    Z4 = X4 + 1j * Y4

    Z9 = Z4.conjugate()
    Z10 = Z3.conjugate()
    Zc2 = Zc1.conjugate()

    surf_list = list()
    # Create all the surfaces for all the cases
    # Air surface Zc1 with magnet_0
    curve_list = list()
    if self.W2 > 0:
        curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Arc1(begin=Z3, end=Z4, radius=R0, is_trigo_direction=True))
    curve_list.append(Segment(Z4, Z5))
    if self.W2 > 0:
        curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z1))
    point_ref = Zc1
    S1 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Magnet_0 surface
    curve_list = list()
    curve_list.append(Segment(Z1, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z12))
    curve_list.append(Segment(Z12, Z1))
    point_ref = (Z1 + Z6 + Z7 + Z12) / 4
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

    # Air surface Zc2 with magnet_0
    curve_list = list()
    curve_list.append(Segment(Z12, Z7))
    if self.W2 + self.W1 < self.W0:
        curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Arc1(begin=Z9, end=Z10, radius=R0, is_trigo_direction=True))
    curve_list.append(Segment(Z10, Z11))
    if self.W2 + self.W1 < self.W0:
        curve_list.append(Segment(Z11, Z12))
    point_ref = Zc2
    S3 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Full surface, no magnet
    curve_list = list()
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Arc1(begin=Z3, end=Z4, radius=R0, is_trigo_direction=True))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Arc1(begin=Z9, end=Z10, radius=R0, is_trigo_direction=True))
    curve_list.append(Segment(Z10, Z11))
    curve_list.append(Segment(Z11, Z2))
    point_ref = Rext - self.H0 - self.H2 / 2
    S4 = SurfLine(line_list=curve_list, label="Hole" + st, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0:
        S1.label = S1.label + "_R0_T0_S0"  # Hole
        S3.label = S3.label + "_R0_T1_S0"  # Hole
        surf_list = [S1, S2, S3]
    else:
        S4.label = S1.label + "_R0_T0_S0"  # Hole
        surf_list = [S4]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
