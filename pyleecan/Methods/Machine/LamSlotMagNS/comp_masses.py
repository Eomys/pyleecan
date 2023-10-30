from ....Classes.LamSlot import LamSlot


def comp_masses(self):
    """Compute the Lamination masses (Mlam, Mmag)

    Parameters
    ----------
    self : LamSlotMagNS
        A LamSlotMagNS object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionary (Mtot, Mlam, Mmag) [kg]

    """

    M_dict = LamSlot.comp_masses(self)
    p = self.get_pole_pair_number()

    Mmag = 0
    if self.magnet_north is not None:
        Mmag += p * (
            self.slot.comp_surface_active()
            * self.magnet_north.Nseg
            * self.magnet_north.Lmag
            * self.magnet_north.mat_type.struct.rho
        )
    if self.magnet_south is not None:
        Mmag += p * (
            self.slot_south.comp_surface_active()
            * self.magnet_south.Nseg
            * self.magnet_south.Lmag
            * self.magnet_south.mat_type.struct.rho
        )
    M_dict["Mmag"] = Mmag
    M_dict["Mtot"] += Mmag

    return M_dict
