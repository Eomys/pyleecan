def comp_fill_factor(self):
    """Compute the fill factor of the winding"""
    if self.winding is None or self.winding.qs == 0:
        return 0
    else:
        (Nrad, Ntan) = self.winding.get_dim_wind()
        S_slot_wind = self.slot.comp_surface_wind()
        S_wind_act = (
            self.winding.conductor.comp_surface_active()
            * self.winding.Ntcoil
            * Nrad
            * Ntan
        )

        return S_wind_act / S_slot_wind
