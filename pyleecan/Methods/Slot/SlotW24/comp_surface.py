# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW24
        A SlotW24 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    return self.comp_surface_wind()
