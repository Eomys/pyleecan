# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotWind._comp_masses
Lamination with Winding computation of all masses method
@date Created on Tue Jan 13 15:26:49 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.Lamination import Lamination


def comp_output_geo(self):
    """Compute the main geometry output

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    output: OutGeoLam
        Main geometry output of the lamintion

    """

    output = Lamination.comp_output_geo(self)
    output.Ksfill = self.comp_fill_factor()
    if self.slot is None:
        output.S_slot = 0
        output.S_slot_wind = 0
    else:
        output.S_slot = self.slot.comp_surface()
        output.S_slot_wind = self.slot.comp_surface_wind()
    # output.S_wind_act = self.winding.conductor.comp_surface_active()

    return output
