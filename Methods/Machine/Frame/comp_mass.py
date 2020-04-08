# -*- coding: utf-8 -*-

from numpy import pi


def comp_mass(self):
    """Compute the mass of the Frame

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    Mfra: float
        Mass of the Frame [kg]

    """

    Vfra = self.comp_volume()

    # Mass computation
    return Vfra * self.mat_type.struct.rho
