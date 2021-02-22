import sys

sys.path.append("C:/Users/Utilisateur/OneDrive/Documents/Github/pyleecan")

from numpy import zeros, ones, pi, array

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from Tests import save_load_path as save_path
from os.path import join

import matplotlib.pyplot as plt
import json
import numpy as np
import pytest


@pytest.mark.skip
@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
@pytest.mark.MeshSol
def test_Slotless_CEFC_002():
    """Validation of magnetic air-gap surface force calculation based on Maxwell Tensor with an academic slotless machine.

    from publication

    """
    Slotless_CEFC = load(join(DATA_DIR, "Machine", "Slotless_CEFC.json"))
    simu = Simu1(name="SM_CEFC_002_save_mag", machine=Slotless_CEFC)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=2, N0=1200
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_path, "CEFC_002_mesh_save.png"), is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_path, "CEFC_002_mesh_interface_save.png"),
        group_names=["stator core", "/", "airgap"],
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_path, "CEFC_002_mu_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B", save_path=join(save_path, "CEFC_002_B_save.png"), is_show_fig=False
    )
    out.mag.meshsolution.plot_contour(
        label="H", save_path=join(save_path, "CEFC_002_H_save.png"), is_show_fig=False
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_path, "CEFC_002_H_stator_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator core", "airgap"],
        save_path=join(save_path, "CEFC_002_mu_stator_airgap_save.png"),
        is_show_fig=False,
    )

    # Test save with MeshSolution object in out
    load_path = join(save_path, "Slotless_CEFC_002.h5")

    out.save(save_path=load_path)


@pytest.mark.skip
def test_Slotless_CEFC_002_load():

    # Test to load the Meshsolution object (inside the output):
    FEMM = load(join(save_path, "Slotless_CEFC_002.h5"))

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(
        save_path=join(save_path, "CEFC_002_mesh_load.png"), is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_mesh(
        group_names=["stator core", "/", "airgap"], is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator core", "airgap"],
        save_path=join(save_path, "CEFC_002_mu_stator_airgap_load.png"),
        is_show_fig=False,
    )
    FEMM.mag.meshsolution.plot_contour(
        label="B", save_path=join(save_path, "CEFC_002_B_load.png"), is_show_fig=False
    )
    FEMM.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_path, "CEFC_002_H_stator_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.plot_contour(
        label="H", group_names=["stator core", "airgap"], is_show_fig=False
    )


# To run it without pytest
if __name__ == "__main__":

    out = test_Slotless_CEFC_002()
    test_Slotless_CEFC_002_load()
