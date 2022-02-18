# -*- coding: utf-8 -*-

from numpy import sin, pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW23
        A SlotW23 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    return self.comp_surface_active() + self.comp_surface_opening()
