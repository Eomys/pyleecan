# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlotMag.get_pole_pair_number
Return the number of pair of pole method
@date Created on Mon Feb 16 13:37:33 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def get_pole_pair_number(self):
    """Return the number of pair of pole of the Lamination

    Parameters
    ----------
    self : LamSlotMag
        A LamSlotMag object

    Returns
    -------
    p: int
        Number of pair of pole

    """

    return self.Nmag // 2
