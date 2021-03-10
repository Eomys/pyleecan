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
def test_Slotless_CEFC_002():
    """Validation of extracting FEMM data with MeshSolution.

    Electrical machine is an academic slotless machine inspired
    from [R. Pile et al., Application Limits of the Airgap Maxwell
    Tensor, CEFC, 2018] but with interior magnet such as Toyota
    Prius machine.

    """
    Slotless_CEFC = load(join(DATA_DIR, "Machine", "Slotless_CEFC.json"))
    simu = Simu1(name="EM_Slotless_CEFC_002_save_mag", machine=Slotless_CEFC)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=2, N0=1200
    )

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, "CEFC_002_mesh_save.png"), is_show_fig=False
    )

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, "CEFC_002_mesh_interface_save.png"),
        group_names=["stator core", "/", "airgap"],
        is_show_fig=False,
    )

    out.mag.meshsolution.plot_contour(
        label="\mu",
        save_path=join(save_plot_path, "CEFC_002_mu_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, "CEFC_002_B_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        save_path=join(save_plot_path, "CEFC_002_H_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_plot_path, "CEFC_002_H_stator_save.png"),
        is_show_fig=False,
    )
    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator core", "airgap"],
        save_path=join(save_plot_path, "CEFC_002_mu_stator_airgap_save.png"),
        is_show_fig=False,
    )

    # Test save with MeshSolution object in out
    load_path = join(save_load_path, "Slotless_CEFC_002.h5")

    out.save(save_path=load_path)

    # Test to load the Meshsolution object (inside the output):
    FEMM = load(join(save_load_path, "Slotless_CEFC_002.h5"))

    # TODO : out.compare(FEMM)

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(
        save_path=join(save_plot_path, "CEFC_002_mesh_load.png"), is_show_fig=False
    )

    FEMM.mag.meshsolution.plot_mesh(
        group_names=["stator core", "/", "airgap"],
        save_path=join(save_plot_path, "CEFC_002_interface_mesh_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator core", "airgap"],
        save_path=join(save_plot_path, "CEFC_002_mu_stator_airgap_load.png"),
        is_show_fig=False,
    )
    FEMM.mag.meshsolution.plot_contour(
        label="B",
        save_path=join(save_plot_path, "CEFC_002_B_load.png"),
        is_show_fig=False,
    )
    FEMM.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator core",
        save_path=join(save_plot_path, "CEFC_002_H_stator_load.png"),
        is_show_fig=False,
    )

    FEMM.mag.meshsolution.plot_contour(
        label="H",
        group_names=["stator core", "airgap"],
        is_show_fig=False,
        save_path=join(save_plot_path, "CEFC_002_H_stator_airgap_load.png"),
    )


# To run it without pytest
if __name__ == "__main__":

    out = test_Slotless_CEFC_002()
