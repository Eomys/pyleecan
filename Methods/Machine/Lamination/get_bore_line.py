# -*- coding: utf-8 -*-
"""@package get_bore_line
@date Created on juin 20 10:56 2018
@author franco_i
"""
from numpy import exp

from pyleecan.Classes.Arc1 import Arc1


def get_bore_line(self, alpha1, alpha2, label=""):
    """

    Parameters
    ----------
    self : Lamination
        a Lamination object
    alpha1 : float
        Startinf angle [rad]
    alpha2 : float
        Ending angle [rad]
    label : str
        the label of the bore line

    Returns
    -------
    bore_line : list
        list of bore line
    
    """
    if alpha1 == alpha2:
        return []
    else:
        Rbo = self.get_Rbo()
        Z1 = Rbo * exp(1j * alpha1)
        Z2 = Rbo * exp(1j * alpha2)
        return [Arc1(begin=Z1, end=Z2, radius=Rbo, label=label)]
