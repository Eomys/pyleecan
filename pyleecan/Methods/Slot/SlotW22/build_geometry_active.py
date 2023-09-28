# -*- coding: utf-8 -*-

from numpy import exp, linspace, meshgrid

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import WIND_LAB, DRAW_PROP_LAB


def build_geometry_active(self, Nrad, Ntan, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object
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
    surf_list:
        List of surface delimiting the winding zone

    """

    # get the name of the lamination
    lam_label = self.parent.get_label()

    Rbo = self.get_Rbo()

    # Polar Meshgrid
    if self.is_outwards():
        r = linspace(Rbo + self.H0, Rbo + self.H0 + self.H2, Nrad + 1)
    else:
        r = linspace(Rbo - self.H0, Rbo - self.H0 - self.H2, Nrad + 1)

    theta = linspace(-self.W2 / 2.0, self.W2 / 2.0, Ntan + 1)
    Z = meshgrid(r, theta)

    Z = Z[0] * exp(1j * Z[1])
    Z = Z.T
    # if self.is_outwards():
    #     assert Z[0][0] == (Rbo + self.H0) * exp(-1j * self.W2 * 0.5)  # Z6
    #     assert Z[Nrad][0] == (Rbo + self.H0 + self.H2) * exp(-1j * self.W2 * 0.5)  # Z5
    #     assert Z[0][Ntan] == (Rbo + self.H0) * exp(1j * self.W2 * 0.5)  # Z3
    #     assert Z[Nrad][Ntan] == (Rbo + self.H0 + self.H2) * exp(
    #         1j * self.W2 * 0.5
    #     )  # Z4
    # else:
    #     assert Z[0][0] == (Rbo - self.H0) * exp(-1j * self.W2 * 0.5)  # Z6
    #     assert Z[Nrad][0] == (Rbo - self.H0 - self.H2) * exp(-1j * self.W2 * 0.5)  # Z5
    #     assert Z[0][Ntan] == (Rbo - self.H0) * exp(1j * self.W2 * 0.5)  # Z3
    #     assert Z[Nrad][Ntan] == (Rbo - self.H0 - self.H2) * exp(
    #         1j * self.W2 * 0.5
    #     )  # Z4

    surf_list = list()
    for jj in range(Ntan):  # jj from 0 to Ntan-1
        for ii in range(Nrad):  # ii from 0 to Nrad-1
            Z1 = Z[ii][jj]
            Z2 = Z[ii][jj + 1]
            Z3 = Z[ii + 1][jj + 1]
            Z4 = Z[ii + 1][jj]
            point_ref = (
                Z[ii][jj] + Z[ii][jj + 1] + Z[ii + 1][jj + 1] + Z[ii + 1][jj]
            ) / 4  # the reference point of the surface
            curve_list = list()
            curve_list.append(
                Arc1(
                    Z1,
                    Z2,
                    abs(Z1),
                    is_trigo_direction=True,
                )
            )
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

    # Correct bottom line for particular case (cf Tests\Validation\Magnetics\test_FEMM_fast_draw.py)
    if (Ntan == 2 and Nrad == 1) and self.W0 != self.W2:
        # Cut Ox- surface
        arc_to_cut = surf_list[0].line_list[0]
        arc1, arc2 = arc_to_cut.split_line(Z1=0, Z2=Rbo * exp(-1j * self.W0 / 2))
        surf_list[0].line_list = [arc1[0], arc2[0]] + surf_list[0].line_list[1:]
        surf_list[0].line_list[1].prop_dict = {DRAW_PROP_LAB: False}
        # Cut Ox+ surface
        arc_to_cut = surf_list[1].line_list[0]
        arc1, arc2 = arc_to_cut.split_line(Z1=0, Z2=Rbo * exp(1j * self.W0 / 2))
        surf_list[1].line_list = [arc1[0], arc2[0]] + surf_list[1].line_list[1:]
        surf_list[1].line_list[0].prop_dict = {DRAW_PROP_LAB: False}

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
