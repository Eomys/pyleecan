# -*- coding: utf-8 -*-
"""@package

@date Created on Mon Nov 27 16:14:00 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""


def comp_height_wind(self):
    """Compute the height of the winding area

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    Hwind: float
        Height of the winding area [m]

    """
    return self.H1 + self.H2
