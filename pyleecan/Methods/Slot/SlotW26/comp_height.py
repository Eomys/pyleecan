# -*- coding: utf-8 -*-

from numpy import arcsin, cos


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """
    Rbo = self.get_Rbo()

    # Computation of the arc height (P1,0,P8)
    alpha = self.comp_angle_opening() / 2
    Harc = float(Rbo * (1 - cos(alpha)))

    # Height of the arc (P2,C1,P7)
    Hwind = self.comp_height_wind()

    if self.is_outwards():
        return self.H0 + Hwind - Harc
    else:
        return self.H0 + Hwind + Harc
