# -*- coding: utf-8 -*-
def comp_length(self):
    """Compute the length of the SurfRing object (length of both surfaces)

    Parameters
    ----------
    self : SurfRing
        A SurfRing object

    Returns
    -------
    length: float
        Length of the surface [m]


    """
    return self.out_surf.comp_length() + self.in_surf.comp_length()
