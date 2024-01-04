# -*- coding: utf-8 -*-


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    Rbo = self.get_Rbo()
    point_dict = self._comp_point_coordinate()
    Z5 = point_dict["Z5"]
    Z4 = point_dict["Z4"]

    return Rbo - abs((Z5 + Z4) / 2)
