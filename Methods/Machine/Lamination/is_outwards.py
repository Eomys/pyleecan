# -*- coding: utf-8 -*-
"""@package Methods.Machine.Lamination.is_outwards
Check if the Slot is outwards or inwards
@date Created on Wed Feb 04 12:47:19 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo: method name is a little confusing - sebastian_g
"""


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
    return not self.is_internal
