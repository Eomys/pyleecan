# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.MachineUD import MachineUD
from pyleecan.Classes.Lamination import Lamination

# init some laminations and a machine
rotor_0 = Lamination(Rint=0.1, Rext=0.2, is_stator=False)
stator_0 = Lamination(Rint=0.3, Rext=0.4, is_stator=True)
stator_1 = Lamination(Rint=0.5, Rext=0.6, is_stator=True)
rotor_1 = Lamination(Rint=0.7, Rext=0.8, is_stator=False)

machine = MachineUD()
machine.lam_list = [rotor_1, stator_1, rotor_0, stator_0]


@pytest.mark.MachineUD
class Test_get_lam_methods(object):
    """unittest to test the Machine get_lam_xxx methods"""

    def test_get_lam_list(self):
        """Test Machine get_lam_list method"""

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

    def test_get_lam_list_label(self):
        """Test Machine get_lam_list_label method"""
        expected = ["Rotor_0", "Stator_0", "Stator_1", "Rotor_1"]
        actual = machine.get_lam_list_label()

        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual, expected)])

    def test_get_lam_by_label(self):
        """Test Machine get_lam_by_label method"""
        assert machine.get_lam_by_label("Stator") == stator_0
        assert machine.get_lam_by_label("Stator_0") == stator_0
        assert machine.get_lam_by_label("Stator_1") == stator_1

        assert machine.get_lam_by_label("Rotor") == rotor_0
        assert machine.get_lam_by_label("Rotor_0") == rotor_0
        assert machine.get_lam_by_label("Rotor_1") == rotor_1

    def test_get_lam_index(self):
        """Test Machine get_lam_index method"""
        # ref. order [rotor_0, stator_0, stator_1, rotor_1]
        assert machine.get_lam_index("Stator") == 1
        assert machine.get_lam_index("Stator_0") == 1
        assert machine.get_lam_index("Stator_1") == 2

        assert machine.get_lam_index("Rotor") == 0
        assert machine.get_lam_index("Rotor_0") == 0
        assert machine.get_lam_index("Rotor_1") == 3

        assert machine.get_lam_index("rotor") is None  # method is case sensitive
        assert machine.get_lam_index("xyz") is None
        assert machine.get_lam_index("Rotor_") is None  # this is also invalid
