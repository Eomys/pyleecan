# -*- coding: utf-8 -*-


def comp_surface_magnets(self):
    """Compute the surface of the hole magnets

    Parameters
    ----------
    self : HoleM58
        A HoleM58 object

    Returns
    -------
    Smag: float
        Surface of the Magnet [m**2]

    """

    S = 0
    if self.magnet_0:
        S += self.H2 * self.W1
    return S
