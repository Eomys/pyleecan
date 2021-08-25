def get_Zs(self):
    """Return the number of holes in the lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    return self.hole[0].Zh
