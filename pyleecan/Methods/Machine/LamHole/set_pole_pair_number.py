def set_pole_pair_number(self, p):
    """Set the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object
    p: int
        Number of pair of pole

    """

    for hole in self.hole:
        hole.Zh = 2 * p
