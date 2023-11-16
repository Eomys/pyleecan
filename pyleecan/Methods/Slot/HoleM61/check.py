from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.HoleM61 import *
from numpy import sqrt


def check(self):
    """Check that the HoleM61 object is correct

    Parameters
    ----------
    self : HoleM61
        A HoleM61 object

    Returns
    -------
    None

    Raises
    _______
    S61_WCheckError
        You must have H1 < H0
        You must have H2 < H0
    """
    # Check that everything is set
    if self.W0 is None:
        raise S61_NoneError("You must set W0 !")

    # add possibility to create hole without magnet
    # elif self.W1 is None:
    #    raise S61_NoneError("You must set W1 !")
    # elif self.W2 is None:
    #    raise S61_NoneError("You must set W2 !")
    elif self.W3 is None:
        raise S61_NoneError("You must set W3 !")
    elif self.H0 is None:
        raise S61_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S61_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S61_NoneError("You must set H2 !")

    if self.H1 > self.H0:
        raise S61_WCheckError("You must have H1 < H0")

    if self.H2 > self.H0:
        raise S61_WCheckError("You must have H2 < H0")
