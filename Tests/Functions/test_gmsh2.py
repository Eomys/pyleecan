import pytest
import sys
import json

from os import makedirs
from os.path import join, isdir
from pyleecan.Functions.load import load
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.definitions import DATA_DIR
from Tests import save_plot_path
from pyleecan.Methods.Simulation.MagElmer import (
    MagElmer_BP_dict,
)

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
    "airbox_line_1": 10,
    "airbox_line_2": 10,
    "airbox_arc": 20,
}


@pytest.mark.long_5s
@pytest.mark.GMSH
@pytest.mark.IPMSM
@pytest.mark.SingleOP
def test_gmsh_ipm():
    """Check generation of the 2D mesh with gmsh"""
    if isinstance(draw_GMSH, ImportError):
        raise ImportError("Fail to import draw_GMSH (gmsh package missing)")

    # Import the machine from a script
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Toyota_Prius.stator.slot.H1 = 1e-3
    save_path = join(save_plot_path, "GMSH")
    if not isdir(save_path):
        makedirs(save_path)
    # Plot the machine
    # im = Toyota_Prius.plot()

    # Create the Simulation
    mySimu = Simu1(name="test_gmsh_ipm", machine=Toyota_Prius)
    myResults = Output(simu=mySimu)

    gmsh_dict = draw_GMSH(
        output=myResults,
        sym=8,
        boundary_prop=MagElmer_BP_dict,
        is_lam_only_S=False,
        is_lam_only_R=False,
        user_mesh_dict=mesh_dict,
        is_sliding_band=True,
        is_airbox=True,
        path_save=join(save_path, "GSMH_model_ipm.msh"),
    )

    with open("test_gmsh_ipm.json", "w") as fw:
        json.dump(gmsh_dict, fw, default=encode_complex, indent=4)

    return gmsh_dict


@pytest.mark.long_5s
@pytest.mark.GMSH
@pytest.mark.SPMSM
@pytest.mark.SingleOP
def test_gmsh_spm():
    """Check generation of the 2D mesh with gmsh"""
    if isinstance(draw_GMSH, ImportError):
        raise ImportError("Fail to import draw_GMSH (gmsh package missing)")

    # Import the machine from a script
    PMSM_A = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))
    PMSM_A.rotor.slot = SlotM10(W1=15e-3, H1=3e-3, H0=0.0, W0=15e-3, Zs=8)

    # PMSM_A.plot()
    save_path = join(save_plot_path, "GMSH")
    if not isdir(save_path):
        makedirs(save_path)

    # Create the Simulation
    mySimu = Simu1(name="test_gmsh_spm", machine=PMSM_A)
    myResults = Output(simu=mySimu)
    mesh_dict["Lamination_Rotor_Bore_Radius_Ext"] = 20

    gmsh_dict = draw_GMSH(
        output=myResults,
        sym=4,
        boundary_prop=MagElmer_BP_dict,
        is_lam_only_S=False,
        is_lam_only_R=False,
        user_mesh_dict=mesh_dict,
        is_sliding_band=True,
        is_airbox=True,
        path_save=join(save_path, "GSMH_model_spm.msh"),
    )

    with open("test_gmsh_spm.json", "w") as fw:
        json.dump(gmsh_dict, fw, default=encode_complex, indent=4)

    return gmsh_dict


@pytest.mark.long_5s
@pytest.mark.GMSH
# @pytest.mark.SPMSM
@pytest.mark.SingleOP
def test_gmsh_benchmark():
    """Check generation of the 2D mesh with gmsh"""
    if isinstance(draw_GMSH, ImportError):
        raise ImportError("Fail to import draw_GMSH (gmsh package missing)")

    # Import the machine from a script
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    # Benchmark.stator.slot.H1 = 1e-3
    save_path = join(save_plot_path, "GMSH")
    if not isdir(save_path):
        makedirs(save_path)
    # Plot the machine
    # im = Toyota_Prius.plot()

    # Create the Simulation
    mySimu = Simu1(name="test_gmsh_benchmark", machine=Benchmark)
    myResults = Output(simu=mySimu)

    gmsh_dict = draw_GMSH(
        output=myResults,
        sym=1,
        boundary_prop=MagElmer_BP_dict,
        is_lam_only_S=False,
        is_lam_only_R=False,
        user_mesh_dict=mesh_dict,
        is_sliding_band=True,
        is_airbox=True,
        path_save=join(save_path, "GSMH_model_benchmark.geo"),
    )

    with open("test_gmsh_ipm.json", "w") as fw:
        json.dump(gmsh_dict, fw, default=encode_complex, indent=4)

    return gmsh_dict


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)


if __name__ == "__main__":
    # gmsh_dict = test_gmsh_ipm()
    # gmsh_dict = test_gmsh_spm()
    gmsh_dict = test_gmsh_benchmark()
