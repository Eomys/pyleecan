# -*- coding: utf-8 -*-


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    return self.Hmag * self.Wmag
