# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW24._comp_alpha
SlotW24 compute opening angle method
@date Created on Mon Jul 06 11:40:07 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin, pi


def comp_alphas(self):
    """Compute the opening angle to have a constant slot.

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    (alpha_0,alpha_2): tuple
        Angle at top and bottom of the slot [rad]

    """
    Rbo = self.get_Rbo()

    # alpha_Tt is the angle of the tooth to have the correct top width
    alpha_Tt = 2 * float(arcsin(self.W3 / (2 * Rbo)))

    # alpha_0 + alpha_Tt = slot_ptich
    # Zs * (alpha_0+alpha_Tt) = 2 pi
    alpha_0 = 2 * pi / self.Zs - alpha_Tt

    if self.is_outwards():
        # alpha_Tb is the angle of the tooth to have the correct bottom width
        alpha_Tb = 2 * float(arcsin(self.W3 / (2 * (Rbo + self.H2))))
    else:
        alpha_Tb = 2 * float(arcsin(self.W3 / (2 * (Rbo - self.H2))))

    # Zs * (alpha_2+alpha_Tb) = 2 pi
    alpha_2 = 2 * pi / self.Zs - alpha_Tb

    return (alpha_0, alpha_2)
