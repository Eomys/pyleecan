# -*- coding: utf-8 -*-

from numpy import vstack, column_stack
from ....Methods.Import.ImportGenMatrixSin import (
    GenSinEmptyError,
    GenSinDimError,
    GenSinTransposeError,
)


def get_data(self):
    """Generate the sinus matrix

    Parameters
    ----------
    self : ImportGenMatrixSin
        An ImportGenMatrixSin object

    Returns
    -------
    matrix: ndarray
        The generated sinus matrix

    """

    if len(self.sin_list) == 0:
        raise GenSinEmptyError("ERROR: The sinus list is empty")

    N = self.sin_list[0].N
    is_T = self.sin_list[0].is_transpose

    for ii in range(1, len(self.sin_list)):
        if self.sin_list[ii].N != N:
            raise GenSinDimError(
                "ERROR: Dimension mismatch between ImportGenVectSin 0 (N="
                + str(N)
                + ") and ImportGenVectSin "
                + str(ii)
                + " (N="
                + str(self.sin_list[ii].N)
                + ")"
            )
        if self.sin_list[ii].is_transpose != is_T:
            raise GenSinTransposeError(
                "ERROR: is_transpose mismatch between ImportGenVectSin 0 ("
                + str(is_T)
                + ") and ImportGenVectSin "
                + str(ii)
                + " ("
                + str(self.sin_list[ii].is_transpose)
                + ")"
            )
    if is_T:  # Conctenate the columns
        matrix = column_stack([sin_obj.get_data() for sin_obj in self.sin_list])
    else:  # Concatenate the lines
        matrix = vstack([sin_obj.get_data() for sin_obj in self.sin_list])
    return self.edit_matrix(matrix)
