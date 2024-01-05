import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM14 import SlotM14


slotM14_test = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 4,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 1,
    }
}

slotM14_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5084631986262793,
        "W0": 0.5084631986262793,
        "Rtopm": 0.97795161891461,
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

slotM14_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5104022927682093,
        "W0": 0.5104022927682093,
        "Rtopm": 0.8529842972222449,
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

slotM14_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5104022927682093,
        "W0": 0.5104022927682093,
        "Rtopm": 0.8351690217446512,
    }
)

# Magnet_Reduction = 0, no reduction
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 8,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 0,
    }
}

slotM14_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5104022927682093,
        "W0": 0.5104022927682093,
        "Rtopm": 1.0079999999999996,
    }
)


class TestComplexRuleSlotM14(object):
    @pytest.mark.parametrize("test_dict", slotM14_test)
    def test_surface_radial_slotM14(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM14()

        machine.rotor.slot.H0 = 0.01
        machine.rotor.slot.H1 = 0.02

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="surface_radial_slotM14", folder="MotorCAD")
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
    a = TestComplexRuleSlotM14()
    for test_dict in slotM14_test:
        a.test_surface_radial_slotM14(test_dict)
    print("Test Done")
