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
        Lamination mass dictionary (Mtot, Mlam, Mmag) [kg]

    """

    M_dict = LamSlot.comp_masses(self)
    p = self.get_pole_pair_number()

    Mmag = (
        2
        * p
        * (
            self.slot.comp_surface_active()
            * self.magnet.Nseg
            * self.magnet.Lmag
            * self.magnet.mat_type.struct.rho
        )
    )

    M_dict["Mmag"] = Mmag
    M_dict["Mtot"] += Mmag

    return M_dict
