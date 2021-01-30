# -*- coding: utf-8 -*-

from numpy import pi
from ....Classes.LamSlot import LamSlot


def comp_masses(self):
    """Compute the Lamination masses (Mlam, Mmag)

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionnary (Mtot, Mlam, Mmag) [kg]

    """

    M_dict = LamSlot.comp_masses(self)
    Mmag = (
        self.slot.comp_surface_active()
        * self.magnet.Lmag
        * self.magnet.mat_type.struct.rho
    )

    M_dict["Mmag"] = Mmag
    M_dict["Mtot"] += Mmag

    return M_dict
