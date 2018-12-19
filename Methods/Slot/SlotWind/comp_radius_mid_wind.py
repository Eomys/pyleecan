# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotWind.comp_angle_eq
SlotW10 Computation of average angle method
@date Created on Tue Dec 09 17:07:09 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_radius_mid_wind(self):
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
    Hwind = self.comp_height_wind()
    if self.is_outwards():
        return Rbo + Hslot - Hwind / 2
    else:
        return Rbo - Hslot + Hwind / 2
