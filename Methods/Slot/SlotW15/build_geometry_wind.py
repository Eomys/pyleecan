# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW15.build_geometry_wind
SlotW15 build_geometry_wind method
@date Created on Mon Nov 27 15:58:38 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import angle
from scipy.optimize import fsolve

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surface delimiting the winding zone

    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"
    [
        Z13,
        Z12,
        Z11,
        Z10,
        Z9,
        Z8,
        Z7,
        Z6,
        Z5,
        Z4,
        Z3,
        Z2,
        Z1,
    ] = self._comp_point_coordinate()

    Ztan1 = (Z2 + Z12) / 2.0
    Ztan2 = Z7
    Zmid = (Ztan1 + Ztan2) / 2.0

    # Zrad1 between Z10 and Z9
    x = fsolve(lambda x: angle((Z10 - (Zmid + 1j * x)) / (Z10 - Z9)), -self.R1)
    Zrad1 = Zmid + 1j * x[0]
    Zrad2 = Zrad1.conjugate()

    # We can split in rad only if Zrad1 is between Z10 and Z9
    is_rad_splittable = Z10.real < Zrad1.real and Zrad1.real < Z9.real

    # Creation of curve
    surf_list = list()
    if Nrad == 1 and Ntan == 2:
        if is_simplified:
            # Part 1 (0,0)

            line1 = Segment(Z12, Ztan1)
            line2 = Segment(Ztan1, Ztan2)
            point_ref = (Z12 + Ztan1 + Ztan2 + Z8 + Z9 + Z10 + Z11) / 7
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (0,1)

            line1 = Segment(Ztan1, Z2)
            point_ref = (Ztan1 + Z2 + Z3 + Z4 + Z5 + Z6 + Ztan2) / 7
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R0_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)

            line1 = Segment(Z12, Ztan1)
            line2 = Segment(Ztan1, Ztan2)
            line3 = Arc1(Ztan2, Z8, -abs(Z7))
            line4 = Arc1(Z8, Z9, -self.R2, is_trigo_direction=False)
            line5 = Segment(Z9, Z10)
            line6 = Arc1(Z10, Z11, -self.R1, is_trigo_direction=False)
            line7 = Segment(Z11, Z12)
            point_ref = (Z12 + Ztan1 + Ztan2 + Z8 + Z9 + Z10 + Z11) / 7
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6, line7],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (0,1)

            line1 = Segment(Ztan1, Z2)
            line2 = Segment(Z2, Z3)
            line3 = Arc1(Z3, Z4, -self.R1, is_trigo_direction=False)
            line4 = Segment(Z4, Z5)
            line5 = Arc1(Z5, Z6, -self.R2, is_trigo_direction=False)
            line6 = Arc1(Z6, Ztan2, -abs(Z7))
            point_ref = (Ztan1 + Z2 + Z3 + Z4 + Z5 + Z6 + Ztan2) / 7
            line7 = Segment(Ztan2, Ztan1)
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6, line7],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

    elif Nrad == 2 and Ntan == 1 and is_rad_splittable:
        if is_simplified:
            # Part 1 (0,0)
            line1 = Segment(Z12, Z2)
            line2 = Segment(Zrad1, Zrad2)
            point_ref = (Z12 + Z2 + Z3 + Z4 + Zrad2 + Zrad1 + Z10 + Z11) / 8
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)

            point_ref = (Zrad1 + Zrad2 + Z5 + Z6 + Z8 + Z9) / 6
            surface = SurfLine(
                line_list=[], label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:

            # Part 1 (0,0)

            line1 = Segment(Z12, Z2)
            line2 = Segment(Z2, Z3)
            line3 = Arc1(Z3, Z4, -self.R1, is_trigo_direction=False)
            line4 = Segment(Z4, Zrad2)
            line5 = Segment(Zrad2, Zrad1)
            line6 = Segment(Zrad1, Z10)
            line7 = Arc1(Z10, Z11, -self.R1, is_trigo_direction=False)
            line8 = Segment(Z11, Z12)
            point_ref = (Z12 + Z2 + Z3 + Z4 + Zrad2 + Zrad1 + Z10 + Z11) / 8
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6, line7, line8],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            line1 = Segment(Zrad1, Zrad2)
            line2 = Segment(Zrad2, Z5)
            line3 = Arc1(Z5, Z6, -self.R2, is_trigo_direction=False)
            line4 = Arc1(Z6, Z8, -abs(Z7), is_trigo_direction=False)
            line5 = Arc1(Z8, Z9, -self.R2, is_trigo_direction=False)
            line6 = Segment(Z9, Zrad1)
            point_ref = (Zrad1 + Zrad2 + Z5 + Z6 + Z8 + Z9) / 6
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    elif Nrad == 2 and Ntan == 2 and is_rad_splittable:
        if is_simplified:
            # Part 1 (0,0)

            line1 = Segment(Z12, Ztan1)
            line2 = Segment(Ztan1, Zmid)
            line3 = Segment(Zmid, Zrad1)
            line4 = Segment(Zrad1, Z10)
            line5 = Arc1(Z10, Z11, -self.R1, is_trigo_direction=False)
            line6 = Segment(Z11, Z12)
            point_ref = (Z12 + Ztan1 + Zmid + Zrad1 + Z10 + Z11) / 6
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)

            line2 = Segment(Zmid, Ztan2)
            line3 = Arc1(Ztan2, Z8, -abs(Z7), is_trigo_direction=False)
            line4 = Arc1(Z8, Z9, -self.R2, is_trigo_direction=False)
            line5 = Segment(Z9, Zrad1)
            point_ref = (Zrad1 + Zmid + Ztan2 + Z8 + Z9) / 5
            line1 = Segment(Zrad1, Zmid)
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part 3 (0,1)
            line1 = Segment(Ztan1, Z2)
            line2 = Segment(Z2, Z3)
            line3 = Arc1(Z3, Z4, -self.R1, is_trigo_direction=False)
            line4 = Segment(Z4, Zrad2)
            line5 = Segment(Zrad2, Zmid)
            line6 = Segment(Zmid, Ztan1)
            point_ref = (Ztan1 + Z2 + Z3 + Z4 + Zrad2 + Zmid) / 6
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part4 (1,1)
            line1 = Segment(Zmid, Zrad2)
            line2 = Segment(Zrad2, Z5)
            line3 = Arc1(Z5, Z6, -self.R2, is_trigo_direction=False)
            line4 = Arc1(Z6, Ztan2, -abs(Z7), is_trigo_direction=False)
            line5 = Segment(Ztan2, Zmid)

            point_ref = (Zmid + Zrad2 + Z5 + Z6 + Ztan2) / 5
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            line1 = Segment(Z12, Ztan1)
            line2 = Segment(Ztan1, Zmid)
            line3 = Segment(Zmid, Zrad1)
            line4 = Segment(Zrad1, Z10)
            line5 = Arc1(Z10, Z11, -self.R1, is_trigo_direction=False)
            line6 = Segment(Z11, Z12)
            point_ref = (Z12 + Ztan1 + Zmid + Zrad1 + Z10 + Z11) / 6
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)

            line2 = Segment(Zmid, Ztan2)
            line3 = Arc1(Ztan2, Z8, -abs(Z7), is_trigo_direction=False)
            line4 = Arc1(Z8, Z9, -self.R2, is_trigo_direction=False)
            line5 = Segment(Z9, Zrad1)
            point_ref = (Zrad1 + Zmid + Ztan2 + Z8 + Z9) / 5
            line1 = Segment(Zrad1, Zmid)
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part 3 (0,1)
            line1 = Segment(Ztan1, Z2)
            line2 = Segment(Z2, Z3)
            line3 = Arc1(Z3, Z4, -self.R1, is_trigo_direction=False)
            line4 = Segment(Z4, Zrad2)
            line5 = Segment(Zrad2, Zmid)
            line6 = Segment(Zmid, Ztan1)
            point_ref = (Ztan1 + Z2 + Z3 + Z4 + Zrad2 + Zmid) / 6
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part4 (1,1)
            line1 = Segment(Zmid, Zrad2)
            line2 = Segment(Zrad2, Z5)
            line3 = Arc1(Z5, Z6, -self.R2, is_trigo_direction=False)
            line4 = Arc1(Z6, Ztan2, -abs(Z7), is_trigo_direction=False)
            line5 = Segment(Ztan2, Zmid)

            point_ref = (Zmid + Zrad2 + Z5 + Z6 + Ztan2) / 5
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    else:  # Default : only one zone
        curve_list = self.build_geometry()
        # Remove the isthmus part
        curve_list = curve_list[1:-1]
        # Add a line to close the winding area
        lines = [Segment(curve_list[-1].end, curve_list[0].begin)]
        lines.extend(curve_list)
        surface = SurfLine(
            line_list=lines, label="Wind" + st + "_R0_T0_S0", point_ref=Zmid
        )
        surf_list.append(surface)
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
