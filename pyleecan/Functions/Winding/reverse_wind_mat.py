# -*- coding: utf-8 -*-


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

    wind_mat = wind_mat[:, :, ::-1, :]
    if wind_mat.shape[1] == 2:
        wind_mat = wind_mat[:, ::-1, :, :]

    return wind_mat
