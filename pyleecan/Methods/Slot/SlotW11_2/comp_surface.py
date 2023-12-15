from pyleecan.Methods.Slot.Slot.comp_surface_active import comp_surface_active


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW11_2
        A SlotW11_2 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    return comp_surface_active(self) + self.comp_surface_opening()
