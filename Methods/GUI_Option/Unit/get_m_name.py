# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:34:01 2017

@author: pierre_b
"""


def get_m_name(self):
    """Return the name of the length unit ([m] by default)

    Parameters
    ----------
    self : Unit
        A Unit object

    Returns
    -------
    unit_name: str
        Name of the current unit
    """
    if self.unit_m == 1:
        return "mm"
    else:
        return "m"
