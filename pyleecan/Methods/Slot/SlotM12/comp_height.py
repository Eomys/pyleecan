# -*- coding: utf-8 -*-

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotM12
        A SlotM12 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    [Z1, Z2, Z3, Z4, _, _, _, _] = self._comp_point_coordinate()

    Rbo = self.get_Rbo()

    if self.is_outwards():
        return abs(Z2) - Rbo
    else:
        return Rbo - abs((Z2 + Z3) / 2)
