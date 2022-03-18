from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    if self.type_close == 2:
        return self.comp_surface_active()
    else:
        return self.comp_surface_active() + self.comp_surface_opening()
