# -*- coding: utf-8 -*-
"""@package Methods.Machine.Notch.check
Check that the Notch is Outward
@date Created on Wed Feb 04 12:47:19 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods import ParentMissingError


def is_outwards(self):
    """Return if the notch is outwards (on an external lamination) or inwards
    (on an internal lamination)

    Parameters
    ----------
    self : Notch
        A Notch object

    Returns
    -------
    is_outwards: bool
        True if the Lamination is not internal and false if not
    """
    if self.parent is not None:
        return self.parent.is_outwards()
    else:
        raise ParentMissingError("Error: The notch is not inside a Lamination")
