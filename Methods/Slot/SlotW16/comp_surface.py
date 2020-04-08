from numpy import pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW16
        A SlotW16 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    Swind = self.comp_surface_wind()
    S0 = (pi * Rbo ** 2 - pi * (Rbo - self.H0) ** 2) * self.W0 / (2 * pi)

    return Swind + S0
