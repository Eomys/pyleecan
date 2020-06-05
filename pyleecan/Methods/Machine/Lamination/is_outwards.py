# -*- coding: utf-8 -*-


def is_outwards(self):
    """Return if the slot is outwards (on an external lamination) or inwards
    (on an internal lamination)

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    is_outwards: bool
        True if the Lamination is not internal and false if not
    """
    return not self.is_internal
