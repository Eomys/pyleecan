# -*- coding: utf-8 -*-
from ....Classes.SlotW22 import SlotW22


def get_polar_eq(self):
    """Returns a polar equivalent of the lamination

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object to convert to polar

    Returns
    -------
    polar_eq: LamSlotWind
        The polar equivalent of the lamination
    """

    # Copy the lamination
    polar_eq = type(self)(init_dict=self.as_dict())

    # Compute the polar dimension of the slot
    Hwind = self.slot.comp_height_wind()
    Histhmus = self.slot.comp_height() - Hwind
    Wwind = self.slot.comp_angle_wind_eq()
    Wisthmus = self.slot.comp_angle_opening()

    polar_eq.slot = SlotW22(
        Zs=self.slot.Zs, H0=Histhmus, W0=Wisthmus, H2=Hwind, W2=Wwind
    )

    # TODO: Polar eq for ventilations ?
    polar_eq.axial_vent = list()

    return polar_eq
