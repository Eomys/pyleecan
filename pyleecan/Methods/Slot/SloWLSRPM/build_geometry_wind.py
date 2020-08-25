# -*- coding: utf-8 -*-

from numpy import angle
from scipy.optimize import fsolve

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object
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
    Rbo = self.get_Rbo()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()

    Ztan1 = Rbo - self.H0
    Ztan2 = Rbo - self.H0 - self.H2
    Zmid = (Ztan1 + Ztan2) / 2.0

    # Zrad1 between Z10 and Z9
    x = fsolve(lambda x: angle((Z5 - (Zmid + 1j * x)) / (Z5 - Z4)), -self.R1)
    Zrad1 = Zmid + 1j * x[0]
    Zrad2 = Zrad1.conjugate()

    # We can split in rad only if Zrad1 is between Z10 and Z9
    is_rad_splittable = Z5.real < Zrad1.real and Zrad1.real < Z4.real

    # Creation of curve
    surf_list = list()
    if Nrad == 1 and Ntan == 2:
        if is_simplified:
            # Part 1 (0,0)
            line1 = Arc1(Z6, Ztan2, -Rbo + self.H0 + self.H2, is_trigo_direction=True)
            line2 = Segment(Ztan2, Ztan1)
            point_ref = (Ztan1 + Z8 + Z7 + Z6 + Ztan2) / 5
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (0,1)
            line1 = Arc1(Ztan2, Z5, -Rbo + self.H0 + self.H2, is_trigo_direction=True)
            point_ref = (Z3 + Ztan1 + Ztan2 + Z5 + Z4) / 5

            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R0_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:

            # Part 1 (0,0)
            line1 = Arc1(Ztan1, Z8, Rbo - self.H0, is_trigo_direction=True)
            line2 = Arc1(Z8, Z7, self.R1, is_trigo_direction=True)
            line3 = Segment(Z7, Z6)
            line4 = Arc1(Z6, Ztan2, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            line5 = Segment(Ztan2, Ztan1)
            point_ref = (Ztan1 + Z8 + Z7 + Z6 + Ztan2) / 5
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (0,1)

            line1 = Arc1(Z3, Ztan1, Rbo - self.H0, is_trigo_direction=True)
            line2 = Segment(Ztan1, Ztan2)
            line3 = Arc1(Ztan2, Z5, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            line4 = Segment(Z5, Z4)
            line5 = Arc1(Z4, Z3, self.R1, is_trigo_direction=True)
            point_ref = (Z3 + Ztan1 + Ztan2 + Z5 + Z4) / 5

            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    elif Nrad == 2 and Ntan == 1 and is_rad_splittable:
        if is_simplified:
            # Part 1 (0,0)
            line1 = Segment(Zrad2, Zrad1)

            point_ref = (Z3 + Z8 + Z7 + Zrad2 + Zrad1 + Z4) / 6
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R0_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)

            # Part2 (1,0)
            line1 = Arc1(Z6, Z5, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            point_ref = (Zrad1 + Zrad2 + Z6 + Z5) / 4
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            line1 = Arc1(Z3, Z8, Rbo - self.H0, is_trigo_direction=True)
            line2 = Arc1(Z8, Z7, self.R1, is_trigo_direction=True)
            line3 = Segment(Z7, Zrad2)
            line4 = Segment(Zrad2, Zrad1)
            line5 = Segment(Zrad1, Z4)
            line6 = Arc1(Z4, Z3, self.R1, is_trigo_direction=True)
            point_ref = (Z3 + Z8 + Z7 + Zrad2 + Zrad1 + Z4) / 6
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5, line6],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (1,0)
            line1 = Segment(Zrad2, Z6)
            line2 = Arc1(Z6, Z5, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            line3 = Segment(Z5, Zrad1)
            line4 = Segment(Zrad1, Zrad2)
            point_ref = (Zrad1 + Zrad2 + Z6 + Z5) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    elif Nrad == 2 and Ntan == 2 and is_rad_splittable:
        if is_simplified:
            # Part 1 (0,0)
            line1 = Segment(Zrad2, Zmid)
            line2 = Segment(Zmid, Ztan1)
            point_ref = (Ztan1 + Z8 + Z7 + Zrad2 + Zmid) / 5
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            line1 = Arc1(Z6, Ztan2, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            line2 = Segment(Ztan2, Zmid)
            point_ref = (Zmid + Zrad2 + Z6 + Zmid) / 4
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 3 (0,1)
            line1 = Segment(Zmid, Zrad1)
            point_ref = (Z3 + Ztan1 + Zmid + Zrad1 + Z4) / 5
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R0_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)

            # Part4 (1,1)
            line1 = Arc1(Ztan2, Z5, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            point_ref = (Zrad1 + Zmid + Ztan2 + Z5) / 4
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R1_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            line1 = Arc1(Ztan1, Z8, Rbo - self.H0, is_trigo_direction=True)
            line2 = Arc1(Z8, Z7, self.R1, is_trigo_direction=True)
            line3 = Segment(Z7, Zrad2)
            line4 = Segment(Zrad2, Zmid)
            line5 = Segment(Zmid, Ztan1)
            point_ref = (Ztan1 + Z8 + Z7 + Zrad2 + Zmid) / 5
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)
            line1 = Segment(Zmid, Zrad2)
            line2 = Segment(Zrad2, Z6)
            line3 = Arc1(Z6, Ztan2, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            line4 = Segment(Ztan2, Zmid)
            point_ref = (Zmid + Zrad2 + Z6 + Zmid) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 3 (0,1)
            line1 = Arc1(Z3, Ztan1, Rbo - self.H0, is_trigo_direction=True)
            line2 = Segment(Ztan1, Zmid)
            line3 = Segment(Zmid, Zrad1)
            line4 = Segment(Zrad1, Z4)
            line5 = Arc1(Z4, Z3, self.R1, is_trigo_direction=True)
            point_ref = (Z3 + Ztan1 + Zmid + Zrad1 + Z4) / 5
            surface = SurfLine(
                line_list=[line1, line2, line3, line4, line5],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part4 (1,1)
            line1 = Segment(Zrad1, Zmid)
            line2 = Segment(Zmid, Ztan2)
            line3 = Arc1(Ztan2, Z5, -Rbo + self.H0 + self.H2, is_trigo_direction=False)
            line4 = Segment(Z5, Zrad1)
            point_ref = (Zrad1 + Zmid + Ztan2 + Z5) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    else:  # Default : only one zone
        curve_list = self.build_geometry()

        # Remove the isthmus part
        curve_list = curve_list[1:-1]
        # Add a line to close the winding area
        lines = [
            Arc1(
                curve_list[-1].end,
                curve_list[0].begin,
                -Rbo + self.H0,
                is_trigo_direction=False,
            )
        ]
        lines.extend(curve_list)
        surface = SurfLine(
            line_list=lines, label="Wind" + st + "_R0_T0_S0", point_ref=Zmid
        )
        surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
