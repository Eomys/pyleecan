from numpy import angle, exp, linspace, zeros

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import WIND_LAB, DRAW_PROP_LAB


def build_geometry_active(self, Nrad, Ntan, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        List of surface delimiting the winding zone

    """

    # get the name of the lamination
    lam_label = self.parent.get_label()

    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]

    X = linspace(Z1, Z2, Nrad + 1)

    # Nrad+1 and Ntan+1 because 3 points => 2 zones
    Z = zeros((Nrad + 1, Ntan + 1), dtype=complex)
    for ii in range(Nrad + 1):
        Z[ii][:] = abs(X[ii]) * exp(
            1j * linspace(angle(X[ii]), angle(X[ii].conjugate()), Ntan + 1)
        )

    assert abs(Z[0][0] - Z1) < 1e-6
    assert abs(Z[Nrad][0] - Z2) < 1e-6
    assert abs(Z[0][Ntan] - Z4) < 1e-6
    assert abs(Z[Nrad][Ntan] - Z3) < 1e-6

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
            curve_list = list()
            curve_list.append(Arc1(Z1, Z2, abs(Z1), is_trigo_direction=True))
            curve_list.append(
                Segment(
                    Z2,
                    Z3,
                    prop_dict={DRAW_PROP_LAB: False},
                )
            )
            curve_list.append(
                Arc1(
                    Z3,
                    Z4,
                    -abs(Z3),
                    is_trigo_direction=False,
                    prop_dict={DRAW_PROP_LAB: False},
                )
            )
            curve_list.append(
                Segment(
                    Z4,
                    Z1,
                    prop_dict={DRAW_PROP_LAB: jj != 0},
                )
            )
            surface = SurfLine(
                line_list=curve_list,
                label=lam_label
                + "_"
                + WIND_LAB
                + "_R"
                + str(ii)
                + "-T"
                + str(jj)
                + "-S0",
                point_ref=point_ref,
            )
            surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
