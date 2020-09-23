import pytest
import sys

from os import makedirs
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.definitions import DATA_DIR
from Tests import save_plot_path
from pyleecan.Functions.GMSH.draw_GMSH import draw_GMSH


@pytest.mark.long
@pytest.mark.GMSH
def test_gmsh_2d():
    """Check generation of the 2D mesh with gmsh"""
    # Import the machine from a script
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    IPMSM_A.stator.slot.H1 = 1e-3
    save_path = join(save_plot_path, "GMSH")
    makedirs(save_path)
    # Plot the machine
    # im = IPMSM_A.plot()

    # Create the Simulation
    mySimu = Simu1(name="EM_SIPMSM_AL_001", machine=IPMSM_A)
    myResults = Output(simu=mySimu)

    mesh_dict = {
        "Lamination_Rotor_Bore_Radius_Ext": 180,
        "surface_line_0": 5,
        "surface_line_1": 10,
        "surface_line_2": 5,
        "surface_line_3": 5,
        "surface_line_4": 10,
        "surface_line_5": 5,
        "Lamination_Stator_Bore_Radius_Int": 10,
        "Lamination_Stator_Yoke_Side": 30,
    }

    draw_GMSH(
        output=myResults,
        sym=2,
        is_lam_only_S=False,
        is_lam_only_R=False,
        user_mesh_dict=mesh_dict,
        path_save=join(save_path, "GSMH_model.msh"),
    )


if __name__ == "__main__":
    sys.exit(test_gmsh_2d())
