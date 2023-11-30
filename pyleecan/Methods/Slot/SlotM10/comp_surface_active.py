# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the Slot active inner surface (by analytical computation)

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object

    Returns
    -------
    Swind: float
        Slot active inner surface [m**2]

    """

    return self.H1 * self.W1
