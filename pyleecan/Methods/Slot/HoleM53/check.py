# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the HoleM53 object is correct

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    None

    Raises
    -------
    S53_Rbo0CheckError
        You must have H0 < Rbo
    S53_Rbo1CheckError
        You must have H1 < Rbo
    S53_W4CheckError
        You must have W4 < pi/2
    S53_W5CheckError
        You must have W5 >=0
    """

    Rbo = self.get_Rbo()

    if Rbo <= self.H0:
        raise S53_Rbo0CheckError("You must have H0 < Rbo")

    if Rbo <= self.H1:
        raise S53_Rbo1CheckError("You must have H1 < Rbo")

    if pi / 2 <= self.W4:
        raise S53_W4CheckError("You must have W4 < pi/2")

    if self.comp_W5() < 0:
        raise S53_W5CheckError("You must have W5 >=0")


class S53_Rbo0CheckError(SlotCheckError):
    """ """

    pass


class S53_Rbo1CheckError(SlotCheckError):
    """ """

    pass


class S53_W4CheckError(SlotCheckError):
    """ """

    pass


class S53_W5CheckError(SlotCheckError):
    """ """

    pass
