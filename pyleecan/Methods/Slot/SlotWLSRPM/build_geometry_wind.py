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

    Zcl = Rbo
    Zch = Rbo + self.H2
    Zmid = (Zcl + Zch) / 2.0

    # Creation of curve
    surf_list = list()
    if Nrad == 1 and Ntan == 2:
        # Part 1 (0,0)
        line1 = Segment(Zch, Z5)
        line2 = Segment(Z5, Z6)
        line3 = Arc1(Z6, Z7, self.R1, is_trigo_direction=True)
        line4 = Segment(Z7, Z8)
        line5 = Arc1(Z8, Zcl, -Rbo, is_trigo_direction=False)
        line6 = Segment(Zcl, Zch)
        point_ref = (Zch + Z5 + Z6 + Z7 + Z8 + Zcl) / 6
        surface = SurfLine(
            line_list=[line1, line2, line3, line4, line5, line6],
            # label="Wind" + st + "_R0_T0_S0",
            label="Wind" + st + "_R0_T1_S0",
            point_ref=point_ref,
        )
        surf_list.append(surface)

        # Part2 (0,1)

        line1 = Segment(Z3, Z4)
        line2 = Segment(Z4, Zch)
        line3 = Segment(Zch, Zcl)
        line4 = Arc1(Zcl, Z1, -Rbo, is_trigo_direction=False)
        line5 = Segment(Z1, Z2)
        line6 = Arc1(Z2, Z3, self.R1, is_trigo_direction=True)
        point_ref = (Z3 + Z4 + Zch + Zcl + Z1 + Z2) / 6

        surface = SurfLine(
            line_list=[line1, line2, line3, line4, line5, line6],
            # label="Wind" + st + "_R0_T1_S0",
            label="Wind" + st + "_R0_T0_S0",
            point_ref=point_ref,
        )
        surf_list.append(surface)
    else:  # Default : only one zone
        curve_list = self.build_geometry()

        # Add a line to close the winding area
        lines = [
            Arc1(
                curve_list[-1].end,
                curve_list[0].begin,
                -Rbo,
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
