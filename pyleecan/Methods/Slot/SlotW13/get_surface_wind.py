# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_wind(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW13
        A SlotW13 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """
    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"
    [Z10, Z9, Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = self._comp_point_coordinate()

    X = linspace(Z7, Z6, Nrad + 1)

    # Nrad+1 and Ntan+1 because 3 points => 2 zones
    Z = zeros((Nrad + 1, Ntan + 1), dtype=complex)
    for ii in range(Nrad + 1):
        Z[ii][:] = linspace(X[ii], X[ii].conjugate(), Ntan + 1)

    assert Z[0][0] == Z7
    assert Z[Nrad][0] == Z6
    assert Z[0][Ntan] == Z4
    assert Z[Nrad][Ntan] == Z5

    # We go thought the surface by Rad then Tan, starting by (0,0)
    surf_list = list()
    for jj in range(Ntan):  # jj from 0 to Ntan-1
        for ii in range(Nrad):  # ii from 0 to Nrad-1
            point_ref = (
                Z[ii][jj] + Z[ii][jj + 1] + Z[ii + 1][jj + 1] + Z[ii + 1][jj]
            ) / 4  # tre reference point of the surface
            # With one zone the order would be [Z7,Z4,Z5,Z6]
            if is_simplified:  # No doubling Line allowed
                curve_list = list()
                if ii == 0:
                    curve_list.append(Segment(Z[ii][jj], Z[ii][jj + 1]))
                if jj != Ntan - 1:
                    curve_list.append(Segment(Z[ii][jj + 1], Z[ii + 1][jj + 1]))
                if ii != Nrad - 1:
                    curve_list.append(Segment(Z[ii + 1][jj + 1], Z[ii + 1][jj]))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )  # surface in the winding area
                surf_list.append(surface)
            else:
                curve_list = list()
                curve_list.append(Segment(Z[ii][jj], Z[ii][jj + 1]))
                curve_list.append(Segment(Z[ii][jj + 1], Z[ii + 1][jj + 1]))
                curve_list.append(Segment(Z[ii + 1][jj + 1], Z[ii + 1][jj]))
                curve_list.append(Segment(Z[ii + 1][jj], Z[ii][jj]))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )  # surface in the winding area
                surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)  # rotation of each surface
        surf.translate(delta)  # translation of each surface

    return surf_list
