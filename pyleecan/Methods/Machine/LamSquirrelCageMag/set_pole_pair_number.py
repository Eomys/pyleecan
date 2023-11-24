def set_pole_pair_number(self, p):
    """Set the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamSquirrelCageMag
        A LamSquirrelCageMag object
    p: int
        Number of pair of pole

    """

    if self.winding is not None:
        self.winding.p = p
    if self.hole is not None:
        for hole in self.hole:
            hole.Zh = 2 * p
