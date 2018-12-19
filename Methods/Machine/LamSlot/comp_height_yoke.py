# -*- coding: utf-8 -*-
"""@package Methods.Machine.LamSlot.comp_yoke_height
Lamination with empty Slot computation of yoke height method
@date Created on Tue Jan 20 10:01:53 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""


def comp_height_yoke(self):
    """Compute the yoke height

    Parameters
    ----------
    self : LamSlot
        A LamSlot object

    Returns
    -------
    Hy: float
        yoke height [m]

    """
    return self.Rext - self.Rint - self.slot.comp_height()
