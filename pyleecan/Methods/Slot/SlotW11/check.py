# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.SlotW11 import *


def check(self):
    """Check that the SlotW11 object is correct

    Parameters
    ----------
    self : SlotW11
        A SlotW11 object

    Returns
    -------
    None

    Raises
    -------
    S11_W01CheckError
        You must have W0 <= W1
    S11_RWCheckError
        You must have 2*R1 <= W2
    S11_RHCheckError
        You must have R1 <= H2
    S11_H1rCheckError
        With H1 in radian, you must have H1 < pi/2

    """

    # if lam.slot.W0 is None:
    #     return "You must set W0 !"
    # elif lam.slot.H0 is None:
    #     return "You must set H0 !"
    # elif lam.slot.H1 is None:
    #     return "You must set H1 !"
    # elif lam.slot.H2 is None:
    #     return "You must set H2 !"
    # elif lam.slot.R1 is None:
    #     return "You must set R1 !"
    # elif self.is_cst_tooth.isChecked() and self.slot.W3 is None:
    #     return translate("In constant tooth mode, you must set W3 !")
    # elif (not self.is_cst_tooth.isChecked()) and self.slot.W1 is None:
    #     return translate("In constant slot mode, you must set W1 !")
    # elif (not self.is_cst_tooth.isChecked()) and self.slot.W2 is None:
    #     return translate("In constant slot mode, you must set W2 !")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S11_H1rCheckError("With H1 in radian, you must have H1 < pi/2")

    if self.W1 < self.W0:
        raise S11_W01CheckError("You must have W0 <= W1")

    if 2 * self.R1 > self.W2:
        raise S11_RWCheckError("You must have 2*R1 <= W2")

    if self.R1 > self.H2:
        raise S11_RHCheckError("You must have R1 <= H2")

    if self.H1_is_rad and self.H1 >= pi / 2:
        raise S11_H1rCheckError("With H1 in radian, you must have H1 < pi/2")
