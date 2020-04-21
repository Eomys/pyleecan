# -*- coding: utf-8 -*-

from numpy import transpose


def edit_matrix(self, matrix):
    """To apply transformation on the matrix

    Parameters
    ----------
    self : ImportMatrix
        An ImportMatrix object
    matrix: ndarray
        The matrix to edit

    Returns
    -------
    matrix: ndarray
        The edited matrix

    """

    if self.is_transpose:
        return transpose(matrix)
    return matrix
