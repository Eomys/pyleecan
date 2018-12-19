# -*- coding: utf-8 -*-
"""@package

@date Created on Wed Apr 27 15:19:10 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_Ntspc(self, Zs):
    """Compute the number of turns in series per phase

    Parameters
    ----------
    self : Winding
        A Winding object
    Zs : int
        Number of slot

    Returns
    -------
    Ntspc: float
        Number of turns in series per phase

    """

    Ncspc = self.comp_Ncspc(Zs)

    return Ncspc * self.Ntcoil
