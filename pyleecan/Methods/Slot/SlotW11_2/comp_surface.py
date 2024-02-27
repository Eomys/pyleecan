def comp_surface(self):
    """Compute the Slot total surface (by analytical computation for comp_surface_opening and numerical computation for comp_surface_active).
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
    return self.comp_surface_active() + self.comp_surface_opening()
