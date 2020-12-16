# -*- coding: utf-8 -*-
import pytest

from os.path import join

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path

DELTA = 1e-6


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.Force
def test_AC_IPMSM_AGSF_transfer():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

    # Load machine
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    # Prepare simulation
    simu = Simu1(name="AC_IPMSM_plot", machine=IPMSM_A)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 11, Nt_tot=2 ** 6, N0=1200
    )

    # Configure simulation
    simu.elec = None
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True,)
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True,)

    # Run simulation
    out = simu.run()

    # Test 2 : with transfer
    simu2 = simu.copy()

    simu2.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 11, Nt_tot=2 ** 6, N0=1200
    )

    simu2.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True,)
    simu2.force = ForceMT(
        is_agsf_transfer=True, is_periodicity_a=True, is_periodicity_t=True,
    )

    out2 = simu2.run()

    out2.plot_2D_Data(
        "force.AGSF",
        "angle[oneperiod]",
        "time=0",
        data_list=[out.force.AGSF],
        legend_list=["With Transfer", "No Transfer"],
        save_path=join(save_path, "test_FM_IPMSM_FL_001_AGSF_compare.png"),
        is_show_fig=False,
    )

    max_r = 42
    out2.plot_2D_Data(
        "force.AGSF",
        "wavenumber",
        "time=0",
        x_min=-max_r,
        x_max=+max_r,
        data_list=[out.force.AGSF],
        legend_list=["With Transfer", "No Transfer"],
        save_path=join(save_path, "test_FM_IPMSM_FL_001_AGSF_compare_fft2.png"),
        is_show_fig=False,
        barwidth=600,
    )

    return out, out2


if __name__ == "__main__":

    out, out2 = test_AC_IPMSM_AGSF_transfer()
