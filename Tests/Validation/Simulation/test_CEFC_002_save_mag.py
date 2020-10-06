from numpy import zeros, ones, pi, array

from pyleecan.Classes.Simu1 import Simu1
from Tests.Validation.Simulation.CEFC_Lam import CEFC_Lam

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from Tests import save_validation_path as save_path
from os.path import join

import matplotlib.pyplot as plt
import json
import numpy as np
from pyleecan.Functions.FEMM import GROUP_SC
import pytest


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
@pytest.mark.MeshSol
def test_CEFC_002(CEFC_Lam):
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    """

    simu = Simu1(name="SM_CEFC_002_save_mag", machine=CEFC_Lam, struct=None)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[2.25353053e02, 2.25353053e02, 2.25353053e02]]))
    Nt_tot = 1
    Na_tot = 1024

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_get_mesh=True,
        is_periodicity_a=False,
        is_save_FEA=False,
        is_sliding_band=True,
    )
    simu.force = None
    simu.struct = None

    out = Output(simu=simu)
    out.post.legend_name = "Slotless lamination"
    simu.run()

    # Test save with MeshSolution object in out
    load_path = join(save_path, "Output.json")
    out.save(save_path=load_path)

    out.mag.meshsolution.plot_mesh(save_path=join(save_path, "CEFC_002_mesh_save.png"))

    out.mag.meshsolution.plot_mesh(
        save_path=join(save_path, "CEFC_002_mesh_interface_save.png"),
        group_names=["stator", "/", "airgap"],
    )

    out.mag.meshsolution.plot_contour(
        label="\mu", save_path=join(save_path, "CEFC_002_mu_save.png")
    )
    out.mag.meshsolution.plot_contour(
        label="B", save_path=join(save_path, "CEFC_002_B_save.png")
    )
    out.mag.meshsolution.plot_contour(
        label="H", save_path=join(save_path, "CEFC_002_H_save.png")
    )
    out.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator",
        save_path=join(save_path, "CEFC_002_H_stator_save.png"),
    )
    out.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator", "airgap"],
        save_path=join(save_path, "CEFC_002_mu_stator_airgap_save.png"),
    )


@pytest.mark.skip
def test_CEFC_002_load():
    load_path = join(save_path, "Output.json")
    # Test to load the Meshsolution object (inside the output):
    with open(load_path) as json_file:
        json_tmp = json.load(json_file)
        FEMM = Output(init_dict=json_tmp)

    # [Important] To test that fields are still working after saving and loading
    FEMM.mag.meshsolution.plot_mesh(save_path=join(save_path, "CEFC_002_mesh_load.png"))

    FEMM.mag.meshsolution.plot_mesh(group_names=["stator", "/", "airgap"])

    FEMM.mag.meshsolution.plot_contour(
        label="\mu",
        group_names=["stator", "airgap"],
        save_path=join(save_path, "CEFC_002_mu_stator_airgap_load.png"),
    )
    FEMM.mag.meshsolution.plot_contour(
        label="B", save_path=join(save_path, "CEFC_002_B_load.png")
    )
    FEMM.mag.meshsolution.plot_contour(
        label="H",
        group_names="stator",
        save_path=join(save_path, "CEFC_002_H_stator_load.png"),
    )

    FEMM.mag.meshsolution.plot_contour(label="H", group_names=["stator", "airgap"])
