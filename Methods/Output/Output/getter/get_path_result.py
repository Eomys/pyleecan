# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath


def get_path_result(self):
    """Return the path to the result folder

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    res_path: str
        path to the result folder
    """

    if self.path_res in [None, ""]:
        # If the path doesn't exist, set the default one
        self.path_res = abspath(
            join(dirname(__file__), "..", "..", "..", "..", "Results")
        )
    return self.path_res
