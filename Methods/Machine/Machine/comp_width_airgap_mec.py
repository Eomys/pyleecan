# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine.comp_width_airgap_mec
Compute the mechanical airgap of the machine method
@date Created on Thu Jan 22 16:30:18 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_width_airgap_mec(self):
    """Compute the mechanical airgap (mag_airgap - magnet or ring)

    Parameters
    ----------
    self: Machine
        Machine object
    Returns
    -------
    mec_gap: float
        The mechanical airgap [m]

    """

    if self.rotor.is_internal:
        return self.stator.comp_radius_mec() - self.rotor.comp_radius_mec()
    else:
        return self.rotor.comp_radius_mec() - self.stator.comp_radius_mec()
