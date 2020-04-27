# -*- coding: utf-8 -*-


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return 0.5 * (self.W0 + self.W2) * self.H2
