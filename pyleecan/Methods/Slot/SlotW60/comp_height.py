# -*- coding: utf-8 -*-


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()
    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11] = self._comp_point_coordinate()

    return Rbo - abs(Z5)
