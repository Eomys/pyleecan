# -*- coding: utf-8 -*-

from numpy import roll


def shift_wind_mat(wind_mat, Nshift):
    """Shift the Winding Matrix of Nshift number of Slot

    Parameters
    ----------
    wind_mat : numpy.ndarray
        A Winding Matrix (Nlay_r, Nlay_theta, Zs,
        qs) (created by comp_connection_mat)
    Nshift : int
        Number of Slot to shift (Integer 0 < Nshift < Zs)

    Returns
    -------
    shift_wind_mat: numpy.ndarray
        The shifted matrix along the Slot

    """
    assert len(wind_mat.shape) == 4, "wind_mat has a wrong shape (dim 4)"
    assert Nshift % 1 == 0, "Nshift must be an integer"

    return roll(wind_mat, shift=Nshift, axis=2)
