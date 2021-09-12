# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineUD import MachineUD
from pyleecan.Classes.LamSlotWind import LamSlotWind

# init some laminations and a machine
rotor_0 = LamSlotWind(Rint=0.1, Rext=0.2, is_stator=False)
stator_0 = LamSlotWind(Rint=0.3, Rext=0.4, is_stator=True)
stator_1 = LamSlotWind(Rint=0.5, Rext=0.6, is_stator=True)
rotor_1 = LamSlotWind(Rint=0.7, Rext=0.8, is_stator=False)

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
        expected = ["Rotor-0", "Stator-0", "Stator-1", "Rotor-1"]
        actual = machine.get_lam_list_label()

        assert len(actual) == len(expected)
        assert all([a == b for a, b in zip(actual, expected)])

    def test_get_lam_by_label(self):
        """Test Machine get_lam_by_label method"""
        assert machine.get_lam_by_label("Stator") == stator_0
        assert machine.get_lam_by_label("Stator-0") == stator_0
        assert machine.get_lam_by_label("Stator-1") == stator_1

        assert machine.get_lam_by_label("Rotor") == rotor_0
        assert machine.get_lam_by_label("Rotor-0") == rotor_0
        assert machine.get_lam_by_label("Rotor-1") == rotor_1

    def test_get_lam_index(self):
        """Test Machine get_lam_index method"""
        # ref. order [rotor_0, stator_0, stator_1, rotor_1]
        assert machine.get_lam_index("Stator") == 1
        assert machine.get_lam_index("Stator-0") == 1
        assert machine.get_lam_index("Stator-1") == 2

        assert machine.get_lam_index("Rotor") == 0
        assert machine.get_lam_index("Rotor-0") == 0
        assert machine.get_lam_index("Rotor-1") == 3

        assert machine.get_lam_index("rotor") is None  # method is case sensitive
        assert machine.get_lam_index("xyz") is None
        assert machine.get_lam_index("Rotor_") is None  # this is also invalid

    def test_get_pole_pair(self):
        """Check that the pole pair is check and returned"""
        mach = MachineSCIM()
        mach.rotor.winding.p = 2
        mach.rotor.is_stator = False
        mach.stator.winding.p = 2
        mach.stator.is_stator = True

        # Correct check
        assert mach.get_pole_pair_number() == 2

        # Error two laminations
        mach.stator.winding.p = 3
        with pytest.raises(Exception) as e:
            mach.get_pole_pair_number()
        assert "ERROR, Stator has a different pole pair number than Rotor" == str(
            e.value
        )

        # Error 4 laminations
        stator_0.winding.p = 56
        with pytest.raises(Exception) as e:
            machine.get_pole_pair_number()
        assert "ERROR, Stator-0 has a different pole pair number than Rotor-1" == str(
            e.value
        )


if __name__ == "__main__":
    a = Test_get_lam_methods()
    a.test_get_pole_pair()
    print("Done")
