import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM13 import SlotM13

slotM13_test = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 4,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 1,
    }
}

slotM13_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.51763809020,
        "W0": 0.517638090205,
        "Rtopm": 0.9724747378,
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

slotM13_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.51763809020,
        "W0": 0.51763809020,
        "Rtopm": 0.835980126309,
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

slotM13_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.51763809020,
        "W0": 0.51763809020,
        "Rtopm": 0.8170990436,
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

slotM13_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.51763809020,
        "W0": 0.51763809020,
        "Rtopm": 1.000000000000001,
    }
)


class TestComplexRuleSlotM13(object):
    @pytest.mark.parametrize("test_dict", slotM13_test)
    def test_surface_breadloaf_slotM13(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM13()

        machine.rotor.slot.H0 = 0.01
        machine.rotor.slot.H1 = 0.02

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="surface_breadloaf_slotM13", folder="MotorCAD")
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
    a = TestComplexRuleSlotM13()
    for test_dict in slotM13_test:
        a.test_surface_breadloaf_slotM13(test_dict)
    print("Test Done")
