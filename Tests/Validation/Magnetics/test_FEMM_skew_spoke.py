from os.path import join

import pytest

from numpy import lcm, pi

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Skew import Skew
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR

is_show_fig = False


@pytest.mark.skip
def test_FEMM_SIPMSM_spoke_skew():

    SIPMSM_spoke_skew = load(join(DATA_DIR, "Machine", "PR0185_machine_ok.json"))

    name = "test_FEMM_SIPMSM_spoke_skew"

    simu = Simu1(name=name, machine=SIPMSM_spoke_skew)

    simu.input = InputCurrent(
        N0=1200,
        Id_ref=0,
        Iq_ref=0,
        Tem_av_ref=0,
        Na_tot=400 * 4,
        Nt_tot=40 * 4,
    )

    # Definition of the magnetic simulation (direct calculation with permeance mmf)
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)

    # Run simulation
    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_FEMM_SIPMSM_spoke_skew()
