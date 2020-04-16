# -*- coding: utf-8 -*-

from numpy import pi, angle, exp

from ....Classes.Circle import Circle
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def get_Zs(self):
    """Return the number of Slot of the Lamination

    Parameters
    ----------
    self : LamSlot
        a LamSlot object

    Returns
    -------
    Zs : float
        Number of Slot
    """

    if self.slot is None:
        return 0
    else:
        return self.slot.Zs
