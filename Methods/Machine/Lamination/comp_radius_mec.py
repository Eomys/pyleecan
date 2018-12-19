# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.comp_mec_radius
Computation of the mechanical radius of the Lamination
@date Created on Tue Mar 15 16:15:07 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def comp_radius_mec(self):
    """Compute the mechanical radius of the Lamination [m]

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Rmec: float
        Mechanical radius [m]

    """

    if self.is_internal:
        return self.Rext
    else:
        return self.Rint
