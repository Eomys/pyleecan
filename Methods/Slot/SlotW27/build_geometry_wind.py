# -*- coding: utf-8 -*-

from numpy import angle
from scipy.optimize import fsolve

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW27
        A SlotW27 object
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
    surf_list: list
        List of surface delimiting the winding zone

    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"
    # getting points coordinate
    [Z1, Z3, Z4, Z5, Z6, Z7, Z8] = self._comp_point_coordinate()
    Ztan1 = (Z3 + Z8) / 2.0
    Ztan2 = (Z5 + Z6) / 2.0
    Zmid = (Ztan1 + Ztan2) / 2.0

    if self.is_trap_wind:
        Zrad1 = Z7
        Zrad2 = Z4
        Zmid = (Z7 + Z4) / 2.0
    elif self.H1 < self.H2:  # Zrad1 between Z6 and Z7
        x = fsolve(
            lambda x: angle((Z7 - (Zmid + 1j * x)) / (Z7 - Z6)),
            -(self.W2 + self.W3) / 4.0,
        )
        Zrad1 = Zmid + 1j * x[0]
        Zrad2 = Zrad1.conjugate()
    elif self.H1 > self.H2:  # Zrad1 between Z8 and Z7
        x = fsolve(
            lambda x: angle((Z7 - (Zmid + 1j * x)) / (Z7 - Z8)),
            -(self.W2 + self.W1) / 4.0,
        )
        Zrad1 = Zmid + 1j * x[0]
        Zrad2 = Zrad1.conjugate()
    else:
        Zrad1 = Z7
        Zrad2 = Z4
    Z_3 = Ztan1 - (self.W0 * 1j / 2)
    Z_8 = Ztan1 + (self.W0 * 1j / 2)
    surf_list = list()
    if Nrad == 1 and Ntan == 2:
        if is_simplified:
            # Part 1 (0,0)
            point_list = [Z8, Ztan1, Ztan2, Z6, Z7]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            curve_list.append(Segment(Z_8, Ztan1))
            curve_list.append(Segment(Ztan1, Ztan2))
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 2 (0,1)
            point_list = [Ztan1, Z3, Z4, Z5, Ztan2]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            curve_list.append(Segment(Ztan1, Z_3))
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            surf_list.append(gen_curve_list([Z8, Ztan1, Ztan2, Z6, Z7], "0", "0", st))
            # Part 2 (0,1)
            surf_list.append(gen_curve_list([Ztan1, Z3, Z4, Z5, Ztan2], "0", "1", st))
    elif Nrad == 2 and Ntan == 1:
        if is_simplified:
            # Part 1 (0,0)
            if not self.is_trap_wind and self.H2 > self.H1:
                point_list = [Z8, Z3, Z4, Zrad2, Zrad1, Z7]
            else:  # H2 == H1
                point_list = [Z8, Z3, Zrad2, Zrad1]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            curve_list.append(Segment(Z_8, Z_3))
            curve_list.append(Segment(Zrad2, Zrad1))
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 2 (1,0)
            if not self.is_trap_wind and self.H1 > self.H2:
                point_list = [Zrad1, Zrad2, Z4, Z5, Z6, Z7]
            else:
                point_list = [Zrad1, Zrad2, Z5, Z6]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            if not self.is_trap_wind and self.H2 > self.H1:
                point_list = [Z8, Z3, Z4, Zrad2, Zrad1, Z7]
            else:  # H2 == H1
                point_list = [Z8, Z3, Zrad2, Zrad1]
            surf_list.append(gen_curve_list(point_list, "0", "0", st))
            # Part 2 (1,0)
            if not self.is_trap_wind and self.H1 > self.H2:
                point_list = [Zrad1, Zrad2, Z4, Z5, Z6, Z7]
            else:
                point_list = [Zrad1, Zrad2, Z5, Z6]
            surf_list.append(gen_curve_list(point_list, "1", "0", st))

    elif Nrad == 2 and Ntan == 2:
        if is_simplified:
            # Part 1 (0,0)
            if not self.is_trap_wind and self.H2 > self.H1:
                point_list = [Z8, Ztan1, Zmid, Zrad1, Z7]
            else:  # H2 == H1
                point_list = [Z8, Ztan1, Zmid, Zrad1]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            curve_list.append(Segment(Z_8, Ztan1))
            curve_list.append(Segment(Ztan1, Zmid))
            curve_list.append(Segment(Ztan1, Zrad1))
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 2 (1,0)
            if not self.is_trap_wind and self.H1 > self.H2:
                point_list = [Zrad1, Zmid, Ztan2, Z6, Z7]
            else:
                point_list = [Zrad1, Zmid, Ztan2, Z6]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            curve_list.append(Segment(Zmid, Ztan2))
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 3 (0,1)
            if not self.is_trap_wind and self.H2 > self.H1:
                point_list = [Ztan1, Z3, Z4, Zrad2, Zmid]
            else:  # H2 == H1
                point_list = [Ztan1, Z3, Zrad2, Zmid]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            curve_list.append(Segment(Ztan1, Z_3))
            curve_list.append(Segment(Zrad2, Zmid))
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 4 (1,1)
            if not self.is_trap_wind and self.H1 > self.H2:
                point_list = [Zmid, Zrad2, Z4, Z5, Ztan2]
            else:  # H2 == H1
                point_list = [Zmid, Zrad2, Z5, Ztan2]
            res = 0
            for Z in point_list:
                res += Z
            point_ref = res / len(point_list)
            curve_list = list()
            surface = SurfLine(
                line_list=curve_list,
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
        else:

            # Part 1 (0,0)
            if not self.is_trap_wind and self.H2 > self.H1:
                point_list = [Z8, Ztan1, Zmid, Zrad1, Z7]
            else:  # H2 == H1
                point_list = [Z8, Ztan1, Zmid, Zrad1]
            surf_list.append(gen_curve_list(point_list, "0", "0", st))
            # Part 2 (1,0)
            if not self.is_trap_wind and self.H1 > self.H2:
                point_list = [Zrad1, Zmid, Ztan2, Z6, Z7]
            else:
                point_list = [Zrad1, Zmid, Ztan2, Z6]
            surf_list.append(gen_curve_list(point_list, "1", "0", st))
            # Part 3 (0,1)
            if not self.is_trap_wind and self.H2 > self.H1:
                point_list = [Ztan1, Z3, Z4, Zrad2, Zmid]
            else:  # H2 == H1
                point_list = [Ztan1, Z3, Zrad2, Zmid]
            surf_list.append(gen_curve_list(point_list, "0", "1", st))
            # Part 4 (1,1)
            if not self.is_trap_wind and self.H1 > self.H2:
                point_list = [Zmid, Zrad2, Z4, Z5, Ztan2]
            else:  # H2 == H1
                point_list = [Zmid, Zrad2, Z5, Ztan2]
            surf_list.append(gen_curve_list(point_list, "1", "1", st))
    else:
        surf_list.append(gen_curve_list([Z8, Z3, Z4, Z5, Z6, Z7], "0", "0", st))

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list


def gen_curve_list(point_list, RX, TY, st):
    """

    Parameters
    ----------
    point_list :

    RX :

    TY :

    st :


    Returns
    -------

    """
    curve_list = list()
    for ii in range(len(point_list) - 1):
        curve_list.append(Segment(point_list[ii], point_list[ii + 1]))
    curve_list.append(Segment(point_list[-1], point_list[0]))

    res = 0
    for Z in point_list:
        res += Z
    point_ref = res / len(point_list)
    surface = SurfLine(
        line_list=curve_list,
        label="Wind" + st + "_R" + RX + "_T" + TY + "_S0",
        point_ref=point_ref,
    )
    return surface
