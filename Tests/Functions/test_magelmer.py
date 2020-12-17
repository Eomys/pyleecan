from os import makedirs
from os.path import join
import pytest
import sys
from shutil import copyfile

import matplotlib.pyplot as plt
from numpy import array, linspace, ones, pi, zeros


from Tests import save_plot_path

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagElmer import MagElmer
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output


from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal


from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

# Gather results in the same folder
save_path = join(save_plot_path, "Elmer")
makedirs(save_path)


mesh_dict = {
    "Lamination_Rotor_Bore_Radius_Ext": 180,
    "surface_line_0": 5,
    "surface_line_1": 10,
    "surface_line_2": 5,
    "surface_line_3": 5,
    "surface_line_4": 10,
    "surface_line_5": 5,
    "Lamination_Stator_Bore_Radius_Int": 10,
    "Lamination_Stator_Yoke_Side_Right": 30,
    "Lamination_Stator_Yoke_Side_Left": 30,
    "int_airgap_arc": 120,
    "int_sb_arc": 120,
    "ext_airgap_arc": 120,
    "ext_sb_arc": 120,
    "airbox_line_1": 10,
    "airbox_line_2": 10,
    "airbox_arc": 20,
}


@pytest.mark.MagElmer
@pytest.mark.long
def test_Elmer():

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    IPMSM_A.stator.slot.H1 = 1e-3
    simu = Simu1(name="elmer", machine=IPMSM_A)
    simu.machine.name = "fig_Elmer_sym"

    # Definition of the enforced output of the electrical module
    N0 = 1500
    Is = ImportMatrixVal(value=array([[20, -10, -10],[20, -10, -10],[20, -10, -10]]))
    Ir = ImportMatrixVal(value=zeros((1, 28)))
    Nt_tot = 3
    Na_tot = 4096
    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.2244,
    )

    # Definition of the magnetic simulation
    # 2 sym + antiperiodicity = 1/4 Lamination
    simu.mag = MagElmer(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
        FEA_dict=mesh_dict,
        is_get_mesh=True,
    )
    # Stop after magnetic computation
    simu.force = None
    simu.struct = None
    # Run simulation
    out = Output(simu=simu)
    simu.run()
    out.mag.meshsolution.plot_mesh(label="magnetic flux density e")
    return out

    # FEMM files (mesh and results) are available in Results folder
    # copyfile(
    #     join(out.path_result, "Femm", "fig_09_FEMM_sym_model.ans"),
    #     join(save_path, "fig_09_FEMM_sym_model.ans"),
    # )
    # copyfile(
    #     join(out.path_result, "Femm", "fig_09_FEMM_sym_model.fem"),
    #     join(save_path, "fig_09_FEMM_sym_model.fem"),
    # )


if __name__ == "__main__":
    out = test_Elmer()
