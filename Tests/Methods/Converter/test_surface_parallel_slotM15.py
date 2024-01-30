import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM15 import SlotM15


slotM15_test = list()
# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 4,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 1,
    }
}

slotM15_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5197086425658616,
        "W0": 0.5311810058686,
        "Rtopm": 0.9764715541024068,
    }
)

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 8,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 7,
    }
}

slotM15_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5217791949266818,
        "W0": 0.5333487892002,
        "Rtopm": 0.8437532376408229,
    }
)

# Magnet_Reduction = Magnet_Thickness max
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 8,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 8,
    }
}

slotM15_test.append(
    {
        "other_dict": other_dict,
        "Rtopm": 0.8248165743381716,
        "W1": 0.5217791949266818,
        "W0": 0.5333487892002,
    }
)

# Magnet_Reduction = 0, no reduction
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 8,
        "Magnet_Arc_[ED]": 150,
        "MagnetReduction": 0,
    }
}

slotM15_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.6480219620511,
        "W0": 0.6668552972224,
        "Rtopm": 1.0080000000000011,
    }
)


class TestComplexRuleSlotM15(object):
    @pytest.mark.parametrize("test_dict", slotM15_test)
    def test_surface_parallel_slotM15(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM15()

        machine.rotor.slot.H0 = 0.01
        machine.rotor.slot.H1 = 0.02

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="surface_parallel_slotM15", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        # retreive expected values
        W0 = test_dict["W0"]
        W1 = test_dict["W1"]
        Rtopm = test_dict["Rtopm"]

        # check the convertion
        msg = f"{machine.rotor.slot.W0} expected {W0}"
        assert machine.rotor.slot.W0 == pytest.approx(W0), msg
        msg = f"{machine.rotor.slot.W1} expected {W1}"
        assert machine.rotor.slot.W1 == pytest.approx(W1), msg
        msg = f"{machine.rotor.slot.Rtopm} expected {Rtopm}"
        assert machine.rotor.slot.Rtopm == pytest.approx(Rtopm), msg


if __name__ == "__main__":
    a = TestComplexRuleSlotM15()
    for test_dict in slotM15_test:
        a.test_surface_parallel_slotM15(test_dict)
    print("Test Done")
