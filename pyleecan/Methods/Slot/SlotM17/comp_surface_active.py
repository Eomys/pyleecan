# -*- coding: utf-8 -*-
from numpy import pi


def comp_surface_active(self):
    """Compute the Slot inner active surface (by analytical computation)

    Parameters
    ----------
    self : SlotM17
        A SlotM17 object

    Returns
    -------
    Swind: float
        Slot inner active surface [m**2]

    """

    return pi / 2 * (self.parent.Rext**2 - self.parent.Rint**2)
