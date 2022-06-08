def has_slot(self, is_bore=True):
    """Return if the lamination has slot on the requested radius
    (notches not taken into account, cf has_notch)

    Parameters
    ----------
    self : LamSlot
        A LamSlot object
    is_bore : bool
        True check if there are slots on the bore, else yoke

    Returns
    -------
    has_slot : bool
        True if the lamination has slot on the requested radius
    """

    return self.slot is not None and self.slot.Zs != 0 and self.slot.is_bore == is_bore
