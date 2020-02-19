# -*- coding: utf-8 -*-

from numpy import pi, angle, exp

from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def get_Zs(self):
    """Return the number of Slot of the Lamination

    Parameters
    ----------
    self : LamSlotMulti
        a LamSlotMulti object

    Returns
    -------
    Zs : float
        Number of Slot

    """

    return len(self.slot_list)
