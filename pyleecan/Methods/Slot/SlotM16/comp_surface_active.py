# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotM16
        A SlotM16 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return self.W1 * self.H1
