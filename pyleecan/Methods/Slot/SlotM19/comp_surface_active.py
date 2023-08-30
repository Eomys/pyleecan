# -*- coding: utf-8 -*-
from numpy import arcsin, pi, sin


def comp_surface_active(self):
    """Compute the Slot active inner surface (by analytical computation)

    Parameters
    ----------
    self : SlotM19
        A SlotM19 object

    Returns
    -------
    Swind: float
        Slot active inner surface [m**2]

    """
    return self.comp_surface()  # Magnet perfectly match the slot
