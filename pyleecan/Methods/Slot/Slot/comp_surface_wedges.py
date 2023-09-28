def comp_surface_wedges(self, Ndisc=200):
    """Compute the Slot wedges surface (by numerical computation).
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
        Slot wedges surface [m**2]

    """

    surf_list = self.get_surface_wedges()

    S = 0
    for surf in surf_list:
        S += surf.comp_surface(Ndisc=Ndisc)
    return S
