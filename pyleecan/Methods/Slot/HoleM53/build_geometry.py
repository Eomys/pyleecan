# -*- coding: utf-8 -*-

from numpy import cos, exp, sin

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB


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
    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id = "R" + str(self.parent.hole.index(self)) + "-"
    vent_label = lam_label + "_" + HOLEV_LAB + "_" + R_id
    mag_label = lam_label + "_" + HOLEM_LAB + "_" + R_id

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
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]
    Z11 = point_dict["Z11"]

    Z1s = point_dict["Z1s"]
    Z2s = point_dict["Z2s"]
    Z3s = point_dict["Z3s"]
    Z4s = point_dict["Z4s"]
    Z5s = point_dict["Z5s"]
    Z6s = point_dict["Z6s"]
    Z7s = point_dict["Z7s"]
    Z8s = point_dict["Z8s"]
    Z9s = point_dict["Z9s"]
    Z10s = point_dict["Z10s"]
    Z11s = point_dict["Z11s"]
    Rext = self.get_Rext()

    # Air surface with magnet_0
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z10))
    curve_list.append(Segment(Z10, Z11))
    curve_list.append(
        Arc1(begin=Z11, end=Z1, radius=-Rext + self.H1, is_trigo_direction=False)
    )
    point_ref = (Z1 + Z2 + Z10 + Z11) / 4
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # magnet_0 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z5, Z9))
        curve_list.append(Segment(Z2, Z10))
    else:
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Segment(Z4, Z9))
        curve_list.append(Segment(Z9, Z10))
        curve_list.append(Segment(Z10, Z3))
    point_ref = (Z3 + Z4 + Z9 + Z10) / 4

    S2 = SurfLine(line_list=curve_list, label=mag_label + "T0-S0", point_ref=point_ref)

    # Air suface with magnet_0 and W1 > 0
    curve_list = list()
    if self.W2 > 0:
        curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    if self.W2 > 0:
        curve_list.append(Segment(Z8, Z9))
        curve_list.append(Segment(Z9, Z5))
        point_ref = (Z5 + Z6 + Z7 + Z8 + Z9) / 5
    else:
        curve_list.append(Segment(Z8, Z6))
        point_ref = (Z6 + Z7 + Z8) / 3
    S3 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface with magnet_1
    curve_list = list()
    curve_list.append(Segment(Z1s, Z2s))
    curve_list.append(Segment(Z2s, Z10s))
    curve_list.append(Segment(Z10s, Z11s))
    curve_list.append(Arc1(Z11s, Z1s, Rext - self.H1, is_trigo_direction=True))
    point_ref = (Z1s + Z2s + Z10s + Z11s) / 4
    S4 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # magnet_1 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(Segment(Z5s, Z9s))
        curve_list.append(Segment(Z2s, Z10s))
    else:
        curve_list.append(Segment(Z3s, Z4s))
        curve_list.append(Segment(Z4s, Z9s))
        curve_list.append(Segment(Z9s, Z10s))
        curve_list.append(Segment(Z10s, Z3s))
    point_ref = (Z3s + Z4s + Z9s + Z10s) / 4
    S5 = SurfLine(line_list=curve_list, label=mag_label + "T1-S0", point_ref=point_ref)

    # Air suface with magnet_1 and W1 > 0
    curve_list = list()
    if self.W2 > 0:
        curve_list.append(Segment(Z5s, Z6s))
    curve_list.append(Segment(Z6s, Z7s))
    curve_list.append(Segment(Z7s, Z8s))
    if self.W2 > 0:
        curve_list.append(Segment(Z8s, Z9s))
        curve_list.append(Segment(Z9s, Z5s))
        point_ref = (Z5s + Z6s + Z7s + Z8s + Z9s) / 5
    else:
        curve_list.append(Segment(Z8s, Z6s))
        point_ref = (Z6s + Z7s + Z8s) / 3
    S6 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air with both magnet and W1 = 0
    curve_list = list()
    if self.W2 > 0:
        curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z6s))
    if self.W2 > 0:
        curve_list.append(Segment(Z6s, Z5s))
    curve_list.append(Segment(Z5s, Z9s))
    if self.W2 > 0:
        curve_list.append(Segment(Z9s, Z8s))
        curve_list.append(Segment(Z8s, Z9))
    curve_list.append(Segment(Z9, Z5))
    point_ref = (Z6 + Z6s + Z8) / 3
    S7 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # first hole without magnet_0 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.H3 > 0:
        curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    if self.H3 > 0:
        curve_list.append(Segment(Z4, Z5))
    if self.W2 > 0:
        curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z11))
    curve_list.append(Arc1(Z11, Z1, -Rext + self.H1, is_trigo_direction=False))
    point_ref = (Z3 + Z4 + Z9 + Z10) / 4
    S8 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # second hole without magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(Segment(Z1s, Z2s))
    if self.H3 > 0:
        curve_list.append(Segment(Z2s, Z3s))
    curve_list.append(Segment(Z3s, Z4s))
    if self.H3 > 0:
        curve_list.append(Segment(Z4s, Z5s))
    if self.W2 > 0:
        curve_list.append(Segment(Z5s, Z6s))
    curve_list.append(Segment(Z6s, Z7s))
    curve_list.append(Segment(Z7s, Z8s))
    curve_list.append(Segment(Z8s, Z11s))
    curve_list.append(Arc1(Z11s, Z1s, -Rext + self.H1, is_trigo_direction=False))
    point_ref = (Z3s + Z4s + Z9s + Z10s) / 4
    S9 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # No magnet_1 and W1 = 0
    curve_list = list()
    curve_list.append(Segment(Z1s, Z2s))
    if self.H3 > 0:
        curve_list.append(Segment(Z2s, Z3s))
    curve_list.append(Segment(Z3s, Z4s))
    if self.H3 > 0:
        curve_list.append(Segment(Z4s, Z5s))
    if self.W2 > 0:
        curve_list.append(Segment(Z5s, Z6s))
    curve_list.append(Segment(Z6s, Z6))
    if self.W2 > 0:
        curve_list.append(Segment(Z6, Z5))
    curve_list.append(Segment(Z5, Z9))
    if self.W2 > 0:
        curve_list.append(Segment(Z9, Z8))
    curve_list.append(Segment(Z8s, Z11s))
    curve_list.append(Arc1(Z11s, Z1s, -Rext + self.H1, is_trigo_direction=False))
    point_ref = (Z3s + Z4s + Z9s + Z10s) / 4
    S10 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # No magnet_0 and W1 = 0
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    if self.H3 > 0:
        curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    if self.H3 > 0:
        curve_list.append(Segment(Z4, Z5))
    if self.W2 > 0:
        curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z6s))
    if self.W2 > 0:
        curve_list.append(Segment(Z6s, Z5s))
    curve_list.append(Segment(Z5s, Z9s))
    if self.W2 > 0:
        curve_list.append(Segment(Z9s, Z8s))
    curve_list.append(Segment(Z8, Z11))
    curve_list.append(Arc1(Z11, Z1, -Rext + self.H1, is_trigo_direction=False))
    point_ref = (Z3 + Z4 + Z9 + Z10) / 4
    S11 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # No magnet and W1 = 0
    curve_list = list()
    curve_list.append(Arc1(Z1, Z11, Rext - self.H1, is_trigo_direction=True))
    curve_list.append(Segment(Z11, Z8))
    curve_list.append(Segment(Z8, Z11s))
    curve_list.append(Arc1(Z11s, Z1s, Rext - self.H1, is_trigo_direction=True))
    curve_list.append(Segment(Z1s, Z2s))
    if self.H3 > 0:
        curve_list.append(Segment(Z2s, Z3s))
    curve_list.append(Segment(Z3s, Z4s))
    if self.H3 > 0:
        curve_list.append(Segment(Z4s, Z5s))
    if self.W2 > 0:
        curve_list.append(Segment(Z5s, Z6s))
    curve_list.append(Segment(Z6s, Z6))
    if self.W2 > 0:
        curve_list.append(Segment(Z6, Z5))
    if self.H3 > 0:
        curve_list.append(Segment(Z5, Z4))
    curve_list.append(Segment(Z4, Z3))
    if self.H3 > 0:
        curve_list.append(Segment(Z3, Z2))
    curve_list.append(Segment(Z2, Z1))

    point_ref = (Z6 + Z8 + Z6s) / 3
    S12 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0 and self.magnet_1 and self.W1 > 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S3.label = vent_label + "T1-S0"  # Hole
        S6.label = vent_label + "T2-S0"  # Hole
        S4.label = vent_label + "T3-S0"  # Hole
        surf_list = [S1, S2, S3, S6, S5, S4]
    elif self.magnet_0 and self.magnet_1 and self.W1 == 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S7.label = vent_label + "T1-S0"  # Hole
        S4.label = vent_label + "T2-S0"  # Hole
        surf_list = [S1, S2, S7, S5, S4]
    elif self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S3.label = vent_label + "T1-S0"  # Hole
        S9.label = vent_label + "T2-S0"  # Hole
        surf_list = [S1, S2, S3, S9]
    elif self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S10.label = vent_label + "T1-S0"  # Hole
        surf_list = [S1, S2, S10]
    elif not self.magnet_0 and self.magnet_1 and self.W1 > 0:
        S8.label = vent_label + "T0-S0"  # Hole
        S6.label = vent_label + "T1-S0"  # Hole
        S4.label = vent_label + "T2-S0"  # Hole
        surf_list = [S8, S6, S5, S4]
    elif not self.magnet_0 and self.magnet_1 and self.W1 == 0:
        S11.label = vent_label + "T0-S0"  # Hole
        S4.label = vent_label + "T2-S0"  # Hole
        surf_list = [S11, S5, S4]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S8.label = vent_label + "T0-S0"  # Hole
        S9.label = vent_label + "T1-S0"  # Hole
        surf_list = [S8, S9]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S12.label = vent_label + "T0-S0"  # Hole
        surf_list = [S12]

    # Apply the transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
