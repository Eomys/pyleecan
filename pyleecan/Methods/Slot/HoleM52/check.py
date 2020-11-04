# -*- coding: utf-8 -*-

from ....Methods.Slot.Slot.check import SlotCheckError


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

    # Check that everything is set
    if self.W0 is None:
        raise S52_NoneError("You must set W0 !")
    elif self.W3 is None:
        raise S52_NoneError("You must set W3 !")
    elif self.H0 is None:
        raise S52_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S52_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S52_NoneError("You must set H2 !")

    if self.H2 >= self.H1:
        print("You must have H2 < H1")
        raise S52_H12CheckError("You must have H2 < H1")

    alpha = self.comp_alpha()
    if alpha <= 0:
        print("The teeth are too wide for the lamination (reduce W3 or H0)")
        raise S52_alphaCheckError(
            "The teeth are too wide for the lamination (reduce W3 or H0)"
        )

    W1 = self.comp_W1()
    if W1 <= 0:
        print("W1 is <=0, you must reduce W0 or W3")
        raise S52_W1CheckError("W1 is <=0, you must reduce W0 or W3")


class S52_NoneError(SlotCheckError):
    """Raised when a propery of HoleM52 is None"""

    pass


class S52_H12CheckError(SlotCheckError):
    """ """

    pass


class S52_alphaCheckError(SlotCheckError):
    """ """

    pass


class S52_W1CheckError(SlotCheckError):
    """ """

    pass
