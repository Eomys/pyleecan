# -*- coding: utf-8 -*-


def comp_surface_active(self, Ndisc=200):
    """Compute the Slot active surface (by numerical computation).
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
        Slot active surface [m**2]

    """

    surf = self.get_surface_active()

    return surf.comp_surface(Ndisc=Ndisc)
