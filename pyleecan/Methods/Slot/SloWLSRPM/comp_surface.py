from numpy import pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
 

    Swind = self.comp_surface_wind()


    return Swind
