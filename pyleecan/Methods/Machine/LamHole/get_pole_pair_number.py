def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    if self.hole is not None and len(self.hole) > 0:
        return self.hole[0].Zh // 2

    else:
        return None
