# -*- coding: utf-8 -*-
"""@package get_Rgap_mec
@date Created on août 17 09:35 2018
@author franco_i
"""


def comp_Rgap_mec(self):
    """Returns the radius of the center of the mecanical airgap

    Parameters
    ----------
    self : Machine
        Machine object

    Returns
    -------
    Rgap_mec: float
        Radius of the center of the mecanical airgap [m]

    """
    stator = self.stator
    rotor = self.rotor
    return (stator.comp_radius_mec() + rotor.comp_radius_mec()) / 2
