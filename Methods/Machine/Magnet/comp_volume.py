# -*- coding: utf-8 -*-


def comp_volume(self):
    """Compute the Magnet volume (by analytical computation)

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    V: float
        Magnet volume [m**3]

    """

    return self.comp_surface() * self.Lmag
