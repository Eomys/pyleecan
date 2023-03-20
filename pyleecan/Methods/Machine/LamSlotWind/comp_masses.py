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
        Lamination mass dictionary (Mtot, Mlam, Mwind) [kg]
    """

    M_dict = LamSlot.comp_masses(self)

    if self.winding is not None:
        # Check
        if self.winding.conductor.cond_mat.struct.rho is None:
            if self.is_stator:
                lam_name = "Stator"
            else:
                lam_name = "Rotor"
            mat_name = str(self.winding.conductor.cond_mat.name)
            raise Exception(
                "Error: The "
                + lam_name
                + " winding conductor material ("
                + mat_name
                + ") is not fully defined. Please set struct.rho"
            )
        # Compute
        L_dict = self.comp_lengths_winding()
        Mwind = (
            self.winding.conductor.comp_surface_active()
            * self.winding.conductor.cond_mat.struct.rho
            * L_dict["Lwtot"]
        )
    else:
        Mwind = 0
    if self.slot is None or self.slot.wedge_mat is None:
        M_dict["Mwedge"] = 0
    else:
        Lf = self.comp_length()  # Include radial ventilation ducts
        M_dict["Mwedge"] = (
            self.slot.wedge_mat.struct.rho
            * Lf
            * self.get_Zs()
            * self.slot.comp_surface_wedges()
        )

    M_dict["Mtot"] += Mwind + M_dict["Mwedge"]
    M_dict["Mwind"] = Mwind

    return M_dict
