# -*- coding: utf-8 -*-

from ....Classes.Lamination import Lamination


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
