# -*- coding: utf-8 -*-

from numpy import angle
from scipy.optimize import fsolve

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        List of surface delimiting the winding zone

    """

    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"

    [Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1, rot_sign] = self._comp_point_coordinate()
    rot_sign = -rot_sign
    Ztan1 = (Z3 + Z8) / 2.0
    Ztan2 = (Z5 + Z6) / 2.0

    if self.H2 / 2.0 > self.R1:  # Zrad1 between Z8 and Z7
        Zmid = (Ztan1 + Ztan2) / 2.0
        x = fsolve(
            lambda x: angle((Z7 - (Zmid + 1j * x)) / (Z7 - Z8)),
            -(self.W2 + self.W1) / 4.0,
        )
        Zrad1 = Zmid + 1j * x[0]
        Zrad2 = Zrad1.conjugate()

    # Alternative points for uneven winding layers (cf ICEM 2020 publication)
    # Zmid1 = (Ztan1 + Ztan2) / 2
    # Zmid1 = (Zmid1 + Ztan1) / 2
    # Zmid2 = (Ztan1 + Ztan2) / 2
    # Zmid2 = (Zmid2 + Ztan2) / 2

    # x = fsolve(
    #     lambda x: angle((Z7 - (Zmid1 + 1j * x)) / (Z7 - Z8)), -(self.W2 + self.W1) / 4.0
    # )
    # Zrad1 = Zmid1 + 1j * x[0]

    # x = fsolve(
    #     lambda x: angle((Z4 - (Zmid2 + 1j * x)) / (Z4 - Z3)), (self.W2 + self.W1) / 4.0
    # )
    # Zrad2 = Zmid2 + 1j * x[0]
    # is_uneven = True

    surf_list = list()
    if Nrad == 1 and Ntan == 2:
        if is_simplified:  # no coincident lines allowed
            # Part 1 (0,0)
            curve_list = list()
            curve_list.append(Segment(Z8, Ztan1))
            curve_list.append(Segment(Ztan1, Ztan2))
            point_ref = (Z8 + Ztan1 + Ztan2 + Z6 + Z7) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (0,1)
            curve_list = list()
            curve_list.append(Segment(Ztan1, Z3))
            point_ref = (Ztan1 + Z3 + Z4 + Z5 + Ztan2) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            curve_list = list()
            curve_list.append(Segment(Z8, Ztan1))
            curve_list.append(Segment(Ztan1, Ztan2))
            if self.W2 > 2 * self.R1:
                curve_list.append(Segment(Ztan2, Z6))
            curve_list.append(
                Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=False)
            )
            curve_list.append(Segment(Z7, Z8))
            point_ref = (Z8 + Ztan1 + Ztan2 + Z6 + Z7) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (0,1)
            curve_list = list()
            curve_list.append(Segment(Ztan1, Z3))
            curve_list.append(Segment(Z3, Z4))
            curve_list.append(
                Arc1(Z4, Z5, rot_sign * self.R1, is_trigo_direction=False)
            )
            if self.W2 > 2 * self.R1:
                curve_list.append(Segment(Z5, Ztan2))
            curve_list.append(Segment(Ztan2, Ztan1))
            point_ref = (Ztan1 + Z3 + Z4 + Z5 + Ztan2) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    # elif is_uneven:  # For ICEM 2020 publication
    #     # Part 1 (0,0)
    #     curve_list = list()
    #     curve_list.append(Segment(Z8, Ztan1))
    #     curve_list.append(Segment(Ztan1, Zmid1))
    #     curve_list.append(Segment(Zmid1, Zrad1))
    #     curve_list.append(Segment(Zrad1, Z8))
    #     point_ref = (Z8 + Ztan1 + Zmid1 + Zrad1) / 4
    #     surface = SurfLine(
    #         line_list=curve_list, label="Wind" + st + "_R0_T0_S0", point_ref=point_ref
    #     )
    #     surf_list.append(surface)
    #     # Part2 (1,0)
    #     curve_list = list()
    #     curve_list.append(Segment(Zrad1, Zmid1))
    #     curve_list.append(Segment(Zmid1, Ztan2))
    #     if self.W2 > 2 * self.R1:
    #         curve_list.append(Segment(Ztan2, Z6))
    #     curve_list.append(Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=True))
    #     curve_list.append(Segment(Z7, Zrad1))
    #     point_ref = (Zrad1 + Zmid1 + Ztan2 + Z6 + Z7) / 5
    #     surface = SurfLine(
    #         line_list=curve_list, label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
    #     )
    #     surf_list.append(surface)
    #     # Part3 (0,1)
    #     curve_list = list()
    #     curve_list.append(Segment(Ztan1, Z3))
    #     curve_list.append(Segment(Z3, Zrad2))
    #     curve_list.append(Segment(Zrad2, Zmid2))
    #     curve_list.append(Segment(Zmid2, Ztan1))
    #     point_ref = (Ztan1 + Z3 + Zrad2 + Zmid2) / 4
    #     surface = SurfLine(
    #         line_list=curve_list, label="Wind" + st + "_R0_T1_S0", point_ref=point_ref
    #     )
    #     surf_list.append(surface)
    #     # Part4 (1,1)
    #     curve_list = list()
    #     curve_list.append(Segment(Zmid2, Zrad2))
    #     curve_list.append(Segment(Zrad2, Z4))
    #     curve_list.append(Arc1(Z4, Z5, rot_sign * self.R1, is_trigo_direction=True))
    #     if self.W2 > 2 * self.R1:
    #         curve_list.append(Segment(Z5, Ztan2))
    #     curve_list.append(Segment(Ztan2, Zmid2))
    #     point_ref = (Zmid2 + Zrad2 + Z4 + Z5 + Ztan2) / 5
    #     surface = SurfLine(
    #         line_list=curve_list, label="Wind" + st + "_R1_T1_S0", point_ref=point_ref
    #     )
    #     surf_list.append(surface)
    elif Nrad == 2 and Ntan == 1 and self.H2 / 2.0 > self.R1:
        if is_simplified:  # no coincident lines allowed
            # Part 1 (0,0)
            curve_list = list()
            curve_list.append(Segment(Z8, Z3))
            curve_list.append(Segment(Zrad2, Zrad1))
            point_ref = (Z8 + Z3 + Zrad2 + Zrad1) / 4
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            curve_list = list()
            point_ref = (Zrad2 + Zrad1 + Z4 + Z5 + Z6 + Z7) / 6
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            curve_list = list()
            curve_list.append(Segment(Z8, Z3))
            curve_list.append(Segment(Z3, Zrad2))
            curve_list.append(Segment(Zrad2, Zrad1))
            curve_list.append(Segment(Zrad1, Z8))
            point_ref = (Z8 + Z3 + Zrad2 + Zrad1) / 4
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            curve_list = list()
            curve_list.append(Segment(Zrad1, Zrad2))
            curve_list.append(Segment(Zrad2, Z4))
            curve_list.append(
                Arc1(Z4, Z5, rot_sign * self.R1, is_trigo_direction=False)
            )
            if self.W2 > 2 * self.R1:
                curve_list.append(Segment(Z5, Z6))
            curve_list.append(
                Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=False)
            )
            curve_list.append(Segment(Z7, Zrad1))
            point_ref = (Zrad2 + Zrad1 + Z4 + Z5 + Z6 + Z7) / 6
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    elif Nrad == 2 and Ntan == 2 and self.H2 / 2.0 > self.R1:
        if is_simplified:  # no coincident lines allowed
            # Part 1 (0,0)
            curve_list = list()
            curve_list.append(Segment(Z8, Ztan1))
            curve_list.append(Segment(Ztan1, Zmid))
            curve_list.append(Segment(Zmid, Zrad1))
            point_ref = (Z8 + Ztan1 + Zmid + Zrad1) / 4
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            curve_list = list()
            curve_list.append(Segment(Zmid, Ztan2))
            point_ref = (Zrad1 + Zmid + Ztan2 + Z6 + Z7) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part3 (0,1)
            curve_list = list()
            curve_list.append(Segment(Ztan1, Z3))
            curve_list.append(Segment(Zrad2, Zmid))
            point_ref = (Ztan1 + Z3 + Zrad2 + Zmid) / 4
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part4 (1,1)
            curve_list = list()
            point_ref = (Zmid + Zrad2 + Z4 + Z5 + Ztan2) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:

            # Part 1 (0,0)
            curve_list = list()
            curve_list.append(Segment(Z8, Ztan1))
            curve_list.append(Segment(Ztan1, Zmid))
            curve_list.append(Segment(Zmid, Zrad1))
            curve_list.append(Segment(Zrad1, Z8))
            point_ref = (Z8 + Ztan1 + Zmid + Zrad1) / 4
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            curve_list = list()
            curve_list.append(Segment(Zrad1, Zmid))
            curve_list.append(Segment(Zmid, Ztan2))
            if self.W2 > 2 * self.R1:
                curve_list.append(Segment(Ztan2, Z6))
            curve_list.append(Arc1(Z6, Z7, rot_sign * self.R1, is_trigo_direction=True))
            curve_list.append(Segment(Z7, Zrad1))
            point_ref = (Zrad1 + Zmid + Ztan2 + Z6 + Z7) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part3 (0,1)
            curve_list = list()
            curve_list.append(Segment(Ztan1, Z3))
            curve_list.append(Segment(Z3, Zrad2))
            curve_list.append(Segment(Zrad2, Zmid))
            curve_list.append(Segment(Zmid, Ztan1))
            point_ref = (Ztan1 + Z3 + Zrad2 + Zmid) / 4
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part4 (1,1)
            curve_list = list()
            curve_list.append(Segment(Zmid, Zrad2))
            curve_list.append(Segment(Zrad2, Z4))
            curve_list.append(Arc1(Z4, Z5, rot_sign * self.R1, is_trigo_direction=True))
            if self.W2 > 2 * self.R1:
                curve_list.append(Segment(Z5, Ztan2))
            curve_list.append(Segment(Ztan2, Zmid))
            point_ref = (Zmid + Zrad2 + Z4 + Z5 + Ztan2) / 5
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    else:
        # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z8, Z3))
        curve_list.append(Segment(Z3, Z4))
        if self.R1 * 2 < self.W2:
            curve_list.append(
                Arc1(
                    Z4,
                    Z5,
                    rot_sign * self.R1,
                    is_trigo_direction=not self.is_outwards(),
                )
            )
            curve_list.append(Segment(Z5, Z6))
            curve_list.append(
                Arc1(
                    Z6,
                    Z7,
                    rot_sign * self.R1,
                    is_trigo_direction=not self.is_outwards(),
                )
            )
        else:  # Z5 == Z6
            curve_list.append(Arc3(Z4, Z7, not self.is_outwards()))
        curve_list.append(Segment(Z7, Z8))
        surface = SurfLine(
            line_list=curve_list, label="Wind" + st + "_R0_T0_S0", point_ref=Zmid
        )
        surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
