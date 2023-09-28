from os.path import join

import pytest

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.FEMM
@pytest.mark.IPMSM
@pytest.mark.MagFEMM
@pytest.mark.SingleOP
@pytest.mark.periodicity
def test_FEMM_clean():
    """test clean of MagFEMM"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_FEMM_clean", machine=Toyota_Prius)

    # Definition of a sinusoidal current
    simu.input = InputCurrent()
    simu.input.OP = OPdq(Id_ref=-100, Iq_ref=200, N0=2000)
    simu.input.Nt_tot = 16  # Number of time step
    simu.input.Na_tot = 1024  # Spatial discretization

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
        is_periodicity_t=True,
        is_get_meshsolution=True,
    )

    out = simu.run()

    # Clean out.mag and out.mag.internal
    out.mag.clean(3)

    return out


if __name__ == "__main__":
    out = test_FEMM_clean()
