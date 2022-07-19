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
def test_FEMM_slotless():
    """Test to compute the Flux in FEMM without slots and without sliding band.

    Electrical machine is an academic slotless machine inspired
    from [R. Pile et al., Application Limits of the Airgap Maxwell
    Tensor, CEFC, 2018] but with interior magnet such as Toyota
    Prius machine.
    """

    Slotless_CEFC = load(join(DATA_DIR, "Machine", "Slotless_CEFC.json"))
    simu = Simu1(name="test_FEMM_slotless", machine=Slotless_CEFC)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2 ** 6,
        Nt_tot=1,
    )

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
    )

    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_FEMM_slotless()
