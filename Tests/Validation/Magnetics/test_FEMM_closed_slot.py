import pytest
from os.path import join
from pyleecan.Classes.OPdq import OPdq

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.IPMSM
@pytest.mark.SingleOP
def test_FEMM_closed_slot():
    """Test to compute the Flux in FEMM with closed slots and make sure that the simulation is running."""

    # Loading the Toyota Prius then closing its slots
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    M400 = load(join(DATA_DIR, "Material", "M400-50A.json"))
    Toyota_Prius.stator.slot.wedge_mat = M400
    simu = Simu1(name="test_FEMM_closed_slot", machine=Toyota_Prius)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2**6,
        Nt_tot=1,
    )

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_closed_slot()
