# -*- coding: utf-8 -*-
"""@package

@date Created on Thu Mar 30 15:07:49 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from numpy import angle
from scipy.optimize import fsolve

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object
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

    [Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = self._comp_point_coordinate()

    Ztan1 = (Z3 + Z7) / 2.0
    Ztan2 = Z5
    Zmid = (Ztan1 + Ztan2) / 2.0

    R5 = Z5.real
    R6 = Z6.real
    R7 = Z7.real

    if abs(R5 - R6) < abs(R6 - R7):  # Zrad1 between Z6 and Z7
        x = fsolve(lambda x: angle((Z7 - (Zmid + 1j * x)) / (Z7 - Z6)), Z6.imag)
        Zrad1 = Zmid + 1j * x[0]
        Zrad2 = Zrad1.conjugate()
    elif abs(R5 - R6) > abs(R6 - R7):  # Zrad1 between Z6 and Z5
        x = fsolve(lambda x: angle((Z6 - (Zmid + 1j * x)) / (Z6 - Z5)), Z6.imag)
        Zrad1 = Zmid + 1j * x[0]
        Zrad2 = Zrad1.conjugate()
    else:
        Zrad1 = Z6
        Zrad2 = Z4

    surf_list = list()
    if Nrad == 1 and Ntan == 2:
        if is_simplified:
            # Part 1 (0,0)
            surf_list.append(
                gen_curve_list_simplified([Z7, Ztan1, Ztan2], "0", "0", st)
            )
            # Part 2 (0,1)
            surf_list.append(gen_curve_list_simplified([Ztan1, Z3], "0", "1", st))
        else:
            # Part 1 (0,0)
            surf_list.append(gen_curve_list([Z7, Ztan1, Ztan2, Z6], "0", "0", st))
            # Part 2 (0,1)
            surf_list.append(gen_curve_list([Ztan1, Z3, Z4, Ztan2], "0", "1", st))
    elif Nrad == 2 and Ntan == 1:
        if is_simplified:
            # Part 1 (0,0)
            if abs(R5 - R6) > abs(R6 - R7):  # Zrad1 between Z6 and Z5
                point_list = [Z7, Z3, Z4, Zrad2, Zrad1, Z6]
            else:
                point_list = [Z7, Z3, Zrad2, Zrad1]
            line1 = Segment(Z7, Z3)
            line2 = Segment(Zrad2, Zrad1)
            point_ref = 0
            for Z in point_list:
                point_ref += Z
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 2 (1,0)
            if abs(R5 - R6) < abs(R6 - R7):  # Zrad1 between Z6 and Z7
                point_list = [Zrad1, Zrad2, Z4, Z5, Z6]
            else:
                point_list = [Zrad1, Zrad2, Z5]
            point_ref = 0
            for Z in point_list:
                point_ref += Z

            point_ref = point_ref / len(point_list)  # point reference of the surface
            surface = SurfLine(
                line_list=[], label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:

            # Part 1 (0,0)
            if abs(R5 - R6) > abs(R6 - R7):  # Zrad1 between Z6 and Z5
                point_list = [Z7, Z3, Z4, Zrad2, Zrad1, Z6]
            else:
                point_list = [Z7, Z3, Zrad2, Zrad1]
            surf_list.append(gen_curve_list(point_list, "0", "0", st))
            # Part 2 (1,0)
            if abs(R5 - R6) < abs(R6 - R7):  # Zrad1 between Z6 and Z7
                point_list = [Zrad1, Zrad2, Z4, Z5, Z6]
            else:
                point_list = [Zrad1, Zrad2, Z5]

            surf_list.append(gen_curve_list(point_list, "1", "0", st))
    elif Nrad == 2 and Ntan == 2:
        if is_simplified:
            # Part 1 (0,0)
            point_list = [Z7, Ztan1, Zmid, Zrad1]
            surf_list.append(gen_curve_list_simplified(point_list, "0", "0", st))
            # Part 2 (1,0)
            point_list = [Zmid, Ztan2]
            surf_list.append(gen_curve_list_simplified(point_list, "1", "0", st))
            # Part 3 (0,1)
            if abs(R5 - R6) < abs(R6 - R7):  # Zrad1 between Z6 and Z7
                point_list = [Ztan1, Z3, Zrad2, Zmid]
            else:
                point_list = [Ztan1, Z3, Z4, Zrad2, Zmid]

            line1 = Segment(Ztan1, Z3)
            line2 = Segment(Zrad2, Zmid)
            point_ref = 0
            for Z in point_list:
                point_ref += Z

            point_ref = point_ref / len(point_list)  # point reference of the surface
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 4 (1,1)
            if abs(R5 - R6) > abs(R6 - R7):  # Zrad1 between Z6 and Z5
                point_list = [Zmid, Zrad2, Z5]
            else:
                point_list = [Zmid, Zrad2, Z4, Ztan2]

            point_ref = 0
            for Z in point_list:
                point_ref += Z

            point_ref = point_ref / len(point_list)  # point reference of the surface
            surface = SurfLine(
                line_list=[], label="Wind" + st + "_R1_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:

            # Part 1 (0,0)
            if abs(R5 - R6) < abs(R6 - R7):  # Zrad1 between Z6 and Z7
                point_list = [Z7, Ztan1, Zmid, Zrad1]
            else:
                point_list = [Z7, Ztan1, Zmid, Zrad1, Z6]
            surf_list.append(gen_curve_list(point_list, "0", "0", st))
            # Part 2 (1,0)
            if abs(R5 - R6) > abs(R6 - R7):  # Zrad1 between Z6 and Z5
                point_list = [Zrad1, Zmid, Ztan2]
            else:
                point_list = [Zrad1, Zmid, Ztan2, Z6]

            surf_list.append(gen_curve_list(point_list, "1", "0", st))
            # Part 3 (0,1)
            if abs(R5 - R6) < abs(R6 - R7):  # Zrad1 between Z6 and Z7
                point_list = [Ztan1, Z3, Zrad2, Zmid]
            else:
                point_list = [Ztan1, Z3, Z4, Zrad2, Zmid]
            surf_list.append(gen_curve_list(point_list, "0", "1", st))
            # Part 4 (1,1)
            if abs(R5 - R6) > abs(R6 - R7):  # Zrad1 between Z6 and Z5
                point_list = [Zmid, Zrad2, Z5]
            else:
                point_list = [Zmid, Zrad2, Z4, Ztan2]

            surf_list.append(gen_curve_list(point_list, "1", "1", st))
    else:
        surf_list.append(gen_curve_list([Z7, Z3, Z4, Z5, Z6], "0", "0", st))

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list


def gen_curve_list(point_list, RX, TX, st):
    """

    Parameters
    ----------
    point_list :

    RX :

    TX :

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
        label="Wind" + st + "_R" + RX + "_T" + TX + "_S0",
        point_ref=point_ref,
    )
    return surface


def gen_curve_list_simplified(point_list, RX, TX, st):
    """

    Parameters
    ----------
    point_list :

    RX :

    TX :

    st :


    Returns
    -------

    """
    curve_list = list()
    for ii in range(len(point_list) - 1):
        curve_list.append(Segment(point_list[ii], point_list[ii + 1]))
    res = 0
    for Z in point_list:
        res += Z
    point_ref = res / len(point_list)
    surface = SurfLine(
        line_list=curve_list,
        label="Wind" + st + "_R" + RX + "_T" + TX + "_S0",
        point_ref=point_ref,
    )
    return surface
