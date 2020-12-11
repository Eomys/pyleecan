# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the Magnet total surface (by numerical computation).

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    S: float
        Magnet total surface [m**2]

    """

    surf_list = self.build_geometry()
    S = 0
    for surf in surf_list:
        S += surf.comp_surface()
    return S
