# -*- coding: utf-8 -*-
"""@package Methods.Machine.Slot.check
Check that the Slot is correct
@date Created on Wed Feb 04 12:47:19 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods import ParentMissingError


def is_outwards(self):
    """Return if the slot is outwards (on an external lamination) or inwards
    (on an internal lamination)

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    is_outwards: bool
        True if the Lamination is not internal and false if not
    """
    if self.parent is not None:
        return not self.parent.is_internal
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")
