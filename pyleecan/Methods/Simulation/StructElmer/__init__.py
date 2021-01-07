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

# --- some constants ---

boundary_list = [
    "MASTER_ROTOR_BOUNDARY",
    "SLAVE_ROTOR_BOUNDARY",
    "SB_ROTOR_BOUNDARY",
    "MASTER_STATOR_BOUNDARY",
    "SLAVE_STATOR_BOUNDARY",
    "SB_STATOR_BOUNDARY",
    "AIRGAP_ARC_BOUNDARY",
    "VP0_BOUNDARY",
    "ROTOR_BORE_CURVE",
]

# dictionary to match FEA boundary conditions (dict values)
# with line labels (dict keys) that are set in the build_geometry methods
boundary_prop = dict()
boundary_prop["int_airgap_line_1"] = "MASTER_ROTOR_BOUNDARY"
boundary_prop["int_airgap_line_2"] = "SLAVE_ROTOR_BOUNDARY"
boundary_prop["int_sb_line_1"] = "MASTER_ROTOR_BOUNDARY"
boundary_prop["int_sb_line_2"] = "SLAVE_ROTOR_BOUNDARY"
boundary_prop["Lamination_Rotor_Yoke_Side_Right"] = "MASTER_ROTOR_BOUNDARY"
boundary_prop["Lamination_Rotor_Yoke_Side_Left"] = "SLAVE_ROTOR_BOUNDARY"
boundary_prop["Shaft_Side_Right"] = "MASTER_ROTOR_BOUNDARY"
boundary_prop["Shaft_Side_Left"] = "SLAVE_ROTOR_BOUNDARY"
boundary_prop["int_sb_arc"] = "SB_ROTOR_BOUNDARY"
boundary_prop["ext_airgap_line_1"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["ext_airgap_line_2"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["ext_sb_line_1"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["ext_sb_line_2"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["airbox_line_1"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["airbox_line_2"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["Lamination_Stator_Yoke_Side_Right"] = "MASTER_STATOR_BOUNDARY"
boundary_prop["Lamination_Stator_Yoke_Side_Left"] = "SLAVE_STATOR_BOUNDARY"
boundary_prop["ext_sb_arc"] = "SB_STATOR_BOUNDARY"
boundary_prop["ext_airgap_arc_copy"] = "AIRGAP_ARC_BOUNDARY"
boundary_prop["airbox_arc"] = "VP0_BOUNDARY"
boundary_prop["Lamination_Rotor_Bore_Radius_Ext"] = "ROTOR_BORE_CURVE"

# dict for the translation of the actual surface labels into Elmer compatible labels,
# i.e. max. 30 characters; key: actual label, value: Elmer label
surface_label = dict()
surface_label["Shaft"] = "SHAFT"
surface_label["Lamination_Rotor_Bore_Radius_Ext"] = "ROTOR_LAM"
surface_label["Lamination_Stator_Bore_Radius_Int"] = "STATOR_LAM"
surface_label["Airgap_int"] = "AG_INT"
surface_label["SlidingBand_int"] = "SB_INT"
surface_label["SlidingBand_ext"] = "SB_EXT"
surface_label["Airgap_ext"] = "AG_EXT"
surface_label["Airbox"] = "AIRBOX"

# TODO: use actual surface labels
for rr in range(0, 20):
    for tt in range(0, 20):
        for ss in range(0, 100):
            old_label = f"Hole_Rotor_R{rr}_T{tt}_S{ss}"
            new_label = f"H_ROTOR_R{rr}T{tt}S{ss}"
            surface_label[old_label] = new_label
            old_label = f"HoleMagnet_Rotor_Parallel_N_R{rr}_T{tt}_S{ss}"
            new_label = f"H_MAGNET_ROT_PAR_N_R{rr}T{tt}S{ss}"
            surface_label[old_label] = new_label
            old_label = f"HoleMagnet_Rotor_Parallel_S_R{rr}_T{tt}_S{ss}"
            new_label = f"H_MAGNET_ROT_PAR_S_R{rr}T{tt}S{ss}"
            surface_label[old_label] = new_label
            old_label = f"HoleMagnet_Rotor_Radial_N_R{rr}_T{tt}_S{ss}"
            new_label = f"H_MAGNET_ROT_RAD_N_R{rr}T{tt}S{ss}"
            surface_label[old_label] = new_label
            old_label = f"HoleMagnet_Rotor_Radial_S_R{rr}_T{tt}_S{ss}"
            new_label = f"H_MAGNET_ROT_RAD_S_R{rr}T{tt}S{ss}"
            surface_label[old_label] = new_label
            old_label = f"Wind_Stator_R{rr}_T{tt}_S{ss}"
            new_label = f"W_STA_R{rr}_T{tt}_S{ss}"
            surface_label[old_label] = new_label
