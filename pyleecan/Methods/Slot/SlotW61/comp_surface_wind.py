# -*- coding: utf-8 -*-


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding

    Parameters
    ----------
    self : SlotW61
        A SlotW61 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return 2 * (self.H2 - self.H3 - self.H4) * ((self.W1 - self.W2) / 2 - self.W3)
