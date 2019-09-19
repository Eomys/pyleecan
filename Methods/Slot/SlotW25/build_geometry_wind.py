# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW25.build_geometry_wind
SlotW25 build_geometry_wind method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import angle, exp, linspace, zeros

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object
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
    [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = self._comp_point_coordinate()
    X = linspace(Z3, Z4, Nrad + 1)

    # Nrad+1 and Ntan+1 because 3 points => 2 zones
    Z = zeros((Nrad + 1, Ntan + 1), dtype=complex)
    for ii in range(Nrad + 1):
        Z[ii][:] = abs(X[ii]) * exp(
            1j * linspace(angle(X[ii]), angle(X[ii].conjugate()), Ntan + 1)
        )

    if self.is_outwards():
        assert abs(Z3) < abs(Z4)
        assert abs(Z6) < abs(Z5)
    assert abs(Z[0][0] - Z3) < 1e-6
    assert abs(Z[Nrad][0] - Z4) < 1e-6
    assert abs(Z[0][Ntan] - Z6) < 1e-6
    assert abs(Z[Nrad][Ntan] - Z5) < 1e-6

    # We go thought the zone by Rad then Tan, starting by (0,0)
    surf_list = list()
    for jj in range(Ntan):  # jj from 0 to Ntan-1
        for ii in range(Nrad):  # ii from 0 to Nrad-1
            Z1 = Z[ii][jj]
            Z2 = Z[ii][jj + 1]
            Z3 = Z[ii + 1][jj + 1]
            Z4 = Z[ii + 1][jj]
            point_ref = (Z1 + Z2 + Z3 + Z4) / 4  # reference point of the surface
            # With one zone the order would be [Z7,Z4,Z5,Z6]
            if is_simplified:
                curve_list = list()
                if ii == 0:
                    curve_list.append(Arc1(Z1, Z2, abs(Z1), is_trigo_direction=True))
                if jj != Ntan - 1:
                    curve_list.append(Segment(Z2, Z3))
                if ii != Nrad - 1:
                    curve_list.append(Arc1(Z3, Z4, -abs(Z3), is_trigo_direction=False))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )
                surf_list.append(surface)
            else:
                curve_list = list()
                curve_list.append(Arc1(Z1, Z2, abs(Z1), is_trigo_direction=True))
                curve_list.append(Segment(Z2, Z3))
                curve_list.append(Arc1(Z3, Z4, -abs(Z3), is_trigo_direction=False))
                curve_list.append(Segment(Z4, Z1))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )
                surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
