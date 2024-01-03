# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW30
        A SlotW30 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    # comp_surface_active is an numerical computation (defined in Slot class)
    # comp_surface_opening is an analytical computation
    return self.comp_surface_active() + self.comp_surface_opening()
