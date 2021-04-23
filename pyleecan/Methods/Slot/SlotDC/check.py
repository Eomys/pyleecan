from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotDC object is correct

    Parameters
    ----------
    self : SlotDC
        A SlotDC object

    Returns
    -------
    None
    """
    if self.W1 >= self.D1:
        raise SlotCheckError("Slot 17 must have W1 < D1")
    if self.W2 >= self.D1:
        raise SlotCheckError("Slot 17 must have W2 < D1")
    if self.W2 >= self.D2:
        raise SlotCheckError("Slot 17 must have W2 < D2")
    if self.H2 <= (self.D1 / 2 + self.D2 / 2):
        raise SlotCheckError("Slot 17 must have D1/2 + D2/2 < H2")
