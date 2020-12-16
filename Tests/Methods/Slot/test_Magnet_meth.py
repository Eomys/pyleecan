# -*- coding: utf-8 -*-

import sys

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMFlat import SlotMFlat
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Methods import ParentMissingError

import pytest


@pytest.mark.METHODS
class TestNotch(object):
    """Test that the methods of Notch behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""
        return MagnetType10(Hmag=5e-3, Wmag=10e-3)

    def test_is_outwards(self, setup):
        """Check that the is_outwards function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.is_outwards()

        lam = LamSlotMag(is_internal=True, Rext=0.1325)
        lam.slot = SlotMFlat(H0=5e-3, W0=10e-3, Zs=12)
        lam.slot.magnet = [setup]
        assert lam.slot.magnet[0].is_outwards() == False
