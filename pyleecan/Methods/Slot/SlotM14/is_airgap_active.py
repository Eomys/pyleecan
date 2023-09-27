def is_airgap_active(self):
    """Return True if a part or the full active surface is in the airgap

    Parameters
    ----------
    self : SlotM14
        A SlotM14 object

    Returns
    -------
    is_airgap_active : bool
        True if a part or the full active surface is in the airgap
    """

    return self.comp_height_active() > self.H0
