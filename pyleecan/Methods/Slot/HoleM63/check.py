from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.HoleM63 import *
from numpy import sqrt


def check(self):
    """Check that the HoleM63 object is correct

    Parameters
    ----------
    self : HoleM63
        A HoleM63 object

    Returns
    -------
    None

    Raises
    _______
    S63_WCheckError
    """

    # Check that everything is set
    if self.W0 is None:
        raise S63_NoneError("You must set W0 !")
    elif self.H0 is None:
        raise S63_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S63_NoneError("You must set H1 !")
