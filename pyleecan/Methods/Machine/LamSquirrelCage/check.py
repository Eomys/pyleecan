# -*- coding: utf-8 -*-

from ....Classes.CondType21 import CondType21
from ....Classes.LamSlotWind import LamSlotWind
from ....Methods.Machine.LamSquirrelCage import *


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self : LamSquirrelCage
        A LamSquirrelCage object

    Returns
    -------
    None

    Raises
    _______
    SCC_NotARotor
        A LamSquirrelCage Lamination can't be a stator
    SCC_WrongCond
        A LamSquirrelCage's conductor must be a type 2_1
    """

    LamSlotWind.check(self)

    if self.is_stator:
        raise SCC_NotARotor("A LamSquirrelCage Lamination can't be " "a stator")

    if not isinstance(self.winding.conductor, CondType21):
        raise SCC_WrongCond("A LamSquirrelCage's conductor must be " "a type 2_1")
