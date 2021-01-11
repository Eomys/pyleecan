# -*- coding: utf-8 -*-

from os import makedirs
from os.path import join, exists

# TODO improve path


def get_path_save_fea(self, output):
    """Return the path to save the FEA simulation

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object

        Returns
    -------
    save_path: str
        Path to save the .fem file

    """
    path_res = output.get_path_result()

    save_dir = join(path_res, "Elmer_Elasticity")
    if not exists(save_dir):
        makedirs(save_dir)

    return save_dir
