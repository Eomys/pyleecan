# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW12.build_geometry_wind
SlotW12 build_geometry_wind method
@date Created on Tue Mar 07 14:54:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import arcsin, exp

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW12
        A SlotW12 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        List of surface delimiting the winding zone

    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"
    Rbo = self.get_Rbo()

    # angle is the angle to rotate Z0 so ||Z1,Z8|| = 2*R2
    angle = float(arcsin(self.R2 / Rbo))

    # comp point coordinate (in complex)
    Z1 = Rbo * exp(1j * angle)

    if self.is_outwards():
        Z3 = Z1 + self.H0 + self.R1 * 2
        Z4 = Z3 + self.H1
        Zrad1 = Z3.conjugate() + (self.H1 + self.R2) / 2.0
        Ztan2 = Z4.real + self.R2
        rot_sign = False
    else:  # inward slot
        Z3 = Z1 - self.H0 - self.R1 * 2
        Z4 = Z3 - self.H1
        Zrad1 = Z3.conjugate() - (self.H1 + self.R2) / 2.0
        Ztan2 = Z4.real - self.R2
        rot_sign = True

    # symetry
    Z5 = Z4.conjugate()
    Z6 = Z3.conjugate()
    Zrad2 = Zrad1.conjugate()
    Ztan1 = Z3.real
    Zmid = (Ztan1 + Ztan2) / 2.0

    surf_list = list()
    if (Nrad == 2 and Ntan == 1) and self.H1 > self.R2:
        if is_simplified:  # no coincident lines allowed
            # Part 1 (0,0)
            line1 = Segment(Z6, Z3)
            line2 = Segment(Zrad2, Zrad1)
            point_ref = (Z6 + Z3 + Zrad2 + Zrad1) / 4
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (1,0)
            point_ref = (Z6 + Z3 + Zrad2 + Zrad1) / 4
            surface = SurfLine(
                line_list=[], label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)
            line1 = Segment(Z6, Z3)
            line2 = Segment(Z3, Zrad2)
            line3 = Segment(Zrad2, Zrad1)
            line4 = Segment(Zrad1, Z6)
            point_ref = (Z6 + Z3 + Zrad2 + Zrad1) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

            # Part2 (1,0)
            line1 = Segment(Zrad1, Zrad2)
            line2 = Segment(Zrad2, Z4)
            line3 = Arc3(Z4, Z5, rot_sign)
            line4 = Segment(Z5, Zrad1)
            point_ref = (Z4 + Z5 + Zrad2 + Zrad1) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    elif Nrad == 1 and Ntan == 2:
        if is_simplified:  # no coincident lines allowed
            # Part 1 (0,0)
            line1 = Segment(Z6, Ztan1)
            point_ref = (Z6 + Ztan1 + Ztan2 + Z5) / 4
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R0_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)
            # Part2 (0,1)

            line1 = Segment(Ztan1, Z3)
            point_ref = (Ztan1 + Z3 + Z4 + Ztan2) / 4
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R0_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)

            line1 = Segment(Z6, Ztan1)
            line2 = Segment(Ztan1, Ztan2)
            line3 = Arc1(Ztan2, Z5, self.R2)
            line4 = Segment(Z5, Z6)
            point_ref = (Z6 + Ztan1 + Ztan2 + Z5) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (0,1)

            line1 = Segment(Ztan1, Z3)
            line2 = Segment(Z3, Z4)
            line3 = Arc1(Z4, Ztan2, self.R2)
            line4 = Segment(Ztan2, Ztan1)
            point_ref = (Ztan1 + Z3 + Z4 + Ztan2) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    elif Nrad == 2 and Ntan == 2 and self.H1 > self.R2:
        if is_simplified:  # no coincident lines allowed
            # Part 1 (0,0)
            line1 = Segment(Z6, Ztan1)
            line2 = Segment(Ztan1, Zmid)
            line3 = Segment(Zmid, Zrad1)
            point_ref = (Z6 + Ztan1 + Zmid + Zrad1) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)

            line1 = Segment(Zmid, Ztan2)
            point_ref = (Zrad1 + Zmid + Ztan2 + Z5) / 4
            surface = SurfLine(
                line_list=[line1], label="Wind" + st + "_R1_T0_S0", point_ref=point_ref
            )
            surf_list.append(surface)
            # Part 3 (0,1)

            line1 = Segment(Ztan1, Z3)
            line2 = Segment(Zrad2, Zmid)
            point_ref = (Ztan1 + Z3 + Zrad2 + Zmid) / 4
            surface = SurfLine(
                line_list=[line1, line2],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part4 (1,1)
            point_ref = (Zmid + Zrad2 + Z4 + Ztan2) / 4
            surface = SurfLine(
                line_list=[], label="Wind" + st + "_R1_T1_S0", point_ref=point_ref
            )
            surf_list.append(surface)
        else:
            # Part 1 (0,0)

            line1 = Segment(Z6, Ztan1)
            line2 = Segment(Ztan1, Zmid)
            line3 = Segment(Zmid, Zrad1)
            line4 = Segment(Zrad1, Z6)
            point_ref = (Z6 + Ztan1 + Zmid + Zrad1) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R0_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part2 (1,0)

            line1 = Segment(Zrad1, Zmid)
            line2 = Segment(Zmid, Ztan2)
            line3 = Arc1(Ztan2, Z5, self.R2)
            line4 = Segment(Z5, Zrad1)
            point_ref = (Zrad1 + Zmid + Ztan2 + Z5) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R1_T0_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part 3 (0,1)

            line1 = Segment(Ztan1, Z3)
            line2 = Segment(Z3, Zrad2)
            line3 = Segment(Zrad2, Zmid)
            line4 = Segment(Zmid, Ztan1)
            point_ref = (Ztan1 + Z3 + Zrad2 + Zmid) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R0_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
            # Part4 (1,1)

            line1 = Segment(Zmid, Zrad2)
            line2 = Segment(Zrad2, Z4)
            line3 = Arc1(Z4, Ztan2, self.R2)
            line4 = Segment(Ztan2, Zmid)
            point_ref = (Zmid + Zrad2 + Z4 + Ztan2) / 4
            surface = SurfLine(
                line_list=[line1, line2, line3, line4],
                label="Wind" + st + "_R1_T1_S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)
    else:  # Default only one zone
        # Creation of curve
        line_list = list()
        line_list.append(Segment(Z6, Z3))
        if self.H1 > 0:
            line_list.append(Segment(Z3, Z4))
        line_list.append(Arc3(Z4, Z5, rot_sign))
        if self.H1 > 0:
            line_list.append(Segment(Z5, Z6))

        surface = SurfLine(
            line_list=line_list, label="Wind" + st + "_R0_T0_S0", point_ref=Zmid
        )
        surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
