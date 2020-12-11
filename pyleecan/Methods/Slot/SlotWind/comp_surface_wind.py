# -*- coding: utf-8 -*-


def comp_surface_wind(self, Ndisc=200):
    """Compute the Slot winding surface (by numerical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotWind
        A SlotWind object
    Ndisc : int
        Number of point to discretize the lines

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    surf = self.get_surface_wind()

    return surf.comp_surface(Ndisc=Ndisc)
