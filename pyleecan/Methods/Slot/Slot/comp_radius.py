# -*- coding: utf-8 -*-

from numpy import exp


def comp_radius(self):
    """Compute the radius of the min and max circle that contains the slot

    Parameters
    ----------
    self : SlotM10
        A SlotM10 object

    Returns
    -------
    (Rmin,Rmax): tuple
        Radius of the circle that contains the slot [m]

    """

    Rbo = self.get_Rbo()

    H = self.comp_height()
    Hmag = self.comp_height_active()

    if H < Hmag:
        if self.is_outwards():
            return (Rbo - Hmag + H, Rbo + H)
        else:
            return (Rbo - H, Rbo + Hmag - H)
    else:
        if self.is_outwards():
            return (Rbo, Rbo + H)
        else:
            return (Rbo - H, Rbo)
