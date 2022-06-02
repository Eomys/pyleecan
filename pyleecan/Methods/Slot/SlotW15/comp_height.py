def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    return self.H0 + self.H1 + self.H2
