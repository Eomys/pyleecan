# -*- coding: utf-8 -*-
"""@package

@date Created on Wed Apr 27 15:15:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_Ncspc(self, Zs):
    """Compute the number of coils in series per parallel circuit

    Parameters
    ----------
    self : Winding
        A Winding object
    Zs : int
        number of slot

    Returns
    -------
    Ncspc: float
        Number of coils in series per parallel circuit

    """

    (Nrad, Ntan) = self.get_dim_wind()
    Ncspc = Zs * Nrad * Ntan / (2.0 * self.qs * self.Npcpp)

    return Ncspc
