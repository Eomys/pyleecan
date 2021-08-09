# -*- coding: utf-8 -*-
from numpy import exp, arcsin, tan, cos, sqrt, sin


def comp_mass_magnet(self):
    """Compute the mass of the magnet (if any)

    Parameters
    ----------
    self : HoleMLSRPM
        A HoleMLSRPM object

    Returns
    -------
    Mmag: float
        mass of the magnet [kg]

    """

    # Simplify the calculate of the magnet surface
    V_magnet = self.comp_volume_magnet()

    if self.magnet_0:
        return V_magnet * self.magnet_0.mat_type.struct.rho
    else:
        return 0
