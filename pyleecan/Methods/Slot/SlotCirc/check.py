from ....Methods.Slot.Slot import SlotCheckError


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
        raise SlotCheckError("You must have W0/2 <= H0")
