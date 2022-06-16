def get_Zs(self):
    """Return the number of holes in the lamination

    Parameters
    ----------
    self : LamH
        A LamH object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    return self.get_pole_pair_number() * 2
