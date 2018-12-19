# -*- coding: utf-8 -*-
"""@package Methods.Machine.Conductor.check
Check that the Conductor is correct
@date Created on Thu Jan 22 17:50:02 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Methods.Machine.LamSlotWind.check import Lam_WindCheckError


def check(self):
    """Check that the Conductor object is correct

    Parameters
    ----------
    self : Conductor
        A Conductor object

    Returns
    -------
    None
    """
    pass


class CondCheckError(Lam_WindCheckError):
    """ """

    pass
