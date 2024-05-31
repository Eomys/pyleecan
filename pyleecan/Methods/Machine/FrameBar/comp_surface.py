# -*- coding: utf-8 -*-

from numpy import pi


def comp_surface(self):
    """Compute the surface of the Frame including the structural bars

    Parameters
    ----------
    self : FrameBar
        A FrameBar object

    Returns
    -------
    Sfra: float
        Surface of the Frame [m**2]

    """

    # Outer Frame Surface
    S_ext = (self.Rext**2) * pi
    S_int = (self.Rint**2) * pi
    S_outer = S_ext - S_int

    # Bar Surface
    S_bar = self.comp_surface_bar()

    return S_outer + S_bar
