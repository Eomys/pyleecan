# -*- coding: utf-8 -*-

from ....Classes.CondType21 import CondType21
from ....Classes.LamSquirrelCage import LamSquirrelCage


def check(self):
    """Check that the Lamination object is correct

    Parameters
    ----------
    self : LamSquirrelCageMag
        A LamSquirrelCageMag object

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

    LamSquirrelCage.check(self)

    # Check p
    p = self.winding.p
    assert len(self.hole) > 1
    for hole in self.hole:
        assert hole.Zh / 2 == p
