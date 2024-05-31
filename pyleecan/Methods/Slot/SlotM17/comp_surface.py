# -*- coding: utf-8 -*-

from numpy import sin, pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM17
        A SlotM17 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    return pi / 2 * (self.parent.Rext**2 - self.parent.Rint**2)
