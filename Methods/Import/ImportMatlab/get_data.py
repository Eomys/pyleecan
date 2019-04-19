# -*- coding: utf-8 -*-

from scipy.io import loadmat
from pyleecan.Methods.Import.ImportMatlab import MatFileError
from os.path import isfile


def get_data(self):
    """Return the value from the .mat file

    Parameters
    ----------
    self : ImportMatlab
        An ImportMatlab object

    Returns
    -------
    value : ?
        Loaded data
    """

    if self.file_path[-4:] != ".mat":
        self.file_path += ".mat"
    if not isfile(self.file_path):
        raise MatFileError("ERROR: The mat file doesn't exist " + self.file_path)

    data_dict = loadmat(self.file_path)
    if self.var_name not in data_dict:
        raise MatFileError(
            "ERROR: The variable "
            + self.var_name
            + " is not available in the file "
            + self.file_path
        )

    return data_dict[self.var_name]
