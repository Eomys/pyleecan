# -*- coding: utf-8 -*-
from numpy import exp, pi

from ...Classes.SurfLine import SurfLine


def get_airgap_surface(lam_int, lam_ext):
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
        List of surface in the airgap including the sliding band surface
    """

    Rgap_mec_int = lam_int.comp_radius_mec()
    Rgap_mec_ext = lam_ext.comp_radius_mec()
    Wgap_mec = Rgap_mec_ext - Rgap_mec_int
    W_sb = Wgap_mec / 3  # Width sliding band
    surf_list = list()

    # Middle
    surf_list.append(
        SurfLine(
            line_list=[],
            point_ref=(Rgap_mec_int + W_sb * 3 / 2) * exp(1j * pi / 2),
            label="Airgap",
        )
    )

    return surf_list
