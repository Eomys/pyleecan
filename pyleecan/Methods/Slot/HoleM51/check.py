# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot import SlotCheckError
from numpy import pi
from ....Methods.Slot.HoleM51 import *


def check(self):
    """Check that the HoleM51 object is correct

    Parameters
    ----------
    self : HoleM51
        A HoleM51 object

    Returns
    -------
    None
    """

    # Check that everything is set
    if self.W0 is None:
        raise S51_NoneError("You must set W0 !")
    elif self.W1 is None:
        raise S51_NoneError("You must set W1 !")
    elif self.W2 is None:
        raise S51_NoneError("You must set W2 !")
    elif self.W3 is None:
        raise S51_NoneError("You must set W3 !")
    elif self.W4 is None:
        raise S51_NoneError("You must set W4 !")
    elif self.W5 is None:
        raise S51_NoneError("You must set W5 !")
    elif self.W6 is None:
        raise S51_NoneError("You must set W6 !")
    elif self.W7 is None:
        raise S51_NoneError("You must set W7 !")
    elif self.H0 is None:
        raise S51_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S51_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S51_NoneError("You must set H2 !")

    Rext = self.get_Rext()
    alpha = self.comp_alpha()

    if self.W0 < (self.W2 + self.W3):
        raise S51_WCheckError("You must have W2+W3 < W0")

    if Rext < self.H0 + self.H2:
        raise S51_RHCheckError("You must have H0+H2 < Rext")

    if alpha > pi / 2:
        raise S51_AlphaCheckError("You must have alpha < pi/2")
