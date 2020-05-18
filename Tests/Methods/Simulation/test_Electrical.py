# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.CondType12 import CondType12
from Tests.Validation.Material.Copper1 import Copper1


def test_resistance():
    """Check that resistance computation is correct
    """
    # Stator from Tests/Validation/Machine/IPMSM_A
    stator = LamSlotWind(
        Rint=80.95e-3,
        Rext=134.62e-3,
        Nrvd=0,
        L1=0.08382,
        Kf1=0.95,
        is_internal=False,
        is_stator=True,
    )
    stator.slot = SlotW11(
        Zs=48, H0=1e-3, H1=0, H2=0.0333, W0=0.00193, W1=0.005, W2=0.008, R1=0.004
    )
    stator.winding = WindingDW1L(
        qs=3,
        Lewout=0.019366,
        p=4,
        Ntcoil=9,
        Npcpp=1,
        Nslot_shift_wind=2,
        is_reverse_wind=True,
    )
    stator.winding.conductor = CondType12(Nwppc=13, Wwire=0.000912, Wins_wire=1e-6)
    stator.winding.conductor.cond_mat = Copper1

    # Compute and check
    result = stator.comp_resistance_wind()
    assert result == pytest.approx(0.035951, abs=0.00001)
