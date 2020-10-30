# -*- coding: utf-8 -*-

import sys

from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Methods import ParentMissingError

import pytest


@pytest.mark.METHODS
class TestHole(object):
    """Test that the methods of Hole behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        return HoleM50(
            Zh=8,
            W0=50e-3,
            W1=2e-3,
            W2=1e-3,
            W3=1e-3,
            W4=20.6e-3,
            H0=17.3e-3,
            H1=1.25e-3,
            H2=0.5e-3,
            H3=6.8e-3,
        )

    def test_get_is_stator(self, setup):
        """Check that the get_is_stator function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.get_is_stator()

        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = [setup]
        assert test_obj.hole[0].get_is_stator() == True

    def test_get_Rbo(self, setup):
        """Check that the get_rbo function can raise an error"""

        with pytest.raises(ParentMissingError) as context:
            setup.get_Rbo()

        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = [setup]
        assert test_obj.hole[0].get_Rbo() == 0.075
