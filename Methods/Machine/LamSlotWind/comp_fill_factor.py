def comp_fill_factor(self):
    """Compute the fill factor of the winding
    """

    S_slot_wind = self.slot.comp_surface_wind()
    S_wind_act = (
        self.winding.conductor.comp_active_surface()
        * self.winding.Ntcoil
        * self.winding.Npcpp
    )

    return S_wind_act / S_slot_wind
