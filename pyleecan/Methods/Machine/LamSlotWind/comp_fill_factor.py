def comp_fill_factor(self):
    """Compute the fill factor of the winding

    Parameters
    ----------
    self : LamSlotWind
        a LamSlotWind object

    Returns
    -------
    Kfill : float
        fill factor of the winding
    """

    if self.winding is None or self.winding.qs == 0 or self.winding.conductor is None:
        return 0
    else:
        # compute the number of conductors per slot
        Ncps = self.winding.comp_Ncps()

        # compute the winding surfaces
        S_slot_wind = self.slot.comp_surface_active()
        S_wind_act = self.winding.conductor.comp_surface_active() * Ncps

        return S_wind_act / S_slot_wind
