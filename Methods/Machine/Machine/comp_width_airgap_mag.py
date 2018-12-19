# -*- coding: utf-8 -*-
"""@package Methods.Machine.Machine.comp_width_airgap_mag
Compute the magnetic airgap of the machine method
@date Created on Thu Jan 22 16:25:34 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_width_airgap_mag(self):
    """Compute the magnetic airgap (distance beetween the two Lamination)

    Parameters
    ----------
    self: Machine
        A Machine object
    Returns
    -------
    mag_gap: float
        The magnetic airgap [m]

    """

    if self.rotor.is_internal:
        return self.stator.Rint - self.rotor.Rext
    else:
        return self.rotor.Rint - self.stator.Rext
