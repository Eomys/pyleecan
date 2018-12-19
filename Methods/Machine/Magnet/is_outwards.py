# -*- coding: utf-8 -*-
"""@package Methods.Machine.Magnet.check
Check that the Magnet is correct
@date Created on Mon Aug 06 15:47:19 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods import ParentMissingError


def is_outwards(self):
    """Return if the magnet is outwards (on an external lamination) or inwards
    (on an internal lamination)

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    is_outwards: bool
        Direction of the magnet
    Raises
    _______
    ParentMissingError
        Error: The magnet is not inside a Slot
    """
    if self.parent is not None:
        return self.parent.is_outwards()
    else:
        raise ParentMissingError("Error: The magnet is not inside a Slot")
