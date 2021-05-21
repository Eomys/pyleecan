# -*- coding: utf-8 -*-

import sys

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.SlotW22 import SlotW22

import pytest


class TestLamSlotWind(object):
    """Test that the methods of LamSlotWind behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        return LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )

    def test_get_name_phase(self, setup):
        """Check that the get_name_phase function can raise an error"""
        setup.winding = None

        assert setup.get_name_phase() == []

        setup.winding = Winding(Npcp=10, Ntcoil=11)

        assert setup.get_name_phase() == ["A", "B", "C"]

    # def test_comp_output_geo(self, setup):
    #     """Check that the comp_output_geo function can raise an error"""
    #     setup.slot = None
    #     result = setup.comp_output_geo()
    #     assert result.S_slot == 0
    #     assert result.S_slot_wind == 0                TODO

    #     setup.slot = SlotW22(H0=0.001, H2=0.01, W0=0.1, W2=0.2)

    #     assert setup.comp_output_geo().S_slot == 0
    #     assert setup.comp_output_geo().S_slot_wind == 0
