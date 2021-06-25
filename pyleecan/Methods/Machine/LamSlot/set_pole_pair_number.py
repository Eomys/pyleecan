def set_pole_pair_number(self, p):
    """Set the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamSlot
        A LamSlot object
    p: int
        Number of pair of pole

    """

    self.slot.Zs = 2 * p
