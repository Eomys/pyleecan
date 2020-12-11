# -*- coding: utf-8 -*-

from ....Methods import ParentMissingError


def is_outwards(self):
    """Return if the magnet is outwards (on an external lamination) or inwards
    (on an internal lamination)

    Parameters
    ----------
    self : Magnet
        A Magnet object

    Returns
    -------
    is_outwards: bool
        Direction of the magnet
    Raises
    _______
    ParentMissingError
        Error: The magnet is not inside a Slot
    """
    if self.parent is not None:
        return self.parent.is_outwards()
    else:
        raise ParentMissingError("Error: The magnet is not inside a Slot")
