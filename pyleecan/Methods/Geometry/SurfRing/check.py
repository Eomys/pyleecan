# -*- coding: utf-8 -*-
def check(self):
    """assert the Surface is correct

    Parameters
    ----------
    self : SurfRing
        A SurfRing object

    Returns
    -------
    None
    """
    self.out_surf.check()
    self.in_surf.check()
