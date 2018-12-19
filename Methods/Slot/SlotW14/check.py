# -*- coding: utf-8 -*-
"""@package

@date Created on Fri Mar 31 12:19:16 2017
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author: pierre_b
@todo unittest it
"""

from pyleecan.Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the SlotW14 object is correct

    Parameters
    ----------
    self : SlotW14
        A SlotW14 object

    Returns
    -------
    None

    Raises
    -------
    S14_Rbo0CheckError
        You must have W0/2 < Rbo
    S14_Rbo1CheckError
        W3 is too high comparing to the lamination bore radius (Rbo)
    """

    Rbo = self.get_Rbo()

    if self.W0 * 0.5 / Rbo >= 1:
        raise S14_Rbo0CheckError("You must have W0/2 < Rbo")

    if self.is_outwards():
        R1 = Rbo + self.H0 + self.H1
    else:
        R1 = Rbo - self.H0 - self.H1

    if self.W3 * 0.5 / R1 >= 1:
        raise S14_Rbo1CheckError(
            "W3 is too high comparing to the lamination bore radius (Rbo)"
        )


class S14_Rbo0CheckError(SlotCheckError):
    """ """

    pass


class S14_Rbo1CheckError(SlotCheckError):
    """ """

    pass
