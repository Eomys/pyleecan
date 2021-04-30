# -*- coding: utf-8 -*-

import sys

from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Methods import ParentMissingError

import pytest


class TestNotch(object):
    """Test that the methods of Notch behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""
        slot_r = SlotW10(Zs=6, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        return NotchEvenDist(notch_shape=slot_r, alpha=0)

    def test_is_outwards(self, setup):
        """Check that the is_outwards function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.is_outwards()

        test_obj = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.notch = [setup]
        assert test_obj.slot.is_outwards() == False

    def test_get_Rbo(self, setup):
        """Check that the get_rbo function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.get_Rbo()

        test_obj = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.95,
            Nrvd=1,
            Wrvd=0.05,
        )
        test_obj.notch = [setup]
        assert test_obj.notch[0].get_Rbo() == 0.5
