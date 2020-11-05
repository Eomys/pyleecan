# -*- coding: utf-8 -*-

from os.path import join, abspath, isdir
from os import makedirs
from .....definitions import RESULT_DIR


def get_path_result(self):
    """Return the path to the result folder. If there is a name for the simulation, the path leads to a sub-folder of
    'Results' folder which has the same name. If this sub-folder does not exist, it creates it.

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    res_path: str
        path to the result folder
    """

    if self.path_result in [None, ""]:
        if self.simu.path_result is not None:
            self.path_result = self.simu.path_result.replace("\\", "/")
        else:
            # If the path doesn't exist, set the default one
            self.path_result = abspath(join(RESULT_DIR, self.simu.name))
        if not isdir(self.path_result):
            makedirs(self.path_result)  # Make sure that the folder exist
    return self.path_result
