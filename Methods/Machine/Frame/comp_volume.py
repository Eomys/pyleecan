# -*- coding: utf-8 -*-

from numpy import pi


def comp_volume(self):
    """Compute the volume of the Frame

    Parameters
    ----------
    self : Frame
        A Frame object

    Returns
    -------
    Vfra: float
        Volume of the Frame [m**3]

    """

    Sfra = self.comp_surface()
    return Sfra * self.Lfra
