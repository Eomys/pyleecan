# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the Slot inner surface for winding

    Parameters
    ----------
    self : SlotW62
        A SlotW62 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return 2 * self.W2 * self.H2
