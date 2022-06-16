def set_pole_pair_number(self, p):
    """Set the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamH
        A LamH object
    p: int
        Number of pair of pole

    """

    for hole in self.get_hole_list():
        hole.Zh = 2 * p
