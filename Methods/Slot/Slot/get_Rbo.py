"""
Created on 31 mai 2018

@author: pierre_b
"""

from pyleecan.Methods import ParentMissingError


def get_Rbo(self):
    """Return the parent lamination bore radius

    Parameters
    ----------
    self : Slot
        A Slot object

    Returns
    -------
    Rbo: float
        The parent lamination bore radius [m]

    """

    if self.parent is not None:
        return self.parent.get_Rbo()
    else:
        raise ParentMissingError("Error: The slot is not inside a Lamination")
