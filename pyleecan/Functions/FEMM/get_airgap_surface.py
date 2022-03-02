# -*- coding: utf-8 -*-
from numpy import exp, pi

from ...Classes.SurfLine import SurfLine
from ...Classes.Segment import Segment
from ...Functions.labels import (
    NO_LAM_LAB,
    AIRGAP_LAB,
    AS_BR_LAB,
    AS_BL_LAB,
    BOUNDARY_PROP_LAB,
)


def get_airgap_surface(lam_int, lam_ext, sym=1):
    """Returns a list of surface in the airgap without sliding band surface

    Parameters
    ----------
    lam_int:
        Internal lamination
    lam_ext:
        External lamination

    Returns
    -------
    surf_list: list
        List of surface in the airgap without sliding band surface
    point_ref: complex
        Airgap point ref
    """

    surf_list = list()

    Rgap_mec_int = lam_int.comp_radius_mec()
    Rgap_mec_ext = lam_ext.comp_radius_mec()
    Wgap_mec = Rgap_mec_ext - Rgap_mec_int

    point_ref = (Rgap_mec_int + Wgap_mec / 2) * exp(1j * pi / sym / 2)

    if sym == 1:
        line_list = list()
    else:
        Z1 = lam_int.get_Rbo()
        Z2 = lam_ext.get_Rbo()

        Z1_bis = Z1 * exp(1j * 2 * pi / sym)
        Z2_bis = Z2 * exp(1j * 2 * pi / sym)

        line_list = [
            Segment(Z1, Z2, prop_dict={BOUNDARY_PROP_LAB: AS_BR_LAB}),
            Segment(Z1_bis, Z2_bis, prop_dict={BOUNDARY_PROP_LAB: AS_BL_LAB}),
        ]

    # Middle
    surf_list.append(
        SurfLine(
            line_list=line_list,
            point_ref=point_ref,
            label=NO_LAM_LAB + "_" + AIRGAP_LAB,
        )
    )

    return surf_list, point_ref
