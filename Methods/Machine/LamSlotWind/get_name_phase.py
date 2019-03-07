# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 14:52:32 2019
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""
from pyleecan.Functions.Winding.gen_phase_list import gen_name


def get_name_phase(self):
    """Return the name of the winding phases

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object

    Returns
    -------
    name_phase: list
        List with the phase names

    """

    return gen_name(self.winding.qs)
