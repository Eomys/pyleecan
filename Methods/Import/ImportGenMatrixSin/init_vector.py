# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 12:57:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from pyleecan.Classes.ImportGenVectSin import ImportGenVectSin
from pyleecan.Methods.Import.ImportGenMatrixSin import InitSinMatDimError


def init_vector(self, f, A, Phi, N, Tf):
    """Create the sin_list according to the input list

    Parameters
    ----------
    self : ImportGenMatrixSin
        An ImportGenMatrixSin object
    f: list
        list of frequency for the sinus
    A: list
        list of amplitude for the sinus
    Phi: list
        list of phase for the sinus
    N: int
        Number of point (same for all the sinus)
    Tf: float
        End time (same for all the sinus)
    """

    if len(f) != len(A):
        raise InitSinMatDimError("ERROR: f and A have different dimensions")
    if len(f) != len(Phi):
        raise InitSinMatDimError("ERROR: f and Phi have different dimensions")

    self.sin_list = list()
    for ii in range(len(f)):
        self.sin_list.append(
            ImportGenVectSin(f=f[ii], A=A[ii], Phi=Phi[ii], N=N, Tf=Tf)
        )
