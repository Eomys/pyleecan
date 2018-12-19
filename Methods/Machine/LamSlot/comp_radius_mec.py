# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlot.comp_mec_radius
Computation of the mechanical radius of the Lamination
@date Created on Thu Feb 05 17:18:38 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_radius_mec(self):
    """Compute the mechanical radius of the Lamination [m]

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    Rmec: float
        Mechanical radius [m]

    """

    if self.is_internal:
        return self.Rext
    else:
        return self.Rint
