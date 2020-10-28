from numpy import zeros, ones, pi, array

from pyleecan.Classes.Simu1 import Simu1
from Tests.Validation.Simulation.CEFC_Lam import CEFC_Lam

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
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
def test_CEFC_003_t0(CEFC_Lam):
    """Validation of magnetic air-gap surface force calculation based on Maxwell Tensor with an academic slotless machine.

    from publication

    """

    simu = Simu1(name="FM_CEFC_003_MT", machine=CEFC_Lam, struct=None)

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
        rot_dir=-1,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_get_mesh=True,
        is_save_FEA=True,
        is_sliding_band=False,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.force = ForceMT()

    out = Output(simu=simu)
    out.post.legend_name = "Slotless lamination"
    simu.run()

    # Plot the AGSF as a function of space with the spatial fft
    out.plot_2D_Data(
        "mag.B",
        "angle{rad}",
        component_list=["radial"],
        save_path=join(save_path, "test_CEFC_003_plot_force_space.png"),
    )
    out.plot_2D_Data(
        "mag.B",
        "wavenumber=[0,78]",
        component_list=["radial"],
        save_path=join(save_path, "test_CEFC_003_plot_force_space_fft.png"),
    )

    # ------------------------------------------------------
