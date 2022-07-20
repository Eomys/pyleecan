# -*- coding: utf-8 -*-

from ....Methods import ParentMissingError


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
    if self.parent is not None:
        if self.is_bore in [True, None]:
            return self.parent.is_outwards()
        else:
            return not self.parent.is_outwards()
    else:
        raise ParentMissingError(
            "Error: The slot is not inside a Lamination or a Notch"
        )
