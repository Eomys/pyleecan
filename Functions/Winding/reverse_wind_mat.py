# -*- coding: utf-8 -*-
"""@package Functions.reverse_wind_mat
Reverse a Winding matrix fonction
@date Created on Tue Dec 16 15:12:10 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""


def reverse_wind_mat(wind_mat):
    """reverse a Winding Matrix along the slot

    Parameters
    ----------
    wind_mat : numpy.ndarray
        A Winding Matrix (Nlay_r, Nlay_theta, Zs, qs)
        (created by comp_connection_mat)

    Returns
    -------
    wind_mat: numpy.ndarray
        The reverse matrix along the Slot

    """
    assert len(wind_mat.shape) == 4, "wind_mat has a wrong shape (dim 4)"

    return wind_mat[:, :, ::-1, :]
