# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the HoleM54 object is correct

    Parameters
    ----------
    self : HoleM54
        A HoleM54 object

    Returns
    -------
    None

    Raises
    -------
    H54_W0CheckError
        You must have W0 < 2*pi/Zh
    H54_R1CheckError
        You must have H0 < R1
    """

    if 2 * pi / self.Zh <= self.W0:
        raise H54_W0CheckError("You must have W0 < 2*pi/Zh")

    if self.R1 <= self.H0:
        raise H54_R1CheckError("You must have H0 < R1")


class H54_W0CheckError(SlotCheckError):
    """ """

    pass


class H54_R1CheckError(SlotCheckError):
    """ """

    pass
