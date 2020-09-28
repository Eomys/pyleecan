# -*- coding: utf-8 -*-

from numpy import arctan


def comp_angle_magnet(self):
    """Compute the angle at the top of the magnet-slot in the slot 
        (underneath the slot opening)

    Parameters
    ----------
    self : SlotMFlat2
        A SlotMFlat2 object

    Returns
    -------
    alpha: float
        Angle at the top of the magnet in the slot [rad]

    """
    Rbo = self.get_Rbo()
    W0 = self.comp_W0m()
    Harc = self.comp_H_arc()
    if self.is_outwards():
        return float(2 * arctan(W0 / (2 * (Rbo + self.H1 - Harc))))
    else:
        return float(2 * arctan(W0 / (2 * (Rbo - self.H1 - Harc))))

    # if self.W0_is_rad:
    #     return self.W0
    # else:  # Convert W0 from m to rad
    #     Rbo = self.get_Rbo()
    #     return float(2 * arcsin(self.W0 / (2 * Rbo)))
