# -*- coding: utf-8 -*-

from ....Methods.Slot.SlotW30 import S30_W0Error
from ....Methods.Slot.SlotW30 import S30_W3Error
from ....Methods.Slot.SlotW30 import S30_R1Error
from ....Methods.Slot.SlotW30 import S30_R2Error


def check(self):
    """Check that the SlotW30 object is correct

    Parameters
    ----------
    self : SlotW30
        A SlotW30 object

    Returns
    -------
    None

    Raises
    -------
    S30_W0Error
        wrong definition of W0
    S30_W3Error
        wrong definition of W3
    S30_R1Error
        wrong definition of R1
    S30_R2Error
        wrong definition of R2
    """
    Rbo = self.get_Rbo()

    if self.W0 == 0:
        raise S30_W0Error("You must have W0 > 0")

    if self.W0 * 0.5 / Rbo >= 1:
        raise S30_W0Error("You must have W0/2 < Rbo")

    if self.is_outwards():
        R1 = Rbo + self.H0 + self.R1
    else:
        R1 = Rbo - self.H0 - self.R1

    if self.W3 * 0.5 / R1 >= 1:
        raise S30_W3Error(
            "W3 is too high comparing to the lamination bore radius (Rbo)"
        )

    if self.H1 < self.R1 + self.R2:
        raise S30_R1Error("You must have R1 + R2 < H1")

    R1 = self.R1
    R2 = self.R2

    self.R1 = 0
    self.R2 = 0
    point_dict = self._comp_point_coordinate()
    self.R1 = R1
    self.R2 = R2

    Z60 = point_dict["Z60"]
    Z80 = point_dict["Z80"]
    Z40 = point_dict["Z40"]
    Z100 = point_dict["Z100"]

    lr2 = abs(Z80 - Z60)
    lr1 = abs(Z100 - Z40) - self.W0

    if R2 >= lr2 / 2:
        raise S30_R2Error("R2 is too high")

    if R1 >= lr1 / 2:
        if self.R1 != 0:
            raise S30_R1Error("R1 is too high")
        else:
            raise S30_W3Error("W3 is too high")
