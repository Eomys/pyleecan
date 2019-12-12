# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:33:52 2017

@author: pierre_b
"""


def set_m2(self, value):
    """Convert the value the correct m² unit (to set in the object in m²)

    Parameters
    ----------
    self : Unit
        A Unit object
    value : float
        Value to convert

    Returns
    -------
    value : float
        value converted in [m²]
    """
    if self.unit_m2 == 1:  # Convert to mm²
        return value / 1000000
    else:
        return value
