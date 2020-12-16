# -*- coding: utf-8 -*-

import os
from os.path import join, isdir


def get_path_save_fea(self, output):
    """Return the path to save the Elmer simulation

    Parameters
    ----------
    self : MagElmer
        a MagElmer object
    output : Output
        an Output object

        Returns
    -------
    save_path: str
        Path to save the .fem file

    """
    save_dir = self.get_path_save(output)

    # if self.file_name not in [None, ""]:
    #     if self.file_name[-4:] != ".fem":
    #         file_name = self.file_name + ".fem"
    #     else:
    #         file_name = self.file_name
    # elif output.simu.machine.name not in [None, ""]:
    #     file_name = output.simu.machine.name + "_model.fem"
    # elif output.simu.name not in [None, ""]:
    #     file_name = output.simu.name + "_model.fem"
    # else:  # Default name
    #     file_name = "FEMM_simulation.fem"
    file_name = "ELMER_simulation"

    return join(save_dir, file_name)
