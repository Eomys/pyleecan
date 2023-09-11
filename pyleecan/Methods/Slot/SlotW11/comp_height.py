# -*- coding: utf-8 -*-

from numpy import cos, exp, arcsin


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    if self.is_cstt_tooth:
        # Compute W1 and W2 to match W3 tooth constraint
        self._comp_W()
    Rbo = self.get_Rbo()
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z5 = point_dict["Z5"]

    Harc = abs(Z1.real - Rbo)

    Harc2 = abs(Z5.real - Rbo)

    if self.is_outwards():
        return abs(Z5) - Rbo
    else:
        return Rbo - Harc - abs(Z5)
