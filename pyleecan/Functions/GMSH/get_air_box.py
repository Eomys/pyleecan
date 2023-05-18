# -*- coding: utf-8 -*-
from numpy import exp, pi

from ...Classes.Arc1 import Arc1
from ...Classes.Arc2 import Arc2
from ...Classes.Circle import Circle
from ...Classes.Segment import Segment
from ...Classes.SurfLine import SurfLine
from ...Functions.labels import (
    AIRBOX_R_LAB,
    NO_LAM_LAB,
    AIRBOX_LAB,
    BOUNDARY_PROP_LAB,
    AIRBOX_SR_LAB,
    AIRBOX_SL_LAB,
    AIRBOX_R_LAB,
)


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
                label=NO_LAM_LAB + "_" + AIRBOX_LAB,
                point_ref=(R_ab / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: AIRBOX_R_LAB},
            )
        )
    else:  # Symmetry
        # Internal AirGap
        Z1 = R_ext
        Z0 = Z1 * exp(1j * 2 * pi / sym)
        Z2 = R_ab
        Z3 = Z2 * exp(1j * 2 * pi / sym)
        airbox_lines = list()
        airbox_lines.append(
            Segment(begin=Z1, end=Z2, prop_dict={BOUNDARY_PROP_LAB: AIRBOX_SR_LAB})
        )
        airbox_lines.append(
            Arc1(
                begin=Z2,
                end=Z3,
                radius=R_ab,
                prop_dict={BOUNDARY_PROP_LAB: AIRBOX_R_LAB},
                is_trigo_direction=True,
            )
        )
        airbox_lines.append(
            Segment(begin=Z3, end=Z0, prop_dict={BOUNDARY_PROP_LAB: AIRBOX_SL_LAB})
        )
        #airbox_lines.append(Arc2(begin=Z0, center=0.0, angle=-2 * pi / sym))
        airbox_lines.append(
             Arc1(
                 begin=Z0, 
                 end=Z1, 
                 radius=-R_ext,
                 is_trigo_direction=False,
                 )
        )
        surf_list.append(
            SurfLine(
                line_list=airbox_lines,
                # point_ref=0.0 * Z2 * exp(1j * pi / sym),
                label=NO_LAM_LAB + "_" + AIRBOX_LAB,
            )
        )

    return surf_list
