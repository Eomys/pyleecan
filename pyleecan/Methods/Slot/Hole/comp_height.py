def comp_height(self):
    """Compute the height of the Hole (Rmax-Rmin)

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    H : float
        Height of the hole

    """

    (Rmin, Rmax) = self.comp_radius()
    return Rmax - Rmin
