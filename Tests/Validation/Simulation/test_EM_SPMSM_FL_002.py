# -*- coding: utf-8 -*-

# External import
import pytest
from numpy import array, pi
from os.path import join

# Pyleecan import
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
@pytest.mark.MeshSol
def test_Magnetic_FEMM_sym():
    """Validation of a polar SIPMSM with surface magnet
    Linear lamination material

    From publication
    Lubin, S. Mezani, and A. Rezzoug,
    “2-D Exact Analytical Model for Surface-Mounted Permanent-Magnet Motors with Semi-Closed Slots,”
    IEEE Trans. Magn., vol. 47, no. 2, pp. 479–492, 2011.
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """
    SPMSM_003 = load(join(DATA_DIR, "Machine", "SPMSM_003.json"))
    simu = Simu1(name="EM_SPMSM_FL_002", machine=SPMSM_003)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(
        value=array(
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    time = ImportGenVectLin(start=0, stop=0.015, num=4, endpoint=True)
    Na_tot = 1024

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.5216 + pi,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_get_mesh=True,
    )
    simu.force = None
    simu.struct = None
    # Copy the simu and activate the symmetry
    assert SPMSM_003.comp_periodicity() == (1, True, 1, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    out = Output(simu=simu_sym)
    out.post.legend_name = "1/2 symmetry"
    out.post.line_color = "r--"
    simu_sym.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_path, "EM_SPMSM_FL_002_mesh.png"), is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        group_names="stator core",
        save_path=join(save_path, "EM_SPMSM_FL_002_mesh_stator.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_mesh(
        group_names=["stator core", "/", "airgap", "stator winding"],
        save_path=join(save_path, "EM_SPMSM_FL_002_mesh_stator_interface.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_path, "EM_SPMSM_FL_002_mu.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B", save_path=join(save_path, "EM_SPMSM_FL_002_B.png"), is_show_fig=False
    )
    out.mag.meshsolution.plot_contour(
        label="H", save_path=join(save_path, "EM_SPMSM_FL_002_H.png"), is_show_fig=False
    )

    out.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_path, "EM_SPMSM_FL_002_H_stator.png"),
        is_show_fig=False,
    )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_Magnetic_FEMM_sym()
