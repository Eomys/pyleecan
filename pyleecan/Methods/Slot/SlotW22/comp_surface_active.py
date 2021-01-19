# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface_active(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """
    Rbo = self.get_Rbo()

    if self.is_outwards():
        # Surface of the external disk
        Sext = ((self.H2 + self.H0 + Rbo) ** 2) * pi

        # Surface of the internal disk
        Sint = ((self.H0 + Rbo) ** 2) * pi
    else:
        # Surface of the external disk
        Sext = ((Rbo - self.H0) ** 2) * pi

        # Surface of the internal disk
        Sint = ((Rbo - self.H2 - self.H0) ** 2) * pi

    # Surface of the ring
    Sring = Sext - Sint

    # Only an W2 angle of the ring
    return Sring * self.W2 / (2 * pi)
