from numpy import zeros, linspace

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import WIND_LAB, DRAW_PROP_LAB


def build_geometry_active(self, Nrad, Ntan, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object
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
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]

    X = linspace(Z5, Z6, Nrad + 1)

    # Nrad+1 and Ntan+1 because 3 points => 2 zones
    Z = zeros((Nrad + 1, Ntan + 1), dtype=complex)
    for ii in range(Nrad + 1):
        Z[ii][:] = linspace(X[ii], X[ii].conjugate(), Ntan + 1)

    assert Z[0][0] == Z5
    assert Z[Nrad][0] == Z6
    assert Z[0][Ntan] == Z8
    assert Z[Nrad][Ntan] == Z7
    Z_8 = Z5 + (self.W2 / 2) + (self.W1 / 2)
    Z_5 = Z5 + (self.W2 / 2) - (self.W1 / 2)
    # We go thought the zone by Rad then Tan, starting by (0,0)
    surf_list = list()
    for jj in range(Ntan):  # jj from 0 to Ntan-1
        for ii in range(Nrad):  # ii from 0 to Nrad-1
            Z1 = Z[ii][jj]
            Z2 = Z[ii][jj + 1]
            Z3 = Z[ii + 1][jj + 1]
            Z4 = Z[ii + 1][jj]
            point_ref = (Z1 + Z2 + Z3 + Z4) / 4
            # With one zone the order would be [Z7,Z4,Z5,Z6]
            curve_list = list()
            curve_list.append(Segment(Z1, Z2))
            curve_list.append(
                Segment(
                    Z2,
                    Z3,
                    prop_dict={DRAW_PROP_LAB: False},
                )
            )
            curve_list.append(
                Segment(
                    Z3,
                    Z4,
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

    # Correct bottom line for particular case (cf Tests\Validation\Magnetics\test_FEMM_fast_draw.py)
    if (
        Ntan == 2
        and Nrad == 1
        and (
            (self.W1 != self.W2 and self.H1 != 0)
            or (self.H1 == 0 and self.W0 != self.W2)
        )
    ):
        if self.H1 > 0:  # Cut on W1
            ZOm = point_dict["Z4"]
            ZOp = point_dict["Z9"]
        else:  # Cut on W0
            ZOm = point_dict["Z2"]
            ZOp = point_dict["Z11"]
        # Cut Ox- surface
        arc_to_cut = surf_list[0].line_list[0]
        arc1, arc2 = arc_to_cut.split_line(Z1=0, Z2=ZOm)
        surf_list[0].line_list = [arc1[0], arc2[0]] + surf_list[0].line_list[1:]
        surf_list[0].line_list[1].prop_dict = {DRAW_PROP_LAB: False}
        # Cut Ox+ surface
        arc_to_cut = surf_list[1].line_list[0]
        arc1, arc2 = arc_to_cut.split_line(Z1=0, Z2=ZOp)
        surf_list[1].line_list = [arc1[0], arc2[0]] + surf_list[1].line_list[1:]
        surf_list[1].line_list[0].prop_dict = {DRAW_PROP_LAB: False}

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
