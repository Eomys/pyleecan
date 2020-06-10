from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotCirc object is correct

    Parameters
    ----------
    self : SlotCirc
        A SlotCirc object

    Returns
    -------
    None
    """
    if self.H0 < self.W0 / 2:
        raise SC_WHCheckError("You must have W0/2 <= H0")


class SC_WHCheckError(SlotCheckError):
    """Raised when a SlotCirc has self.H0 < self.W0/2
    """

    pass
