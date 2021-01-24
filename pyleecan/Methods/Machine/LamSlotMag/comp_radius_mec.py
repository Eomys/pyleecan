# -*- coding: utf-8 -*-

from numpy import array


def comp_radius_mec(self):
    """Compute the mechanical radius of the Lamination [m]

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    Rmec: float
        Mechanical radius [m]

    """

    (Rmin, Rmax) = self.slot.comp_radius()

    if self.is_internal:  # inward Slot
        # Top radius of the magnet
        return max(self.Rext, Rmax)
    else:
        return min(self.Rint, Rmin)
