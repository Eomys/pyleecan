def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotWLSRPM
        A SlotWLSRPM object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    return self.get_Ryoke()-self.get_Rbo()