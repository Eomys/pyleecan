# -*- coding: utf-8 -*-

from os.path import join, isdir
from os import mkdir


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
    if not isdir(save_dir):
        mkdir(save_dir)
    if self.file_name not in [None, ""]:
        if file_name[-4:] != ".fem":
            file_name = file_name + ".fem"
        else:
            file_name = file_name
    elif output.simu.machine.name not in [None, ""]:
        file_name = output.simu.machine.name + "_model.fem"
    elif output.simu.name not in [None, ""]:
        file_name = output.simu.name + "_model.fem"
    else:  # Default name
        file_name = "FEMM_simulation.fem"

    return join(save_dir, file_name)
