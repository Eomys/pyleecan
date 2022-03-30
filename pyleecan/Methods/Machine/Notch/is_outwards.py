# -*- coding: utf-8 -*-

from ....Methods import ParentMissingError


def is_outwards(self):
    """Return if the notch is outwards (on an external lamination) or inwards
    (on an internal lamination). If the notch is on the yoke, it is inwards or
    outwards respectively.

    Parameters
    ----------
    self : Notch
        A Notch object

    Returns
    -------
    is_outwards: bool
        True if the Lamination is not internal and false if not. For yoke notch,
        result is negated.
    """
    if self.parent is not None:
        return self.is_yoke ^ self.parent.is_outwards()
    else:
        raise ParentMissingError("Error: The notch is not inside a Lamination")
