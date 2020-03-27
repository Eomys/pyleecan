# -*- coding: utf-8 -*-
"""
@date Created on Fri Feb 22 12:55:30 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""
from pandas import read_excel
from pyleecan.Methods.Import.ImportMatrixXls import XlsFileError
from os.path import isfile

from pyleecan.Functions.path_tools import abs_file_path


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
    df = read_excel(
        file_path, self.sheet, header=None, usecols=self.usecols, skiprows=self.skiprows
    )
    return self.edit_matrix(df.values)
