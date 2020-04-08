# -*- coding: utf-8 -*-

from pyleecan.Methods.Slot.SlotW15 import S15InnerError


def check(self):
    """Check that the SlotW15 object is correct

    Parameters
    ----------
    self : SlotW15
        A SlotW15 object

    Returns
    -------
    None

    Raises
    -------
    S15InnerError
        Slot Type 15 can't be used on inner lamination
    """

    if not self.is_outwards():
        raise S15InnerError("Slot Type 15 can't be used on inner lamination")
