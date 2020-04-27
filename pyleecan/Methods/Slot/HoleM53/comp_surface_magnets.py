# -*- coding: utf-8 -*-


def comp_surface_magnets(self):
    """Compute the surface of the magnets (if any)

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    Smag: float
        Surface of the Magnets [m**2]

    """

    S = 0
    if self.magnet_0:
        S += self.H2 * self.W3
    if self.magnet_1:
        S += self.H2 * self.W3
    return S
