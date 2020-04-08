# -*- coding: utf-8 -*-

from numpy import arcsin, pi

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW28 object is correct

    Parameters
    ----------
    self : SlotW28
        A SlotW28 object

    Returns
    -------
    None

    Raises
    -------
    S28_RboW0CheckError
        You must have W0/2 < Rbo
    S28_R1W3CheckError
        W3 is too high comparing to the lamination bore radius (Rbo)
    S28_ZsCheckError
        There are too many slots to match W3 and R1
    """

    Rbo = self.get_Rbo()

    #    if self.R1 * 2 <= self.W0:
    #        raise S28_WCheckError("You must have W0 < 2*R1")

    if self.W0 * 0.5 / Rbo >= 1:
        raise S28_RboW0CheckError("You must have W0/2 < Rbo")

    if self.is_outwards():
        R1 = Rbo + self.H0 + self.R1
    else:
        R1 = Rbo - self.H0

    if self.W3 * 0.5 / R1 >= 1:
        raise S28_R1W3CheckError(
            "W3 is too high comparing to the lamination bore radius (Rbo)"
        )

    if self.R1 / R1 >= 1:
        raise S28_R1R1CheckError(
            "R1 is too high comparing to the lamination bore radius (Rbo)"
        )

    alpha = 2 * arcsin((2 * self.R1 + self.W3) * 0.5 / R1)

    if alpha > 2 * pi / self.Zs:
        raise S28_ZsCheckError("There are too many slots to match W3 and R1")


class S28_WCheckError(SlotCheckError):
    """ """

    pass


class S28_RboW0CheckError(SlotCheckError):
    """ """

    pass


class S28_R1W3CheckError(SlotCheckError):
    """ """

    pass


class S28_R1R1CheckError(SlotCheckError):
    """ """

    pass


class S28_ZsCheckError(SlotCheckError):
    """ """

    pass
