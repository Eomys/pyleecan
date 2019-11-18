# -*- coding: utf-8 -*-

import os
from os.path import join, isdir


def get_path_save(self, output):
    """Return the path to save the FEMM simulation

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object

        Returns
    -------
    save_path: str
        Path to save the FEMM simulation

    """
    path_res = output.get_path_result()

    save_dir = join(path_res, "Femm")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    return save_dir
