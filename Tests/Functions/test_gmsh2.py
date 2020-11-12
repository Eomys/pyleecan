import pytest
import sys
import json

from os import makedirs
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.definitions import DATA_DIR
from Tests import save_plot_path

try:
    from pyleecan.Functions.GMSH.draw_GMSH import draw_GMSH
except:
    draw_GMSH = ImportError

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
}


@pytest.mark.long
@pytest.mark.GMSH
def test_gmsh_ipm():
    """Check generation of the 2D mesh with gmsh"""
    if isinstance(draw_GMSH, ImportError):
        raise ImportError("Fail to import draw_GMSH (gmsh package missing)")

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

    gmsh_dict = draw_GMSH(
        output=myResults,
        sym=8,
        is_lam_only_S=False,
        is_lam_only_R=False,
        user_mesh_dict=mesh_dict,
        is_sliding_band=True,
        path_save=join(save_path, "GSMH_model_ipm.msh"),
    )

    with open("gmsh_test_ipm.json", "w") as fw:
        json.dump(gmsh_dict, fw, default=encode_complex, indent=4)



@pytest.mark.long
@pytest.mark.GMSH
def test_gmsh_spm():
    """Check generation of the 2D mesh with gmsh"""
    if isinstance(draw_GMSH, ImportError):
        raise ImportError("Fail to import draw_GMSH (gmsh package missing)")
        
    # Import the machine from a script
    PMSM_A = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))
    save_path = join(save_plot_path, "GMSH")
    makedirs(save_path)
    # Plot the machine
    # im = PMSM_A.plot()

    # Create the Simulation
    mySimu = Simu1(name="EM_SPMSM_AL_001", machine=PMSM_A)
    myResults = Output(simu=mySimu)

    gmsh_dict = draw_GMSH(
        output=myResults,
        sym=4,
        is_lam_only_S=False,
        is_lam_only_R=False,
        user_mesh_dict=mesh_dict,
        is_sliding_band=True,
        path_save=join(save_path, "GSMH_model_spm.msh")
    )

    with open("gmsh_test_spm.json", "w") as fw:
        json.dump(gmsh_dict, fw, default=encode_complex, indent=4)


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)

if __name__ == '__main__':
     sys.exit(test_gmsh_ipm())

