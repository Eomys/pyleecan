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

    point_dict = self._comp_point_coordinate()
    Z5 = point_dict["Z5"]

    return Rbo - abs(Z5)
