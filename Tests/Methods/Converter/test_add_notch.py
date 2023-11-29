import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.Notch import Notch
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.SlotM19 import SlotM19


rule_list = list()

# add equation rules
other_dict = {
    "[Dimensions]": {
        "PoleNotchDepth": 2,
        "PoleNotchArc_Outer": 120,
        "PoleNotchArc_Inner": 140,
    }
}


class TestComplexRuleNotch(object):
    def test_add_notch(self):
        """test rule complex"""
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.notch.append(Notch())
        machine.rotor.notch[0] = NotchEvenDist()
        machine.rotor.notch[0].notch_shape = SlotM19()

        rule = RuleComplex(fct_name="add_notch", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 1}
        )

        assert machine.rotor.notch[0].notch_shape.W1 == pytest.approx(
            0.5176380902050414
        )
        assert machine.rotor.notch[0].notch_shape.W0 == pytest.approx(
            0.6014115990085462
        )


if __name__ == "__main__":
    a = TestComplexRuleNotch()
    a.test_add_notch()
    print("Test Done")
