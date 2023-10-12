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

    Rmec = self.get_Rbo()
    if self.slot.is_airgap_active():
        # Part of the active surface is in the airgap
        # => Reduce mechanical airgap
        (Rmin, Rmax) = self.slot.comp_radius()
        if self.is_internal:  # inward Slot
            # Top radius of the magnet
            Rmec = max(Rmec, Rmax)
        else:
            Rmec = min(Rmec, Rmin)

    # Handles key in the airgap
    if self.notch is not None:
        for notch in self.notch:
            if notch.has_key():
                (Rmin, Rmax) = notch.notch_shape.comp_radius()
                if self.is_internal:  # inward Slot
                    Rmec = max(Rmec, Rmax)
                else:
                    Rmec = min(Rmec, Rmin)
    return Rmec
