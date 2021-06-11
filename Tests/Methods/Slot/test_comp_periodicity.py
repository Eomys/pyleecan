from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Winding import Winding

import pytest


"""pytest for comp_periodicity"""


@pytest.mark.periodicity
def test_comp_periodicity():
    rotor = LamSlotWind(
        Rint=0.2,
        Rext=0.5,
        is_internal=True,
        is_stator=False,
        L1=0.95,
        Nrvd=1,
        Wrvd=0.05,
    )
    rotor.winding = None
    assert rotor.comp_periodicity() == (1, False, 1, False)
