# -*- coding: utf-8 -*-


from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB, update_RTS_index


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
    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    RTS_id = "R" + str(self.parent.hole.index(self)) + "-T0-S0"
    vent_label = lam_label + "_" + HOLEV_LAB + "_" + RTS_id
    mag_label = lam_label + "_" + HOLEM_LAB + "_" + RTS_id

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

    surf_list = list()
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

    # if self.magnet_0:
    #     S1 = SurfLine(line_list=curve_list_mag, label=magnet_label, point_ref=point_ref)

    # else:
    #     S1 = SurfLine(line_list=curve_list_mag, label="Hole", point_ref=point_ref)

    # surf_list = [S1]

    S1 = SurfLine(line_list=curve_list_mag, label=mag_label, point_ref=point_ref)

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

    S2 = SurfLine(line_list=curve_list_air, label=vent_label, point_ref=point_ref)

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

    S3 = SurfLine(line_list=curve_list_air, label=vent_label, point_ref=point_ref)

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

    S4 = SurfLine(line_list=curve_list_air, label=vent_label, point_ref=point_ref)

    if self.magnet_0:
        S2.label = update_RTS_index(S2.label, T_id=0)
        S3.label = update_RTS_index(S3.label, T_id=1)
        surf_list = [S1, S2, S3]
    else:
        S4.label = update_RTS_index(S4.label, T_id=0)
        surf_list = [S4]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
