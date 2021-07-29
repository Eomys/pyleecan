# -*- coding: utf-8 -*-
from os.path import join
import subprocess

from ....Functions.get_path_binary import get_path_binary


class ElmerProcessError(Exception):
    """Raised when there is an Elmer Binary process error"""

    pass


def _execute(binary_name, cwd, logger, parameter=None):
    """Function to execute Elmer Binaries in the current working directory 'cwd'"""
    # Elmer must be installed and in the PATH
    binary = get_path_binary(binary_name)

    cmd = ['"' + binary + '"']
    logger.info(f"Calling {binary_name}: " + " ".join(map(str, cmd)))

    if parameter:
        cmd.extend(parameter)

    popen = subprocess.Popen(
        " ".join(cmd),
        stdout=subprocess.PIPE,
        universal_newlines=True,
        shell=True,
        cwd=cwd,
    )

    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise ElmerProcessError(
            f"Elmer Process Error while executing {' '.join(cmd)}: Return Code [{return_code}]"
        )


# dictionary to match StructElmer FEA boundary conditions (dict values)
# with pyleecan line boundary properties (dict keys)
# that are set in the build_geometry methods
StructElmer_BP_dict = dict()
StructElmer_BP_dict["int_airgap_line_1"] = "MASTER_ROTOR_BOUNDARY"
StructElmer_BP_dict["int_airgap_line_2"] = "SLAVE_ROTOR_BOUNDARY"
StructElmer_BP_dict["int_sb_line_1"] = "MASTER_ROTOR_BOUNDARY"
StructElmer_BP_dict["int_sb_line_2"] = "SLAVE_ROTOR_BOUNDARY"
StructElmer_BP_dict["Lamination_Rotor_Yoke_Side_Right"] = "MASTER_ROTOR_BOUNDARY"
StructElmer_BP_dict["Lamination_Rotor_Yoke_Side_Left"] = "SLAVE_ROTOR_BOUNDARY"
StructElmer_BP_dict["Shaft_Side_Right"] = "MASTER_ROTOR_BOUNDARY"
StructElmer_BP_dict["Shaft_Side_Left"] = "SLAVE_ROTOR_BOUNDARY"
StructElmer_BP_dict["int_sb_arc"] = "SB_ROTOR_BOUNDARY"
StructElmer_BP_dict["ext_airgap_line_1"] = "MASTER_STATOR_BOUNDARY"
StructElmer_BP_dict["ext_airgap_line_2"] = "SLAVE_STATOR_BOUNDARY"
StructElmer_BP_dict["ext_sb_line_1"] = "MASTER_STATOR_BOUNDARY"
StructElmer_BP_dict["ext_sb_line_2"] = "SLAVE_STATOR_BOUNDARY"
StructElmer_BP_dict["airbox_line_1"] = "MASTER_STATOR_BOUNDARY"
StructElmer_BP_dict["airbox_line_2"] = "SLAVE_STATOR_BOUNDARY"
StructElmer_BP_dict["Lamination_Stator_Yoke_Side_Right"] = "MASTER_STATOR_BOUNDARY"
StructElmer_BP_dict["Lamination_Stator_Yoke_Side_Left"] = "SLAVE_STATOR_BOUNDARY"
StructElmer_BP_dict["ext_sb_arc"] = "SB_STATOR_BOUNDARY"
StructElmer_BP_dict["ext_airgap_arc_copy"] = "AIRGAP_ARC_BOUNDARY"
StructElmer_BP_dict["airbox_arc"] = "VP0_BOUNDARY"
StructElmer_BP_dict["Lamination_Rotor_Bore_Radius_Ext"] = "ROTOR_BORE_CURVE"

# List of all StructElmer Boundary conditions
StructElmer_BP_list = list(set(StructElmer_BP_dict.values()))