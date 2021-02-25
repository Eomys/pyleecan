# -*- coding: utf-8 -*-

from ....Classes.MagFEMM import MagFEMM


def set_reused_data(self, simu, output, is_log=True, simu_type="VarSimu"):
    """Resuse some data from the reference simulation to skip computation

    Parameters
    ----------
    self : VarSimu
        a VarSimu object
    simu : Simulation
        The simulation to update
    output : Output
        Output from the reference simulation to enforce
    is_log : bool
        True to log the changes
    simu_type : str
        Name of the multi-simulation kind
    """

    if simu.layer == 2:
        TAB = "    "
    else:
        TAB = ""

    if self.is_reuse_femm_file and isinstance(simu.mag, MagFEMM):
        if is_log:
            self.get_logger().info(
                TAB
                + simu_type
                + ": Using same FEMM file for all simulation ("
                + output.mag.internal.FEMM_dict["path_save"]
                + ")"
            )
        simu.mag.import_file = output.mag.internal.FEMM_dict["path_save"]
        simu.mag.FEMM_dict_enforced = output.mag.internal.FEMM_dict
