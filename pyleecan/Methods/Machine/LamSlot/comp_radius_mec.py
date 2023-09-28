# -*- coding: utf-8 -*-


def comp_radius_mec(self):
    """Compute the mechanical radius of the Lamination [m]

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    Rmec: float
        Mechanical radius [m]
    """

    if self.slot.is_airgap_active():
        # Part of the active surface is in the airgap
        # => Reduce mechanical airgap
        (Rmin, Rmax) = self.slot.comp_radius()
        if self.is_internal:  # inward Slot
            # Top radius of the magnet
            return max(self.Rext, Rmax)
        else:
            return min(self.Rint, Rmin)
    else:
        return self.get_Rbo()
