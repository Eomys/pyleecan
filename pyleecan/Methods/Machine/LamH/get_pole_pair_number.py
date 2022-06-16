def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamH
        A LamH object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    return self.get_hole_list()[0].Zh // 2
