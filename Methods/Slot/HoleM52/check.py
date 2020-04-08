# -*- coding: utf-8 -*-

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the HoleM52 object is correct

    Parameters
    ----------
    self : HoleM52
        A HoleM52 object

    Returns
    -------
    None

    Raises
    -------
    S52_H12CheckError
        You must have H2 < H1
    S52_alphaCheckError
        The teeth are too wide for the lamination (reduce W3 or H0)
    S52_W1CheckError
        W1 is <=0, you must reduce W0 or W3
    """

    if self.H2 >= self.H1:
        raise S52_H12CheckError("You must have H2 < H1")

    alpha = self.comp_alpha()
    if alpha <= 0:
        raise S52_alphaCheckError(
            "The teeth are too wide for the lamination (reduce W3 or H0)"
        )

    W1 = self.comp_W1()
    if W1 <= 0:
        raise S52_W1CheckError("W1 is <=0, you must reduce W0 or W3")


class S52_H12CheckError(SlotCheckError):
    """ """

    pass


class S52_alphaCheckError(SlotCheckError):
    """ """

    pass


class S52_W1CheckError(SlotCheckError):
    """ """

    pass
