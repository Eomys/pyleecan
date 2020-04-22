# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Hole total surface (by numerical computation).

    Parameters
    ----------
    self : Hole
        A Hole object

    Returns
    -------
    S : float
        Slot total surface [m**2]

    """

    surf_list = self.build_geometry()
    S = 0
    for surf in surf_list:
        S += surf.comp_surface()

    return S
