# -*- coding: utf-8 -*-

from numpy import exp

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB


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
    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    vent_label = lam_label + "_" + surf_type + "_R" + str(R_id) + "-"
    mag_label = lam_label + "_" + HOLEM_LAB + "_R" + str(R_id) + "-"

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]
    Z11 = point_dict["Z11"]

    # modify points for void radius in case
    is_radius = False
    if self.R0 > 0:
        if self.R0 < (self.H1 - self.H2) and self.R0 < self.W1:
            is_radius = True
            Z1R = Z1 - 1j * self.R0
            Z1L = Z1 - self.R0
            Z9L = Z9 + 1j * self.R0
            Z9R = Z9 - self.R0

        else:
            self.get_logger().warning("Radius R0 enforced to 0.")

    # Creation of the air curve
    curve_list = list()
    if is_radius:
        curve_list.append(Arc1(Z1R, Z1L, self.R0))
    curve_list.append(Segment(Z1L if is_radius else Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z11))
    curve_list.append(Segment(Z11, Z1R if is_radius else Z1))
    point_ref = (Z1 + Z2 + Z3 + Z11) / 4
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)

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
    S2 = SurfLine(line_list=curve_list, label=mag_label + "T0-S0", point_ref=point_ref)

    # Creation of the second air curve
    curve_list = list()
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9R if is_radius else Z9))
    if is_radius:
        curve_list.append(Arc1(Z9R, Z9L, self.R0))
    curve_list.append(Segment(Z9L if is_radius else Z9, Z10))
    curve_list.append(Segment(Z10, Z7))
    point_ref = (Z7 + Z8 + Z9 + Z10) / 4
    S3 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Area with no magnet (S1 + S2 + S3)
    curve_list = list()
    if is_radius:
        curve_list.append(Arc1(Z1R, Z1L, self.R0))
    curve_list.append(Segment(Z1L if is_radius else Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    if self.H2 > 0:
        curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z6))
    if self.H2 > 0:
        curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9R if is_radius else Z9))
    if is_radius:
        curve_list.append(Arc1(Z9R, Z9L, self.R0))
    curve_list.append(Segment(Z9L if is_radius else Z9, Z1R if is_radius else Z1))
    point_ref = (Z11 + Z4 + Z6 + Z10) / 4
    S4 = SurfLine(line_list=curve_list, point_ref=point_ref)

    if self.magnet_0:
        S1.label = vent_label + "T0-S0"  # Hole
        S3.label = vent_label + "T1-S0"  # Hole
        surf_list = [S1, S2, S3]
    else:
        S4.label = vent_label + "T0-S0"  # Hole
        surf_list = [S4]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
