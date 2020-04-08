# -*- coding: utf-8 -*-

from ....Methods.Machine.Lamination.check import LaminationCheckError
from numpy import pi


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object

    Returns
    -------
    None
    """

    super(type(self), self).check()

    # Check all the slots
    for slot in self.slot_list:
        slot.check()

    #
    if len(self.alpha.shape) > 1:
        raise LamSlotMultiAlphaError("Alpha should have be a vector (1D array)")
    if len(self.alpha) != len(self.slot_list):
        raise LamSlotMultiAlphaError("Alpha should have the same length as slot_list")
    if self.alpha[0] < 0:
        raise LamSlotMultiAlphaError(
            "Alpha should be an ordered array with values between 0 and 2*pi"
        )
    for ii in range(len(self.alpha) - 1):
        if self.alpha[ii] > self.alpha[ii + 1]:
            raise LamSlotMultiAlphaError(
                "Alpha should be an ordered array with values between 0 and 2*pi"
            )
    if self.alpha[-1] > 2 * pi:
        raise LamSlotMultiAlphaError(
            "Alpha should be an ordered array with values between 0 and 2*pi"
        )


class LamSlotMultiAlphaError(LaminationCheckError):
    """ """

    pass
