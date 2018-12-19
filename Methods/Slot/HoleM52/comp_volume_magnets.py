# -*- coding: utf-8 -*-
"""@package

@date Created on Tue Feb 02 09:26:13 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_volume_magnets(self):
    """Compute the volume of the magnet (if any)

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    Vmag: float
        Volume of the magnet [m**3]

    """
    if self.magnet_0:
        return self.W0 * self.H1 * self.magnet_0.Lmag
    else:
        return 0
