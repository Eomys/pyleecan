# -*- coding: utf-8 -*-

import sys

from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Methods import ParentMissingError

import pytest


class TestSlot(object):
    """Test that the methods of Slot behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        return SlotW10(H0=0.10, H1=5.3, H2=0.12, W0=0.10, W1=0.14, W2=0.15)

    def test_is_outwards(self, setup):
        """Check that the is_outwards function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.is_outwards()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = setup
        assert test_obj.slot.is_outwards() == False
        setup.check()

    def test_get_is_stator(self, setup):
        """Check that the get_is_stator function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.get_is_stator()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = setup
        assert test_obj.slot.get_is_stator() == True

    def test_get_Rbo(self, setup):
        """Check that the get_rbo function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.get_Rbo()

        test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        test_obj.slot = setup
        assert test_obj.slot.get_Rbo() == 0.2
