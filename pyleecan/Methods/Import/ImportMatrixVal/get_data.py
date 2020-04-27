# -*- coding: utf-8 -*-


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
