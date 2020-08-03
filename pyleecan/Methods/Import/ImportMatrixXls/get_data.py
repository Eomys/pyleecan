# -*- coding: utf-8 -*-
from pandas import read_excel
from ....Methods.Import.ImportMatrixXls import XlsFileError
from os.path import isfile

from ....Functions.path_tools import abs_file_path


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
    file_path = abs_file_path(self.file_path, is_check=False)
    if not isfile(file_path):
        raise XlsFileError("ERROR: The xls file doesn't exist " + self.file_path)
    if self.usecols == "":
        self.usecols = None
    df = read_excel(
        file_path, self.sheet, header=None, usecols=self.usecols, skiprows=self.skiprows
    )
    return self.edit_matrix(df.values)
