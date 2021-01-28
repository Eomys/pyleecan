# -*- coding: utf-8 -*-

from numpy import angle, exp, linspace, zeros

from ....Classes.Arc2 import Arc2
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def build_geometry_active(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object
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

    # get the name of the lamination
    st = self.get_name_lam()

    [Z8, Z7, Z6, Z5, Z4, Z3, Z2, Z1] = self._comp_point_coordinate()
    X = linspace(Z6, Z5, Nrad + 1)

    # Nrad+1 and Ntan+1 because 3 points => 2 zones
    Z = zeros((Nrad + 1, Ntan + 1), dtype=complex)
    for ii in range(Nrad + 1):
        Z[ii][:] = linspace(X[ii], X[ii].conjugate(), Ntan + 1)

    # The bottom and top are Arc and not a line
    Z[0][:] = abs(Z6) * exp(1j * linspace(angle(Z6), angle(Z3), Ntan + 1))
    Z[Nrad][:] = abs(Z5) * exp(1j * linspace(angle(Z5), angle(Z4), Ntan + 1))

    assert abs(Z[0][0] - Z6) < 1e-6
    assert abs(Z[Nrad][0] - Z5) < 1e-6
    assert abs(Z[0][Ntan] - Z3) < 1e-6
    assert abs(Z[Nrad][Ntan] - Z4) < 1e-6

    Zc = 0  # Center of the machine

    # We go thought the zone by Rad then Tan, starting by (0,0)
    surf_list = list()
    for jj in range(Ntan):  # jj from 0 to Ntan-1
        for ii in range(Nrad):  # ii from 0 to Nrad-1
            Z1 = Z[ii][jj]
            Z2 = Z[ii][jj + 1]
            Z3 = Z[ii + 1][jj + 1]
            Z4 = Z[ii + 1][jj]
            point_ref = (Z1 + Z2 + Z3 + Z4) / 4
            # With one zone the order would be [Z6,Z3,Z4,Z5]
            if is_simplified:  # No doubling Line allowed
                curve_list = list()
                if ii == 0:
                    curve_list.append(Segment(Z1, Z2))
                if jj != Ntan - 1:
                    curve_list.append(Segment(Z2, Z3))
                if ii != Nrad - 1:
                    curve_list.append(Segment(Z3, Z4))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind_" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )
                surf_list.append(surface)
            else:
                curve_list = list()
                curve_list.append(Segment(Z1, Z2))
                curve_list.append(Segment(Z2, Z3))
                if ii == Nrad - 1:  # Top zone
                    curve_list.append(Arc2(Z3, Zc, angle(Z4) - angle(Z3)))
                else:
                    curve_list.append(Segment(Z3, Z4))
                curve_list.append(Segment(Z4, Z1))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind_" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )
                surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
