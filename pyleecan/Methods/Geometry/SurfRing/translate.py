# -*- coding: utf-8 -*-


def translate(self, Zt):
    """Translate the surface

    Parameters
    ----------
    self : SurfRing
        A SurfRing object

    Zt : complex
        Complex value for translation

    Returns
    -------
    None
    """
    if Zt == 0:
        return  # Nothing to do
    # Check if the Surface is correct
    self.check()

    self.out_surf.translate(Zt)
    self.in_surf.translate(Zt)

    if self.point_ref is not None:
        self.point_ref += Zt
