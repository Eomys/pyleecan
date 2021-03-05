# -*- coding: utf-8 -*-
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Classes.ForceMT import ForceMT

from Tests import save_plot_path
from os.path import join
from numpy import zeros, ones, pi, array

import matplotlib.pyplot as plt
import json
import numpy as np
import pytest


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_Slotless_CEFC_003():
    """Validation of AGSF calculation on slotless machine.

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

    simu.force = ForceMT()

    out = simu.run()

    # Plot the AGSF as a function of space with the spatial fft
    out.plot_2D_Data(
        "force.AGSF",
        "angle{rad}",
        component_list=["radial"],
        save_path=join(save_plot_path, "test_CEFC_003_plot_force_space.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.AGSF",
        "wavenumber=[0,78]",
        component_list=["radial"],
        save_path=join(save_plot_path, "test_CEFC_003_plot_force_space_fft.png"),
        is_show_fig=False,
    )

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_Slotless_CEFC_003()
