# -*- coding: utf-8 -*-


def comp_surface_magnets(self):
    """Compute the surface of the hole magnets

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object

    Returns
    -------
    Smag: float
        Surface of the 2 Magnets [m**2]

    """

    S = 0
    if self.magnet_0:
        S += self.H3 * self.W4
    if self.magnet_1:
        S += self.H3 * self.W4
    return S
