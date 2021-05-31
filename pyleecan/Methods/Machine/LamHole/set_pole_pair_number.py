def set_pole_pair_number(self, p):
    """Set the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object
    p: int
        Number of pair of pole

    """

    self.hole[0].Zh = 2 * p
