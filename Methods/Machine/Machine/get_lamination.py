# -*- coding: utf-8 -*-
"""@package get_lamination
@date Created on aout 17 10:01 2018
@author franco_i
"""


def get_lamination(self, is_internal):
    """Returns internal Lamination of the machine

    Parameters
    ----------
    self : Machine
        Machine object
    is_internal : bool
        true if The lamination returned is internal

    Returns
    -------
        lam : Lamination
            the internal Lamination

    """
    if self.rotor.is_internal == is_internal:
        return self.rotor
    else:
        return self.stator
