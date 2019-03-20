# -*- coding: utf-8 -*-
"""@package Methods.Machine.Frame.comp_mass
Frame computation the mass methods
@date Created on Thu Jan 29 13:20:03 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

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
