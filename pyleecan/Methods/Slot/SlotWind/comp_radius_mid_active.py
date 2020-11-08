# -*- coding: utf-8 -*-


def comp_radius_mid_active(self):
    """Compute the radius at the middle of the winding part of the slot

    Parameters
    ----------
    self : SlotWind
        A SlotWind object

    Returns
    -------
    Rmw: float
        Mid winding radius [m]

    """

    Rbo = self.get_Rbo()
    Hslot = self.comp_height()
    Hwind = self.comp_height_active()
    if self.is_outwards():
        return Rbo + Hslot - Hwind / 2
    else:
        return Rbo - Hslot + Hwind / 2
