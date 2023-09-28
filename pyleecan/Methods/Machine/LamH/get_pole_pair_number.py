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

    hole_list = self.get_hole_list()
    if len(hole_list) > 0:
        return hole_list[0].Zh // 2
    else:
        return None
