# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.get_Rbo
Return lamination bore radius
@date Created on Tue Mai 29 17:51:12 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def get_Rbo(self):
    """Return the bore lamination radius

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    Rbo: float
        The lamination bore radius [m]

    """

    if self.is_internal:
        return self.Rext
    else:
        return self.Rint
