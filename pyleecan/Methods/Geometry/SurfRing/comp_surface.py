# -*- coding: utf-8 -*-


def comp_surface(self):
    """Compute the SurfRing surface

    Parameters
    ----------
    self : SurfRing
        A SurfRing object

    Returns
    -------
    surf: float
        The SurfRing surface [m**2]

    """

    Sout = self.out_surf.comp_surface()
    Sin = self.in_surf.comp_surface()

    assert Sout > Sin

    return Sout - Sin
