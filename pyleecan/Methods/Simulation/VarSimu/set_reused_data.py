# -*- coding: utf-8 -*-

from ....Classes.MagFEMM import MagFEMM


def set_reused_data(self, simu, output):
    """Resuse some data from the reference simulation to skip computation

    Parameters
    ----------
    self : VarSimu
        a VarSimu object
    simu : Simulation
        The simulation to update
    output : Output
        Output from the reference simulation to enforce
    """

    if self.is_reuse_femm_file and isinstance(simu.mag, MagFEMM):
        simu.mag.import_file = output.mag.FEMM_dict["path_save"]
        simu.mag.FEMM_dict = output.mag.FEMM_dict
