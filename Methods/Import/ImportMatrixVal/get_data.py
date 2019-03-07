# -*- coding: utf-8 -*-
"""
@date Created on Fri Feb 22 12:55:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def get_data(self):
    """Return the object's matrix

    Parameters
    ----------
    self : ImportMatrixVal
        An ImportMatrixVal object

    Returns
    -------
    matrix: ndarray
        The object's matrix

    """

    return self.edit_matrix(self.value)
