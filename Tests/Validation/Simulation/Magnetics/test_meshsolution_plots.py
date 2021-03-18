from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output

from Tests import save_plot_path
from Tests import save_load_path
from os.path import join
from numpy import zeros, ones, pi, array

import matplotlib.pyplot as plt
import json
import numpy as np
import pytest


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
@pytest.mark.MeshSol
def test_Slotless_CEFC():
    """Validation of extracting FEMM data with MeshSolution.

    Electrical machine is an academic slotless machine inspired
    from [R. Pile et al., Application Limits of the Airgap Maxwell
    Tensor, CEFC, 2018] but with interior magnet such as Toyota
    Prius machine.

    """
    Slotless_CEFC = load(join(DATA_DIR, "Machine", "Slotless_CEFC.json"))
    simu = Simu1(name="test_Slotless_CEFC", machine=Slotless_CEFC)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=1, N0=1200
    )

    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_save.png"), is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        group_names=["stator core", "airgap"],
        save_path=join(save_plot_path, simu.name + "_mesh_stator_airgap_save.png"),
        is_show_fig=False,
    )

    test_meshsol = out.mag.meshsolution.get_group(["stator core", "airgap"])
    test_meshsol.plot_mesh(
        group_names=["stator core"],
        save_path=join(save_plot_path, simu.name + "_mesh_stator_bis_save.png"),
        is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_interface_save.png"),
        group_names=["stator core", "/", "airgap"],
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_plot_path, simu.name + "_stator_save.png"),
        is_show_fig=False,
    )

    test_meshsol.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_plot_path, simu.name + "_H_stator_bis_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator core", "airgap"],
        save_path=join(save_plot_path, simu.name + "_mu_stator_airgap_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["rotor core", "rotor magnets"],
        save_path=join(save_plot_path, simu.name + "_mu_rotor_save.png"),
        is_show_fig=False,
    )

    # Test save with MeshSolution object in out
    load_path = join(save_load_path, simu.name + ".h5")

    out.save(save_path=load_path)

    # Test to load the Meshsolution object (inside the output):
    FEMM = load(load_path)

    # TODO : out.compare(FEMM)

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_load.png"), is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["rotor core", "rotor magnets"],
        save_path=join(save_plot_path, simu.name + "_mu_rotor_load.png"),
        is_show_fig=False,
    )

@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
@pytest.mark.MeshSol
def test_Toyota_Prius():
    """Validation of extracting FEMM data with MeshSolution with Toyota Prius electrical machine.

    """
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    simu = Simu1(name="test_Toyota_Prius", machine=IPMSM_A)
    
    # Definition of the enforced output of the electrical module
    N0 = 2504
    Is_mat = zeros((1, 3))
    Is_mat[0, :] = array([0, 12.2474, -12.2474])
    Is = ImportMatrixVal(value=Is_mat)
    Nt_tot = 1
    Na_tot = 2048

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.86,
    )

    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_save.png"), is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        group_names=["stator core", "airgap"],
        save_path=join(save_plot_path, simu.name + "_mesh_stator_airgap_save.png"),
        is_show_fig=False,
    )

    test_meshsol = out.mag.meshsolution.get_group(["stator core", "airgap"])
    test_meshsol.plot_mesh(
        group_names=["stator core"],
        save_path=join(save_plot_path, simu.name + "_mesh_stator_bis_save.png"),
        is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_interface_save.png"),
        group_names=["stator core", "/", "airgap"],
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_plot_path, simu.name + "_mu_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_plot_path, simu.name + "_H_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_plot_path, simu.name + "_stator_save.png"),
        is_show_fig=False,
    )

    test_meshsol.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_plot_path, simu.name + "_H_stator_bis_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator core", "airgap"],
        save_path=join(save_plot_path, simu.name + "_mu_stator_airgap_save.png"),
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["rotor core", "rotor magnets"],
        save_path=join(save_plot_path, simu.name + "_mu_rotor_save.png"),
        is_show_fig=False,
    )

    # Test save with MeshSolution object in out
    load_path = join(save_load_path, simu.name + ".h5")

    out.save(save_path=load_path)

    # Test to load the Meshsolution object (inside the output):
    FEMM = load(load_path)

    # TODO : out.compare(FEMM)

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, simu.name + "_mesh_load.png"), is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, simu.name + "_B_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["rotor core", "rotor magnets"],
        save_path=join(save_plot_path, simu.name + "_mu_rotor_load.png"),
        is_show_fig=False,
    )


# To run it without pytest
if __name__ == "__main__":

    #out = test_Slotless_CEFC()
    out = test_Toyota_Prius()
