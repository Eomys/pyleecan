# -*- coding: utf-8 -*-
from numpy import zeros


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


def reverse_layer(wind_mat):
    """reverse the Winding Matrix along the layer

    Parameters
    ----------
    wind_mat : numpy.ndarray
        A Winding Matrix (Nlay_r, Nlay_theta, Zs, qs)
        (created by comp_connection_mat)

    Returns
    -------
    wind_mat: numpy.ndarray
        The reverse matrix along the layer

    """
    assert len(wind_mat.shape) == 4, "wind_mat has a wrong shape (dim 4)"

    wind_mat = wind_mat[:, ::-1, :, :]
    wind_mat = wind_mat[::-1, :, :, :]

    return wind_mat


def change_layer(wind_mat):
    """Change the Winding Matrix along the layer

    Parameters
    ----------
    wind_mat : numpy.ndarray
        A Winding Matrix (Nlay_r, Nlay_theta, Zs, qs)
        (created by comp_connection_mat)

    Returns
    -------
    wind_mat: numpy.ndarray
        The winding matrix with changed layers

    """
    wind_shape = wind_mat.shape
    assert len(wind_shape) == 4, "wind_mat has a wrong shape (dim 4)"

    if wind_shape[0] == 1 and wind_shape[1] != 1:
        wind_mat2 = zeros((wind_shape[1], wind_shape[0], wind_shape[2], wind_shape[3]))
        wind_mat2[:, 0, :, :] = wind_mat[0, :, :, :]
        return wind_mat2
    elif wind_shape[0] != 1 and wind_shape[1] == 1:
        wind_mat2 = zeros((wind_shape[1], wind_shape[0], wind_shape[2], wind_shape[3]))
        wind_mat2[0, :, :, :] = wind_mat[:, 0, :, :]
        return wind_mat2
    else:
        return wind_mat
