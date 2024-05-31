from numpy import pi


def comp_surface_opening(self):
    """Compute the Slot opening surface (by analytical computation).
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

    S0 = (pi * Rbo**2 - pi * (Rbo - self.H0) ** 2) * self.W0 / (2 * pi)

    return S0
