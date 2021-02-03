# -*- coding: utf-8 -*-

from numpy import arcsin, pi

from pyleecan.Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.HoleM57 import *


def check(self):
    """Check that the HoleM57 object is correct

    Parameters
    ----------
    self : HoleM57
        A HoleM57 object

    Returns
    -------
    None

    Raises
    _______
    """
    # Check that everything is set
    if self.W0 is None:
        raise S57_NoneError("You must set W0 !")
    elif self.W1 is None:
        raise S57_NoneError("You must set W1 !")
    elif self.W2 is None:
        raise S57_NoneError("You must set W2 !")
    elif self.W3 is None:
        raise S57_NoneError("You must set W3 !")
    elif self.W4 is None:
        raise S57_NoneError("You must set W4 !")
    elif self.H1 is None:
        raise S57_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S57_NoneError("You must set H2 !")
