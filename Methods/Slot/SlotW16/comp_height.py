"""
Created on 23 avr. 2018

@author: pierre_b
"""


def comp_height(self):
    """Compute the height of the Slot.
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW16
        A SlotW16 object

    Returns
    -------
    Htot: float
        Height of the slot [m]

    """

    return self.H0 + self.H2
