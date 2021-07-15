# -*- coding: utf-8 -*-

from numpy import pi


def comp_volume(self):
    """Compute the volume of the Frame and structural Bars

    Parameters
    ----------
    self : FrameBar
        A FrameBar object

    Returns
    -------
    Vfra: float
        Volume of the Frame and structural bars [m**3]

    """

    Sfra = self.comp_surface()
    Sbar = self.comp_surface_bar()
    if self.Lfra is None:
        return 0
    else:
        return (Sfra + Sbar) * self.Lfra
