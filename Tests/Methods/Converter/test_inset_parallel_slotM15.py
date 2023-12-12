import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM15 import SlotM15


slotM12_test = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 4,
        "Magnet_Arc_[ED]": 120,
    }
}
slotM12_test.append(
    {"other_dict": other_dict, "W1": 0.5155675378442213, "Rtopm": 0.001}
)

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 8,
        "Magnet_Arc_[ED]": 40,
    }
}
slotM12_test.append(
    {"other_dict": other_dict, "W1": 0.1729169936113538, "Rtopm": 0.001}
)


class TestComplexRuleSlotM15(object):
    @pytest.mark.parametrize("test_dict", slotM12_test)
    def test_inset_parallel_slotM15(self, test_dict):
        """test rule complex"""
        other_dict = test_dict["other_dict"]
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM15()

        rule = RuleComplex(fct_name="inset_breadloaf_slotM12", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        Rtopm = test_dict["Rtopm"]
        W1 = test_dict["W1"]

        assert machine.rotor.slot.W1 == pytest.approx(W1)
        assert machine.rotor.slot.Rtopm == pytest.approx(Rtopm)


if __name__ == "__main__":
    a = TestComplexRuleSlotM15()
    for test_dict in slotM12_test:
        a.test_inset_parallel_slotM15(test_dict)
    print("Test Done")
