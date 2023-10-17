# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError


def check(self):
    """Check that the SlotM11 object is correct

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object

    Returns
    -------
    None
    """
    # percentage of the slot pitch that W0 and W1 should not exceed
    slot_pitch_tol = 0.99

    if self.W1 is not None and self.W0 < self.W1:
        raise SlotCheckError("You must have W1 <= W0")
    if self.W1 is not None and self.W1 >= slot_pitch_tol * 2 * pi / self.Zs:
        raise SlotCheckError("You must have W1 < pi/p (use ring magnet instead)")
    if self.W0 >= slot_pitch_tol * 2 * pi / self.Zs:
        raise SlotCheckError("You must have W0 < pi/p")
