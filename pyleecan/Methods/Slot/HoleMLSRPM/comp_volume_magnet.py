# -*- coding: utf-8 -*-

from numpy import exp, arcsin, tan, cos, sqrt, sin


def comp_volume_magnet(self):
    """Compute the volume of the magnet (if any)

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object

    Returns
    -------
    Vmag: float
        Volume of the magnet [m**3]

    """
    S_magnet = self.comp_surface_magnet()

    if self.magnet_0:
        return S_magnet * self.magnet_0.Lmag
    else:
        return 0
