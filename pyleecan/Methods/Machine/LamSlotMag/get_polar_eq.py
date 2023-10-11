import numpy as np

from ....Classes.SlotM11 import SlotM11
from ....Classes.SlotM18 import SlotM18


def get_polar_eq(self):
    """Returns a polar equivalent of the lamination

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object to convert to polar

    Returns
    -------
    polar_eq: LamSlotMag
        The polar equivalent of the lamination
    """

    # Copy the lamination
    polar_eq = type(self)(init_dict=self.as_dict())

    # Compute the polar dimension of the slot
    Hmag = self.slot.comp_height_active()
    H0 = self.slot.comp_height()
    Wmag = self.slot.comp_angle_active_eq()
    W0 = self.slot.comp_angle_opening()

    if np.isclose(Wmag, W0):
        # Ring magnet
        polar_eq.slot = SlotM18(Zs=self.slot.Zs, Hmag=Hmag)
    else:
        # Polar magnet
        polar_eq.slot = SlotM11(Zs=self.slot.Zs, Hmag=Hmag, H0=H0, Wmag=Wmag, W0=W0)

    # TODO: Polar eq for ventilations ?
    polar_eq.axial_vent = list()

    return polar_eq
