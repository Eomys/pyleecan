# -*- coding: utf-8 -*-

from ....Classes.LamSlot import LamSlot


def comp_masses(self):
    """Compute the Lamination masses

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionnary (Mtot, Mlam, Mwind) [kg]
    """

    M_dict = LamSlot.comp_masses(self)

    if self.winding is not None:
        L_dict = self.comp_lengths_winding()
        Mwind = (
            self.winding.conductor.comp_surface_active()
            * self.winding.conductor.cond_mat.struct.rho
            * L_dict["Lwtot"]
        )
    else:
        Mwind = 0

    M_dict["Mtot"] += Mwind
    M_dict["Mwind"] = Mwind

    return M_dict
