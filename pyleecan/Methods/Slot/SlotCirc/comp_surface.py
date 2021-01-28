# -*- coding: utf-8 -*-

from numpy import sin, tan


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    return self.comp_surface_active()
