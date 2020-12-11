# -*- coding: utf-8 -*-

from numpy import sin, pi


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    [Z1, Z2, _, _, _, _, _, _] = self._comp_point_coordinate()

    R1 = abs(Z1)
    R2 = abs(Z2)

    S1 = pi * R1 ** 2 * (self.W0 / (2 * pi))
    S2 = pi * R2 ** 2 * (self.W0 / (2 * pi))

    return abs(S1 - S2)
