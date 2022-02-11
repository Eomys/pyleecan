def comp_surface_opening(self, Ndisc=200):
    """Compute the Slot opening surface (by numerical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : Slot
        A Slot object
    Ndisc : int
        Number of point to discretize the lines

    Returns
    -------
    S: float
        Slot opening surface [m**2]

    """

    surf = self.get_surface_opening()

    return surf.comp_surface(Ndisc=Ndisc)
