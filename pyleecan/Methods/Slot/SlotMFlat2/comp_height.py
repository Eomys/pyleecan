# -*- coding: utf-8 -*-

from numpy import cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    # Computation of the arc height
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    if self.is_outwards():
        return self.H0 - Harc
    else:
        return self.H0 + Harc
