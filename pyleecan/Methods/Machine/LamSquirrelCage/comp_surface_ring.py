# -*- coding: utf-8 -*-


def comp_surface_ring(self):
    """Computation of the ring cross-section surface area

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    Lring: float
        Surface area of the cross-section of the ring [m^2]

    """
    Hscr = self.Hscr
    Lscr = self.Lscr

    return Lscr * Hscr
