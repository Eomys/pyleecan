# -*- coding: utf-8 -*-


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
