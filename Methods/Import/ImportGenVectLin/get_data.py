# -*- coding: utf-8 -*-
"""
@date Created on Thu Mar 07 12:56:30 2019
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import linspace


def get_data(self):
    """Generate the linspace vector

    Parameters
    ----------
    self : ImportGenVectLin
        An ImportGenVectLin object

    Returns
    -------
    vect: ndarray
        The generated linspace vector

    """

    vect = linspace(
        start=self.start, stop=self.stop, num=self.num, endpoint=self.endpoint
    )

    return self.edit_matrix(vect)
