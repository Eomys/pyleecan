def set_pole_pair_number(self, p):
    """Set the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    p: int
        Number of pair of pole

    """

    if self.winding is not None:
        self.winding.p = p
