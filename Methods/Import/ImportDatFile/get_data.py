# -*- coding: utf-8 -*-

from pyleecan.Methods.Import.ImportMatlab import MatFileError
from os.path import isfile
import numpy as np


def get_data(self):
    """Return the value from the .mat file

    Parameters
    ----------
    self : ImportMatlab
        An ImportMatlab object

    Returns3
    -------
    value : ?
        Loaded data
    """
    #path_save = join(MAIN_DIR, "Results", "Femm", "Mesh") + '\\'

    if self.file_path[-4:] != ".dat":
        self.file_path += ".dat"
    if not isfile(self.file_path):
        raise MatFileError("ERROR: The dat file doesn't exist " + self.file_path)

    data_dict = np.loadtxt(self.file_path)

    return data_dict
