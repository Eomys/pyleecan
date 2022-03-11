from numpy import pi, arcsin, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW25
        A SlotW25 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    if self.type_close == 1:
        return self.comp_surface_active() + self.comp_surface_opening()
    elif self.type_close == 2:
        return self.comp_surface_active()
