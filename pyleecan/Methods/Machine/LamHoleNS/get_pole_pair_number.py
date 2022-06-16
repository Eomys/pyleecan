def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamHoleNS
        A LamHoleNS object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    return self.hole_north[0].Zh
