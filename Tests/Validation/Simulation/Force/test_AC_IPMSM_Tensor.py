# -*- coding: utf-8 -*-
import pytest

from os.path import join
from numpy import zeros, exp, pi, real, meshgrid, mean

from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path

DELTA = 1e-6




@pytest.mark.validation
@pytest.mark.Force
@pytest.mark.long
def test_AC_IPMSM_AGSF_Tensor():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

        # Load machine
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    # Prepare simulation
    simu = Simu1(name="AC_IPMSM_plot", machine=IPMSM_A)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=2, N0=1200
    )

    simu.elec = None

    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )
    simu.force = ForceMT(
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    # Run simulation
    out = simu.run()

    out.plot_2D_Data(
        "force.AGSF",
        "wavenumber",
        "freqs=160",
        save_path=join(save_path, simu.name + "_AGSF_space_fft_freq160_no_sym.png"),
        is_show_fig=False,
    )

    return out


if __name__ == "__main__":

    out = test_AC_IPMSM_AGSF_Tensor()

