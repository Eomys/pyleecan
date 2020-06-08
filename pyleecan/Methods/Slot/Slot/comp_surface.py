# -*- coding: utf-8 -*-


def comp_surface(self, Ndisc=200):
    """Compute the Slot total surface (by numerical computation).
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
        Slot total surface [m**2]
    """

    surf = self.get_surface()
    return surf.comp_surface(Ndisc=Ndisc)
