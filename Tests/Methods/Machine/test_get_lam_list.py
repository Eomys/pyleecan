# -*- coding: utf-8 -*-
import pytest

from pyleecan.Functions.load import load
from pyleecan.Classes.MachineUD import MachineUD
from pyleecan.Classes.Lamination import Lamination


@pytest.mark.METHODS
@pytest.mark.DEV
class Test_get_lam_list(object):
    """unittest to test Machine get_lam_list method"""

    def test_get_lam_list(self):
        """Test Machine get_lam_list method"""
        # setup laminations
        rotor_0 = Lamination(Rint=0.1, Rext=0.2, is_stator=False)
        stator_0 = Lamination(Rint=0.3, Rext=0.4, is_stator=True)
        stator_1 = Lamination(Rint=0.5, Rext=0.6, is_stator=True)
        rotor_1 = Lamination(Rint=0.7, Rext=0.8, is_stator=False)

        # setup machine
        machine = MachineUD()
        machine.lam_list = [rotor_1, stator_1, rotor_0, stator_0]

        # test expected and actual sorted full list
        expected = [rotor_0, stator_0, stator_1, rotor_1]
        actual = machine.get_lam_list()

        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual, expected)])

        # test expected and actual sorted stator list
        expected = [stator_0, stator_1]
        actual = machine.get_lam_list(key="Stator")

        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual, expected)])

        # test expected and actual sorted rotor list
        expected = [rotor_0, rotor_1]
        actual = machine.get_lam_list(key="Rotor")

        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual, expected)])
