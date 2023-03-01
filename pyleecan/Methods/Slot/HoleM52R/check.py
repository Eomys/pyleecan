# -*- coding: utf-8 -*-
from numpy import pi, sqrt, angle

from ....Methods.Slot.Slot import SlotCheckError
from ....Methods.Slot.HoleM52R import *


def check(self):
    """Check that the HoleM52 object is correct

    Parameters
    ----------
    self : HoleM52R
        A HoleM52R object

    Returns
    -------
    None

    Raises
    -------
    S52R_H12CheckError
        You must have H2 < H1
    S52R_alphaCheckError
        The teeth are too wide for the lamination (reduce W3 or H0)
    S52R_W1CheckError
        W1 is <=0, you must reduce W0 or W3
    """

    # Check that everything is set
    if self.W0 is None:
        raise S52R_NoneError("You must set W0 !")
    elif self.W1 is None:
        raise S52R_NoneError("You must set W1 !")
    elif self.H0 is None:
        raise S52R_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S52R_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S52R_NoneError("You must set H2 !")
    elif self.R0 is None:
        raise S52R_NoneError("You must set R0 !")

    if self.H2 >= self.H1:
        raise S52R_H12CheckError("You must have H2 < H1")

    if self.R0 >= self.H1:
        raise S52R_R0CheckError("You must have R0 < H1")

    if self.R0 >= self.H1 - self.H2:
        raise S52R_R0CheckError("You must have R0 < H1")

    h = self.H1 - self.H2
    w = self.W0 + self.W1
    Z2 = sqrt((self.get_Rext() - self.H0) ** 2 - h ** 2) - h + 1j * w / 2

    if angle(Z2) >= pi / self.Zh:
        raise S52R_widthCheckError(
            "The hole is too wide for the lamination (reduce W1, H0 or W0)"
        )
