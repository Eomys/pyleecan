# -*- coding: utf-8 -*-
from numpy import exp, pi

from ...Classes.Arc1 import Arc1
from ...Classes.Arc2 import Arc2
from ...Classes.Circle import Circle
from ...Classes.Segment import Segment
from ...Classes.SurfLine import SurfLine


def get_air_box(sym, machine):
    """Returns  an outer surface surrounding the external lamination

    Parameters
    ----------
    sym: int
        Symmetry factor (1= full machine, 2= half of the machine...)
    machine: float
        to extract laminations

    Returns
    -------
    surf_list: list
        Outer surface (Air Box)
    """
    lam_list = machine.get_lam_list()
    lam_int = lam_list[0]
    lam_ext = lam_list[1]

    R_ext = lam_ext.get_Ryoke()
    R_ab = 1.5 * R_ext  # Default at 1.5 times external lam radius

    surf_list = list()
    if sym == 1:  # Complete machine
        # TO-DO: Airbox Full Machine no implemented yet.

        surf_list.append(
            Circle(
                center=0,
                radius=R_ab,
                label="Airbox",
                point_ref=(R_ab / 2) * exp(1j * pi / 2),
                line_label="Airbox_arc",
            )
        )
    else:  # Symmetry
        # Internal AirGap
        Z1 = R_ext
        Z0 = Z1 * exp(1j * 2 * pi / sym)
        Z2 = R_ab
        Z3 = Z2 * exp(1j * 2 * pi / sym)
        airbox_lines = list()
        airbox_lines.append(Segment(begin=Z1, end=Z2, label="airbox_line_1"))
        airbox_lines.append(
            Arc1(
                begin=Z2,
                end=Z3,
                radius=R_ab,
                label="airbox_arc",
                is_trigo_direction=True,
            )
        )
        airbox_lines.append(Segment(begin=Z3, end=Z0, label="airbox_line_2"))
        airbox_lines.append(
            Arc2(begin=Z0, center=0.0, angle=-2 * pi / sym, label="lam_ext_arc")
        )
        surf_list.append(
            SurfLine(
                line_list=airbox_lines,
                # point_ref=0.0 * Z2 * exp(1j * pi / sym),
                label="Airbox",
            )
        )

    return surf_list
