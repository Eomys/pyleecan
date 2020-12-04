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

    if self.path_name:
        path_name = self.path_name
    elif output.simu.machine.name:
        path_name = output.simu.machine.name + "_Model"
    elif output.simu.name:
        path_name = output.simu.name + "_Model"
    else:  # Default name
        path_name = "FEA_Model.fem"

    save_dir = join(path_res, "StructElmer", path_name)
    if not exists(save_dir):
        makedirs(save_dir)

    return save_dir
