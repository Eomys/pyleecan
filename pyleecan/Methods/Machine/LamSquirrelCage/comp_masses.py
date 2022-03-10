# -*- coding: utf-8 -*-

from ....Classes.LamSlot import LamSlot


def comp_masses(self):
    """Compute the Lamination masses

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionary (Mtot, Mlam, Mwind, Mring) [kg]
    """

    if self.is_stator:
        lam_name = "Stator"
    else:
        lam_name = "Rotor"
    M_dict = LamSlot.comp_masses(self)

    if self.winding is not None:
        # Check
        if self.winding.conductor.cond_mat.struct.rho is None:
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
            * self.get_Zs()
            * self.winding.conductor.cond_mat.struct.rho
            * L_dict["Lwht"]
        )
    else:
        Mwind = 0

    # Adding Short circuit ring
    # Check
    if self.ring_mat.struct.rho is None:
        mat_name = str(self.ring_mat.name)
        raise Exception(
            "Error: The "
            + lam_name
            + " Short circuit ring material ("
            + mat_name
            + ") is not fully defined. Please set struct.rho"
        )
    Sring = self.comp_surface_ring()
    Lring = self.comp_length_ring()
    Mring = Sring * Lring * self.ring_mat.struct.rho

    M_dict["Mtot"] += Mwind + Mring
    M_dict["Mwind"] = Mwind + Mring
    M_dict["Mring"] = Mring

    return M_dict
