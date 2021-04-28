from pyleecan.Classes.Winding import Winding


def comp_fill_factor(self):
    """Compute the fill factor of the winding"""
    if self.winding is None or self.winding.qs == 0 or type(self.winding) is Winding:
        return 0
    else:
        # compute the number of conductors per slot
        Ncps_ = abs(self.winding.get_connection_mat().sum(axis=(0, 1))).sum(axis=1)
        Ncps = Ncps_.mean()

        if Ncps_.std() != 0:
            self.get_logger().warning(
                "LamSlotWind.comp_fill_factor: "
                "Uneven number of conductors per slot. "
                + "Max. number of conductors will be used to compute slot fill factor."
            )
            Ncps = Ncps_.max()

        # compute the winding surfaces
        S_slot_wind = self.slot.comp_surface_active()
        S_wind_act = self.winding.conductor.comp_surface_active() * Ncps

        return S_wind_act / S_slot_wind
