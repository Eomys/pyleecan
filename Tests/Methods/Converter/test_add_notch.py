import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM19 import SlotM19


notch_l = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "PoleNotchDepth": 2,
        "PoleNotchArc_Outer": 120,
        "PoleNotchArc_Inner": 140,
    }
}
notch_l.append(
    {"other_dict": other_dict, "W1": 0.5176380902050414, "W0": 0.601411599008546}
)

# Common values
other_dict = {
    "[Dimensions]": {
        "PoleNotchDepth": 2,
        "PoleNotchArc_Outer": 150,
        "PoleNotchArc_Inner": 100,
    }
}
notch_l.append(
    {"other_dict": other_dict, "W1": 0.6428789306063232, "W0": 0.4328792278762058}
)


class TestComplexRuleNotch(object):
    @pytest.mark.parametrize("test_dict", notch_l)
    def test_add_notch(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.notch.append(NotchEvenDist())
        machine.rotor.notch[0].notch_shape = SlotM19()

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="add_notch_slotM19", folder="MotorCAD")
        p = 8  # number of pole
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / p) * (pi / 180), "m": 1}
        )

        # retreive expected values
        W0 = test_dict["W0"]
        W1 = test_dict["W1"]

        # check the convertion
        msg = f"{machine.rotor.notch[0].notch_shape.W1} expected {W1}"
        assert machine.rotor.notch[0].notch_shape.W1 == pytest.approx(W1), msg
        msg = f"{machine.rotor.notch[0].notch_shape.W0} expected {W0}"
        assert machine.rotor.notch[0].notch_shape.W0 == pytest.approx(W0), msg


if __name__ == "__main__":
    a = TestComplexRuleNotch()
    for test_dict in notch_l:
        a.test_add_notch(test_dict)
    print("Test Done")
